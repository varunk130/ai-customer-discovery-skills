# Jobs-to-be-Done Analysis

**Source:** 12 customer interviews (Enterprise PM & Engineering leads), 47 NPS open-ended responses, 23 support tickets  
**Product Context:** B2B SaaS project management platform for cross-functional teams (50-500 seat orgs)  
**Date:** March 30, 2026  
**Analyst:** JTBD Extractor (Claude Code Skill)

---

## Context

*What I found in your files:*

- **Existing personas:** 3 personas documented - "Overloaded PM", "Engineering Lead", "Executive Sponsor"
- **Known jobs:** Personas had functional tasks listed but no formal JTBD statements or emotional/social jobs
- **Product positioning:** Positioned as "the single source of truth for project execution" - strong on task management, weaker on stakeholder communication

---

## Jobs Identified

*Opportunity Score = Importance + (Importance − Satisfaction). Higher = bigger opportunity.*

### ⚙️ Functional Jobs

| Job Statement | Imp. | Sat. | Opp. | Evidence |
|---|---|---|---|---|
| **When** preparing for a weekly leadership sync, **I want to** see cross-team status at a glance, **so I can** report progress without chasing 5 people for updates | 9 | 3 | 15 | *"I spend 2 hours every Monday morning Slacking people for updates just to fill out a slide."* - PM, Series C fintech |
| **When** a project timeline shifts, **I want to** instantly see downstream impact on dependencies, **so I can** re-prioritize before things break | 9 | 4 | 14 | *"By the time I realize something slipped, three other teams are already blocked."* - Eng Lead, healthtech |
| **When** onboarding a new team member mid-project, **I want to** give them full context in one place, **so I can** get them productive in days instead of weeks | 8 | 3 | 13 | *"New hires spend their first two weeks just figuring out where things live."* - PM, edtech |
| **When** scoping a new initiative, **I want to** reference how similar past projects actually went, **so I can** give realistic estimates instead of guessing | 8 | 2 | 14 | *"We keep making the same estimation mistakes because nobody looks back at what actually happened."* - VP Eng, logistics |
| **When** a stakeholder asks about a specific deliverable, **I want to** pull up its full history and current state, **so I can** answer confidently without digging through Slack threads | 7 | 4 | 10 | *"I end up scrolling through 3 months of Slack to find who decided what and when."* - PM, martech |

### 💜 Emotional Jobs

| Job Statement | Imp. | Sat. | Opp. | Evidence |
|---|---|---|---|---|
| **When** presenting project status to executives, **I want to feel** confident and in control, **so I can** advocate for my team without anxiety | 9 | 3 | 15 | *"The worst feeling is when the CEO asks a question and I have to say 'let me get back to you.'"* - Sr. PM, enterprise SaaS |
| **When** managing 4+ concurrent projects, **I want to feel** like nothing is falling through the cracks, **so I can** sleep at night and not dread Monday mornings | 9 | 4 | 14 | *"I wake up at 3am thinking 'did I follow up on that thing?' It's unsustainable."* - PM, fintech |
| **When** dependencies slip and deadlines are at risk, **I want to feel** empowered to act quickly, **so I can** resolve issues before they escalate into fire drills | 8 | 3 | 13 | *"I don't mind problems - I mind finding out about them too late to do anything."* - Eng Lead, healthtech |
| **When** my project succeeds, **I want to feel** recognized for the coordination work, **so I can** stay motivated in a role that's often invisible | 7 | 3 | 11 | *"Engineering gets the credit for shipping. Nobody sees the 200 decisions I made to keep it on track."* - PM, edtech |

### 👥 Social Jobs

| Job Statement | Imp. | Sat. | Opp. | Evidence |
|---|---|---|---|---|
| **When** presenting to leadership, **I want to be seen as** someone who has everything under control, **so I can** earn trust for larger, more strategic initiatives | 9 | 4 | 14 | *"If I look like I'm scrambling, they won't give me the big projects."* - Sr. PM, enterprise SaaS |
| **When** working across engineering, design, and business teams, **I want to be seen as** a fair and transparent coordinator, **so I can** maintain trust when making hard tradeoff calls | 8 | 5 | 11 | *"If people think I'm playing favorites with priorities, the whole system breaks down."* - PM, fintech |
| **When** proposing process changes, **I want to be seen as** data-driven and pragmatic (not bureaucratic), **so I can** get buy-in without being labeled 'the process person' | 7 | 3 | 11 | *"The moment you say 'process improvement,' engineers tune out. I need data to back it up."* - PM, logistics |

---

## Comparison to Existing Personas

*How these jobs relate to your current understanding:*

- **Confirms:** "Overloaded PM" persona's core pain around status reporting and multi-project juggling is strongly validated. 11 of 12 interviewees mentioned this unprompted.
- **Expands:** Emotional and social jobs were entirely missing from persona docs. The anxiety around executive visibility and the desire for recognition are significant drivers - possibly more than functional gaps.
- **Contradicts:** Persona docs assumed "Engineering Lead" primarily cares about sprint velocity. Interviews reveal they care more about **early warning on cross-team dependencies** than internal team speed.

---

## Top Opportunities

### 1. Auto-Generated Status Intelligence
**Job:** When preparing for a weekly leadership sync, I want to see cross-team status at a glance, so I can report progress without chasing people for updates.  
**Opportunity Score:** 15  
**Why Underserved:** Current tools require manual updates that are always stale. PMs spend 2-3 hours/week compiling status from Slack, docs, and tickets.  
**Desired Outcomes:**
- Status is always current without anyone manually updating it
- I can generate an exec-ready summary in under 60 seconds
- Changes since last week are highlighted automatically

**Solution Space:** AI-generated status rollups from activity signals (commits, ticket updates, Slack threads, doc edits). Auto-drafted weekly summary with anomaly detection.

---

### 2. Dependency Impact Radar
**Job:** When a project timeline shifts, I want to instantly see downstream impact on dependencies, so I can re-prioritize before things break.  
**Opportunity Score:** 14  
**Why Underserved:** Dependency tracking exists but is manual and static. No tool proactively alerts when a slip in Team A creates a cascade risk for Teams B, C, D.  
**Desired Outcomes:**
- Alerted within hours (not days) when a dependency is at risk
- Can see the full blast radius of a delay in one view
- Can simulate "what if this slips 2 weeks?" scenarios

**Solution Space:** Dynamic dependency graph with real-time health signals. Automated risk propagation alerts. Scenario modeling for timeline changes.

---

### 3. Historical Project Intelligence
**Job:** When scoping a new initiative, I want to reference how similar past projects actually went, so I can give realistic estimates instead of guessing.  
**Opportunity Score:** 14  
**Why Underserved:** Retrospectives happen but insights aren't structured or searchable. Estimation debt compounds across quarters.  
**Desired Outcomes:**
- Can search "projects like this" and see actual timelines vs. estimates
- Pattern recognition: "projects with 3+ team dependencies typically take 40% longer"
- New team members can learn from institutional history

**Solution Space:** Structured project archives with tagging. AI-powered estimation assistant trained on your org's actual delivery data.

---

## Feature Request Translation

| What They Asked For | The Real Job |
|---|---|
| "Add a dashboard" | Know if I'm on track without manually compiling status |
| "Gantt chart view" | See dependency chains and identify cascade risks at a glance |
| "Export to PDF" | Share progress with executives who won't log into our tool |
| "Slack integration" | Get alerted about risks in my existing workflow, not another app |
| "More chart types" | Tell a compelling, data-backed story to justify my team's work |
| "API access" | Connect project data to our BI tools so leadership trusts the numbers |
| "Templates for projects" | Stop reinventing the wheel and learn from what worked before |
| "Better search" | Find the decision history for any deliverable without archaeology |
| "Mobile app" | Check status during back-to-back meetings without opening a laptop |
| "Permissions/roles" | Share the right level of detail with each audience without manual filtering |

---

## Recommendations

1. **Prioritize auto-generated status intelligence** - it's the #1 opportunity and directly addresses the most emotionally charged pain point (executive anxiety). Quick wins: AI-drafted weekly summaries from existing activity data.

2. **Build the dependency impact radar as a differentiator** - competitors have dependency tracking, but nobody does proactive cascade alerting well. This is a moat opportunity.

3. **Don't build a Gantt chart** - the underlying job is about dependency visibility, not the specific visualization. A dynamic dependency graph with health signals would serve the job better.

4. **Surface emotional jobs in your marketing** - "Sleep better knowing nothing's falling through the cracks" will resonate more than "Track tasks across teams."

---

## Suggested Next Steps

- [ ] Update `personas.md` with emotional and social jobs discovered
- [ ] Validate opportunity scores with quantitative survey (n=100+ PMs)
- [ ] Run a design sprint on "auto-generated status intelligence" - highest opportunity, clearest solution space
- [ ] Add "dependency impact" questions to next round of user interviews
- [ ] Share Feature Request Translation table with engineering to reframe backlog items

---

⚠️ **Note:** Importance and satisfaction scores are estimated from 12 interviews + 47 NPS responses. Directionally strong but validate with a larger quantitative sample before making major prioritization decisions. Emotional and social job scores have lower confidence (fewer direct data points) - consider dedicated interview questions in next research round.
