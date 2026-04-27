---
name: jtbd-extractor
version: 0.2.0
description: Extracts functional, emotional, and social Jobs-To-Be-Done from research, with opportunity scoring.
when_to_use:
  - You have research data and want to articulate the customer''s underlying job
  - You are framing a product strategy and need a JTBD list to prioritize against
  - You want to translate persona pains into actionable jobs
inputs:
  - name: research_data
    type: markdown
    required: true
    description: Coded interviews, survey verbatims, or persona cards
  - name: include_opportunity_scoring
    type: string
    required: false
    description: 'true | false — whether to apply Ulwick opportunity scoring (default true)'
outputs:
  - name: jobs
    type: markdown
    description: Functional, emotional, and social jobs in canonical JTBD statement form
  - name: opportunity_scores
    type: markdown
    description: Importance × satisfaction-gap scoring per job
tags: [synthesis, jtbd, opportunity, prioritization]
maintainer: "@varunk130"
---

# jtbd-extractor

## Purpose

Convert messy research into canonical JTBD statements: `When [situation], I want to [motivation], so I can [outcome].` Surface functional + emotional + social dimensions, then score opportunity using Ulwick''s importance × satisfaction-gap framework.

## Instructions

1. **Cluster research excerpts** by underlying situation.
2. **Author functional jobs** in canonical form. Be ruthless about removing solution language.
3. **For each functional job, surface the emotional and social jobs.** Most JTBD work stops at functional — this is the core mistake.
4. **Score opportunity** per job:
   - Importance (1–10): how much does this matter to the customer?
   - Satisfaction (1–10): how well are existing solutions meeting it?
   - Opportunity = Importance + max(Importance − Satisfaction, 0)
   - >12 = high opportunity, 10–12 = medium, <10 = low
5. **Output ranked job list** with opportunity scores.

## Output format

Two markdown sections: jobs (with all three dimensions) and opportunity scores.

## Limitations

- Opportunity scoring requires importance/satisfaction signal in the research; if missing, the skill estimates from sentiment and flags as low-confidence.
- Jobs are extracted from the data provided — if the research is biased, so are the jobs.