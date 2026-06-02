# Synthetic Interview Transcript

> Fully synthetic. Use for testing `jtbd-extractor` without sharing real customer recordings.

**Context:** B2B SaaS analytics product, 40-minute discovery call with the head of growth at a mid-market e-commerce company.

---

**Interviewer:** Walk me through the last time you tried to answer "why did revenue drop last week?"

**Interviewee:** Honestly it took the whole team a day. I pulled the top-line number, our analyst pulled cohort breakdowns, marketing pulled channel-level data. We were all looking at different cuts. By the time we agreed on the cause it was Wednesday and the week was already a write-off.

**Interviewer:** What would "fast enough" look like?

**Interviewee:** I want to ask the question Monday morning and have the answer before standup. Not a dashboard - an actual answer. "Revenue dropped 8% because organic traffic from Brand X campaign dropped off after the budget reset on Friday." Like that.

**Interviewer:** What have you tried?

**Interviewee:** Two BI tools. One was too generic, the other needed a data engineer to maintain. We also tried just having the analyst on Slack, but she's a single point of failure and she's at capacity.

**Interviewer:** What happens if you don't solve this?

**Interviewee:** We keep losing a day a week to ambiguity. Worse, we make a wrong call on where to spend next week's budget because we never figured out what actually moved this week.

---

Run the extractor on this file:

```bash
jtbd-extract examples/synthetic-interview.md
```
