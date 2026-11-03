# Streamwears 3.0 (23) — Authorized Glasses Recovery

## What changed

- Fixed a false **Check Developer Mode** warning after Meta AI already showed camera access as **Allowed**.
- Streamwears now preserves an approved camera grant while Meta briefly reloads the glasses device link.
- Authorized Blayzer Optics/00FQ and other compatible Meta glasses keep reconnecting without reopening the permission flow.
- The connection screen now says **Camera access allowed** while the link finishes, then **Glasses camera connected** after real camera frames arrive.

## Privacy behavior retained

- The glasses camera starts only after the user taps **Start Preview** when they are not live.
- Live broadcasts keep their protected reconnect behavior when the user switches apps or the glasses briefly sleep.

## What to test

1. Confirm Meta AI reports Streamwears camera access as **Allowed**.
2. Return to Streamwears and tap **Start Preview**.
3. Verify Streamwears waits for and reconnects the glasses without showing **Check Developer Mode**.
4. Verify the live preview begins and the status changes to **Glasses camera connected** once the glasses are open, worn and connected.
