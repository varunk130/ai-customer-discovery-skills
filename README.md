# AI Customer Discovery Skills

4 shipped skills for product discovery (target: 12) — from raw customer signal to validated opportunity — from raw customer signal to validated opportunity. Built for [Claude Code](https://docs.anthropic.com/en/docs/claude-code) and [GitHub Copilot](https://github.com/features/copilot).

## Why This Library Exists

Customer discovery is the first place product work goes wrong: signals get cherry-picked, opportunities get sized by gut feel, and personas get over-fitted to whoever shouted loudest in the last interview. This library captures the structured workflows that turn raw signal into evidence — each skill is a self-contained markdown file that any compatible AI agent can load on demand.

## Skills Catalog

| Skill | What it does | Use when |
|-------|--------------|----------|
| [competitive-analyzer](skills/competitive-analyzer/SKILL.md) | Disciplined competitive teardown that picks the 4–6 buyer-weighted dimensions, scores every competitor, and surfaces gap + risk maps | You need a defensible competitive analysis that changes a decision, not a 40-row feature grid |
| [north-star-metric-finder](skills/north-star-metric-finder/SKILL.md) | Identifies a candidate North Star Metric using five strict criteria, then maps the input metrics that drive it | You're picking the single metric that will steer two years of roadmap decisions |
| [feedback-prioritizer](skills/feedback-prioritizer/SKILL.md) | Triages raw customer feedback into a ranked list using the RSCF model, with an explicit `Do Not Act` list for vocal-minority signals | A backlog of tickets / interviews / NPS / sales notes is piling up and the team needs focus |
| [assumption-mapper](skills/assumption-mapper/SKILL.md) | Surfaces hidden assumptions, classifies them Known / Believed / Hoped × Critical–Low, and outputs a ranked test plan | You're about to commit real investment to a bet and need to know what could kill it first |

## Installation

```bash
git clone https://github.com/varunk130/ai-customer-discovery-skills.git
cp -r ai-customer-discovery-skills/skills/* ~/.claude/skills/
```

Restart Claude Code (or your agent of choice) and invoke skills via slash commands or natural-language prompts.

## License

MIT
