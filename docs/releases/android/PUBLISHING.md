# Publishing Android updates

StreamwearsIRL is closed source. This repository only contains release infrastructure, downloads and documentation.

1. Build a release APK with a higher Android `versionCode` and the existing Streamwears signing key. Keep the package name `com.streamwear.app`. Never upload the signing key or passwords.
2. Create a GitHub release and upload the signed APK named exactly **Streamwears.apk**. Publish the release; drafts are not offered to users. A prerelease is supported for this beta.
3. The **Refresh Android update feed** action reads the APK's version, checks its signature and SHA-256, and updates `updates/android.json`. The app reads this small public feed instead of downloading the APK during checks.
4. If replacing the APK on an existing release, delete the old asset and upload the replacement under the same name. The scheduled action catches asset replacements every 30 minutes; you can also run the action manually for an immediate feed refresh. Prefer a higher version code for every release.

Android 3.3 and later check when opened (at most once per 15 minutes) and about hourly in the background. Users must allow notifications. Tapping an alert opens the direct APK download; Android still asks the user to confirm installation. Checks pause during a LIVE. Android power management, an offline device or GitHub scheduling can delay an alert. This is scheduled checking, not instant push delivery.

Users on older builds must install 3.3 or later once to enable this feature. Install over the existing app to retain saved connections. A new build with the same version code is detected by its APK hash; an identical reupload does not trigger duplicate alerts. Older version codes are ignored. Debug builds use a different signing key and cannot replace the public release.
