# StreamwearsIRL Support

Start with the [quick-start guide](README.md#your-first-stream), or [contact support](https://streamwearsirl.com/support).

## Downloads

- **iPhone:** [Apple TestFlight beta](https://testflight.apple.com/join/Ee36dYF9).
- **Android 12+:** [Signed Android 3.3 APK](https://github.com/issaghostlife/streamwears/releases/download/android-v3.3/Streamwears.apk) · [Release notes](https://github.com/issaghostlife/streamwears/releases/tag/android-v3.3).

## Common questions

**Do I need stream keys?** TikTok, Facebook Live, Kick and Twitch use account sign-in. Instagram requires a stream URL and key from Live Producer; manual setup is included on both iOS and Android. Use Accounts → Instagram. Confirm the final Go live step in Instagram Live Producer after Streamwears sends video, and prepare a fresh key for each broadcast.

**Where is the App Store version?** The iOS beta is available through TestFlight. A phone-camera App Store version is planned. Meta glasses access for our App Store release is still pending; use the iOS TestFlight beta for those features now.

**My glasses are not connecting.** Check pairing and firmware in Meta AI, keep Bluetooth enabled, approve the requested permissions and try preview again. Include the glasses model and firmware when reporting a problem.

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
