---
name: assumption-mapper
description: 'Surfaces the assumptions a product or strategy depends on, classifies them by criticality and evidence quality, and produces a prioritized test plan. Use when: assumption mapping, identify assumptions, what could go wrong, leap-of-faith assumptions, riskiest assumption test, RAT, assumption inventory, validate before building.'
---

# Assumption Mapper

Every product bet rests on a stack of assumptions. This skill makes them explicit, classifies each as Known / Believed / Hoped, and produces a ranked test plan so the team validates the riskiest assumptions *before* committing to build.

## Core Principle

**The assumptions you don't write down are the ones that kill the product.** Hidden assumptions become "obvious in hindsight" only because no one stress-tested them. The mapper's job is to drag them into the open and force a verdict on each.

## The 3-Tier Classification

| Tier | Definition | Action |
|------|------------|--------|
| **Known** | Direct evidence, multiple independent sources, recent data | No test needed; document the evidence link |
| **Believed** | Reasonable inference from indirect or partial evidence | Test if assumption is *critical*; defer if not |
| **Hoped** | Wishful thinking dressed as reasoning; no real evidence | Test before any meaningful investment |

Cross with criticality (Critical / High / Medium / Low) → the **Critical × Hoped** quadrant is the team's actual risk surface.

## Assumption Categories

The mapper walks through 5 categories to surface assumptions a one-shot brainstorm misses:

| Category | Example Assumptions |
|----------|---------------------|
| **Customer / Demand** | "SMB ops leaders feel this pain weekly"; "buyers will pay $X" |
| **Solution / Product** | "Our approach is materially better than the workaround"; "the model can hit 90% accuracy on this task" |
| **Channel / Distribution** | "We can acquire this segment via content"; "our sales team can sell this without retraining" |
| **Economic / Unit** | "CAC stays under $X at this segment"; "support cost scales sublinearly" |
| **Competitive / Time** | "Incumbents won't ship this within 6 months"; "the platform shift continues for 2+ years" |

## Output

Save to `outputs/assumption-map-[initiative]-[YYYY-MM-DD].md`

- **Assumption Inventory** - every assumption surfaced, by category
- **Classification Matrix** - Known / Believed / Hoped × Critical / High / Medium / Low
- **Risk Surface** - the Critical × Hoped quadrant, called out explicitly
- **Test Plan** - for each Critical × (Hoped or Believed) assumption: smallest test that would invalidate it, expected duration, success criteria
- **Defer List** - Low-criticality assumptions that don't justify a test (named so they're not silently treated as Known)

## Process

### Step 1: Frame the Bet
I'll ask:
> "Describe the initiative or strategy in 2-3 sentences. What does success look like 12 months from now?"

### Step 2: Walk the 5 Categories
Surface 4-8 assumptions per category. Aim for *uncomfortable* assumptions - the ones the team would rather not name.

### Step 3: Classify
For each assumption, classify Known / Believed / Hoped with the evidence (or absence thereof) noted.

### Step 4: Rank by Criticality
Critical = the bet fails if this assumption is wrong. Most initiatives have 3-5 Critical assumptions; if the count is higher, the initiative is too entangled and should be decomposed.

### Step 5: Build the Test Plan
For each Critical × (Hoped or Believed), design the *smallest test that would invalidate* the assumption. Tests are ranked by speed-to-disconfirm, not by speed-to-confirm.

### Step 6: Pre-Mortem Pass
For each Critical × Hoped, write one sentence: "If this assumption is wrong, the initiative fails because…" If you can't write that sentence, the assumption isn't actually Critical.

## Tips
1. **Tests are designed to disconfirm, not confirm.** Confirmation bias is the default; rigorous tests look for the cheapest way to be proven wrong.
2. **Decompose entangled bets.** An initiative with 8 Critical assumptions is really 3 initiatives stacked.
3. **Re-map at major milestones.** Yesterday's Known can become today's Believed when context shifts.
4. **Hoped is not a slur.** Most novel products start with several Hoped assumptions; the discipline is acknowledging them, not avoiding them.
