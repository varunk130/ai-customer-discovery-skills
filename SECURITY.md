# Security Policy

## Reporting a Vulnerability

These skills consume potentially sensitive customer research data (interviews, support tickets, NPS responses). Please report any vulnerability or data-handling concern privately.

**Do not** open a public issue for security reports.

Instead:

1. Open a private security advisory at https://github.com/varunk130/ai-customer-discovery-skills/security/advisories/new
2. Or email the maintainer (see profile).

You can expect:

- Acknowledgment within 7 days
- A coordinated fix or mitigation plan
- Credit in the changelog if you wish

## Supported Versions

Only the latest minor release on the `main` branch is supported.

## Scope

In scope:

- Prompt injection vulnerabilities in shipped skills
- Data leakage between skills
- Insecure default examples

Out of scope:

- Issues in third-party tools (Claude Code, GitHub Copilot)
- Misuse of skills outside their documented intent