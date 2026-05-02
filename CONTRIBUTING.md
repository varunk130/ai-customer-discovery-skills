# Contributing to ai-customer-discovery-skills

First — thank you for considering a contribution. This project ships AI skills that handle real customer research data, so contribution standards are stricter than a typical script library.

> **TL;DR**: All changes go through a Pull Request. The `main` branch is protected. The maintainer (@varunk130) is the sole reviewer required for merge.

---

## Table of Contents

- [Ground rules](#ground-rules)
- [Branching model](#branching-model)
- [Commit conventions](#commit-conventions)
- [Pull Request process](#pull-request-process)
- [Authoring a new skill](#authoring-a-new-skill)
- [SKILL.md schema](#skillmd-schema)
- [Local validation](#local-validation)
- [Style guide](#style-guide)
- [Reporting bugs](#reporting-bugs)
- [Proposing new skills](#proposing-new-skills)
- [Code of Conduct](#code-of-conduct)

---

## Ground rules

1. **Never commit customer data.** Even sample interview transcripts must be synthetic or fully redacted.
2. **No direct pushes to `main`.** The branch is protected by a ruleset. PRs are required.
3. **One concern per PR.** Easier to review, easier to revert, better for the contribution graph.
4. **Open an issue first** for substantial changes (>100 lines, new skill, breaking change).
5. **All discussions happen in the open** — use Issues or Discussions, not DMs.

---

## Branching model

We use a simple trunk-based flow:

- `main` — protected, always releasable.
- `feat/<short-name>` — new skills or features.
- `fix/<short-name>` — bug fixes.
- `docs/<short-name>` — documentation only.
- `chore/<short-name>` — tooling, CI, configs.
- `refactor/<short-name>` — internal restructuring with no behavior change.

Branches are deleted on merge.

---

## Commit conventions

We follow [Conventional Commits 1.0.0](https://www.conventionalcommits.org/):

```
<type>(<optional scope>): <short description>

<optional body>

<optional footer>
```

Allowed types: `feat`, `fix`, `docs`, `chore`, `ci`, `refactor`, `test`, `style`, `perf`.

Examples:

- `feat(persona-cartographer): add relationship-edge inference`
- `docs: clarify SKILL.md `inputs` schema`
- `ci: add markdown link check workflow`

Breaking changes use `!` after the type, e.g. `feat!: rename input field`.

---

## Pull Request process

1. **Fork or branch** from the latest `main`.
2. **Open a draft PR early** if you want feedback while iterating.
3. **Fill the PR template completely** — it asks the questions reviewers need.
4. **Pass CI** — lint, link check, and SKILL.md schema validator must be green.
5. **Request review** from `@varunk130`. Other contributors may comment, but only the maintainer can approve and merge.
6. **Resolve review threads** before requesting re-review.
7. **Squash on merge.** Keep `main` history linear and readable.

> **Branch protection rules in effect:**
> - PR required, no direct pushes
> - 1 approving review required (maintainer)
> - Stale reviews dismissed on push
> - All review threads must be resolved
> - Linear history required (no merge commits on `main`)
> - Force-push and deletion blocked

---

## Authoring a new skill

A "skill" is a reusable unit of AI-assisted work — it lives in `skills/<skill-name>/` and is invoked from Claude Code, GitHub Copilot, or any agent harness that supports the skill format.

Every skill folder must contain:

```
skills/<skill-name>/
├── SKILL.md              # spec — required
├── README.md             # human overview — required
├── examples/             # at least 1 worked example — required
│   └── basic-example.md
└── prompts/              # optional reusable prompt fragments
```

Open a [`new-skill-proposal` issue](.github/ISSUE_TEMPLATE/new_skill_proposal.yml) before authoring. This helps avoid duplicate work and ensures the skill fits the library's scope (the customer discovery → insight → opportunity lifecycle).

---

## SKILL.md schema

Every `SKILL.md` must include the following frontmatter and sections:

```markdown
---
name: skill-name
version: 0.1.0
description: One-sentence description (max 140 chars)
when_to_use:
  - Trigger condition 1
  - Trigger condition 2
inputs:
  - name: input_name
    type: string | markdown | json | file
    required: true
    description: ...
outputs:
  - name: output_name
    type: markdown | json
    description: ...
tags: [discovery, synthesis, ...]
maintainer: "@varunk130"
---

# <skill-name>

## Purpose
...

## Instructions
1. ...
2. ...

## Output format
...

## Examples
See `examples/`.

## Limitations
...
```

The CI workflow `validate-skills.yml` enforces this schema.

---

## Local validation

Before opening a PR:

```bash
# Lint markdown
npx markdownlint-cli2 "**/*.md"

# Check links
npx markdown-link-check **/*.md

# Validate SKILL.md schema (script in scripts/)
node scripts/validate-skills.js
```

CI runs the same checks on every PR.

---

## Style guide

- Use **sentence case** for headings (`## How it works`, not `## How It Works`).
- Wrap markdown at ~100 chars where reasonable.
- Use fenced code blocks with a language tag.
- Prefer concrete examples over abstract description.
- Avoid jargon without definition.

---

## Reporting bugs

Use the [bug report template](.github/ISSUE_TEMPLATE/bug_report.yml). Include:

- Skill name and version
- Steps to reproduce
- Expected vs. actual output
- Agent/runtime (Claude Code, Copilot CLI, etc.)

---

## Proposing new skills

Use the [new skill proposal template](.github/ISSUE_TEMPLATE/new_skill_proposal.yml). The maintainer will tag it `roadmap` if accepted.

---

## Code of Conduct

This project follows the [Contributor Covenant 2.1](CODE_OF_CONDUCT.md). By participating you agree to abide by it.