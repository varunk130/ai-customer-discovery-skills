"""Command-line interface for the AI Customer Discovery toolkit.

Usage:
    acds list                          # list all skills
    acds show <skill>                  # show a skill's instructions
    acds run <skill> --input "..."     # render the skill prompt
"""

from __future__ import annotations

import sys
from pathlib import Path

import click

from .loader import load_skills
from .runner import SkillRunner


@click.group()
@click.option(
    "--skills-dir",
    type=click.Path(exists=True, file_okay=False, path_type=Path),
    default=Path("skills"),
    show_default=True,
    help="Path to the skills directory.",
)
@click.pass_context
def main(ctx: click.Context, skills_dir: Path) -> None:
    """AI Customer Discovery skill toolkit."""
    ctx.ensure_object(dict)
    ctx.obj["library"] = load_skills(skills_dir)


@main.command("list")
@click.pass_context
def list_skills(ctx: click.Context) -> None:
    """List all available skills."""
    library = ctx.obj["library"]
    if not library.skills:
        click.echo("No skills found.")
        sys.exit(1)
    for skill in library:
        click.echo(f"{skill.slug:40s}  {skill.description[:60]}")


@main.command("show")
@click.argument("name")
@click.pass_context
def show_skill(ctx: click.Context, name: str) -> None:
    """Show a skill's full instructions."""
    library = ctx.obj["library"]
    skill = library.by_name(name)
    click.echo(f"# {skill.name}\n{skill.description}\n\n{skill.instructions}")


@main.command("run")
@click.argument("name")
@click.option("--input", "user_input", required=True, help="User input passed to the skill.")
@click.pass_context
def run_skill(ctx: click.Context, name: str, user_input: str) -> None:
    """Render and run a skill against the configured backend."""
    library = ctx.obj["library"]
    skill = library.by_name(name)
    runner = SkillRunner()
    click.echo(runner.run(skill, user_input))


if __name__ == "__main__":  # pragma: no cover
    main()
