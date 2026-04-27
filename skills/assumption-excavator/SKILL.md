---
name: assumption-excavator
version: 0.1.0
description: Surfaces hidden assumptions in a brief and ranks them by test cost × failure cost.
when_to_use:
  - You have a product brief, PRD, or strategy doc you want to pressure-test
  - You suspect the plan rests on unexamined assumptions
  - You need to design a validation backlog before committing engineering
inputs:
  - name: brief
    type: markdown
    required: true
    description: The brief, PRD, or strategy doc to excavate
outputs:
  - name: assumptions
    type: markdown
    description: All assumptions found, classified by category (user, market, technical, business, organizational)
  - name: priority_grid
    type: markdown
    description: 2x2 grid of assumptions by test cost × failure cost, with top 3 to validate next
tags: [decide, assumptions, validation, risk]
maintainer: "@varunk130"
---

# assumption-excavator

## Purpose

Most plans fail not because of bad strategy but because a hidden assumption was wrong. Excavating assumptions makes the bet structure visible.

## Instructions

1. **Parse the brief** sentence by sentence. For every claim that is not a stated fact, mark it as a candidate assumption.
2. **Classify** each assumption:
   - **User**: about who the user is, what they want, or how they behave
   - **Market**: about market size, willingness to pay, competition
   - **Technical**: about feasibility, performance, scalability
   - **Business**: about unit economics, sales motion, pricing
   - **Organizational**: about team capacity, skills, alignment
3. **Score each assumption**:
   - Test cost: Free / Cheap / Moderate / Expensive
   - Failure cost: Recoverable / Painful / Catastrophic
4. **Plot on a 2×2** (test cost × failure cost) and surface the top 3 in the "cheap to test, catastrophic if wrong" quadrant — these always validate first.

## Output format

Two markdown sections: assumptions list (categorized) and priority grid with top 3 to validate.

## Limitations

- Cannot detect assumptions that the author actively concealed.
- Test cost and failure cost are estimates; a domain expert should review.