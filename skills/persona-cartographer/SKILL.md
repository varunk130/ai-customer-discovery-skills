---
name: persona-cartographer
version: 0.1.0
description: Generates personas as a relationship graph, surfacing influence, blocking, and approval dynamics.
when_to_use:
  - You are building a B2B or multi-stakeholder product
  - Traditional persona cards feel flat or fail to predict adoption blockers
  - You need to model decision-making units, not just individuals
inputs:
  - name: research_corpus
    type: markdown
    required: true
    description: Coded interviews, sales call notes, or org research
  - name: target_segment
    type: string
    required: false
    description: e.g. "mid-market SaaS finance teams"
outputs:
  - name: persona_cards
    type: markdown
    description: 3–6 named personas with goals, pains, JTBDs, and current behaviors
  - name: relationship_graph
    type: markdown
    description: Mermaid graph showing influence, blocking, approval, and information-flow edges
  - name: adoption_risks
    type: markdown
    description: Predicted adoption blockers based on the graph topology
tags: [synthesis, persona, b2b, relationships, graph]
maintainer: "@varunk130"
---

# persona-cartographer

## Purpose

In B2B, the user is rarely the buyer, the buyer is rarely the champion, and the champion is rarely the blocker. Flat persona cards lose this. `persona-cartographer` produces a graph.

## Instructions

1. **Extract candidate persona archetypes** from the corpus — cluster by role, goals, and behavior. Aim for 3–6.
2. **Author each persona card**: name, role, top 3 goals, top 3 pains, primary JTBD, current behaviors, tools they live in.
3. **Map relationships** as a Mermaid directed graph. Edge types:
   - `--influences-->`
   - `--needs approval from-->`
   - `--blocks-->`
   - `--escalates to-->`
   - `--informs-->`
4. **Identify adoption risks** by inspecting graph topology:
   - Any persona with `--blocks-->` edges and no champion → adoption blocker
   - Any decision flow that requires ≥3 approvals → likely procurement friction
   - Any "shadow" persona (mentioned but never interviewed) → research gap

## Output format

Three markdown sections: persona cards, Mermaid relationship graph, adoption risks. See [`examples/basic-example.md`](./examples/basic-example.md).

## Limitations

- Requires research with ≥2 distinct roles to produce a meaningful graph.
- Graph reflects what was *said* in research; political dynamics may be hidden. Cross-check with sales.