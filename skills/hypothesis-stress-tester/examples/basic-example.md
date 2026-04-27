# Basic example: hypothesis-stress-tester

## Input
Hypothesis: If we add an in-app AI assistant to our analytics product, mid-market accounts will increase weekly active users 20%, because they currently struggle with SQL.

## Expected output (abbreviated)
- **Red-team (High/Medium)**: "Mid-market analysts already use ChatGPT in another tab — your in-app version is redundant and trust-deficient." → Defense: explicit data-context advantage; trust framing.
- **Alternative-cause (High/High)**: WAU could rise from a launch novelty bump that decays in 60 days, not from durable AI value. → Defense: pre-register success metric as Day-90 retention, not initial WAU.
- **Second-order (Medium/Medium)**: Success could hide bad SQL skill development in your user base, increasing dependency lock-in (good for retention, bad for trust). → Defense: ship a "show the SQL" mode.

**Survivability: Conditional.** Strongest attack to address first: the alternative-cause (novelty) attack. Re-define success as Day-90 retention before building.