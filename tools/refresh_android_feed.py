"""Publish APK metadata only; this repository does not contain app source."""
import hashlib
import json
import os
from pathlib import Path
import re
import subprocess
import tempfile
import urllib.request

REPO = 'issaghostlife/streamwears'
CERTIFICATE = 'd6a8d7f1b73192935e07d54469dbea97cbcc3a24ef332f6256f4efcf7a1539f7'
headers = {'Authorization': 'Bearer ' + os.environ['GH_TOKEN'], 'Accept': 'application/vnd.github+json', 'User-Agent': 'StreamwearsIRL-update-feed'}
request = urllib.request.Request(f'https://api.github.com/repos/{REPO}/releases?per_page=100', headers=headers)
with urllib.request.urlopen(request, timeout=60) as response:
    releases = json.load(response)
assets = [a for r in releases if not r['draft'] for a in r['assets'] if a['name'] == 'Streamwears.apk' and a['state'] == 'uploaded']
if not assets:
    print('No published Streamwears.apk yet; leaving feed unchanged.')
    raise SystemExit(0)
asset = max(assets, key=lambda a: a['updated_at'])
feed_path = Path('updates/android.json')
current = json.loads(feed_path.read_text(encoding='utf-8')) if feed_path.exists() else {}
remote_digest = asset.get('digest', '').removeprefix('sha256:')
url = asset['browser_download_url']
if not re.fullmatch(r'https://github\.com/issaghostlife/streamwears/releases/download/[A-Za-z0-9._-]+/Streamwears\.apk', url):
    raise SystemExit('Unexpected APK download URL.')
if remote_digest and current.get('sha256') == remote_digest and current.get('url') == url and os.environ.get('VERIFY_APK') != 'true':
    print('Published APK is unchanged.')
    raise SystemExit(0)
sdk = Path(os.environ.get('ANDROID_HOME') or os.environ['ANDROID_SDK_ROOT'])
build_tools = sorted((sdk / 'build-tools').glob('*'), key=lambda p: [int(n) for n in re.findall(r'\d+', p.name)])[-1]
with tempfile.TemporaryDirectory() as folder:
    apk = Path(folder) / 'Streamwears.apk'
    with urllib.request.urlopen(url, timeout=180) as response, apk.open('wb') as output:
        total = 0
        while chunk := response.read(1024 * 1024):
            total += len(chunk)
            if total > 200 * 1024 * 1024:
                raise SystemExit('APK exceeds expected size limit.')
            output.write(chunk)
    digest = hashlib.sha256(apk.read_bytes()).hexdigest()
    if total != asset['size'] or (remote_digest and digest != remote_digest):
        raise SystemExit('Downloaded APK digest/size mismatch.')
    signature = subprocess.check_output([str(build_tools / 'apksigner'), 'verify', '--print-certs', str(apk)], text=True)
    fingerprints = [value.lower() for value in re.findall(r'certificate SHA-256 digest:\s*([0-9a-f]{64})', signature, re.IGNORECASE)]
    print('APK signing certificate SHA-256:', ', '.join(fingerprints) or signature[:300])
    if fingerprints != [CERTIFICATE]:
        raise SystemExit('APK was not signed with the Streamwears release certificate.')
    badging = subprocess.check_output([str(build_tools / 'aapt'), 'dump', 'badging', str(apk)], text=True)
    package = re.search(r"package: name='([^']+)' versionCode='(\d+)' versionName='([^']+)'", badging)
    if not package or package[1] != 'com.streamwear.app':
        raise SystemExit('Unexpected APK package.')
    code = int(package[2])
    if code < current.get('versionCode', 0):
        raise SystemExit('Refusing to publish an older Android version.')
    feed = {'versionCode': code, 'versionName': package[3], 'url': url, 'sha256': digest, 'publishedAt': asset['updated_at'], 'assetId': asset['id']}
    feed_path.parent.mkdir(exist_ok=True)
    feed_path.write_text(json.dumps(feed, indent=2) + '\n', encoding='utf-8')
    print(f'Update feed ready for Android {package[3]} ({code}).')
