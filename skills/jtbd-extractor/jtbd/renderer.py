"""Render JTBD analysis to HTML and Markdown."""

from jtbd.models import JTBDAnalysis, Job
from html import escape as esc


def _bar_pct(score: int, max_score: int) -> int:
    return round((score / max_score) * 100) if max_score else 0


def _cat_class(cat: str) -> str:
    return {"functional": "f", "emotional": "e", "social": "s"}.get(cat, "f")


def _cat_label(cat: str) -> str:
    return {"functional": "Functional", "emotional": "Emotional", "social": "Social"}.get(cat, cat.title())


def _cat_tag_class(cat: str) -> str:
    return {"functional": "tag-func", "emotional": "tag-emot", "social": "tag-soc"}.get(cat, "tag-func")


def _cat_card_class(cat: str) -> str:
    return {"functional": "jc-func", "emotional": "jc-emot", "social": "jc-soc"}.get(cat, "jc-func")


def _cat_icon(cat: str) -> str:
    return {"functional": "⚙️", "emotional": "💜", "social": "👥"}.get(cat, "📋")


def _job_card_html(job: Job) -> str:
    cc = _cat_card_class(job.category)
    icon = esc(job.icon) if job.icon else "📌"
    return f'''<div class="job-card {cc}">
  <div class="jc-head"><span class="jc-icon">{icon}</span><span class="jc-score">Opp: {job.opportunity}</span></div>
  <div class="jc-stmt"><strong>When</strong> {esc(job.situation)}, <strong>{"I want to feel" if job.category == "emotional" else "I want to be seen as" if job.category == "social" else "I want to"}</strong> {esc(job.action)}, <strong>so I can</strong> {esc(job.outcome)}</div>
  {f'<div class="jc-quote">{esc(job.evidence)}</div>' if job.evidence else ''}
</div>'''


def render_html(analysis: JTBDAnalysis, author: str = "Varun Kulkarni") -> str:
    stats = analysis.stats
    max_opp = stats["max_opportunity"]

    # Opportunity rows
    opp_rows = ""
    for i, job in enumerate(analysis.top_opportunities, 1):
        cat_cls = _cat_class(job.category)
        tag_cls = _cat_tag_class(job.category)
        label = _cat_label(job.category)
        short = esc(job.action[:60])
        pct = _bar_pct(job.opportunity, max_opp)
        opp_rows += f'''<div class="opp-row">
  <div class="opp-rank rank-{min(i,5)}">{i}</div>
  <div class="opp-text">{short} <span class="type-tag {tag_cls}">{label}</span></div>
  <div class="opp-bar-track"><div class="opp-bar-fill {cat_cls}" style="width:{pct}%"></div></div>
  <div class="opp-score">{job.opportunity}</div>
</div>\n'''

    # Job card sections
    def _section(cat_key, cat_icon, cat_name, jobs):
        if not jobs:
            return ""
        cards = "\n".join(_job_card_html(j) for j in jobs)
        return f'''<div class="section">
  <div class="section-label">{cat_icon} {cat_name}</div>
  <div class="jobs-grid">{cards}</div>
</div>\n'''

    func_html = _section("functional", "⚙️", "Functional Jobs", analysis.functional_jobs)
    emot_html = _section("emotional", "💜", "Emotional Jobs", analysis.emotional_jobs)
    soc_html = _section("social", "👥", "Social Jobs", analysis.social_jobs)

    # Persona comparison
    cmp_html = ""
    if analysis.persona_comparison:
        pc = analysis.persona_comparison
        cmp_html = f'''<div class="section">
  <div class="section-label">Persona Comparison</div>
  <div class="comparison">
    <div class="cmp-card cmp-confirms"><div class="cmp-icon">✅</div><h4>Confirms</h4><p>{esc(pc.confirms)}</p></div>
    <div class="cmp-card cmp-expands"><div class="cmp-icon">🔭</div><h4>Expands</h4><p>{esc(pc.expands)}</p></div>
    <div class="cmp-card cmp-contradicts"><div class="cmp-icon">⚠️</div><h4>Contradicts</h4><p>{esc(pc.contradicts)}</p></div>
  </div>
</div>\n'''

    # Translations
    trans_html = ""
    if analysis.translations:
        rows = "\n".join(
            f'<div class="trans-row"><div class="t-said">"{esc(t.request)}"</div>'
            f'<div class="t-arr">→</div><div class="t-need">{esc(t.real_job)}</div></div>'
            for t in analysis.translations
        )
        trans_html = f'''<div class="trans-card">
  <h3>Feature Request Translation</h3>
  <div class="sub">What they asked for → what they actually need</div>
  <div class="trans-grid">
    <div class="trans-head">What They Said</div><div></div><div class="trans-head">The Real Job</div>
    {rows}
  </div>
</div>\n'''

    # Recommendations
    recs_html = ""
    if analysis.recommendations:
        cards = "\n".join(
            f'<div class="rec-card"><div class="rec-num">{i}</div><p>{esc(r)}</p></div>'
            for i, r in enumerate(analysis.recommendations, 1)
        )
        recs_html = f'''<div class="section">
  <div class="section-label">Recommendations</div>
  <div class="recs">{cards}</div>
</div>\n'''

    return _HTML_TEMPLATE.format(
        author=esc(author), title=esc(analysis.title),
        product_context=esc(analysis.product_context),
        source=esc(analysis.source), date=esc(analysis.date),
        total_jobs=stats["total_jobs"], n_func=stats["functional"],
        n_emot=stats["emotional"], n_soc=stats["social"],
        max_opp=max_opp, opp_rows=opp_rows,
        func_html=func_html, emot_html=emot_html, soc_html=soc_html,
        cmp_html=cmp_html, trans_html=trans_html, recs_html=recs_html,
    )


def render_markdown(analysis: JTBDAnalysis) -> str:
    lines = [
        f"# {analysis.title}\n",
        f"**Source:** {analysis.source}  ",
        f"**Product Context:** {analysis.product_context}  ",
        f"**Date:** {analysis.date}\n",
        "---\n",
    ]

    def _job_table(jobs, cat_label, cat_icon):
        if not jobs:
            return
        lines.append(f"### {cat_icon} {cat_label}\n")
        lines.append("| Job Statement | Imp. | Sat. | Opp. | Evidence |")
        lines.append("|---|---|---|---|---|")
        for j in jobs:
            lines.append(f"| {j.statement} | {j.importance} | {j.satisfaction} | {j.opportunity} | {j.evidence} |")
        lines.append("")

    lines.append("## Jobs Identified\n")
    _job_table(analysis.functional_jobs, "Functional Jobs", "⚙️")
    _job_table(analysis.emotional_jobs, "Emotional Jobs", "💜")
    _job_table(analysis.social_jobs, "Social Jobs", "👥")

    if analysis.translations:
        lines.append("## Feature Request Translation\n")
        lines.append("| What They Asked For | The Real Job |")
        lines.append("|---|---|")
        for t in analysis.translations:
            lines.append(f'| "{t.request}" | {t.real_job} |')
        lines.append("")

    if analysis.recommendations:
        lines.append("## Recommendations\n")
        for i, r in enumerate(analysis.recommendations, 1):
            lines.append(f"{i}. {r}")
        lines.append("")

    return "\n".join(lines)


_HTML_TEMPLATE = '''<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{title}</title>
<style>
  @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800&display=swap');
  *{{margin:0;padding:0;box-sizing:border-box}}
  body{{font-family:'Inter',system-ui,sans-serif;background:#fff;color:#1a1a2e}}
  .page{{max-width:1200px;margin:0 auto;padding:48px 32px 64px}}
  .header{{text-align:center;margin-bottom:48px;animation:fadeUp .5s ease-out}}
  .header .byline{{font-size:13px;color:#6b7280;margin-bottom:6px}}.header .byline strong{{color:#7c3aed}}
  .header .badge{{display:inline-flex;align-items:center;gap:6px;background:rgba(139,92,246,.08);border:1px solid rgba(139,92,246,.2);border-radius:20px;padding:5px 14px;font-size:11px;font-weight:600;color:#7c3aed;text-transform:uppercase;letter-spacing:1px;margin-bottom:16px}}
  .header .badge .dot{{width:6px;height:6px;border-radius:50%;background:#7c3aed;animation:pulse 2s infinite}}
  .header h1{{font-size:36px;font-weight:800;color:#1a1a2e;margin-bottom:8px}}.header h1 span{{background:linear-gradient(135deg,#7c3aed,#6366f1);-webkit-background-clip:text;-webkit-text-fill-color:transparent}}
  .header .sub{{font-size:15px;color:#6b7280;max-width:600px;margin:0 auto;line-height:1.5}}
  .meta-bar{{display:flex;justify-content:center;gap:32px;flex-wrap:wrap;margin-bottom:48px;padding:16px 0;border-top:1px solid #f3f4f6;border-bottom:1px solid #f3f4f6}}
  .meta-item{{text-align:center}}.meta-item .val{{font-size:22px;font-weight:800;color:#7c3aed}}.meta-item .lbl{{font-size:11px;color:#9ca3af;text-transform:uppercase;letter-spacing:.8px;margin-top:2px}}
  .section{{margin-bottom:48px;animation:fadeUp .6s ease-out}}
  .section-label{{font-size:11px;font-weight:700;text-transform:uppercase;letter-spacing:2px;color:#7c3aed;margin-bottom:20px}}
  .opp-row{{display:grid;grid-template-columns:28px 1fr 200px 50px;align-items:center;gap:12px;padding:14px 0;border-bottom:1px solid #f3f4f6}}
  .opp-rank{{width:28px;height:28px;border-radius:50%;display:flex;align-items:center;justify-content:center;font-size:12px;font-weight:700;color:#fff}}
  .rank-1{{background:linear-gradient(135deg,#7c3aed,#a78bfa)}}.rank-2{{background:linear-gradient(135deg,#6366f1,#818cf8)}}.rank-3,.rank-4,.rank-5{{background:linear-gradient(135deg,#8b5cf6,#a78bfa)}}
  .opp-text{{font-size:14px;color:#1a1a2e;font-weight:500}}.type-tag{{display:inline-block;font-size:10px;font-weight:600;padding:2px 8px;border-radius:10px;margin-left:8px;vertical-align:middle}}
  .tag-func{{background:#eff6ff;color:#2563eb}}.tag-emot{{background:#fdf2f8;color:#db2777}}.tag-soc{{background:#ecfdf5;color:#059669}}
  .opp-bar-track{{height:24px;background:#f3f4f6;border-radius:6px;overflow:hidden}}.opp-bar-fill{{height:100%;border-radius:6px;transition:width 1.2s cubic-bezier(.22,1,.36,1)}}
  .opp-bar-fill.f{{background:linear-gradient(90deg,#3b82f6,#60a5fa)}}.opp-bar-fill.e{{background:linear-gradient(90deg,#ec4899,#f472b6)}}.opp-bar-fill.s{{background:linear-gradient(90deg,#10b981,#34d399)}}
  .opp-score{{font-size:16px;font-weight:800;color:#7c3aed;text-align:right}}
  .jobs-grid{{display:grid;grid-template-columns:repeat(3,1fr);gap:20px}}
  .job-card{{border-radius:16px;padding:24px 20px;border:1px solid #e5e7eb;transition:transform .25s,box-shadow .25s;position:relative;overflow:hidden}}
  .job-card:hover{{transform:translateY(-3px)}}.job-card::after{{content:'';position:absolute;top:0;left:0;right:0;height:3px;border-radius:16px 16px 0 0}}
  .jc-func{{background:#f8faff}}.jc-func::after{{background:linear-gradient(90deg,#3b82f6,#60a5fa)}}.jc-func:hover{{box-shadow:0 8px 30px rgba(59,130,246,.12)}}
  .jc-emot{{background:#fef7fb}}.jc-emot::after{{background:linear-gradient(90deg,#ec4899,#f472b6)}}.jc-emot:hover{{box-shadow:0 8px 30px rgba(236,72,153,.12)}}
  .jc-soc{{background:#f0fdf8}}.jc-soc::after{{background:linear-gradient(90deg,#10b981,#34d399)}}.jc-soc:hover{{box-shadow:0 8px 30px rgba(16,185,129,.12)}}
  .jc-head{{display:flex;justify-content:space-between;align-items:center;margin-bottom:12px}}.jc-icon{{font-size:22px}}.jc-score{{font-size:11px;font-weight:700;color:#fff;padding:3px 10px;border-radius:12px}}
  .jc-func .jc-score{{background:#3b82f6}}.jc-emot .jc-score{{background:#ec4899}}.jc-soc .jc-score{{background:#10b981}}
  .jc-stmt{{font-size:13px;color:#374151;line-height:1.6;margin-bottom:12px}}.jc-stmt strong{{color:#1a1a2e}}
  .jc-quote{{background:rgba(0,0,0,.03);border-left:3px solid #e5e7eb;border-radius:0 8px 8px 0;padding:10px 14px;font-size:12px;color:#6b7280;font-style:italic;line-height:1.5}}
  .jc-func .jc-quote{{border-left-color:#3b82f6}}.jc-emot .jc-quote{{border-left-color:#ec4899}}.jc-soc .jc-quote{{border-left-color:#10b981}}
  .comparison{{display:grid;grid-template-columns:repeat(3,1fr);gap:20px}}
  .cmp-card{{border-radius:14px;padding:22px 20px;border:1px solid #e5e7eb}}.cmp-icon{{font-size:20px;margin-bottom:8px}}.cmp-card h4{{font-size:14px;font-weight:700;margin-bottom:8px}}.cmp-card p{{font-size:13px;color:#4b5563;line-height:1.6}}
  .cmp-confirms{{background:#ecfdf5}}.cmp-confirms h4{{color:#059669}}.cmp-expands{{background:#eff6ff}}.cmp-expands h4{{color:#2563eb}}.cmp-contradicts{{background:#fef2f2}}.cmp-contradicts h4{{color:#dc2626}}
  .trans-card{{background:#fafafa;border:1px solid #e5e7eb;border-radius:16px;padding:28px;margin-bottom:48px}}
  .trans-card h3{{font-size:16px;font-weight:700;color:#1a1a2e;margin-bottom:4px}}.trans-card .sub{{font-size:13px;color:#6b7280;margin-bottom:20px}}
  .trans-grid{{display:grid;grid-template-columns:1fr 32px 1fr;gap:8px 0}}.trans-head{{font-size:11px;font-weight:700;text-transform:uppercase;letter-spacing:1px;color:#9ca3af;padding:0 16px 8px}}
  .t-said,.t-arr,.t-need{{padding:12px 16px;border-bottom:1px solid #f3f4f6;font-size:13px;transition:background .15s}}
  .t-said{{color:#db2777;font-style:italic;border-radius:8px 0 0 8px}}.t-arr{{color:#7c3aed;font-weight:700;text-align:center;font-size:16px;display:flex;align-items:center;justify-content:center}}.t-need{{color:#059669;font-weight:500;border-radius:0 8px 8px 0}}
  .recs{{display:grid;grid-template-columns:repeat(2,1fr);gap:20px}}
  .rec-card{{border-radius:14px;padding:24px;border:1px solid #e5e7eb;background:#fafafa;transition:transform .2s,box-shadow .2s}}.rec-card:hover{{transform:translateY(-2px);box-shadow:0 8px 24px rgba(0,0,0,.06)}}
  .rec-num{{width:28px;height:28px;border-radius:50%;background:linear-gradient(135deg,#7c3aed,#6366f1);color:#fff;display:flex;align-items:center;justify-content:center;font-size:12px;font-weight:700;margin-bottom:12px}}
  .rec-card p{{font-size:13px;color:#4b5563;line-height:1.6}}
  .footer{{text-align:center;margin-top:48px;padding-top:24px;border-top:1px solid #f3f4f6}}
  .footer .meta{{font-size:11px;color:#9ca3af;margin-top:16px}}
  @keyframes fadeUp{{from{{opacity:0;transform:translateY(20px)}}to{{opacity:1;transform:translateY(0)}}}}
  @keyframes pulse{{0%,100%{{opacity:1}}50%{{opacity:.4}}}}
  @media(max-width:900px){{.jobs-grid,.comparison,.recs{{grid-template-columns:1fr}}.meta-bar{{gap:16px}}}}
</style>
</head>
<body>
<div class="page">
  <div class="header">
    <div class="byline">Built by <strong>{author}</strong></div>
    <div class="badge"><span class="dot"></span> JTBD Extractor</div>
    <h1>{title}</h1>
    <div class="sub">{product_context}</div>
  </div>
  <div class="meta-bar">
    <div class="meta-item"><div class="val">{total_jobs}</div><div class="lbl">Jobs Found</div></div>
    <div class="meta-item"><div class="val">{n_func}</div><div class="lbl">Functional</div></div>
    <div class="meta-item"><div class="val">{n_emot}</div><div class="lbl">Emotional</div></div>
    <div class="meta-item"><div class="val">{n_soc}</div><div class="lbl">Social</div></div>
    <div class="meta-item"><div class="val">{max_opp}</div><div class="lbl">Max Opportunity</div></div>
  </div>
  <div class="section">
    <div class="section-label">Top Opportunities — Ranked by Score</div>
    {opp_rows}
  </div>
  {func_html}
  {emot_html}
  {soc_html}
  {cmp_html}
  {trans_html}
  {recs_html}
  <div class="footer">
    <div class="meta">JTBD Extractor · Built by {author}</div>
  </div>
</div>
</body>
</html>'''
