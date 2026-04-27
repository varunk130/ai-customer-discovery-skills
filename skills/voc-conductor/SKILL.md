---
name: voc-conductor
version: 0.1.0
description: Aggregates Voice of Customer streams across channels into a channel-weighted theme map.
when_to_use:
  - You receive customer signal from 3+ channels (reviews, tickets, social, NPS, sales)
  - You need a single weekly/monthly synthesis the leadership team can act on
  - You want to know whether a theme is real or one channel's bias
inputs:
  - name: streams
    type: json
    required: true
    description: 'Array of {channel, items[]} objects. Channels e.g. "support", "g2", "twitter", "nps", "sales".'
  - name: weighting_profile
    type: string
    required: false
    description: Override the default channel weights (see SKILL.md)
outputs:
  - name: theme_map
    type: markdown
    description: Themes ranked by channel-weighted score, with per-channel breakdown
  - name: bias_warnings
    type: markdown
    description: Themes that appear in only one channel — flagged for verification
tags: [voc, aggregation, capture, multi-channel]
maintainer: "@varunk130"
---

# voc-conductor

## Purpose

VoC dashboards routinely double-count: the same customer pain shows up in a support ticket, a churn-survey response, *and* a Twitter rant — but counted as 3 separate signals, the team chases noise. `voc-conductor` weights and deduplicates across channels.

## Instructions

1. **Normalize** each stream item: `{text, customer_id?, timestamp, channel, source_url?}`.
2. **Cluster** items into candidate themes using semantic similarity (target 8–15 themes).
3. **Apply channel weights.** Default profile (override via input):
   - `sales_call`: 1.0 (high intent, but low N)
   - `support_ticket`: 0.9 (real pain, but skewed to power users)
   - `nps_verbatim`: 0.8 (broad, but selection bias)
   - `g2_review`: 0.6 (high incentive bias)
   - `twitter`: 0.4 (loud minority)
4. **Deduplicate by customer_id** within a 30-day window — same person, same theme = 1 signal.
5. **Compute weighted score** per theme. Rank.
6. **Flag bias warnings** for any theme that appears in ≤1 channel — likely an artefact of that channel's audience.

## Output format

Two markdown sections: ranked theme map (with per-channel breakdown table) and bias warnings.

## Limitations

- Channel weights are heuristics. Validate against your own conversion data and tune.
- Deduplication requires a stable `customer_id` across channels; without one, falls back to fuzzy name matching.
- Does not detect sarcasm in social channels.