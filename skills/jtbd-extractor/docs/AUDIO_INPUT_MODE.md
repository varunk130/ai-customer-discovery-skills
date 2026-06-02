# Audio Input Mode - Scaffolding & Operating Notes

This document describes how the project is structured to *prepare* for audio interview input via Whisper transcription, without enabling any live transcription calls or external dependencies. Today the skill expects clean text input; this file documents the planned env-var toggle, the adapter seam, and the diarization schema - so the path from text-only to audio-supported is a configuration change, not a refactor.

> **No Whisper integration is wired in this commit.** Every code path still expects text input. This is scaffolding only - schema, documented adapter seam, and operating notes. Anyone who later wires the actual transcription has a single, well-defined function to patch.

---

## Why Scaffold Now (and Not Wire Yet)

- The repository is a public technical demonstration. Wiring Whisper would either bundle a multi-GB local model (heavy, fragile) or require an API key (high friction for visitors).
- The text-input mode is the *correct default* for the demo. Audio input should be an opt-in for self-hosted deployments only.
- Decoupling the audio adapter from the JTBD extraction pipeline is independently valuable - it lets future contributors swap transcription backends (Whisper local, Whisper API, AssemblyAI, Deepgram) behind one stable interface.

---

## The Three Modes

The skill is structured around three operating modes, selected by environment variable. Today only `text` is implemented end-to-end; `audio-local` and `audio-api` are documented seams.

| Mode | `INPUT_MODE` value | Behavior | Status |
|------|--------------------|----------|--------|
| **Text** (default) | unset, or `text` | Skill expects clean transcript text on stdin / as input | ✅ Implemented |
| **Audio (local)** | `audio-local` | Routes audio file → local Whisper model → transcript with diarization → existing JTBD pipeline | 🟡 Scaffolded - adapter seam is documented |
| **Audio (API)** | `audio-api` | Same as `audio-local`, but uses an HTTP API for transcription | 🟡 Scaffolded |

**Resolution rule:** if `INPUT_MODE` is `audio-local` or `audio-api` but the required dependencies / credentials are missing, the application **must** error with a clear message. The skill never silently degrades from audio to a guess.

---

## Environment Variables

| Variable | Default | Used By | Notes |
|----------|---------|---------|-------|
| `INPUT_MODE` | `text` | All adapters | One of: `text`, `audio-local`, `audio-api` |
| `WHISPER_MODEL_PATH` | *(unset)* | `audio-local` mode | Path to local Whisper model weights |
| `WHISPER_API_URL` | *(unset)* | `audio-api` mode | URL of the transcription API (any OpenAI-Whisper-compatible endpoint) |
| `WHISPER_API_KEY` | *(unset)* | `audio-api` mode | API key; absence in `audio-api` mode is a hard error |
| `MAX_AUDIO_SECONDS` | `7200` | Cost guardrail | Reject files over 2 hours; longer interviews need explicit chunking |
| `DIARIZATION_ENABLED` | `true` | Both audio modes | Whether to run speaker diarization for quote attribution |

---

## Cost & Resource Guardrails

These run *before* any transcription would be issued, so they apply even if the call site is later wired:

1. **Audio length cap** - reject files over `MAX_AUDIO_SECONDS` (default 2 hours).
2. **Format whitelist** - only `.mp3`, `.wav`, `.m4a`, `.ogg`, `.flac` accepted. Other formats fail fast with a clear error.
3. **Local-first preference** - `audio-local` mode is the recommended path for sensitive customer interviews so audio never leaves the machine.
4. **Cache-by-content-hash** - transcribed text is cached on disk keyed by `sha256(audio_file)` so repeated runs of the same interview do not re-transcribe.

---

## Diarization Schema

When `DIARIZATION_ENABLED=true`, the transcription adapter must return text in this normalized form so downstream JTBD extraction can attribute quotes:

```jsonc
{
  "audio_source": "interview-2026-04-12-acme.mp3",
  "audio_duration_sec": 2847,
  "speakers": [
    { "id": "S1", "label": "Interviewer", "speaking_time_sec": 412 },
    { "id": "S2", "label": "Participant", "speaking_time_sec": 2435 }
  ],
  "segments": [
    {
      "start_sec": 0.0,
      "end_sec": 12.4,
      "speaker_id": "S1",
      "text": "Thanks for joining today. Walk me through the last time you ran into this problem."
    },
    {
      "start_sec": 12.6,
      "end_sec": 38.2,
      "speaker_id": "S2",
      "text": "Sure. So this was last Tuesday — I was trying to..."
    }
  ]
}
```

Speaker labels (`Interviewer` / `Participant`) are filled by a simple heuristic (longer cumulative speaking time = participant) unless explicitly provided. Quote attribution in JTBD output uses `speaker_id` so labels can be re-mapped without losing traceability.

---

## The Single Documented Seam

When wiring real transcription later, exactly **one** function should change:

```
src/audio_adapter.transcribe(audio_path: str) -> DiarizedTranscript
```

Currently this function raises `NotImplementedError` with a message pointing at this document. The live implementation:
1. Validates the file (format, length, exists)
2. Routes to local model OR API based on `INPUT_MODE`
3. Caches by file hash if `INPUT_MODE` ≠ `text`
4. Returns the diarization schema above

Everything downstream - JTBD extraction, quote attribution, opportunity scoring - already consumes the diarization schema (it's the same shape as a hand-prepared transcript with speaker tags), so wiring this function alone is sufficient.

---

## Roadmap Beyond Scaffolding

Out of scope for this commit:

- [ ] Wire the actual `transcribe()` adapter for `audio-local` mode (faster-whisper recommended)
- [ ] Wire the `audio-api` adapter against an OpenAI-Whisper-compatible endpoint
- [ ] Add chunking for files > `MAX_AUDIO_SECONDS` (split → transcribe → re-stitch with offsets preserved)
- [ ] Add a `--smoke-test` CLI flag that transcribes a 10-second sample to verify connectivity
- [ ] Per-interview cost report (estimated tokens / API call cost / local-model wall time)

---

## Workflow When Implemented

```
.mp3 / .wav / .m4a
      │
      ▼
[audio_adapter.transcribe]   ← single seam to wire
      │
      ▼
DiarizedTranscript (JSON)
      │
      ▼
[existing JTBD extraction]   ← unchanged
      │
      ▼
JTBD statements with speaker-attributed quotes
```

The seam ensures the JTBD pipeline never has to know whether its input came from text, local Whisper, or an API.
