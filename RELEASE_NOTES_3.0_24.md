# Streamwears 3.0 (24) — Blayzer preview recovery

This targeted TestFlight build fixes the camera preview remaining on **Connecting** after Streamwear and the glasses were already approved in Meta AI.

- Treats **Allowed** as camera authorization while continuing to wait for the actual glasses link.
- Follows per-device link, hinge, wear, and compatibility changes so Start Preview resumes as soon as the pair is ready.
- Requires a real video frame before reporting the glasses camera as connected.
- Stops the endless spinner after 12 seconds and performs one clean session retry.
- Uses Meta's official raw, medium-resolution 24 fps camera path on that retry when the HEVC path reports streaming but sends no frames.
- Accepts the fully updated glasses toolkit 1.0.0 with the app's Meta iOS SDK 1.0.1 and starts directly in raw compatibility mode when Meta reports that 1.0.x pairing as a device update mismatch.
- Keeps the camera off until the user taps **Start Preview** when they are not live.
- Adds a compact **Crowdfund Streamwears** card below King Coop in Settings, opening the secure Square contribution page in one tap.

## Blayzer / RB Meta 00FQ tester check

1. Update to build 24 in TestFlight.
2. Wear the glasses with both arms open and confirm they are connected in Meta AI.
3. Open Streamwear and tap **Start Preview** once.
4. If the glasses toolkit is accepted as fully compatible, Streamwear tries HEVC first and automatically retries with raw video when no frame arrives. If Meta reports the glasses toolkit 1.0.0 as a device update mismatch, Streamwear starts with raw video immediately.
5. Confirm moving camera video appears. In Settings, the active mode may show **Raw · compatibility mode**.

If both attempts finish without a frame, send the Streamwear glasses diagnostics plus the glasses firmware and Meta AI versions. Build 24 exits the connecting state and reports that result instead of hanging.
