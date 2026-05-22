# Architecture overview

## Mental model

The library follows a single, opinionated path:

```
RAW CUSTOMER SIGNAL  →  CODED INSIGHT  →  VALIDATED OPPORTUNITY
      (capture)            (synthesize)        (decide)
```

Every skill belongs to one of three layers. Skills are designed to *compose* - the output of one is a valid input to the next.

## The three layers

### 1. Capture (raw → structured)

Skills that take messy, unstructured customer signal and produce structured data.

- `signal-archaeologist`
- `interview-decoder`
- `voc-conductor`
- `discovery-question-architect`

### 2. Synthesize (structured → insight)

Skills that take structured data and produce coded, comparable insights.

- `persona-cartographer`
- `jtbd-extractor`
- `journey-shadower`
- `insight-distiller`

### 3. Decide (insight → opportunity)

Skills that take insights and produce a defensible decision artefact.

- `problem-prism`
- `opportunity-triangulator`
- `assumption-excavator`
- `hypothesis-stress-tester`

## Composition pattern

A typical end-to-end discovery cycle uses 4-6 skills:

```
voc-conductor → interview-decoder → jtbd-extractor → opportunity-triangulator → hypothesis-stress-tester
```

See `docs/workflows/` for canonical recipes.

## Why this shape

Most discovery libraries are flat collections of prompts. They produce inconsistent outputs because each skill assumes a different input format. This library enforces a contract: every skill's output schema is a valid input schema for at least one downstream skill. That makes pipelines reliable.

## Non-goals

- This library does **not** ship a runtime, agent harness, or orchestrator. It ships specifications + prompts that any agent can execute.
- It does **not** opine on storage, vector search, or retrieval.
- It is **not** a substitute for talking to customers - it amplifies that work, not replaces it.