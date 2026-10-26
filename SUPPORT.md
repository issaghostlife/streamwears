# StreamwearsIRL Support

Start with the [quick-start guide](README.md#your-first-stream), or [contact support](https://streamwearsirl.com/support).

## Downloads

- **iPhone:** [Apple TestFlight beta](https://testflight.apple.com/join/Ee36dYF9).
- **Android 12+:** [Signed Android 3.5 APK](https://github.com/issaghostlife/streamwears/releases/download/android-v3.5/Streamwears.apk) · [Release notes](https://github.com/issaghostlife/streamwears/releases/tag/android-v3.5).

## Meta glasses beta access

The APK is publicly downloadable, but this Meta Wearables project currently has an invite-only release channel. An owner must invite your personal Meta account email and you must accept at [wearables.meta.com/invites](https://wearables.meta.com/invites). Downloading an APK or installing TestFlight alone does not grant channel membership. [Request beta access here](https://streamwearsirl.com/beta.php). Confirm your testing agreement and personal Meta email. Requests are processed periodically, subject to available places. The local invitation processor needs the owner's computer/app available and Meta/hosting sessions signed in; requests remain queued while processing is unavailable.

**“Application data is currently unavailable” on Android:** update to 3.5 and check beta membership. Meta integration 1.1.0 now includes the Android package and original release certificate; the previous released configuration lacked both. In the app, **Meta connection help** shows the installed package/certificate for troubleshooting. Do not uninstall to troubleshoot saved sessions. If it persists, report your app/Meta AI version, glasses model and whether the invitation was accepted; do not share tokens or passwords.

## Common questions

**Do I need stream keys?** TikTok, Facebook Live, Kick and Twitch use account sign-in. On iPhone, Instagram Live uses the connected account and requests fresh streaming credentials automatically; no copied key or Safari step is needed. Android 3.5 also supports Instagram session login and automatic Live setup, plus YouTube authorization. Manual Instagram Live Producer URL/key setup remains available in Android Accounts and iPhone Settings → Stream keys.

**Where is the App Store version?** The iOS beta is available through TestFlight. A phone-camera App Store version is planned. Meta glasses access for our App Store release is still pending; use the iOS TestFlight beta for those features now.

**My glasses are not connecting.** Install iPhone TestFlight build 3.0 (23) or newer. Check pairing and firmware in Meta AI, keep Bluetooth enabled, then connect from Streamwears and choose **Always Allow** when Meta AI asks. If Meta AI shows **Allowed**, Streamwears should show **Camera access allowed** while it restores the Blayzer Optics/00FQ or other compatible glasses link. Tap **Start Preview**; the app changes to **Glasses camera connected** only after real video frames arrive. If it still stalls, include the glasses model, firmware and the screen where it stopped in your report.

**Why did the glasses camera stay off after waking?** This is the intended privacy behavior in build 3.0 (22). When you are not live, charging, deep sleep, reopening Streamwears or putting the glasses back on will not activate the camera. Tap **Start Preview** when you want video. During an active live, Streamwears still protects the broadcast across app switching and resumes glasses video when possible.

**Chat is missing.** Make sure the platform LIVE has started and the connected account has the required permissions. Saved sessions are reused while valid; reconnect if the platform reports that authorization has expired.

**My stream is lagging.** Lower the output quality, reduce the number of destinations, check upload signal and let the phone cool down. Tell us whether you were on Wi-Fi or cellular when reporting the issue.

**The Android update will not install.** Check that your phone runs Android 12 or newer and that you downloaded the signed APK linked here. Contact support before removing an existing installation, since uninstalling clears saved local connections.

## Report a bug

Use [GitHub Issues](https://github.com/issaghostlife/streamwears/issues/new) or [private support](https://streamwearsirl.com/support). Include:

- Phone model and OS version.
- StreamwearsIRL app version/build.
- Glasses model/firmware, if applicable, and whether you used glasses or a phone camera.
- Streaming platform and connection type (Wi-Fi/cellular).
- What you tried, what happened instead and whether it happens every time.

Never include passwords, access tokens, stream keys, API/OAuth secrets or signing credentials in a public report. [Report security issues privately](SECURITY.md).

**Android update notifications:** Install 3.3 or later and allow notifications. Use Settings → App updates for a manual check or to open Android notification settings. Checks run about hourly and when opened; phones that are asleep/offline can receive alerts later. Tap an alert to download, then confirm installation over the existing app.
