---
name: north-star-metric-finder
description: 'Identifies a candidate North Star Metric (NSM) for a product — the single metric that captures the value the product delivers to its customers and predicts long-term business growth. Tests candidates against five criteria and surfaces input metrics that move it. Use when: north star metric, NSM, single metric that matters, primary metric, growth metric, value-capture metric, what should we measure.'
---

# North Star Metric Finder

Identify a candidate North Star Metric (NSM) that satisfies five strict criteria, then map the 3–5 input metrics that drive it. The output is a defensible recommendation, not a brainstormed list.

## Core Principle

**A North Star Metric is a forcing function, not a slogan.** Adopting the wrong one quietly skews two years of roadmap decisions. The five criteria below exist to *eliminate* candidates that look reasonable but fail under stress.

## The Five Criteria

| Criterion | The Question | Failure Example |
|-----------|--------------|-----------------|
| **Value-capturing** | Does this metric only go up when customers receive real value? | "Logins per week" — easy to game with notification spam |
| **Predictive** | Does this metric lead revenue and retention by ≥1 quarter? | "MRR" — lagging, not leading |
| **Actionable** | Can the team move this metric with deliberate actions? | "NPS" — moves slowly, hard to attribute changes |
| **Understandable** | Can every employee state the metric and why it matters in one sentence? | "Weekly active accounts with ≥3 successful API calls in their primary workspace" |
| **Singular** | Is this a single metric, not an index of three? | A weighted composite hides which input is broken |

A candidate must pass all five. Three out of five is not a NSM — it's a useful KPI.

## Output

Save to `outputs/nsm-[product]-[YYYY-MM-DD].md`

- **Recommended NSM** + the five-criteria pass/fail evaluation
- **Runner-up candidates** with the criterion they failed and why
- **Input metrics** (3–5) that drive the NSM, with the *direction* and *expected magnitude*
- **Counter-metrics** that prevent gaming (e.g., NSM ↑ + churn ↑ = bad)
- **Cadence** — how often to review the NSM and re-validate it

## Process

### Step 1: Generate Candidates
I'll ask:
> "What does your product *do* for the customer? What's the moment they get value? Share your current top-line metrics and a one-sentence pitch."

I generate 6–10 candidate NSMs grounded in the value moment, not the business model.

### Step 2: Five-Criteria Pass
Score each candidate pass/fail on all five criteria. Eliminate any with a fail.

### Step 3: Map Input Metrics
For the top candidate, identify the 3–5 metrics that *cause* it to move (e.g., "weekly active value-events" might be driven by activation rate, frequency, expansion of use cases).

### Step 4: Counter-Metric Pairing
Every NSM needs a guardrail. Pair the NSM with 1–2 counter-metrics that catch the most likely gaming pattern.

### Step 5: Stress Test
Walk through three scenarios and ask: would adopting this NSM lead to a *better* decision than the current top metric? If not, re-open candidates.

## Tips
1. **The value moment matters more than the business moment.** "Subscription started" is the business moment; "first successful workflow completed" is the value moment. The latter is almost always the better NSM.
2. **Beware composite metrics.** They feel comprehensive but obscure root causes. If you can't avoid one, score the components separately too.
3. **Re-validate annually.** Product evolves; the value moment can shift.
