<div align="center">

# 🎯 AI Customer Discovery Skills

### Turn raw customer signal into validated product opportunities — in minutes, not weeks

[![Skills](https://img.shields.io/badge/Shipped_Skills-4-blue?style=for-the-badge)](#-skills-catalog)
[![Roadmap](https://img.shields.io/badge/Target-12_skills-orange?style=for-the-badge)](#-roadmap)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg?style=for-the-badge)](LICENSE)
[![Built with Claude Code](https://img.shields.io/badge/Built_with-Claude_Code-D97757?logo=anthropic&logoColor=white&style=for-the-badge)](https://claude.ai/code)
[![GitHub Copilot](https://img.shields.io/badge/GitHub-Copilot-24292e?logo=github&logoColor=white&style=for-the-badge)](https://github.com/features/copilot)

**Maintained by [Varun Kulkarni](https://github.com/varunk130)**

</div>

---

## 🔭 The Discovery Flywheel

```mermaid
flowchart LR
    subgraph SIGNAL["📥 RAW SIGNAL"]
        S1["Support tickets"]
        S2["Sales call notes"]
        S3["NPS / surveys"]
        S4["Interviews"]
    end

    subgraph SKILLS["🧠 DISCOVERY SKILLS"]
        K1["feedback-prioritizer<br/>RSCF ranking"]
        K2["competitive-analyzer<br/>buyer-weighted teardown"]
        K3["assumption-mapper<br/>K/B/H × Crit/Low"]
        K4["north-star-metric-finder<br/>5-criteria pick"]
    end

    subgraph OUTPUT["🎯 VALIDATED OPPORTUNITY"]
        O1["Ranked backlog"]
        O2["Defensible competitive POV"]
        O3["Ranked test plan"]
        O4["North Star + input metrics"]
    end

    SIGNAL --> K1 --> O1
    SIGNAL --> K2 --> O2
    SIGNAL --> K3 --> O3
    SIGNAL --> K4 --> O4

    classDef skill fill:#1a73e8,color:#fff,stroke:#1558b0,stroke-width:2px,rx:6,ry:6
    classDef signal fill:#fef7e0,color:#202124,stroke:#fbbc04,stroke-width:1px,rx:6,ry:6
    classDef output fill:#e6f4ea,color:#0d652d,stroke:#0d652d,stroke-width:2px,rx:6,ry:6
    class K1,K2,K3,K4 skill
    class S1,S2,S3,S4 signal
    class O1,O2,O3,O4 output
```

---

## Why This Library Exists

Customer discovery is the first place product work goes wrong: signals get cherry-picked, opportunities get sized by gut feel, and personas get over-fitted to whoever shouted loudest in the last interview. This library captures the structured workflows that turn raw signal into evidence — each skill is a self-contained markdown file that any compatible AI agent can load on demand.

---

## ⚡ Quickstart

```bash
# 1. Clone the repo
git clone https://github.com/varunk130/ai-customer-discovery-skills.git

# 2. Install skills globally for Claude Code
mkdir -p ~/.claude/skills
cp -r ai-customer-discovery-skills/skills/* ~/.claude/skills/

# 3. Restart Claude Code, then run a skill:
#      /feedback-prioritizer        — triage a backlog of support tickets
#      /competitive-analyzer        — score competitors on buyer dimensions
#      /assumption-mapper           — surface and rank bet-killing assumptions
#      /north-star-metric-finder    — pick a 2-year-horizon north star
```

**GitHub Copilot users:** copy the same `skills/` directory into `.github/skills/` in any repo and invoke via natural language.

**Project-local install:** drop the skills into `.claude/skills/` inside your project to scope them to one codebase.

---

## 📋 Skills Catalog

| Skill | What it does | Use when |
|-------|--------------|----------|
| [competitive-analyzer](skills/competitive-analyzer/SKILL.md) | Disciplined competitive teardown that picks the 4–6 buyer-weighted dimensions, scores every competitor, and surfaces gap + risk maps | You need a defensible competitive analysis that changes a decision, not a 40-row feature grid |
| [north-star-metric-finder](skills/north-star-metric-finder/SKILL.md) | Identifies a candidate North Star Metric using five strict criteria, then maps the input metrics that drive it | You're picking the single metric that will steer two years of roadmap decisions |
| [feedback-prioritizer](skills/feedback-prioritizer/SKILL.md) | Triages raw customer feedback into a ranked list using the RSCF model, with an explicit `Do Not Act` list for vocal-minority signals | A backlog of tickets / interviews / NPS / sales notes is piling up and the team needs focus |
| [assumption-mapper](skills/assumption-mapper/SKILL.md) | Surfaces hidden assumptions, classifies them Known / Believed / Hoped × Critical–Low, and outputs a ranked test plan | You're about to commit real investment to a bet and need to know what could kill it first |

---

## 🗺 Roadmap

4 of 12 skills shipped. Additional skills planned: persona-validator, jtbd-mapper, opportunity-sizer, switch-cost-analyzer, willingness-to-pay-tester, and more. Watch this repo for releases.

---

## License

[MIT](LICENSE) — use freely, attribution appreciated.
