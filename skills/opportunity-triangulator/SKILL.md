---
name: opportunity-triangulator
version: 0.1.0
description: Sizes opportunity using 3 independent methods (top-down, bottoms-up, value-based) and quantifies the spread.
when_to_use:
  - You need to size a new opportunity for a strategy doc or board update
  - A single TAM number feels too neat and you want intellectual honesty
  - You are comparing two opportunities and need apples-to-apples sizing
inputs:
  - name: opportunity
    type: string
    required: true
    description: One-paragraph description of the opportunity
  - name: known_inputs
    type: markdown
    required: false
    description: Any existing data — comparable markets, internal usage, pricing, etc.
outputs:
  - name: estimates
    type: markdown
    description: Three independent estimates with assumptions, math, and sources
  - name: spread_analysis
    type: markdown
    description: Spread between methods, confidence rating, and what would tighten it
tags: [decide, sizing, tam, opportunity, triangulation]
maintainer: "@varunk130"
---

# opportunity-triangulator

## Purpose

A single TAM number is precision theatre. It hides assumptions and overstates confidence. Triangulating with 3 methods and showing the spread is more honest — and frequently changes the decision.

## Instructions

1. **Restate the opportunity** in one paragraph including target buyer, problem, and proposed value exchange.
2. **Estimate (Method A: top-down)**: industry analyst data → addressable segment → reasonable share. Show every multiplier.
3. **Estimate (Method B: bottoms-up)**: number of target accounts × average contract value × adoption rate. Show every multiplier.
4. **Estimate (Method C: value-based)**: per-customer value created (cost saved, revenue added) × number of customers × value-capture rate.
5. **Compute spread**: ratio of max:min estimate.
   - <2× → high confidence
   - 2–5× → medium confidence (typical)
   - >5× → low confidence — the opportunity is fundamentally uncertain, get more data before betting
6. **Recommend** which assumptions to validate first to tighten the estimate.

## Output format

Two markdown sections: estimates (three subsections, one per method) and spread analysis (with confidence rating + next-steps).

## Limitations

- Only as good as inputs. Garbage assumptions in, garbage triangulation out.
- Does not model time-to-revenue or competition.