---
name: insight-distiller
version: 0.1.0
description: Synthesizes insights across multiple research sources with confidence intervals and source trails.
when_to_use:
  - You have research from 2+ methods (e.g. interviews + surveys + analytics)
  - You need to publish an insight memo with defensible evidence
  - You want to know which insights are well-supported vs speculative
inputs:
  - name: sources
    type: json
    required: true
    description: 'Array of {type, label, data} — types: interviews, survey, analytics, support, sales'
  - name: research_question
    type: string
    required: true
    description: The decision the insights need to inform
outputs:
  - name: insights
    type: markdown
    description: Ranked insights with confidence (L/M/H) and source trail
  - name: contradictions
    type: markdown
    description: Cases where sources disagree, with hypothesis on why
  - name: gaps
    type: markdown
    description: Areas where the research question is unanswered or under-evidenced
tags: [synthesis, insights, evidence, multi-source]
maintainer: "@varunk130"
---

# insight-distiller

## Purpose

Synthesis without evidence trails is opinion. `insight-distiller` enforces that every insight cite its sources, declare its confidence, and explicitly acknowledge gaps and contradictions.

## Instructions

1. **Normalize sources** into a common shape: `{source_id, type, excerpt_or_metric}`.
2. **Cluster excerpts/metrics into candidate insights.** An insight is a statement that:
   - Answers (or partially answers) the research question
   - Is supported by ≥2 source items (ideally from ≥2 source types)
3. **Score confidence**:
   - High: ≥3 sources, ≥2 source types, no contradicting evidence
   - Medium: 2 sources, possibly contradicting evidence with explanation
   - Low: 1 source, OR contradicting evidence outweighs support
4. **Build the source trail** for each insight: list the exact source_ids and a 1-line excerpt.
5. **Surface contradictions** explicitly — these are often more valuable than the insights.
6. **Identify gaps** — parts of the research question that the data does not address.

## Output format

Three markdown sections: insights (ranked, with confidence + source trail), contradictions, gaps.

## Limitations

- Confidence is a rough heuristic. Quantitative evidence (e.g. a 1000-person survey) deserves more weight than the rules give it.
- Source trails are only as good as the source labels — invest in good labeling upstream.