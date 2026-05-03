"""Tests for the loader module."""

from __future__ import annotations

from pathlib import Path

import pytest

from ai_customer_discovery.loader import Skill, load_skills
from ai_customer_discovery.runner import SkillRunner


@pytest.fixture()
def sample_skills(tmp_path: Path) -> Path:
    root = tmp_path / "skills"
    (root / "signal-extractor").mkdir(parents=True)
    (root / "signal-extractor" / "SKILL.md").write_text(
        "---\n"
        "name: signal-extractor\n"
        "description: Extract customer signals from raw transcripts.\n"
        "---\n"
        "Step 1: read the transcript.\n"
        "Step 2: extract signals.\n",
        encoding="utf-8",
    )
    (root / "jtbd-mapper").mkdir(parents=True)
    (root / "jtbd-mapper" / "SKILL.md").write_text(
        "---\n"
        "name: jtbd-mapper\n"
        "description: Map signals to Jobs-to-be-Done.\n"
        "---\n"
        "Map each signal to a JTBD.\n",
        encoding="utf-8",
    )
    return root


def test_load_skills_finds_all(sample_skills: Path) -> None:
    library = load_skills(sample_skills)
    assert len(library) == 2
    assert set(library.names()) == {"signal-extractor", "jtbd-mapper"}


def test_skill_lookup_by_name_and_slug(sample_skills: Path) -> None:
    library = load_skills(sample_skills)
    by_name = library.by_name("signal-extractor")
    assert isinstance(by_name, Skill)
    assert by_name.description.startswith("Extract")


def test_skill_lookup_missing_raises(sample_skills: Path) -> None:
    library = load_skills(sample_skills)
    with pytest.raises(KeyError):
        library.by_name("does-not-exist")


def test_load_skills_missing_root(tmp_path: Path) -> None:
    with pytest.raises(FileNotFoundError):
        load_skills(tmp_path / "missing")


def test_runner_renders_prompt(sample_skills: Path) -> None:
    library = load_skills(sample_skills)
    skill = library.by_name("signal-extractor")
    runner = SkillRunner()
    output = runner.run(skill, "transcript text here")
    assert "signal-extractor" in output
    assert "transcript text here" in output
    assert "Instructions" in output
