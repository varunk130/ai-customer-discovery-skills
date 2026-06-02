"""CLI for JTBD Extractor — load JSON, generate HTML/Markdown reports."""

import argparse
import json
import sys
from pathlib import Path
from jtbd.models import JTBDAnalysis
from jtbd.renderer import render_html, render_markdown


def main():
    parser = argparse.ArgumentParser(
        prog="jtbd",
        description="JTBD Extractor — Turn research data into Jobs-to-be-Done visual reports.",
    )
    parser.add_argument("input", help="JSON file with JTBD analysis data")
    parser.add_argument("-o", "--output", help="Output file path (default: stdout or auto-named)")
    parser.add_argument("-f", "--format", choices=["html", "markdown", "json"], default="html", help="Output format (default: html)")
    parser.add_argument("--author", default="Varun Kulkarni", help="Author name for the report")
    parser.add_argument("--open", action="store_true", help="Open HTML output in browser")

    args = parser.parse_args()

    # Load input
    input_path = Path(args.input)
    if not input_path.exists():
        print(f"Error: {input_path} not found", file=sys.stderr)
        sys.exit(1)

    with open(input_path, encoding="utf-8") as f:
        data = json.load(f)

    analysis = JTBDAnalysis.from_json(data)

    # Render
    if args.format == "html":
        output = render_html(analysis, author=args.author)
    elif args.format == "markdown":
        output = render_markdown(analysis)
    else:
        output = analysis.to_json()

    # Write output
    if args.output:
        out_path = Path(args.output)
        out_path.write_text(output, encoding="utf-8")
        print(f"✅ Saved {args.format} to {out_path}")
    else:
        ext = {"html": ".html", "markdown": ".md", "json": ".json"}[args.format]
        out_path = input_path.with_suffix(ext)
        out_path.write_text(output, encoding="utf-8")
        print(f"✅ Saved {args.format} to {out_path}")

    # Open in browser
    if args.open and args.format == "html":
        import webbrowser
        webbrowser.open(str(out_path.resolve()))


if __name__ == "__main__":
    main()
