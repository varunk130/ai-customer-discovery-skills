---
name: interview-decoder
version: 0.1.0
description: Decodes a single interview transcript into themes, contradictions, unspoken assumptions, and follow-ups.
when_to_use:
  - You have just finished a discovery or usability interview
  - You want to spot moments where the participant contradicted themselves
  - You need follow-up questions for the next round
inputs:
  - name: transcript
    type: markdown
    required: true
    description: Time-stamped or speaker-labeled transcript
  - name: research_question
    type: string
    required: false
    description: The question that motivated this interview
outputs:
  - name: coded_transcript
    type: markdown
    description: Inline tags for themes, sentiment, behaviors, beliefs
  - name: contradiction_map
    type: markdown
    description: Pairs of statements that conflict, with confidence rating
  - name: unspoken_assumptions
    type: markdown
    description: Beliefs the participant treated as obvious but never stated
  - name: follow_ups
    type: markdown
    description: 5–10 questions for the next interview to resolve uncertainty
tags: [discovery, interview, synthesis, capture]
maintainer: "@varunk130"
---

# interview-decoder

## Purpose

Single-interview analysis is usually shallow. Researchers extract obvious themes and miss the diagnostic gold: the moments a participant contradicts themselves, or treats a belief as obvious without ever stating it.

## Instructions

1. **Parse the transcript** into participant utterances. Strip interviewer questions for theme coding (but retain them for follow-up generation).
2. **Code each utterance** with up to 3 tags from: `behavior`, `belief`, `goal`, `pain`, `workaround`, `desired_outcome`, `constraint`, `emotion`.
3. **Build the contradiction map.** For every pair of `belief` or `behavior` codes, check for semantic conflict. Score confidence Low/Medium/High.
4. **Surface unspoken assumptions** — phrases like "obviously," "of course," "everyone knows," or behaviors described without justification ("I just always export it first").
5. **Generate 5–10 follow-up questions** prioritized by:
   - Resolving a Medium/High contradiction
   - Probing an unspoken assumption
   - Filling a gap in the original research question

## Output format

Four discrete markdown sections, in the order: coded transcript, contradictions, unspoken assumptions, follow-ups. See [`examples/basic-example.md`](./examples/basic-example.md).

## Limitations

- Single-pass analysis. For higher-confidence coding, run twice and compare.
- Contradiction detection is conservative; tune by lowering the confidence threshold in the prompt.
- Does not infer cross-interview patterns — use `insight-distiller` for that.