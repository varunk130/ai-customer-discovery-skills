"""Data models for JTBD analysis."""

from dataclasses import dataclass, field
from typing import Optional
import json


@dataclass
class Job:
    """A single Jobs-to-be-Done statement with scoring."""
    situation: str
    action: str
    outcome: str
    category: str  # "functional", "emotional", "social"
    importance: int  # 1-10
    satisfaction: int  # 1-10
    evidence: str = ""
    icon: str = ""

    @property
    def opportunity(self) -> int:
        return self.importance + (self.importance - self.satisfaction)

    @property
    def statement(self) -> str:
        verb = {
            "functional": "I want to",
            "emotional": "I want to feel",
            "social": "I want to be seen as",
        }.get(self.category, "I want to")
        return f"When {self.situation}, {verb} {self.action}, so I can {self.outcome}"

    def to_dict(self) -> dict:
        return {
            "situation": self.situation, "action": self.action, "outcome": self.outcome,
            "category": self.category, "importance": self.importance,
            "satisfaction": self.satisfaction, "opportunity": self.opportunity,
            "evidence": self.evidence, "icon": self.icon, "statement": self.statement,
        }


@dataclass
class Translation:
    """Maps a feature request to the real underlying job."""
    request: str
    real_job: str

    def to_dict(self) -> dict:
        return {"request": self.request, "real_job": self.real_job}


@dataclass
class PersonaComparison:
    """How findings relate to existing personas."""
    confirms: str = ""
    expands: str = ""
    contradicts: str = ""

    def to_dict(self) -> dict:
        return {"confirms": self.confirms, "expands": self.expands, "contradicts": self.contradicts}


@dataclass
class JTBDAnalysis:
    """Complete JTBD analysis results."""
    title: str = "Jobs-to-be-Done Analysis"
    product_context: str = ""
    source: str = ""
    author: str = "JTBD Extractor"
    date: str = ""
    jobs: list[Job] = field(default_factory=list)
    translations: list[Translation] = field(default_factory=list)
    recommendations: list[str] = field(default_factory=list)
    persona_comparison: Optional[PersonaComparison] = None

    @property
    def functional_jobs(self) -> list[Job]:
        return sorted([j for j in self.jobs if j.category == "functional"], key=lambda j: -j.opportunity)

    @property
    def emotional_jobs(self) -> list[Job]:
        return sorted([j for j in self.jobs if j.category == "emotional"], key=lambda j: -j.opportunity)

    @property
    def social_jobs(self) -> list[Job]:
        return sorted([j for j in self.jobs if j.category == "social"], key=lambda j: -j.opportunity)

    @property
    def top_opportunities(self) -> list[Job]:
        return sorted(self.jobs, key=lambda j: -j.opportunity)[:6]

    @property
    def stats(self) -> dict:
        return {
            "total_jobs": len(self.jobs),
            "functional": len(self.functional_jobs),
            "emotional": len(self.emotional_jobs),
            "social": len(self.social_jobs),
            "max_opportunity": max((j.opportunity for j in self.jobs), default=0),
            "avg_opportunity": round(sum(j.opportunity for j in self.jobs) / len(self.jobs), 1) if self.jobs else 0,
        }

    def to_dict(self) -> dict:
        return {
            "title": self.title, "product_context": self.product_context,
            "source": self.source, "author": self.author, "date": self.date,
            "jobs": [j.to_dict() for j in self.jobs],
            "translations": [t.to_dict() for t in self.translations],
            "recommendations": self.recommendations,
            "persona_comparison": self.persona_comparison.to_dict() if self.persona_comparison else None,
            "stats": self.stats,
        }

    def to_json(self, indent: int = 2) -> str:
        return json.dumps(self.to_dict(), indent=indent)

    @classmethod
    def from_json(cls, data: str | dict) -> "JTBDAnalysis":
        d = json.loads(data) if isinstance(data, str) else data
        jobs = [Job(**{k: v for k, v in j.items() if k not in ("opportunity", "statement")}) for j in d.get("jobs", [])]
        translations = [Translation(**t) for t in d.get("translations", [])]
        pc = PersonaComparison(**d["persona_comparison"]) if d.get("persona_comparison") else None
        return cls(
            title=d.get("title", ""), product_context=d.get("product_context", ""),
            source=d.get("source", ""), author=d.get("author", ""), date=d.get("date", ""),
            jobs=jobs, translations=translations,
            recommendations=d.get("recommendations", []), persona_comparison=pc,
        )
