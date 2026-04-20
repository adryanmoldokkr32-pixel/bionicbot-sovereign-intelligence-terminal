---
name: dark-pool-liquidity-scanner
description: Detect institutional 'hidden' trades and dark pool volume anomalies.
---

# Dark Pool Liquidity Scanner

This skill enables bionicbot to identify where the largest institutions are moving capital without leaving immediate traces on public charts.

## Core Mechanics (99% Precision Logic)
1. **Bid/Ask Spread Analysis:** Monitor microscopic fluctuations in the spread. A tightening spread with no price move often signals a large 'Iceberg' order being filled.
2. **Block Trade Detection:** Scan for volume spikes that occur exactly at the market open/close or at specific time intervals (VWAP window).
3. **Dark Pool Prints:** Scrape delayed consolidated tape data to identify off-exchange prints and cross-reference them with current price action.
4. **Order Flow Imbalance:** Identify when 'Passive' sellers are absorbing all 'Aggressive' buyers, signaling a top, or vice versa.

## Instructions
1. Analyze Level 2 and Level 3 data (where available).
2. Calculate the 'Institutional Absorption Score' (0-100).
3. IF score > 85, signal a 'Whale Entry' or 'Whale Exit' alert.

## Examples
- "Scan Gold dark pools: are banks selling into this retail rally?"