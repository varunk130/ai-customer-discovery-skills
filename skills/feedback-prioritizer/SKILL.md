---
name: feedback-prioritizer
description: 'Triages a backlog of raw customer feedback into a ranked list of opportunities scored on reach, severity, strategic fit, and confidence. Outputs a prioritized list with explicit "do not act" callouts for vocal-minority signals. Use when: triage feedback, prioritize feature requests, customer feedback backlog, what should we build next, opportunity scoring, RICE feedback, feedback synthesis.'
---

# Feedback Prioritizer

Convert a stack of customer feedback (tickets, interview notes, NPS comments, sales loss reasons) into a small ranked list of opportunities, with explicit reasoning for what *not* to act on. The single most important section of the output is "Do Not Act" — vocal-minority signals that look compelling but would distract the roadmap.

## Core Principle

**Most feedback is noise; the prioritizer's job is to find the signal *and* name the noise.** A ranked list without a "Do Not Act" section silently licenses the team to chase the loudest voices.

## Scoring Model: RSCF

Each candidate opportunity is scored 1–5 on four dimensions:

| Letter | Dimension | Question |
|--------|-----------|----------|
| **R** | Reach | What share of paying customers will benefit? |
| **S** | Severity | When the problem hits, how badly does it hurt? |
| **C** | Strategic fit | Does this align with the current strategy or pull us off-mission? |
| **F** | Confidence | How certain are we, given evidence quality and quantity? |

**Score = R × S × C × F / 25** (normalized to 0–25). Confidence acts as a multiplier that crushes weakly-evidenced items.

## Output

Save to `outputs/feedback-priority-[period]-[YYYY-MM-DD].md`

| Section | Description |
|---------|-------------|
| **Top 5 Opportunities** | Ranked by RSCF, with evidence count and source breakdown |
| **Watch List** | Promising but evidence-light items (Confidence ≤ 2) — gather more data |
| **Do Not Act** | Vocal-minority signals with explicit reasoning for de-prioritization |
| **Patterns Across Sources** | Themes that appeared in 3+ independent channels (highest-trust signal) |
| **Counterfactual Check** | "If we only did the top-1 item, would the next quarter look meaningfully better?" |

## Process

### Step 1: Intake
I'll ask:
> "Share the feedback corpus (paste, file, or sample). Tell me the time window, source mix (tickets / interviews / NPS / sales / churn), and your current strategy in one sentence."

### Step 2: Cluster
Group raw items into themes. Items that repeat across *different* sources weight more than the same item repeated 50× from one source.

### Step 3: Score
Score each theme 1–5 on R, S, C, F with a one-line rationale per dimension. Compute RSCF.

### Step 4: Pattern Pass
Surface themes that appeared in 3+ source types — these are the highest-trust signals even if individual scores are middling.

### Step 5: Build the Do-Not-Act List
Identify items that:
- Came from a single loud source
- Conflict with strategy (low C)
- Would require disproportionate effort relative to RSCF
For each, write *why* it's tempting and why it's wrong.

### Step 6: Counterfactual
Test the top-1 against the question: "If this is all we shipped next quarter, is the quarter visibly better?" If no, re-open the ranking.

## Tips
1. **Source diversity beats source volume.** 3 channels saying the same thing is stronger than 30 customers saying it on one.
2. **Confidence is the multiplier that matters.** A 4×4×4×1 scores 16; a 3×3×3×4 scores 27. Evidence quality wins.
3. **Always publish the Do Not Act list.** It's the only section that protects strategic focus.
