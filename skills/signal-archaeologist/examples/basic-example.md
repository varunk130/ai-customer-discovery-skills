# Basic example: signal-archaeologist

## Input

Archive of 850 support tickets from 2024-01 to 2025-12, plus 120 NPS comments.

## Expected output (abbreviated)

**Top slow-burning theme**: "permissions confusion in shared workspaces"
- 2024 Q1: 4 mentions, sentiment -0.2
- 2024 Q3: 11 mentions, sentiment -0.4
- 2025 Q1: 19 mentions, sentiment -0.5
- 2025 Q3: 31 mentions, sentiment -0.6
- velocity: +7.2/quarter
- decay_weighted_importance: 0.83 (rank #1 of 14 themes)

**Buried signal flagged**: "export takes >5 min on accounts >50k rows" — 2 mentions/quarter for 18 months, no team currently owns it.