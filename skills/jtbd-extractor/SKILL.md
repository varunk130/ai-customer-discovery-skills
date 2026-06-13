---
name: jtbd-extractor
version: 1.0.0
description: 'Turn raw research into Jobs-to-be-Done statements showing what users are really trying to accomplish. Use when: extract jobs, jtbd analysis, jobs to be done, what job is the user hiring, underlying user needs.'
when_to_use: 'You have a corpus of customer conversations and need structured, prioritized Jobs-to-be-Done output you can actually act on.'
inputs:
  - Interview transcripts
  - Support tickets, sales call notes, NPS comments
  - Optional: audio recordings (see docs/AUDIO_INPUT_MODE.md)
outputs:
  - Functional, emotional, and social JTBD statements
  - Opportunity scoring per job
  - Markdown and HTML reports rendered via the included Python CLI
tags: ['discovery', 'jtbd', 'research-synthesis', 'opportunity-scoring']
maintainer: varunk130
---

# JTBD Extractor

Turn raw research into Jobs-to-be-Done statements showing what users are really trying to accomplish - reframing feature requests as underlying needs and uncovering innovation opportunities.

## Output
Save to `discovery/outputs/jtbd-[persona]-[YYYY-MM-DD].md`

## When to Use This Skill
- Reframing feature requests into underlying needs
- Finding innovation opportunities in saturated markets
- Training your team to think in jobs, not features

## What You'll Get

I'll generate a complete Jobs-to-be-Done analysis with:
- **JTBD statements** - Properly formatted "When [situation], I want to [action], so I can [outcome]"
- **Job categories** - Separated into Functional, Emotional, and Social jobs
- **Opportunity scores** - Importance + (Importance - Satisfaction) to show where to focus
- **Evidence tracking** - Direct quotes and behavior supporting each job
- **Feature translation** - Mapping what users asked for to what they actually need
- **Top opportunities** - Ranked list of underserved jobs worth solving

## What You'll Need
- Interview transcripts, survey responses, or customer feedback
- Context on your product/market

## Process

### Step 1: Review Your Context

I'll start by checking your context files to understand what you already know:
- **personas.md** - What jobs do your existing personas have?
- **product.md** - What problems does your product solve today?
- **Research files** - Any prior interview snapshots or feedback data?

I'll share what I find. For example:
> "I see your personas in personas.md already have some Jobs-to-be-Done statements. I'll compare what I extract from this research to see if it confirms or expands on those jobs."

### Step 2: Request Research Data

If you haven't provided data yet, I'll ask:
> "I need research data to extract jobs from. Do you have any of these?
> - Interview transcripts or notes
> - Survey responses (especially open-ended)
> - Support tickets or feature requests
> - Customer feedback
>
> You can paste it here or point me to files in your context/ folder."

I won't generate placeholder output without actual data.

### Step 3: Identify Jobs

I'll extract statements that reveal what users are trying to accomplish:
- Listening for "I need to...", "I'm trying to...", "I want to..."
- Looking beyond the literal request to the underlying goal
- Connecting to your existing personas when relevant

### Step 4: Format as JTBD

I'll structure each job properly:
```
When [situation/trigger],
I want to [motivation/action],
So I can [expected outcome].
```

### Step 5: Categorize Jobs

I'll sort jobs into three types:
- **Functional:** The practical task (get a report to my boss)
- **Emotional:** How they want to feel (confident, in control)
- **Social:** How they want to be perceived (competent, innovative)

### Step 6: Score Opportunities

I'll rate each job on:
- **Importance:** How much does this matter?
- **Satisfaction:** How well served is this today?
- **Opportunity** = Importance + (Importance - Satisfaction)

I'll be honest about confidence. If I'm inferring scores from limited data, I'll say so:
> "⚠️ Scores are estimated from this interview. Validate with quantitative research before prioritizing."

## Output Template

```markdown
# Jobs-to-be-Done Analysis

**Source:** [Research inputs]
**Product Context:** [Your product/market]

## Context
*What I found in your files:*
- **Existing personas:** [From personas.md, or "None found"]
- **Known jobs:** [Any JTBD already documented]
- **Product positioning:** [From product.md]

## Jobs Identified

*Opportunity Score = Importance + (Importance - Satisfaction). Higher = bigger opportunity.*

### Functional Jobs
| Job Statement | Importance | Satisfaction | Opportunity | Evidence |
|--------------|------------|--------------|-------------|----------|
| When [situation], I want to [action], so I can [outcome] | 8/10 | 4/10 | 12 | [Quote or behavior] |

### Emotional Jobs
| Job Statement | Importance | Satisfaction | Opportunity | Evidence |
|--------------|------------|--------------|-------------|----------|
| When [situation], I want to feel [emotion], so I can [outcome] | 9/10 | 3/10 | 15 | [Quote or behavior] |

### Social Jobs
| Job Statement | Importance | Satisfaction | Opportunity | Evidence |
|--------------|------------|--------------|-------------|----------|
| When [situation], I want to be seen as [perception] | 7/10 | 5/10 | 9 | [Quote or behavior] |

## Comparison to Existing Personas
*How these jobs relate to your current understanding:*
- **Confirms:** [Jobs that match existing persona JTBD]
- **Expands:** [New jobs not in current personas]
- **Contradicts:** [Jobs that conflict with assumptions]

## Top Opportunities

### 1. [Highest opportunity job]
**Job:** [Full statement]
**Why Underserved:** [Current solutions fail because...]
**Desired Outcomes:**
- [Outcome 1]
- [Outcome 2]
**Solution Space:** [Types of solutions that could address this]

### 2. [Second highest]
[Same structure]

## Feature Request Translation
| Request (What They Said) | Job (What They Need) |
|-------------------------|---------------------|
| "Add a dashboard" | "Know if I'm on track without manual checking" |
| "Export to PDF" | "Share progress with stakeholders who don't have access" |

## Recommendations
1. [How to address top opportunity]
2. [Research to validate]

## Suggested Next Steps
- [ ] Update `personas.md` with new jobs discovered
- [ ] Validate importance/satisfaction scores with quantitative survey
- [ ] Add high-opportunity jobs to backlog for prioritization

---
⚠️ **Note:** Importance and satisfaction scores are estimated from research context. Validate with quantitative research (surveys, larger sample) before making prioritization decisions.
```

## Framework Reference

**Jobs-to-be-Done** (Christensen/Ulwick):
- People don't buy products, they hire them to do a job
- Jobs are stable; solutions change
- Opportunity = Importance + (Importance - Satisfaction)

## Tips for Best Results
1. **I'll connect to your existing personas** - If you keep personas.md updated, I'll show how new jobs relate
2. **I focus on jobs, not solutions** - "I need a hole" not "Hire a drill"
3. **I'll find emotional and social jobs** - They often drive decisions more than functional ones
4. **I'll flag confidence levels** - Low-confidence scores need validation with quantitative research
