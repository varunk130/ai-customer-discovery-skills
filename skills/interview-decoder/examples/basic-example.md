# Basic example: interview-decoder

## Input

30-min onboarding interview transcript with a B2B SaaS customer.

## Expected output (abbreviated)

**Contradiction (High):**
- @04:12 "I never use the dashboard, our team lives in Slack."
- @19:48 "First thing I do every Monday is check the weekly summary on the dashboard."
→ Likely: dashboard usage is occasional but high-stakes.

**Unspoken assumption:**
- Participant said "of course we use SSO." This is treated as universal — but our pricing page lists SSO as Enterprise-only.

**Follow-up #1:** When you said the dashboard is "the source of truth," who else on your team treats it that way?