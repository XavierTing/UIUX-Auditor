#!/usr/bin/env python3
"""
Generate a self-contained HTML audit report with embedded screenshots.

Usage:
    python3 generate_html.py <audit-dir> <output-file>

Example:
    python3 generate_html.py audits/2026-03-09_precious-metals/ audits/2026-03-09_precious-metals/report.html

Expects:
    <audit-dir>/report.md
    <audit-dir>/findings.json
    <audit-dir>/screenshots/*-annotated.png
    <audit-dir>/screenshots/*.png
"""

import base64
import json
import os
import re
import sys
from datetime import date
from pathlib import Path


def img_to_base64(path):
    with open(path, "rb") as f:
        data = base64.b64encode(f.read()).decode("utf-8")
    ext = Path(path).suffix.lower()
    mime = {"png": "image/png", "jpg": "image/jpeg", "jpeg": "image/jpeg"}.get(
        ext.lstrip("."), "image/png"
    )
    return f"data:{mime};base64,{data}"


def severity_color(sev):
    return {
        "critical": "#B5481F",
        "high": "#A6680A",
        "medium": "#7B6E14",
        "low": "#4B6F44",
    }.get(sev, "#6B6A63")


def severity_bg(sev):
    return {
        "critical": "#F7E8DF",
        "high": "#F5EBD4",
        "medium": "#F0EED4",
        "low": "#E3EEDE",
    }.get(sev, "#F0EFE9")


def severity_border(sev):
    return {
        "critical": "#E8C7B3",
        "high": "#DFCEA7",
        "medium": "#D8D4A8",
        "low": "#C7D8BD",
    }.get(sev, "#E8E6DF")


def dated_output_path(audit_dir, output_file):
    """Route the HTML output into a fresh per-generation subfolder so each
    regeneration produces a new dated folder containing just the report.

        audits/{audit-date}_{product}/
        └── reports/
            └── {YYYY-MM-DD}/
                └── report.html

    The audit folder itself stays as the canonical home for report.md,
    findings.json, and screenshots/ — only the regenerated HTML moves into
    a dated sibling subfolder.
    """
    audit_dir = Path(audit_dir)
    today = date.today().isoformat()
    out = Path(output_file)
    # Keep just the basename from output_file (default report.html); ignore any
    # caller-supplied directory portion.
    filename = out.name or "report.html"
    target_dir = audit_dir / "reports" / today
    target_dir.mkdir(parents=True, exist_ok=True)
    return target_dir / filename


def build_html(audit_dir, output_file):
    output_file = dated_output_path(audit_dir, output_file)
    audit_dir = Path(audit_dir)
    screenshots_dir = audit_dir / "screenshots"

    # Load findings
    findings_path = audit_dir / "findings.json"
    findings = []
    if findings_path.exists():
        with open(findings_path) as f:
            findings = json.load(f)

    # Load report markdown for metadata
    report_path = audit_dir / "report.md"
    report_md = ""
    if report_path.exists():
        with open(report_path) as f:
            report_md = f.read()

    # Extract header metadata from markdown
    title = "UI/UX Audit Report"
    meta = {}
    for line in report_md.split("\n")[:20]:
        if line.startswith("# "):
            title = line[2:].strip()
        m = re.match(r"\*\*(.+?):\*\*\s*(.+)", line)
        if m:
            meta[m.group(1).strip()] = m.group(2).strip()

    # Extract executive summary
    exec_summary = ""
    in_exec = False
    for line in report_md.split("\n"):
        if "EXECUTIVE SUMMARY" in line:
            in_exec = True
            continue
        if in_exec and line.startswith("## ") and "EXECUTIVE" not in line:
            break
        if in_exec and line.strip() and not line.startswith("---"):
            exec_summary += line + "\n"

    # Extract score
    score_match = re.search(r"Score:\s*(\d+\.?\d*)\s*/\s*10", exec_summary)
    score = score_match.group(1) if score_match else "N/A"

    # Collect annotated screenshots
    annotated_screens = []
    if screenshots_dir.exists():
        for png in sorted(screenshots_dir.glob("*-annotated.png")):
            screen_name = png.stem.replace("-annotated", "")
            raw = screenshots_dir / f"{screen_name}.png"
            findings_json = screenshots_dir / f"{screen_name}-findings.json"

            screen_findings = []
            if findings_json.exists():
                with open(findings_json) as f:
                    sf = json.load(f)
                # Enrich with full finding data
                findings_map = {fi["number"]: fi for fi in findings}
                for item in sf:
                    full = findings_map.get(item["number"], {})
                    screen_findings.append(
                        {
                            **item,
                            "finding": full.get("finding", item.get("label", "")),
                            "recommendation": full.get("recommendation", ""),
                            "screen": full.get("screen", ""),
                            "dimension": full.get("dimension", ""),
                        }
                    )

            annotated_screens.append(
                {
                    "name": screen_name.replace("-", " ").title(),
                    "annotated_img": img_to_base64(str(png)),
                    "raw_img": img_to_base64(str(raw)) if raw.exists() else None,
                    "findings": sorted(
                        screen_findings,
                        key=lambda x: [
                            "critical",
                            "high",
                            "medium",
                            "low",
                        ].index(x.get("severity", "low")),
                    ),
                }
            )

    # Extract sections from report.md
    sections = {}
    current_section = None
    current_content = []
    for line in report_md.split("\n"):
        if line.startswith("## "):
            if current_section:
                sections[current_section] = "\n".join(current_content)
            current_section = line[3:].strip()
            current_content = []
        elif current_section:
            current_content.append(line)
    if current_section:
        sections[current_section] = "\n".join(current_content)

    # Build findings table rows
    severity_order = {"critical": 0, "high": 1, "medium": 2, "low": 3}
    sorted_findings = sorted(findings, key=lambda x: severity_order.get(x.get("severity", "low"), 4))

    findings_rows = ""
    for f in sorted_findings:
        sev = f.get("severity", "medium")
        findings_rows += f"""
        <tr class="finding-row" data-severity="{sev}">
            <td class="finding-num">#{f['number']}</td>
            <td>{f.get('screen', '')}</td>
            <td>{f.get('dimension', '')}</td>
            <td><span class="severity-badge severity-{sev}">{sev.upper()}</span></td>
            <td>{f.get('finding', '')}</td>
            <td class="recommendation">{f.get('recommendation', '')}</td>
        </tr>"""

    # Build annotated screenshot sections
    screenshots_html = ""
    for screen in annotated_screens:
        findings_list = ""
        for sf in screen["findings"]:
            sev = sf.get("severity", "medium")
            x = sf.get("x", 0)
            y = sf.get("y", 0)
            findings_list += f"""
                <div class="screen-finding" data-finding-number="{sf['number']}" data-x="{x}" data-y="{y}" data-severity="{sev}" style="border-left: 4px solid {severity_color(sev)}; background: {severity_bg(sev)};">
                    <span class="finding-badge" style="background: {severity_color(sev)};">#{sf['number']}</span>
                    <span class="severity-tag severity-{sev}">{sev.upper()}</span>
                    <span class="finding-text">{sf.get('finding', sf.get('label', ''))}</span>
                    <div class="finding-rec">→ {sf.get('recommendation', '')}</div>
                </div>"""

        screenshots_html += f"""
        <div class="screen-section">
            <h3>{screen['name']}</h3>
            <div class="screen-layout">
                <svg class="connector-overlay" aria-hidden="true"></svg>
                <div class="screenshot-col">
                    <div class="screenshot-container">
                        <img src="{screen['annotated_img']}" alt="{screen['name']} - Annotated" class="screenshot" />
                    </div>
                </div>
                <div class="screen-findings">
                    <h4>Findings on this screen:</h4>
                    {findings_list}
                </div>
            </div>
        </div>"""

    # Extract top 5 recommendations
    top5_html = ""
    top5_section = sections.get("TOP 5 PRIORITY RECOMMENDATIONS", "")
    recs = re.split(r"###\s*\d+\.\s*", top5_section)
    for rec in recs[1:]:
        lines = rec.strip().split("\n")
        rec_title = lines[0].strip()
        rec_body = ""
        for line in lines[1:]:
            line = line.strip()
            if not line:
                continue
            m = re.match(r"- \*\*(.+?):\*\*\s*(.*)", line)
            if m:
                label, value = m.group(1), m.group(2)
                effort_class = ""
                if "Effort" in label:
                    effort_class = "quick-win" if "Quick" in value else ("medium-lift" if "Medium" in value else "large-effort")
                rec_body += f'<div class="rec-item"><strong>{label}:</strong> <span class="{effort_class}">{value}</span></div>'
            else:
                rec_body += f"<p>{line}</p>"

        top5_html += f"""
        <div class="recommendation-card">
            <h4>{rec_title}</h4>
            {rec_body}
        </div>"""

    # Extract accessibility summary
    a11y_html = ""
    a11y_section = sections.get("ACCESSIBILITY SUMMARY", "")
    a11y_rows = re.findall(r"\|\s*(.+?)\s*\|\s*(\w+)\s*\|\s*(\w[\w\s]*)\s*\|\s*(.+?)\s*\|", a11y_section)
    for criterion, level, status, details in a11y_rows:
        if criterion.startswith("---") or criterion.startswith("WCAG"):
            continue
        status_class = status.strip().lower().replace(" ", "-")
        a11y_html += f"""
        <tr>
            <td>{criterion}</td>
            <td>{level}</td>
            <td><span class="a11y-status a11y-{status_class}">{status.strip()}</span></td>
            <td>{details}</td>
        </tr>"""

    # Extract what's working well
    working_well_html = ""
    ww_section = sections.get("WHAT'S WORKING WELL", "")
    ww_items = re.findall(r"\d+\.\s*\*\*(.+?)\*\*\s*(.+?)(?=\n\d+\.|\Z)", ww_section, re.DOTALL)
    for ww_title, ww_desc in ww_items:
        working_well_html += f"""
        <div class="working-well-item">
            <h4>{ww_title}</h4>
            <p>{ww_desc.strip()}</p>
        </div>"""

    # Count severities
    sev_counts = {}
    for f in findings:
        s = f.get("severity", "medium")
        sev_counts[s] = sev_counts.get(s, 0) + 1

    # Generate full HTML
    html = f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{title}</title>
<style>
  @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&family=Source+Serif+4:opsz,wght@8..60,400;8..60,500;8..60,600;8..60,700&family=JetBrains+Mono:wght@400;500&display=swap');

  :root {{
    --bg: #FAF9F5;
    --surface: #FAF9F5;
    --text: #191919;
    --muted: #6B6A63;
    --hairline: #E8E6DF;
    --hairline-strong: #D6D3C8;
    --accent: #CC785C;

    --critical: #B5481F; --critical-bg: #F7E8DF; --critical-border: #E8C7B3;
    --high: #A6680A;     --high-bg: #F5EBD4;     --high-border: #DFCEA7;
    --medium: #7B6E14;   --medium-bg: #F0EED4;   --medium-border: #D8D4A8;
    --low: #4B6F44;      --low-bg: #E3EEDE;      --low-border: #C7D8BD;

    --serif: 'Source Serif 4', 'Source Serif Pro', 'Iowan Old Style', Georgia, 'Times New Roman', serif;
    --sans: 'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', system-ui, sans-serif;
    --mono: 'JetBrains Mono', ui-monospace, 'SF Mono', Menlo, Consolas, monospace;
  }}
  * {{ margin: 0; padding: 0; box-sizing: border-box; }}
  body {{ font-family: var(--sans); color: var(--text); background: var(--bg); line-height: 1.6; font-size: 17px; -webkit-font-smoothing: antialiased; }}
  .container {{ max-width: 1080px; margin: 0 auto; padding: 48px 32px 96px; }}
  h1, h2, h3, h4 {{ font-family: var(--serif); font-weight: 500; letter-spacing: -0.01em; color: var(--text); }}
  p {{ margin: 0; }}
  a {{ color: var(--accent); text-decoration: none; border-bottom: 1px solid currentColor; }}
  hr {{ border: none; border-top: 1px solid var(--hairline); margin: 48px 0; }}
  .mono {{ font-family: var(--mono); font-variant-numeric: tabular-nums; }}
  .eyebrow {{ font-family: var(--mono); font-size: 12px; letter-spacing: 0.12em; text-transform: uppercase; color: var(--muted); }}

  /* Header / masthead */
  .report-header {{ padding: 24px 0 56px; border-bottom: 1px solid var(--hairline); margin-bottom: 56px; }}
  .report-header .eyebrow {{ margin-bottom: 24px; }}
  .report-header h1 {{ font-size: 52px; line-height: 1.1; margin-bottom: 16px; letter-spacing: -0.02em; }}
  .report-header .subtitle {{ font-family: var(--sans); font-size: 18px; color: var(--muted); margin-bottom: 40px; max-width: 720px; line-height: 1.5; }}
  .meta-grid {{ display: grid; grid-template-columns: repeat(auto-fit, minmax(180px, 1fr)); gap: 0; border-top: 1px solid var(--hairline); }}
  .meta-item {{ padding: 20px 24px 20px 0; border-right: 1px solid var(--hairline); }}
  .meta-item:last-child {{ border-right: none; padding-right: 0; }}
  .meta-item .label {{ font-family: var(--mono); font-size: 11px; text-transform: uppercase; letter-spacing: 0.1em; color: var(--muted); margin-bottom: 8px; }}
  .meta-item .value {{ font-family: var(--sans); font-size: 15px; color: var(--text); font-weight: 500; }}

  /* Score + Summary */
  .score-section {{ display: grid; grid-template-columns: 240px 1fr; gap: 56px; margin-bottom: 64px; align-items: flex-start; }}
  .score-card {{ padding: 0; }}
  .score-number {{ font-family: var(--serif); font-size: 96px; line-height: 0.95; font-weight: 500; color: var(--text); letter-spacing: -0.04em; font-variant-numeric: tabular-nums; }}
  .score-label {{ font-family: var(--mono); font-size: 12px; letter-spacing: 0.1em; text-transform: uppercase; color: var(--muted); margin-top: 12px; }}
  .summary-card {{ padding: 0; }}
  .summary-card h2 {{ font-size: 22px; margin-bottom: 16px; font-weight: 500; }}
  .summary-card p {{ font-size: 17px; color: var(--text); line-height: 1.7; }}

  /* Severity stats — flat row, hairline-divided */
  .severity-stats {{ display: grid; grid-template-columns: repeat(4, 1fr); gap: 0; margin-bottom: 80px; border-top: 1px solid var(--hairline); border-bottom: 1px solid var(--hairline); }}
  .stat-card {{ padding: 28px 24px; border-right: 1px solid var(--hairline); display: flex; flex-direction: column; gap: 4px; }}
  .stat-card:last-child {{ border-right: none; }}
  .stat-count {{ font-family: var(--serif); font-size: 44px; font-weight: 500; font-variant-numeric: tabular-nums; line-height: 1; letter-spacing: -0.02em; }}
  .stat-card.critical .stat-count {{ color: var(--critical); }}
  .stat-card.high .stat-count {{ color: var(--high); }}
  .stat-card.medium .stat-count {{ color: var(--medium); }}
  .stat-card.low .stat-count {{ color: var(--low); }}
  .stat-label {{ font-family: var(--mono); font-size: 11px; text-transform: uppercase; letter-spacing: 0.12em; color: var(--muted); margin-top: 8px; }}

  /* Section — editorial, no card chrome */
  .section {{ padding: 0; margin-bottom: 80px; }}
  .section h2 {{ font-size: 32px; margin-bottom: 28px; padding-bottom: 16px; border-bottom: 1px solid var(--hairline); font-weight: 500; letter-spacing: -0.015em; }}

  /* Findings table — ledger */
  .findings-table {{ width: 100%; border-collapse: collapse; font-size: 14px; font-family: var(--sans); }}
  .findings-table th {{ background: transparent; padding: 12px 12px; text-align: left; font-family: var(--mono); font-size: 11px; text-transform: uppercase; letter-spacing: 0.1em; color: var(--muted); border-bottom: 1px solid var(--hairline-strong); font-weight: 500; }}
  .findings-table td {{ padding: 16px 12px; border-bottom: 1px solid var(--hairline); vertical-align: top; line-height: 1.5; }}
  .finding-row:hover {{ background: rgba(232, 230, 223, 0.35); }}
  .finding-num {{ font-family: var(--mono); font-variant-numeric: tabular-nums; font-weight: 500; white-space: nowrap; color: var(--muted); }}
  .recommendation {{ color: var(--muted); font-size: 14px; }}

  /* Severity badges — outline pills */
  .severity-badge {{ display: inline-block; padding: 3px 10px; border-radius: 2px; font-family: var(--mono); font-size: 10px; font-weight: 500; letter-spacing: 0.1em; text-transform: uppercase; border: 1px solid; background: transparent; }}
  .severity-critical {{ color: var(--critical); border-color: var(--critical-border); background: var(--critical-bg); }}
  .severity-high {{ color: var(--high); border-color: var(--high-border); background: var(--high-bg); }}
  .severity-medium {{ color: var(--medium); border-color: var(--medium-border); background: var(--medium-bg); }}
  .severity-low {{ color: var(--low); border-color: var(--low-border); background: var(--low-bg); }}

  /* Screenshots — hairline-bordered, no card chrome */
  .screen-section {{ margin-bottom: 64px; }}
  .screen-section h3 {{ font-size: 24px; margin-bottom: 24px; color: var(--text); font-weight: 500; letter-spacing: -0.01em; }}
  .screen-layout {{ display: flex; gap: 40px; position: relative; align-items: flex-start; }}
  .screenshot-col {{ flex: 0 0 58%; min-width: 0; }}
  .screenshot-container {{ border-radius: 2px; overflow: hidden; border: 1px solid var(--hairline-strong); background: #fff; }}
  .screenshot {{ width: 100%; height: auto; display: block; }}
  .connector-overlay {{ position: absolute; inset: 0; width: 100%; height: 100%; pointer-events: none; overflow: visible; z-index: 2; }}
  .screen-findings {{ flex: 1 1 42%; min-width: 0; display: flex; flex-direction: column; gap: 12px; }}
  .screen-findings h4 {{ font-family: var(--mono); font-size: 11px; text-transform: uppercase; letter-spacing: 0.12em; color: var(--muted); margin-bottom: 4px; font-weight: 500; }}
  .screen-finding {{ padding: 16px 18px; border-radius: 2px; display: flex; flex-wrap: wrap; align-items: flex-start; gap: 10px; position: relative; background: transparent; border: 1px solid var(--hairline); border-left-width: 3px !important; }}
  .finding-badge {{ display: inline-flex; align-items: center; justify-content: center; min-width: 32px; height: 24px; padding: 0 8px; border-radius: 2px; color: white; font-family: var(--mono); font-size: 11px; font-weight: 500; font-variant-numeric: tabular-nums; flex-shrink: 0; }}
  .severity-tag {{ font-family: var(--mono); font-size: 10px; font-weight: 500; letter-spacing: 0.1em; padding: 2px 8px; border-radius: 2px; text-transform: uppercase; }}
  .severity-tag.severity-critical {{ background: var(--critical-bg); color: var(--critical); }}
  .severity-tag.severity-high {{ background: var(--high-bg); color: var(--high); }}
  .severity-tag.severity-medium {{ background: var(--medium-bg); color: var(--medium); }}
  .severity-tag.severity-low {{ background: var(--low-bg); color: var(--low); }}
  .finding-text {{ font-size: 15px; flex: 1; min-width: 200px; line-height: 1.5; color: var(--text); }}
  .finding-rec {{ width: 100%; font-size: 14px; color: var(--muted); padding-left: 44px; margin-top: 6px; line-height: 1.55; }}
  @media (max-width: 900px) {{
    .screen-layout {{ flex-direction: column; }}
    .screenshot-col, .screen-findings {{ flex: 1 1 auto; width: 100%; }}
    .connector-overlay {{ display: none; }}
  }}

  /* Recommendations — editorial blocks */
  .recommendation-card {{ background: transparent; border-radius: 0; padding: 28px 0; margin-bottom: 0; border-left: none; border-bottom: 1px solid var(--hairline); }}
  .recommendation-card:last-child {{ border-bottom: none; }}
  .recommendation-card h4 {{ font-family: var(--serif); font-size: 22px; margin-bottom: 16px; color: var(--text); font-weight: 500; letter-spacing: -0.01em; }}
  .rec-item {{ margin-bottom: 10px; font-size: 15px; line-height: 1.6; }}
  .rec-item strong {{ color: var(--text); font-weight: 600; }}
  .quick-win {{ font-family: var(--mono); background: var(--low-bg); color: var(--low); padding: 2px 8px; border-radius: 2px; font-size: 11px; font-weight: 500; text-transform: uppercase; letter-spacing: 0.08em; }}
  .medium-lift {{ font-family: var(--mono); background: var(--medium-bg); color: var(--medium); padding: 2px 8px; border-radius: 2px; font-size: 11px; font-weight: 500; text-transform: uppercase; letter-spacing: 0.08em; }}
  .large-effort {{ font-family: var(--mono); background: var(--critical-bg); color: var(--critical); padding: 2px 8px; border-radius: 2px; font-size: 11px; font-weight: 500; text-transform: uppercase; letter-spacing: 0.08em; }}

  /* Accessibility table */
  .a11y-table {{ width: 100%; border-collapse: collapse; font-size: 14px; }}
  .a11y-table th {{ background: transparent; padding: 12px 12px; text-align: left; font-family: var(--mono); font-size: 11px; text-transform: uppercase; letter-spacing: 0.1em; color: var(--muted); border-bottom: 1px solid var(--hairline-strong); font-weight: 500; }}
  .a11y-table td {{ padding: 14px 12px; border-bottom: 1px solid var(--hairline); line-height: 1.5; }}
  .a11y-status {{ font-family: var(--mono); padding: 2px 8px; border-radius: 2px; font-size: 10px; font-weight: 500; letter-spacing: 0.1em; text-transform: uppercase; border: 1px solid; }}
  .a11y-fail {{ background: var(--critical-bg); color: var(--critical); border-color: var(--critical-border); }}
  .a11y-missing {{ background: var(--high-bg); color: var(--high); border-color: var(--high-border); }}
  .a11y-unclear {{ background: var(--medium-bg); color: var(--medium); border-color: var(--medium-border); }}
  .a11y-pass {{ background: var(--low-bg); color: var(--low); border-color: var(--low-border); }}
  .a11y-likely {{ background: var(--low-bg); color: var(--low); border-color: var(--low-border); }}

  /* Working well — editorial */
  .working-well-item {{ background: transparent; border-left: none; padding: 24px 0; border-radius: 0; margin-bottom: 0; border-bottom: 1px solid var(--hairline); }}
  .working-well-item:last-child {{ border-bottom: none; }}
  .working-well-item h4 {{ color: var(--text); font-family: var(--serif); font-size: 20px; margin-bottom: 8px; font-weight: 500; letter-spacing: -0.01em; }}
  .working-well-item p {{ color: var(--muted); font-size: 15px; line-height: 1.6; }}

  /* Footer */
  .report-footer {{ text-align: left; padding: 48px 0 0; margin-top: 64px; border-top: 1px solid var(--hairline); color: var(--muted); font-family: var(--mono); font-size: 12px; letter-spacing: 0.08em; text-transform: uppercase; }}

  @media print {{
    body {{ background: white; }}
    .container {{ max-width: none; padding: 0; }}
    .section {{ break-inside: avoid; }}
    .screen-section {{ break-inside: avoid; }}
    a {{ color: var(--text); border-bottom: none; }}
  }}
</style>
</head>
<body>
<div class="container">

  <!-- Header -->
  <div class="report-header">
    <div class="eyebrow">UI / UX Audit &nbsp;·&nbsp; {meta.get('Audit Date', 'N/A')}</div>
    <h1>{title}</h1>
    <div class="subtitle">A senior UX audit across nine usability dimensions with a regulated-banking lens. Findings, severity, and prioritised recommendations.</div>
    <div class="meta-grid">
      <div class="meta-item"><div class="label">Audit Date</div><div class="value">{meta.get('Audit Date', 'N/A')}</div></div>
      <div class="meta-item"><div class="label">Platform</div><div class="value">{meta.get('Platform', 'N/A')}</div></div>
      <div class="meta-item"><div class="label">Persona</div><div class="value">{meta.get('Auditor Persona', 'N/A')}</div></div>
      <div class="meta-item"><div class="label">Flow Scope</div><div class="value">{meta.get('Flow Scope', 'N/A')}</div></div>
    </div>
  </div>

  <!-- Score + Summary -->
  <div class="score-section">
    <div class="score-card">
      <div class="score-number mono">{score}</div>
      <div class="score-label">UX Health Score / 10</div>
    </div>
    <div class="summary-card">
      <h2>Executive Summary</h2>
      <p>{exec_summary.strip()}</p>
    </div>
  </div>

  <!-- Severity Stats -->
  <div class="severity-stats">
    <div class="stat-card critical"><div class="stat-count">{sev_counts.get('critical', 0)}</div><div class="stat-label">Critical</div></div>
    <div class="stat-card high"><div class="stat-count">{sev_counts.get('high', 0)}</div><div class="stat-label">High</div></div>
    <div class="stat-card medium"><div class="stat-count">{sev_counts.get('medium', 0)}</div><div class="stat-label">Medium</div></div>
    <div class="stat-card low"><div class="stat-count">{sev_counts.get('low', 0)}</div><div class="stat-label">Low</div></div>
  </div>

  <!-- Findings Table -->
  <div class="section">
    <h2>All Findings ({len(findings)})</h2>
    <div style="overflow-x: auto;">
      <table class="findings-table">
        <thead>
          <tr><th>#</th><th>Screen / Component</th><th>Dimension</th><th>Severity</th><th>Finding</th><th>Recommendation</th></tr>
        </thead>
        <tbody>{findings_rows}</tbody>
      </table>
    </div>
  </div>

  <!-- Annotated Screenshots -->
  <div class="section">
    <h2>Annotated Screenshots</h2>
    <p style="color: var(--muted); margin-bottom: 32px; font-size: 15px; line-height: 1.6; max-width: 720px;">Each screenshot is annotated with numbered markers. Severity-coloured connector lines link each marker on the screenshot to its finding card on the right.</p>
    {screenshots_html}
  </div>

  <!-- Top 5 Recommendations -->
  <div class="section">
    <h2>Top 5 Priority Recommendations</h2>
    {top5_html}
  </div>

  <!-- Accessibility Summary -->
  <div class="section">
    <h2>Accessibility Summary</h2>
    <table class="a11y-table">
      <thead><tr><th>WCAG Criterion</th><th>Level</th><th>Status</th><th>Details</th></tr></thead>
      <tbody>{a11y_html}</tbody>
    </table>
    <p style="margin-top: 16px; font-weight: 600; color: var(--high);">Overall Accessibility Risk Level: HIGH</p>
  </div>

  <!-- What's Working Well -->
  <div class="section">
    <h2>What's Working Well</h2>
    {working_well_html}
  </div>

  <!-- Footer -->
  <div class="report-footer">
    Generated by UX Audit Skill &middot; {meta.get('Audit Date', '')}
  </div>

</div>
<script>
(function() {{
  const SEVERITY_COLORS = {{
    critical: '#B5481F',
    high: '#A6680A',
    medium: '#7B6E14',
    low: '#4B6F44'
  }};
  const SVG_NS = 'http://www.w3.org/2000/svg';
  const MARKER_OFFSET = 10; // matches annotate.py: marker drawn at (x-10, y-10)

  function drawConnectors() {{
    document.querySelectorAll('.screen-layout').forEach(function(layout) {{
      const svg = layout.querySelector('.connector-overlay');
      const img = layout.querySelector('.screenshot');
      if (!svg || !img || !img.naturalWidth) return;

      const layoutRect = layout.getBoundingClientRect();
      const imgRect = img.getBoundingClientRect();
      const scaleX = imgRect.width / img.naturalWidth;
      const scaleY = imgRect.height / img.naturalHeight;

      svg.setAttribute('viewBox', '0 0 ' + layoutRect.width + ' ' + layoutRect.height);
      svg.setAttribute('width', layoutRect.width);
      svg.setAttribute('height', layoutRect.height);
      while (svg.firstChild) svg.removeChild(svg.firstChild);

      layout.querySelectorAll('.screen-finding[data-finding-number]').forEach(function(card) {{
        const x = parseFloat(card.dataset.x) - MARKER_OFFSET;
        const y = parseFloat(card.dataset.y) - MARKER_OFFSET;
        if (isNaN(x) || isNaN(y)) return;

        // Marker centre on the displayed screenshot
        const sx = (imgRect.left - layoutRect.left) + x * scaleX;
        const sy = (imgRect.top  - layoutRect.top)  + y * scaleY;

        const badge = card.querySelector('.finding-badge');
        if (!badge) return;
        const bRect = badge.getBoundingClientRect();
        const ex = bRect.left - layoutRect.left;
        const ey = (bRect.top - layoutRect.top) + bRect.height / 2;

        // Pill bounds (in displayed pixels). Pill in PNG is 22 px tall, width
        // grows with digit count (matches annotate.py PILL_MIN_WIDTH and PILL_HPAD).
        const numStr = (card.dataset.findingNumber || '0') + '';
        const pillWNative = Math.max(24, 8 * numStr.length + 14);
        const hw = (pillWNative / 2) * scaleX;
        const hh = 11 * scaleY;

        // Compute where the line from marker-centre toward the badge exits the
        // pill rectangle. That's the smallest t > 0 such that the line crosses
        // a vertical edge (|t·dx| = hw) or a horizontal edge (|t·dy| = hh).
        const dx_dir = ex - sx;
        const dy_dir = ey - sy;
        const t1 = (Math.abs(dx_dir) > 0.001) ? hw / Math.abs(dx_dir) : Infinity;
        const t2 = (Math.abs(dy_dir) > 0.001) ? hh / Math.abs(dy_dir) : Infinity;
        const t = Math.min(t1, t2, 1);
        const sx2 = sx + t * dx_dir;
        const sy2 = sy + t * dy_dir;

        const color = SEVERITY_COLORS[card.dataset.severity] || '#6B7280';
        const dxCtrl = Math.max(40, (ex - sx2) * 0.5);
        const d = 'M ' + sx2 + ' ' + sy2 +
                  ' C ' + (sx2 + dxCtrl) + ' ' + sy2 + ', ' +
                  (ex - dxCtrl) + ' ' + ey + ', ' +
                  ex + ' ' + ey;

        const path = document.createElementNS(SVG_NS, 'path');
        path.setAttribute('d', d);
        path.setAttribute('fill', 'none');
        path.setAttribute('stroke', color);
        path.setAttribute('stroke-width', '1.5');
        path.setAttribute('stroke-opacity', '0.6');
        path.setAttribute('stroke-linecap', 'round');
        path.setAttribute('stroke-dasharray', '3 4');
        svg.appendChild(path);
      }});
    }});
  }}

  let rafId = null;
  function scheduleRedraw() {{
    if (rafId) cancelAnimationFrame(rafId);
    rafId = requestAnimationFrame(drawConnectors);
  }}

  window.addEventListener('load', drawConnectors);
  window.addEventListener('resize', scheduleRedraw);
  document.querySelectorAll('.screenshot').forEach(function(img) {{
    if (img.complete && img.naturalWidth) return;
    img.addEventListener('load', drawConnectors);
  }});
}})();
</script>
</body>
</html>"""

    with open(output_file, "w") as f:
        f.write(html)

    file_size = os.path.getsize(output_file) / (1024 * 1024)
    print(f"HTML report generated: {output_file} ({file_size:.1f} MB)")


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python3 generate_html.py <audit-dir> <output-file>")
        sys.exit(1)
    build_html(sys.argv[1], sys.argv[2])
