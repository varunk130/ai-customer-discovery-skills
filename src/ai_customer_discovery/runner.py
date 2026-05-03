"""Lightweight skill runner.

Provides a uniform interface for invoking a loaded :class:`Skill` against an
LLM backend. The default backend simply renders the prompt — real backends
(Anthropic, OpenAI, local models) can be plugged in via ``backend``.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Callable, Protocol

from .loader import Skill


class Backend(Protocol):
    def __call__(self, prompt: str, **kwargs) -> str:  # pragma: no cover
        ...


def _echo_backend(prompt: str, **_: object) -> str:
    """Default no-op backend: returns the rendered prompt verbatim."""
    return prompt


@dataclass
class SkillRunner:
    """Render a skill's instructions with user input and call a backend."""

    backend: Backend = _echo_backend

    def render(self, skill: Skill, user_input: str) -> str:
        return (
            f"# Skill: {skill.name}\n"
            f"{skill.description}\n\n"
            f"## Instructions\n{skill.instructions}\n\n"
            f"## User Input\n{user_input}\n"
        )

    def run(self, skill: Skill, user_input: str, **kwargs) -> str:
        prompt = self.render(skill, user_input)
        return self.backend(prompt, **kwargs)


def make_runner(backend: Callable[..., str] | None = None) -> SkillRunner:
    return SkillRunner(backend=backend or _echo_backend)
