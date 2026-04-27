# Basic example: assumption-excavator

## Input
PRD for adding an enterprise SSO tier at /mo seat add-on.

## Expected output (abbreviated)
- **User assumption**: "Enterprise admins want SSO bundled separately." → Test: 5 customer interviews. Cost: Cheap. Failure cost: Painful.
- **Business assumption**: "Customers will pay $2k/mo as an add-on rather than expect it included." → Test: pricing survey + 3 sales conversations. Cost: Cheap. Failure cost: Catastrophic.
- **Technical assumption**: "Existing identity service can support SCIM at this scale." → Test: load test. Cost: Moderate. Failure cost: Catastrophic.

**Validate first** (cheap × catastrophic): the $2k pricing assumption — wrong here, the entire bet is voided.