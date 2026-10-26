# StreamwearsIRL Support

Start with the [quick-start guide](README.md#your-first-stream), or [contact support](https://streamwearsirl.com/support).

## Downloads

- **iPhone:** [Apple TestFlight beta](https://testflight.apple.com/join/Ee36dYF9).
- **Android 12+:** [Signed Android 3.7.1 APK](https://github.com/issaghostlife/streamwears/releases/download/android-v3.7.1/Streamwears.apk) · [Release notes](https://github.com/issaghostlife/streamwears/releases/tag/android-v3.7.1).

## Android glasses: Developer Mode

The public Android 3.7.1 APK uses Meta's documented **0/0 Developer Mode configuration**. A Streamwears Meta channel invitation is not required for this Android setup.

Pair/update the glasses in Meta AI. Go to **Meta AI → Settings → App info**, reveal Developer Mode by tapping App version five times if needed, then turn it on. Check the glasses' Device Access Toolkit app is installed/updated. Return to Streamwears, connect, approve camera access and start preview. This is Meta AI Developer Mode, not Android phone Developer options.

If Meta shows an integration/link error: verify Developer Mode is still on, check DAT installation, close/reopen Meta AI, and reconnect Streamwears. An old registered-channel connection may need disconnecting in Meta AI. Avoid uninstalling Streamwears or clearing its storage unless you are ready to lose local saved connections. If the problem remains, send app/Meta AI/firmware versions and Meta connection-help diagnostics, never passwords or tokens. [Meta's Android maintainer guidance](https://github.com/facebook/meta-wearables-dat-android/issues/214).

## Registered beta channel (separate route)

The optional [invitation request form](https://streamwearsirl.com/beta.php) remains for iPhone/registered-channel testers who agree to test. It is not an Android 3.7.1 prerequisite. That channel is limited to 100 active users plus pending invites; users accept their own invitations. Scheduled invitation processing depends on the owner's computer/app and signed-in hosting/Meta sessions.

## Common questions

**Do I need stream keys?** TikTok, Facebook Live, Kick and Twitch use account sign-in. On iPhone, Instagram Live uses the connected account and requests fresh streaming credentials automatically; no copied key or Safari step is needed. Android 3.7.1 also supports Instagram session login and automatic Live setup, plus YouTube authorization. Manual Instagram Live Producer URL/key setup remains available in Android Accounts and iPhone Settings → Stream keys.

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
