## StreamwearsIRL Android 3.5 beta

Updated from the October 26 iOS archive and its native Android counterpart, while preserving the existing Android release's saved-account storage, original signing identity, streaming recovery and update alerts.

- Meta Device Access Toolkit 1.0.1, registration-error reporting, immediate glasses-camera approval after registration, and a connection-help screen showing the installed package and public certificate fingerprint.
- Preview startup now retries once at medium HEVC quality and ends the connecting state if no frames arrive. LIVE reconnect protection continues independently. A stopped or paused preview does not repeatedly reopen after a successful preview outside LIVE/recording.
- YouTube account login with PKCE, automatic broadcast preparation and provider confirmation after video publishing connects.
- Instagram session login, approval/verification-code handling and automatic fresh LIVE preparation. Manual Instagram Live Producer URL/key setup remains available.
- Five tabs: Studio, Accounts, AI, Live and Settings. AI setup help and phone-camera Live Text/translation are included. The bundled OCR recognizer reads Latin-script text; translation language models download when needed.
- TikTok gifts and provider-reported viewers appear in Studio. Chat sending is offered only when the connected backend explicitly enables it.
- Optional public Live discovery, Facebook profile/Page selection, selfie PiP, custom RTMP destinations, encrypted session reuse, and manual/automatic app-update checks.
- Google Play Full Access purchase/restore integration is included; availability depends on the app/product being configured in Google Play. The direct APK does not bypass purchase eligibility.

**Install over the existing APK** to retain saved connections. The package remains `com.streamwear.app`; versionCode is 12. The APK uses the original direct-distribution signing certificate, not the separate Play upload key.

**Meta configuration corrected:** the previous released Meta integration had no Android package or signature. Version **1.1.0** now includes `com.streamwear.app` and the original direct-release signing identity and is active on the existing private channel. This fixes a verified configuration omission; physical glasses registration still needs device validation. Meta currently offers this project an invite-only channel. APK availability does not grant glasses access: invited users must accept with their personal Meta account at [Meta invitations](https://wearables.meta.com/invites).

**Validation:** optimized/debug builds, 17 unit tests and four emulator instrumentation tests passed; lint has zero errors. The original-signed 3.2 APK upgraded in place to 3.5, and the optimized release opened AI and Live Text without an app crash. This does not establish real broadcast performance.

**Meta integration error:** “Application data is currently unavailable” is a Meta AI registration error, not a TikTok/Facebook password error. Android package/certificate and the released project/channel/tester configuration must match in Meta's developer portal. This release does not claim to override Meta authorization or prove a hardware registration pass without device testing.

This is a native Android release, not a binary conversion of SwiftUI or Apple's frameworks. Physical phone/glasses and authenticated provider broadcasts are still required to validate end-to-end camera, audio, latency, network handoffs and account eligibility. Zero dropped frames and exact behavior on every device are not claimed.

[Official Android download](https://streamwearsirl.com/uploads/Streamwears.apk) · [GitHub APK mirror](https://github.com/issaghostlife/streamwears/releases/download/android-v3.5/Streamwears.apk) · [iPhone TestFlight](https://testflight.apple.com/join/Ee36dYF9) · [Support](https://streamwearsirl.com/support)

The app is closed source. GitHub source archives contain public documentation/release infrastructure, not application source.
