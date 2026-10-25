# Streamwears 3.0 (20)

Instagram Live and TikTok LIVE can now connect without asking creators to paste stream keys.

## What’s new

- Connect an Instagram account once, then start Instagram Live directly from Studio.
- Streamwears requests fresh Instagram RTMPS credentials and starts the Instagram broadcast automatically.
- Removed the outdated Safari and Live Producer final-step message for automatically connected Instagram accounts.
- Creator Progress now shows every connected channel, including automatically authorized Instagram accounts.
- Live discovery now displays the connected creator username for each active platform.
- Kept manual Instagram RTMP setup under **Settings → Stream keys** as an advanced fallback.
- Platform preparation now runs concurrently, reducing Go Live setup time when several destinations are enabled.
- TikTok LIVE account connection, chat, events, gifts, and automatic LIVE setup remain available without a pasted stream key.

## TestFlight testing requested

1. Connect Instagram from Destinations and confirm the account remains connected after closing and reopening Streamwears.
2. Start a private or test Instagram Live from Studio and confirm it becomes live without opening Safari or pasting a stream key.
3. End the broadcast and start a second Instagram Live to verify Streamwears requests fresh credentials automatically.
4. Start Instagram and TikTok together and compare Go Live setup time with the previous build.
5. Confirm Instagram no longer shows the “final step” Safari or Live Producer instruction while live.
6. Report the iPhone model, iOS version, glasses model/firmware, enabled destinations, and the exact on-screen message if setup fails.

Instagram and TikTok publishing depend on each account’s LIVE eligibility and may be affected by platform-side changes. Never include passwords, verification codes, session data, or stream keys in a test report.
