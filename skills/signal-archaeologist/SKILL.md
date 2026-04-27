---
name: signal-archaeologist
version: 0.1.0
description: Mines historical customer artefacts (tickets, calls, NPS) for buried signals with velocity scoring.
when_to_use:
  - You have 6+ months of accumulated support, sales, or NPS text data
  - You need to surface trends that single-quarter analyses miss
  - You suspect a slow-burning problem is being ignored
inputs:
  - name: archive
    type: file
    required: true
    description: Folder of dated text artefacts (one per record, ISO date in filename or header)
  - name: time_window
    type: string
    required: false
    description: Lookback window (e.g. "12m"). Defaults to all available.
outputs:
  - name: signal_timeline
    type: markdown
    description: Chronological signal map with frequency, sentiment, and velocity per theme
  - name: decay_corrected_themes
    type: json
    description: Themes ranked by recency-weighted importance (half-life = 90 days)
tags: [discovery, voc, capture, historical, archaeology]
maintainer: "@varunk130"
---

# signal-archaeologist

## Purpose

Most customer signals decay in salience faster than they decay in importance. Quarterly reports surface what is loud now; truly persistent problems get buried. `signal-archaeologist` excavates them.

## Instructions

1. **Index the archive.** For each artefact extract: ISO date, source channel, raw text, customer segment (if present).
2. **Cluster into candidate themes** using semantic similarity. Aim for 8–20 themes.
3. **Compute per-theme metrics** for each rolling 30-day window:
   - frequency (count of mentions)
   - sentiment (−1 to +1, mean)
   - velocity (Δ frequency vs. previous window)
4. **Apply a 90-day exponential decay** to weight recent signals — but flag any theme whose *velocity* is positive across 3+ consecutive windows. These are the "slow burns."
5. **Produce two artefacts:**
   - A markdown timeline grouped by theme, with sparkline-style frequency notation.
   - A JSON ranked list of themes by `decay_weighted_importance × velocity_score`.

## Output format

See [`examples/basic-example.md`](./examples/basic-example.md).

## Limitations

- Requires reasonably consistent text quality across the time window. Highly templated tickets will under-cluster.
- Sentiment scoring is coarse; do not use as a quantitative SLA metric.
- Does not deduplicate the same customer raising the same issue across multiple channels.