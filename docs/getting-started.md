# Getting started

This guide takes you from zero to your first skill execution in under 10 minutes.

## Prerequisites

You need one of:

- [Claude Code](https://www.anthropic.com/claude-code) — recommended
- [GitHub Copilot CLI](https://docs.github.com/en/copilot) with skills extension
- Any agent runtime that supports the SKILL.md format

## 1. Clone the library

```bash
git clone https://github.com/varunk130/ai-customer-discovery-skills.git
cd ai-customer-discovery-skills
```

## 2. Pick a skill

Browse `skills/` or read [`docs/architecture.md`](architecture.md) for the layered overview. For your first run we recommend `interview-decoder` — it has the lowest setup overhead.

## 3. Run a worked example

```bash
# In Claude Code:
> Use the interview-decoder skill on examples/saas-onboarding-research/transcript-01.md
```

The skill will produce a coded transcript with themes, sentiment, contradictions, and follow-up questions.

## 4. Compose a workflow

Once one skill works, try a 2-step pipeline:

```bash
> Run interview-decoder on transcript-01.md, then pipe the output into jtbd-extractor.
```

See [`docs/workflows/`](workflows/) for canonical multi-skill recipes.

## 5. Bring your own data

Drop your real (anonymized!) customer interviews into a local folder and re-run. Never commit customer data to this repo.

## Troubleshooting

| Symptom | Likely cause | Fix |
|--------|-------------|-----|
| Skill not found | Agent doesn't see `skills/` directory | Point your agent at the repo root |
| Output is generic | Input was too short or unstructured | Use the discovery-question-architect skill first |
| Schema validation fails locally | Missing frontmatter field | Run `node scripts/validate-skills.js` and fix |

## Next steps

- Read [`CONTRIBUTING.md`](../CONTRIBUTING.md) if you want to add a skill.
- Watch the [Discussions](https://github.com/varunk130/ai-customer-discovery-skills/discussions) for new releases.
- Star the repo if it helps your work — it genuinely helps with discoverability.