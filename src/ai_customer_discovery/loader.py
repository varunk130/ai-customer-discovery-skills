"""Skill loader.

Walks the ``skills/`` directory of the repository, parses each skill's
front-matter and instructions, and returns a typed in-memory representation.
"""

from __future__ import annotations

import re
from dataclasses import dataclass, field
from pathlib import Path
from typing import Iterable, Iterator

import yaml

FRONT_MATTER_RE = re.compile(r"^---\s*\n(?P<fm>.*?)\n---\s*\n(?P<body>.*)$", re.DOTALL)


@dataclass(frozen=True)
class Skill:
    """A single skill loaded from a SKILL.md file."""

    name: str
    description: str
    path: Path
    instructions: str
    metadata: dict = field(default_factory=dict)

    @property
    def slug(self) -> str:
        return self.path.parent.name


@dataclass
class SkillLibrary:
    """A collection of skills loaded from the repository."""

    root: Path
    skills: list[Skill] = field(default_factory=list)

    def __iter__(self) -> Iterator[Skill]:
        return iter(self.skills)

    def __len__(self) -> int:
        return len(self.skills)

    def by_name(self, name: str) -> Skill:
        for skill in self.skills:
            if skill.name == name or skill.slug == name:
                return skill
        raise KeyError(f"Skill not found: {name}")

    def names(self) -> list[str]:
        return [s.name for s in self.skills]


def _parse_skill_file(path: Path) -> Skill:
    text = path.read_text(encoding="utf-8")
    match = FRONT_MATTER_RE.match(text)
    if not match:
        raise ValueError(f"Missing YAML front-matter in {path}")
    metadata = yaml.safe_load(match.group("fm")) or {}
    name = str(metadata.get("name") or path.parent.name)
    description = str(metadata.get("description") or "").strip()
    return Skill(
        name=name,
        description=description,
        path=path,
        instructions=match.group("body").strip(),
        metadata=metadata,
    )


def discover_skill_files(root: Path) -> Iterable[Path]:
    """Yield every SKILL.md file under ``root``."""
    yield from sorted(root.rglob("SKILL.md"))


def load_skills(root: Path | str = "skills") -> SkillLibrary:
    """Load all skills under ``root`` into a :class:`SkillLibrary`."""
    root_path = Path(root)
    if not root_path.exists():
        raise FileNotFoundError(f"Skills directory not found: {root_path}")
    library = SkillLibrary(root=root_path)
    for skill_file in discover_skill_files(root_path):
        try:
            library.skills.append(_parse_skill_file(skill_file))
        except ValueError:
            continue
    return library
