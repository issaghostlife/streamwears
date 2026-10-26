# StreamwearsIRL Android 3.6 — Developer Mode test build

Android glasses users can use Meta's supported Developer Mode route instead of joining Streamwears' registered Meta release channel.

- The downloadable signed APK sets both Meta APPLICATION_ID and CLIENT_TOKEN to 0, matching Meta's Android development guidance. Version 3.5 used registered-beta credentials.
- Studio and Meta connection help now explain enabling Developer Mode in Meta AI, registering, approving camera access and starting preview. A tester invitation is not a prerequisite for this build.
- The package and original signing key are retained, so install over the current signed app. Streaming account storage is unchanged. An existing Meta integration may need disconnecting in Meta AI and reconnecting when changing modes.
- This is a Developer Mode testing build; it does not enable Meta-approved public production distribution.
- Existing capture, streaming protection, chat, provider login, Instagram manual fallback, AI and update features are retained.

## Setup

Pair/update glasses in Meta AI. Open Meta AI Settings → App info; tap App version five times if Developer Mode is hidden, then enable it. With glasses connected, install/update the Device Access Toolkit app if prompted. Return to Streamwears and tap Connect Meta glasses; approve registration and camera access, then Start preview. Developer Mode is configured in Meta AI, not Android phone Developer options/USB debugging.

The optional registered-channel build can still be built explicitly with `-PstreamwearMetaAccess=registeredBeta`; that separate route requires an accepted Meta invitation and Developer Mode off. The website's Android download is the Developer Mode build.

## Verification and limits

The signed APK's actual manifest must contain 0/0 and package com.streamwear.app, versionCode13. Original-key signature, unit/build checks and emulator upgrade/UI checks are recorded during release verification. Physical glasses registration, real broadcast sound/video/chat and sustained network behavior remain unverified here; no zero-drop claim is made.

[Download Android](https://streamwearsirl.com/uploads/Streamwears.apk) · [Meta Android Developer Mode guidance](https://github.com/facebook/meta-wearables-dat-android/issues/214) · [Meta configuration guide](https://github.com/facebook/meta-wearables-dat-android/blob/main/plugins/mwdat-android/skills/getting-started/SKILL.md)

Closed source. Public source archives contain documentation and release infrastructure only.
