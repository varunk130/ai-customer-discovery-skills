---
name: competitive-analyzer
description: 'Structured competitive teardown for product discovery — surface the 4–6 dimensions buyers actually weigh, score every competitor on each, and identify exploitable gaps. Use when: competitive analysis, competitor teardown, market positioning, where do we win, where do we lose, competitive gap analysis, competitor audit.'
---

# Competitive Analyzer

Run a disciplined competitive teardown that goes beyond a feature checklist. The output is the smallest set of *decision-relevant* dimensions, scored objectively across competitors, with explicit gaps you can attack and risks you should defend.

## Core Principle

**A competitive analysis is only useful if it changes a decision.** Most teardowns produce 40-row feature grids that no one reads. This skill forces brutal selection: pick the 4–6 dimensions buyers actually weigh, score them with a defensible rubric, and surface the 2–3 moves the analysis implies.

## Output

Save to `outputs/competitive-analysis-[market]-[YYYY-MM-DD].md`

| Artifact | Description |
|----------|-------------|
| **Dimension Map** | The 4–6 buyer-weighted dimensions with rationale for inclusion |
| **Scoring Matrix** | Each competitor scored 1–5 on each dimension, with one-line evidence per cell |
| **Gap Map** | Dimensions where every competitor underperforms — the white space |
| **Risk Map** | Dimensions where one competitor strongly outperforms us |
| **Implied Moves** | 2–3 concrete strategic moves the analysis suggests, ranked by leverage |

## Process

### Step 1: Frame the Market
I'll ask:
> "What market are we analyzing, and from whose perspective? List the competitors (3–7 works best). What's the deal context — what's a typical buyer trying to accomplish?"

### Step 2: Pick the Dimensions
Generate a candidate list of 12–15 dimensions, then ruthlessly cut to 4–6 by applying two filters:
- **Decision relevance** — does this dimension actually move buying decisions?
- **Discriminating power** — do competitors meaningfully differ on it? (Dimensions where everyone scores the same get cut.)

### Step 3: Score with Evidence
For each (competitor × dimension) cell, score 1–5 with a single sentence of *evidence* — a public artifact, a customer quote, a product behavior — not opinion.

### Step 4: Identify Gaps and Risks
Two scans across the matrix:
- **Gap** — any dimension where the *highest* score is ≤3 → market is underserved, opportunity
- **Risk** — any dimension where a competitor scores 5 and we score ≤3 → defensive priority

### Step 5: Implied Moves
Translate the gap and risk maps into 2–3 concrete moves: build, partner, position, retreat. Each move includes the *evidence* from the matrix that justifies it.

## Tips
1. **Evidence-only scoring.** A score without evidence is opinion; opinions don't survive the next leadership review.
2. **Cut the matrix until it hurts.** A 4-dimension matrix that gets used beats a 12-dimension matrix that gets ignored.
3. **Re-run quarterly.** Competitive position shifts; rerun cadence keeps the analysis honest.
