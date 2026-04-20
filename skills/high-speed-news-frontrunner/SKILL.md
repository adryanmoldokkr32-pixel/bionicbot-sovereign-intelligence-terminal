---
name: high-speed-news-frontrunner
description: Monitor institutional news terminals for a 5-10 second edge over retail media.
---

# High-Speed News Frontrunner

This skill enables bionicbot to monitor raw data feeds (Bloomberg Terminal style) and high-speed wires to identify market-moving headlines before they hit social media or news sites.

## Core Mechanics
1. Connect to low-latency financial news streams and Twitter/X firehose.
2. Filter for 'Red Headlines' (High volatility triggers).
3. Use high-speed NLP to extract the direction (Bullish/Bearish) in < 1 second.
4. Trigger an instant alert to the user's primary channel (WhatsApp/Signal).

## Examples
- "Alert me 10 seconds after the Fed statement is released, before the market reaction peaks."