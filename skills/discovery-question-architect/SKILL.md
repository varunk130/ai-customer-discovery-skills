---
name: discovery-question-architect
version: 0.1.0
description: Generates bias-checked, open-ended discovery questions for any research topic.
when_to_use:
  - You are designing the next round of discovery interviews
  - You need to upgrade a question bank that is producing thin answers
  - You want to audit a colleague's interview guide for leading questions
inputs:
  - name: topic
    type: string
    required: true
    description: The research topic or hypothesis under exploration
  - name: existing_questions
    type: markdown
    required: false
    description: Optional existing question bank to audit and improve
  - name: interview_length_min
    type: string
    required: false
    description: Target interview length to size the bank appropriately
outputs:
  - name: question_bank
    type: markdown
    description: Categorized question bank with rationale per question
  - name: bias_audit
    type: markdown
    description: Bias scores and rewrites for any leading or double-barrelled questions
tags: [discovery, interview, question-design, capture, bias]
maintainer: "@varunk130"
---

# discovery-question-architect

## Purpose

Bad interview questions silently invalidate research. Leading questions get agreement; double-barrelled ones get half-answers; "would you" hypotheticals get aspirational lies. This skill generates clean banks and audits existing ones.

## Instructions

1. **Categorize the topic** into 4–6 angles (e.g., context, current behavior, pain, workarounds, desired outcome, willingness to pay).
2. **Generate 3–5 questions per angle**, all open-ended. Avoid:
   - Leading: "Don''t you find X frustrating?"
   - Double-barrelled: "How often do you X and why?"
   - Hypothetical: "Would you pay for X?"
   - Confirmation-biased: framing that assumes the answer
   - Closed: yes/no
   - Jargon-loaded
3. **Audit each question** against the 6-point bias checklist. Score 0 (clean) to 3 (severe).
4. **Rewrite** any question scoring ≥2 with a clean alternative.
5. **Add rationale** per question — what the answer should reveal.
6. **Size the bank** to fit the target interview length (rule of thumb: 4 minutes per primary question + follow-ups).

## Output format

Two markdown sections: question bank (organized by angle, with rationale) and bias audit (table of original → score → rewrite).

## Limitations

- Cultural and domain-specific bias can slip through. Have a domain expert review.
- Cannot judge whether the *topic itself* is well-framed — pair with `problem-prism`.