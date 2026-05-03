"""AI Customer Discovery — Python toolkit.

A small Python package that loads, validates, and runs the markdown-defined
skills in this repository so they can be invoked from CI, notebooks, or other
Python applications (not just AI coding agents).
"""

from .loader import Skill, SkillLibrary, load_skills
from .runner import SkillRunner

__all__ = ["Skill", "SkillLibrary", "load_skills", "SkillRunner"]
__version__ = "0.1.0"
