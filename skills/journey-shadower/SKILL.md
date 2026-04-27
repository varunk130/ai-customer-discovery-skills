---
name: journey-shadower
version: 0.1.0
description: Simulates a persona''s journey hour-by-hour through a scenario, with friction scoring per touchpoint.
when_to_use:
  - You need to find micro-frictions in onboarding, activation, or first value
  - Stage-level journey maps are too coarse to be actionable
  - You are diagnosing a drop-off and need to localize it
inputs:
  - name: persona
    type: markdown
    required: true
    description: Persona card or research excerpt describing the user
  - name: scenario
    type: string
    required: true
    description: The journey to simulate (e.g. "first 24 hours after signup")
  - name: known_touchpoints
    type: markdown
    required: false
    description: Documented product touchpoints in this scenario
outputs:
  - name: hour_by_hour
    type: markdown
    description: Simulated timeline with goal, action, expectation, reality, friction score (0–5)
  - name: friction_hotspots
    type: markdown
    description: Top 3 friction events with hypothesized root cause and fix direction
tags: [synthesis, journey-map, friction, onboarding]
maintainer: "@varunk130"
---

# journey-shadower

## Purpose

Stage-level journey maps ("Onboarding," "Activation") are too coarse to debug retention. The 11th-minute friction is what makes someone close the tab. `journey-shadower` runs at hour granularity.

## Instructions

1. **Anchor the simulation** in the persona''s real-world context — what else is happening in their day, what device, what mental state.
2. **For each hour (or finer if needed) of the scenario**, produce a row:
   - Hour
   - Persona''s active goal
   - Action they take
   - Expectation they bring
   - Reality they hit
   - Friction score (0 = none, 5 = abandonment-likely)
   - One-line emotional reaction
3. **Identify friction hotspots** — events with score ≥3.
4. **For each hotspot, hypothesize:**
   - Root cause (UX / data / docs / pricing / mismatch with expectation)
   - One concrete fix direction

## Output format

Two markdown sections: hour-by-hour table and friction hotspots. See [`examples/basic-example.md`](./examples/basic-example.md).

## Limitations

- A simulation, not real data. Use to *generate hypotheses*, then validate with session recordings or interviews.
- Friction scoring is qualitative; use the same persona + scenario to compare alternatives, not as an absolute metric.