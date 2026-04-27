---
name: problem-prism
version: 0.1.0
description: Refracts a single problem statement through 5 lenses (user, business, technical, regulatory, emotional).
when_to_use:
  - You suspect your problem framing is too narrow
  - Your team keeps generating the same kind of solutions
  - You need to widen the option space before prioritizing
inputs:
  - name: problem_statement
    type: string
    required: true
    description: A one-paragraph problem description
  - name: context
    type: markdown
    required: false
    description: Optional product/market/team context
outputs:
  - name: refractions
    type: markdown
    description: The same problem reframed through 5 lenses, each with implications
  - name: highest_leverage_frame
    type: markdown
    description: A recommendation for which lens to optimize against, with rationale
tags: [decide, framing, problem-statement, divergent-thinking]
maintainer: "@varunk130"
---

# problem-prism

## Purpose

How-Might-We rewrites change the verb. They do not change the *frame of reference*. `problem-prism` does. The same problem viewed through a regulatory lens vs an emotional lens generates entirely different — and equally valid — solution categories.

## Instructions

1. **Restate the problem** in your own words to confirm understanding. Strip solution language.
2. **Refract through 5 lenses**, producing one paragraph per lens:
   - **User lens**: what is the user trying to accomplish, and what is in their way?
   - **Business lens**: what economic mechanism is broken, and who pays the cost?
   - **Technical lens**: what system constraint or capability gap is creating this?
   - **Regulatory / policy lens**: what rule, contract, or norm is implicated?
   - **Emotional lens**: what feeling is the user trying to avoid or seek?
3. **For each lens**, list 2–3 implications — what kind of solution becomes plausible.
4. **Recommend the highest-leverage frame** based on:
   - Which lens has the largest gap between current and possible state?
   - Which lens does the team have permission and capability to act on?
   - Which lens is most under-explored in current strategy?

## Output format

Two markdown sections: refractions (one per lens) and highest-leverage frame (with rationale).

## Limitations

- Lens choice is heuristic; some problems have natural primary lenses (e.g. healthcare → regulatory).
- Recommends a frame, not a solution. Use with `opportunity-triangulator` next.