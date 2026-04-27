---
name: hypothesis-stress-tester
version: 0.1.0
description: Attacks a product hypothesis from 6 adversarial angles and reports survivability.
when_to_use:
  - You have a hypothesis you are about to bet engineering quarters on
  - Your team is too aligned and you suspect groupthink
  - You need a structured pre-mortem
inputs:
  - name: hypothesis
    type: string
    required: true
    description: A specific testable hypothesis ("If we do X, then Y will happen because Z")
  - name: context
    type: markdown
    required: false
    description: Relevant market, product, and team context
outputs:
  - name: attacks
    type: markdown
    description: 6 adversarial scenarios, each with severity and likelihood
  - name: survivability
    type: markdown
    description: Overall survivability rating + the strongest attack to address before proceeding
tags: [decide, hypothesis, adversarial, pre-mortem]
maintainer: "@varunk130"
---

# hypothesis-stress-tester

## Purpose

Pre-mortems often degrade into "what could go wrong" brainstorms. This skill runs a structured, adversarial attack across 6 distinct attack surfaces — much harder for the hypothesis to survive all of them.

## Instructions

For the supplied hypothesis, generate one attack per category:

1. **Red-team attack**: a competitor or skeptic argues the hypothesis is false.
2. **Market-timing attack**: the hypothesis is *true but at the wrong time* (too early / too late).
3. **Alternative-cause attack**: even if Y happens, it might not be *because of* X (confounding cause).
4. **Scaling-failure attack**: works at small scale but breaks above N customers / N data points.
5. **Second-order-effect attack**: succeeding at the hypothesis triggers a worse downstream consequence.
6. **Ethical / trust attack**: succeeding erodes user trust, brand, or regulatory position.

For each:
- Score severity (Low/Medium/High)
- Score likelihood (Low/Medium/High)
- Suggest one defense or test that would mitigate

Then rate **overall survivability**: Strong / Conditional / Fragile, and name the single strongest attack to address first.

## Output format

Two markdown sections: attacks (6 subsections) and survivability assessment.

## Limitations

- Quality depends on context. Vague hypotheses produce vague attacks — refine the hypothesis first.
- Some attacks may not apply to all hypotheses; mark as "N/A" rather than forcing.