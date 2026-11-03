# Streamwears 3.0 (22) — Test notes

This build fixes Meta glasses camera privacy and reconnection behavior, including Blayzer Optics/00FQ.

## What changed

- Putting glasses on after charging or deep sleep no longer starts the camera automatically. The camera starts only after **Start Preview** or another camera feature the user explicitly chooses.
- While live, Streamwears still protects the broadcast when the app moves to the background and resumes glasses video when possible.
- If glasses video pauses during a live broadcast, viewers now see a branded Streamwears screen explaining that video will return and audio remains live.
- The first Meta camera approval flow now continues after **Always allow** instead of remaining on **Resuming glasses video**.

## What to test

1. Connect Blayzer Optics/00FQ or another supported Meta pair and choose **Always allow** in Meta AI.
2. Confirm Streamwears returns from Meta AI and can start preview.
3. Stop preview, let the glasses enter deep sleep or place them in the charging case, then put them on again while Streamwears is open. Confirm the camera stays off until **Start Preview** is tapped.
4. Start a live stream, switch to another app, and confirm the live session remains active with audio and the branded pause screen.
5. Return to Streamwears and confirm glasses video resumes in the existing live session.
