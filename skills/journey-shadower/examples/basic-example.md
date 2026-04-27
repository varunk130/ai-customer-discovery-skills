# Basic example: journey-shadower

## Input
Persona: Maya, mid-market controller. Scenario: First 24 hours after signing up for an accounting integration tool.

## Expected output (abbreviated)
| Hour | Goal | Action | Expected | Got | Friction |
|---|---|---|---|---|---|
| 0:00 | Verify the tool fits | Sign up | Free trial without CC | Asked for CC | 4 |
| 0:08 | Connect QuickBooks | Click "Connect" | OAuth in 2 clicks | Redirected to docs page | 3 |
| 1:30 | First report | Run "month close" | Report with line items | Empty state — sync still running | 5 |

**Friction hotspot #1** (score 5): Sync takes >1hr but UI does not communicate this. Fix: add expected-time indicator or async email.