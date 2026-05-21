#!/usr/bin/env python3
"""
Generate a combined comparative HTML report from multiple audit directories.

Usage:
    python3 generate_combined_html.py <output-file> <audit-dir-1> [<audit-dir-2> ...]

Example:
    python3 generate_combined_html.py combined-report.html \
        audits/2026-03-09_precious-metals-trading \
        audits/2026-03-10_precious-metals-trading-audited

Expects each audit-dir to contain:
    report.md, findings.json, screenshots/*-annotated.png
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
        "critical": "#B5481F", "high": "#A6680A",
        "medium": "#7B6E14", "low": "#4B6F44",
    }.get(sev.lower() if sev else "", "#6B6A63")


def severity_bg(sev):
    return {
        "critical": "#F7E8DF", "high": "#F5EBD4",
        "medium": "#F0EED4", "low": "#E3EEDE",
    }.get(sev.lower() if sev else "", "#F0EFE9")


def parse_audit(audit_dir):
    """Parse a single audit directory into structured data."""
    audit_dir = Path(audit_dir)
    screenshots_dir = audit_dir / "screenshots"
    data = {"dir": str(audit_dir), "name": audit_dir.name}

    # Load findings
    findings_path = audit_dir / "findings.json"
    data["findings"] = []
    if findings_path.exists():
        with open(findings_path) as f:
            data["findings"] = json.load(f)

    # Load report markdown
    report_path = audit_dir / "report.md"
    data["report_md"] = ""
    if report_path.exists():
        with open(report_path) as f:
            data["report_md"] = f.read()

    # Extract metadata
    data["title"] = "UI/UX Audit Report"
    data["meta"] = {}
    for line in data["report_md"].split("\n")[:20]:
        if line.startswith("# "):
            data["title"] = line[2:].strip()
        m = re.match(r"\*\*(.+?):\*\*\s*(.+)", line)
        if m:
            data["meta"][m.group(1).strip()] = m.group(2).strip().strip("`")

    # Extract executive summary
    exec_summary = ""
    in_exec = False
    for line in data["report_md"].split("\n"):
        if "EXECUTIVE SUMMARY" in line:
            in_exec = True
            continue
        if in_exec and line.startswith("## ") and "EXECUTIVE" not in line:
            break
        if in_exec and line.strip() and not line.startswith("---"):
            exec_summary += line + " "
    data["exec_summary"] = exec_summary.strip().replace("**", "")

    # Extract score
    score_match = re.search(r"Score:\s*(\d+\.?\d*)\s*/\s*10", exec_summary)
    data["score"] = score_match.group(1) if score_match else "N/A"

    # Severity counts
    sev_counts = {}
    for f in data["findings"]:
        s = f.get("severity", "medium").lower()
        sev_counts[s] = sev_counts.get(s, 0) + 1
    data["sev_counts"] = sev_counts

    # Collect annotated screenshots
    data["screens"] = []
    if screenshots_dir.exists():
        for png in sorted(screenshots_dir.glob("*-annotated.png")):
            screen_name = png.stem.replace("-annotated", "")
            findings_json = screenshots_dir / f"{screen_name}-findings.json"
            screen_findings = []
            if findings_json.exists():
                with open(findings_json) as fj:
                    sf = json.load(fj)
                findings_map = {fi["number"]: fi for fi in data["findings"]}
                for item in sf:
                    full = findings_map.get(item["number"], {})
                    screen_findings.append({
                        **item,
                        "finding": full.get("finding", item.get("label", "")),
                        "recommendation": full.get("recommendation", ""),
                        "severity": item.get("severity", full.get("severity", "medium")),
                    })
            data["screens"].append({
                "name": screen_name.replace("-", " ").title(),
                "img": img_to_base64(str(png)),
                "findings": sorted(screen_findings,
                    key=lambda x: ["critical", "high", "medium", "low"].index(
                        x.get("severity", "low").lower())),
            })

    # Extract sections
    sections = {}
    current_section = None
    current_content = []
    for line in data["report_md"].split("\n"):
        if line.startswith("## "):
            if current_section:
                sections[current_section] = "\n".join(current_content)
            current_section = line[3:].strip()
            current_content = []
        elif current_section:
            current_content.append(line)
    if current_section:
        sections[current_section] = "\n".join(current_content)
    data["sections"] = sections

    return data


def build_findings_rows(findings):
    severity_order = {"critical": 0, "high": 1, "medium": 2, "low": 3}
    sorted_findings = sorted(findings, key=lambda x: severity_order.get(x.get("severity", "medium").lower(), 4))
    rows = ""
    for f in sorted_findings:
        sev = f.get("severity", "medium").lower()
        rows += f"""
        <tr class="finding-row">
            <td class="finding-num">#{f['number']}</td>
            <td>{f.get('screen', '')}</td>
            <td>{f.get('dimension', '')}</td>
            <td><span class="severity-badge severity-{sev}">{sev.upper()}</span></td>
            <td>{f.get('finding', '')}</td>
            <td class="recommendation">{f.get('recommendation', '')}</td>
        </tr>"""
    return rows


def build_screenshots_html(screens):
    html = ""
    for screen in screens:
        findings_list = ""
        for sf in screen["findings"]:
            sev = sf.get("severity", "medium").lower()
            x = sf.get("x", 0)
            y = sf.get("y", 0)
            findings_list += f"""
                <div class="screen-finding" data-finding-number="{sf['number']}" data-x="{x}" data-y="{y}" data-severity="{sev}" style="border-left: 4px solid {severity_color(sev)}; background: {severity_bg(sev)};">
                    <span class="finding-badge" style="background: {severity_color(sev)};">#{sf['number']}</span>
                    <span class="severity-tag severity-{sev}">{sev.upper()}</span>
                    <span class="finding-text">{sf.get('finding', sf.get('label', ''))}</span>
                </div>"""
        html += f"""
        <div class="screen-section">
            <h4>{screen['name']}</h4>
            <div class="screen-layout">
                <svg class="connector-overlay" aria-hidden="true"></svg>
                <div class="screenshot-col">
                    <div class="screenshot-container">
                        <img src="{screen['img']}" alt="{screen['name']}" class="screenshot" />
                    </div>
                </div>
                <div class="screen-findings">{findings_list}</div>
            </div>
        </div>"""
    return html


def build_comparison_table(original, reaudit):
    """Build a status comparison table between two audits."""
    # Try to find the ORIGINAL FINDINGS STATUS section in reaudit
    status_section = reaudit["sections"].get("ORIGINAL FINDINGS STATUS (Cross-reference with prior audit)", "")
    if not status_section:
        # Fallback: build comparison from findings
        return ""

    rows = ""
    table_rows = re.findall(r"\|\s*(\d+)\s*\|\s*(.+?)\s*\|\s*(\w[\w\s]*)\s*\|\s*(.+?)\s*\|", status_section)
    for num, finding, status, notes in table_rows:
        if num.startswith("-") or num == "Original #":
            continue
        status_clean = status.strip().upper()
        status_class = status_clean.lower().replace(" ", "-")
        status_color_map = {
            "FIXED": "#4B6F44", "PARTIALLY FIXED": "#7B6E14",
            "NOT FIXED": "#A6680A", "WORSE": "#B5481F",
        }
        color = status_color_map.get(status_clean, "#6B7280")
        rows += f"""
        <tr>
            <td class="finding-num">#{num}</td>
            <td>{finding.strip()}</td>
            <td><span class="status-badge" style="background: {color}; color: white;">{status_clean}</span></td>
            <td>{notes.strip()}</td>
        </tr>"""

    if not rows:
        return ""

    return f"""
    <div class="section">
        <h2>Finding Resolution Status</h2>
        <p style="color: var(--muted); margin-bottom: 24px; font-size: 15px;">Cross-reference of original findings against the audited version.</p>
        <div style="overflow-x: auto;">
            <table class="findings-table">
                <thead><tr><th>#</th><th>Original Finding</th><th>Status</th><th>Notes</th></tr></thead>
                <tbody>{rows}</tbody>
            </table>
        </div>
    </div>"""


def dated_output_path(output_file):
    """Route the combined HTML output into a fresh per-generation subfolder:

        audits/                                  (or wherever the user pointed)
        └── reports/
            └── {YYYY-MM-DD}/
                └── combined-report.html

    `output_file`'s directory portion is treated as the base (typically
    `audits/`); the script appends `reports/<today>/<basename>` underneath it.
    """
    out = Path(output_file)
    today = date.today().isoformat()
    base_dir = out.parent if out.parent != Path('') else Path('.')
    filename = out.name or "combined-report.html"
    target_dir = base_dir / "reports" / today
    target_dir.mkdir(parents=True, exist_ok=True)
    return target_dir / filename


def build_combined_html(output_file, audit_dirs):
    output_file = dated_output_path(output_file)
    audits = [parse_audit(d) for d in audit_dirs]

    # Determine if this is a comparative (2+ audits) or single
    is_comparative = len(audits) > 1
    product_name = audits[0]["title"].replace("UI/UX AUDIT REPORT: ", "")

    # Build score comparison
    score_cards = ""
    for i, a in enumerate(audits):
        label = a["meta"].get("Audit Date", f"Audit {i+1}")
        suffix = " (Original)" if i == 0 and is_comparative else (" (Re-audit)" if i > 0 else "")
        score_color = "#B5481F" if float(a["score"]) < 5 else ("#A6680A" if float(a["score"]) < 7 else ("#7B6E14" if float(a["score"]) < 8 else "#4B6F44")) if a["score"] != "N/A" else "#6B6A63"
        score_cards += f"""
        <div class="score-card">
            <div class="score-number mono" style="color: {score_color};">{a['score']}</div>
            <div class="score-label">{label}{suffix}</div>
        </div>"""

    # Build severity comparison
    severity_comparison = ""
    if is_comparative:
        for sev in ["critical", "high", "medium", "low"]:
            cells = ""
            for a in audits:
                cells += f'<td class="stat-count" style="color: {severity_color(sev)};">{a["sev_counts"].get(sev, 0)}</td>'
            severity_comparison += f"""
            <tr>
                <td><span class="severity-badge severity-{sev}">{sev.upper()}</span></td>
                {cells}
            </tr>"""

    # Build per-audit sections
    audit_sections = ""
    for i, a in enumerate(audits):
        label = a["meta"].get("Audit Date", f"Audit {i+1}")
        suffix = " (Original)" if i == 0 and is_comparative else (" (Re-audit)" if i > 0 else "")

        # Executive summary
        audit_sections += f"""
        <div class="section">
            <h2>{label}{suffix} — Executive Summary</h2>
            <p>{a['exec_summary']}</p>
        </div>"""

        # Findings table
        audit_sections += f"""
        <div class="section">
            <h2>{label}{suffix} — All Findings ({len(a['findings'])})</h2>
            <div style="overflow-x: auto;">
                <table class="findings-table">
                    <thead><tr><th>#</th><th>Screen</th><th>Dimension</th><th>Severity</th><th>Finding</th><th>Recommendation</th></tr></thead>
                    <tbody>{build_findings_rows(a['findings'])}</tbody>
                </table>
            </div>
        </div>"""

        # Screenshots
        if a["screens"]:
            audit_sections += f"""
            <div class="section">
                <h2>{label}{suffix} — Annotated Screenshots</h2>
                {build_screenshots_html(a['screens'])}
            </div>"""

    # Comparison table (if 2 audits)
    comparison_html = ""
    if is_comparative and len(audits) >= 2:
        comparison_html = build_comparison_table(audits[0], audits[-1])

    # Extract top 5 from latest audit
    top5_html = ""
    latest = audits[-1]
    top5_section = latest["sections"].get("TOP 5 PRIORITY RECOMMENDATIONS", "")
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
                    effort_class = "quick-win" if "Quick" in value else ("medium-lift" if "Medium" in value else "")
                rec_body += f'<div class="rec-item"><strong>{label}:</strong> <span class="{effort_class}">{value}</span></div>'
        top5_html += f"""
        <div class="recommendation-card">
            <h4>{rec_title}</h4>
            {rec_body}
        </div>"""

    # What's working well from latest
    working_well_html = ""
    ww_section = latest["sections"].get("WHAT'S WORKING WELL", "")
    ww_items = re.findall(r"\d+\.\s*\*\*(.+?)\*\*\s*(.+?)(?=\n\d+\.|\Z)", ww_section, re.DOTALL)
    for ww_title, ww_desc in ww_items:
        working_well_html += f"""
        <div class="working-well-item">
            <h4>{ww_title}</h4>
            <p>{ww_desc.strip()}</p>
        </div>"""

    # Meta from latest audit
    meta = latest["meta"]
    audit_date_display = " vs ".join(a["meta"].get("Audit Date", "N/A") for a in audits) if is_comparative else meta.get("Audit Date", "N/A")

    # Build severity stats grid
    total_original = len(audits[0]["findings"])
    total_latest = len(audits[-1]["findings"])

    severity_stats_html = ""
    if is_comparative:
        severity_stats_html = f"""
        <div class="section" style="padding: 24px;">
            <h2>Severity Comparison</h2>
            <table class="findings-table" style="max-width: 600px;">
                <thead><tr><th>Severity</th><th>Original ({total_original} total)</th><th>Re-audit ({total_latest} total)</th></tr></thead>
                <tbody>{severity_comparison}</tbody>
            </table>
        </div>"""
    else:
        for sev in ["critical", "high", "medium", "low"]:
            count = audits[0]["sev_counts"].get(sev, 0)
            severity_stats_html += f"""
            <div class="stat-card {sev}">
                <div class="stat-count">{count}</div>
                <div class="stat-label">{sev.upper()}</div>
            </div>"""
        severity_stats_html = f'<div class="severity-stats">{severity_stats_html}</div>'

    title = f"Combined UI/UX Audit: {product_name}" if is_comparative else product_name

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
  .mono {{ font-family: var(--mono); font-variant-numeric: tabular-nums; }}
  .eyebrow {{ font-family: var(--mono); font-size: 12px; letter-spacing: 0.12em; text-transform: uppercase; color: var(--muted); }}

  /* Header / masthead */
  .report-header {{ padding: 24px 0 56px; border-bottom: 1px solid var(--hairline); margin-bottom: 56px; }}
  .report-header .eyebrow {{ margin-bottom: 24px; }}
  .report-header h1 {{ font-size: 52px; line-height: 1.1; margin-bottom: 16px; letter-spacing: -0.02em; font-weight: 500; }}
  .report-header .subtitle {{ font-family: var(--sans); font-size: 18px; color: var(--muted); margin-bottom: 40px; max-width: 720px; line-height: 1.5; }}
  .meta-grid {{ display: grid; grid-template-columns: repeat(auto-fit, minmax(180px, 1fr)); gap: 0; border-top: 1px solid var(--hairline); }}
  .meta-item {{ padding: 20px 24px 20px 0; border-right: 1px solid var(--hairline); }}
  .meta-item:last-child {{ border-right: none; padding-right: 0; }}
  .meta-item .label {{ font-family: var(--mono); font-size: 11px; text-transform: uppercase; letter-spacing: 0.1em; color: var(--muted); margin-bottom: 8px; }}
  .meta-item .value {{ font-family: var(--sans); font-size: 15px; color: var(--text); font-weight: 500; }}

  /* Score section — flat, hairline-divided */
  .score-section {{ display: flex; gap: 0; margin-bottom: 64px; flex-wrap: wrap; border-top: 1px solid var(--hairline); border-bottom: 1px solid var(--hairline); }}
  .score-card {{ padding: 28px 32px; flex: 1; min-width: 180px; border-right: 1px solid var(--hairline); display: flex; flex-direction: column; gap: 8px; }}
  .score-card:last-child {{ border-right: none; }}
  .score-number {{ font-family: var(--serif); font-size: 64px; font-weight: 500; line-height: 0.95; color: var(--text); letter-spacing: -0.03em; font-variant-numeric: tabular-nums; }}
  .score-label {{ font-family: var(--mono); font-size: 11px; text-transform: uppercase; letter-spacing: 0.1em; color: var(--muted); margin-top: 4px; }}
  .score-arrow {{ font-family: var(--serif); font-size: 36px; display: flex; align-items: center; color: var(--accent); font-weight: 500; padding: 0 24px; }}

  /* Severity stats — hairline row */
  .severity-stats {{ display: grid; grid-template-columns: repeat(4, 1fr); gap: 0; margin-bottom: 80px; border-top: 1px solid var(--hairline); border-bottom: 1px solid var(--hairline); }}
  .stat-card {{ padding: 28px 24px; border-right: 1px solid var(--hairline); display: flex; flex-direction: column; gap: 4px; background: transparent; box-shadow: none; }}
  .stat-card:last-child {{ border-right: none; }}
  .stat-count {{ font-family: var(--serif); font-size: 44px; font-weight: 500; font-variant-numeric: tabular-nums; line-height: 1; letter-spacing: -0.02em; }}
  .stat-card.critical .stat-count {{ color: var(--critical); }}
  .stat-card.high .stat-count {{ color: var(--high); }}
  .stat-card.medium .stat-count {{ color: var(--medium); }}
  .stat-card.low .stat-count {{ color: var(--low); }}
  .stat-label {{ font-family: var(--mono); font-size: 11px; text-transform: uppercase; letter-spacing: 0.12em; color: var(--muted); margin-top: 8px; }}

  /* Section — editorial */
  .section {{ background: transparent; border-radius: 0; padding: 0; margin-bottom: 80px; box-shadow: none; }}
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
  .status-badge {{ display: inline-block; padding: 3px 10px; border-radius: 2px; font-family: var(--mono); font-size: 10px; font-weight: 500; letter-spacing: 0.1em; text-transform: uppercase; }}

  /* Screenshots */
  .screen-section {{ margin-bottom: 64px; }}
  .screen-section h4 {{ font-family: var(--serif); font-size: 24px; margin-bottom: 24px; color: var(--text); font-weight: 500; letter-spacing: -0.01em; }}
  .screen-layout {{ display: flex; gap: 40px; position: relative; align-items: flex-start; }}
  .screenshot-col {{ flex: 0 0 58%; min-width: 0; }}
  .screenshot-container {{ border-radius: 2px; overflow: hidden; border: 1px solid var(--hairline-strong); background: #fff; }}
  .screenshot {{ width: 100%; height: auto; display: block; }}
  .connector-overlay {{ position: absolute; inset: 0; width: 100%; height: 100%; pointer-events: none; overflow: visible; z-index: 2; }}
  .screen-findings {{ flex: 1 1 42%; min-width: 0; display: flex; flex-direction: column; gap: 12px; }}
  .screen-finding {{ padding: 16px 18px; border-radius: 2px; display: flex; flex-wrap: wrap; align-items: flex-start; gap: 10px; position: relative; background: transparent; border: 1px solid var(--hairline); border-left-width: 3px !important; }}
  .finding-badge {{ display: inline-flex; align-items: center; justify-content: center; min-width: 32px; height: 24px; padding: 0 8px; border-radius: 2px; color: white; font-family: var(--mono); font-size: 11px; font-weight: 500; font-variant-numeric: tabular-nums; flex-shrink: 0; }}
  .severity-tag {{ font-family: var(--mono); font-size: 10px; font-weight: 500; letter-spacing: 0.1em; padding: 2px 8px; border-radius: 2px; text-transform: uppercase; }}
  .severity-tag.severity-critical {{ background: var(--critical-bg); color: var(--critical); }}
  .severity-tag.severity-high {{ background: var(--high-bg); color: var(--high); }}
  .severity-tag.severity-medium {{ background: var(--medium-bg); color: var(--medium); }}
  .severity-tag.severity-low {{ background: var(--low-bg); color: var(--low); }}
  .finding-text {{ font-size: 15px; flex: 1; min-width: 200px; line-height: 1.5; color: var(--text); }}

  /* Recommendations — editorial blocks */
  .recommendation-card {{ background: transparent; border-radius: 0; padding: 28px 0; margin-bottom: 0; border-left: none; border-bottom: 1px solid var(--hairline); }}
  .recommendation-card:last-child {{ border-bottom: none; }}
  .recommendation-card h4 {{ font-family: var(--serif); font-size: 22px; margin-bottom: 16px; color: var(--text); font-weight: 500; letter-spacing: -0.01em; }}
  .rec-item {{ margin-bottom: 10px; font-size: 15px; line-height: 1.6; }}
  .rec-item strong {{ color: var(--text); font-weight: 600; }}
  .quick-win {{ font-family: var(--mono); background: var(--low-bg); color: var(--low); padding: 2px 8px; border-radius: 2px; font-size: 11px; font-weight: 500; text-transform: uppercase; letter-spacing: 0.08em; }}
  .medium-lift {{ font-family: var(--mono); background: var(--medium-bg); color: var(--medium); padding: 2px 8px; border-radius: 2px; font-size: 11px; font-weight: 500; text-transform: uppercase; letter-spacing: 0.08em; }}

  /* Working well — editorial */
  .working-well-item {{ background: transparent; border-left: none; padding: 24px 0; border-radius: 0; margin-bottom: 0; border-bottom: 1px solid var(--hairline); }}
  .working-well-item:last-child {{ border-bottom: none; }}
  .working-well-item h4 {{ color: var(--text); font-family: var(--serif); font-size: 20px; margin-bottom: 8px; font-weight: 500; letter-spacing: -0.01em; }}
  .working-well-item p {{ color: var(--muted); font-size: 15px; line-height: 1.6; }}

  /* Footer */
  .report-footer {{ text-align: left; padding: 48px 0 0; margin-top: 64px; border-top: 1px solid var(--hairline); color: var(--muted); font-family: var(--mono); font-size: 12px; letter-spacing: 0.08em; text-transform: uppercase; }}

  /* Improvement banner — calm editorial, not green-celebratory */
  .improvement-banner {{ background: transparent; border: 1px solid var(--hairline-strong); border-radius: 2px; padding: 28px 32px; margin-bottom: 64px; display: flex; align-items: center; gap: 32px; }}
  .improvement-banner .delta {{ font-family: var(--serif); font-size: 56px; font-weight: 500; color: var(--low); font-variant-numeric: tabular-nums; letter-spacing: -0.03em; line-height: 1; }}
  .improvement-banner .delta-text {{ font-family: var(--mono); font-size: 12px; color: var(--muted); text-transform: uppercase; letter-spacing: 0.1em; margin-top: 8px; }}

  @media (max-width: 900px) {{
    .screen-layout {{ flex-direction: column; }}
    .screenshot-col, .screen-findings {{ flex: 1 1 auto; width: 100%; }}
    .connector-overlay {{ display: none; }}
  }}
  @media print {{
    body {{ background: white; }}
    .container {{ max-width: none; padding: 0; }}
    .section {{ break-inside: avoid; }}
    a {{ color: var(--text); border-bottom: none; }}
  }}
</style>
</head>
<body>
<div class="container">

  <div class="report-header">
    <div class="eyebrow">{'Comparative ' if is_comparative else ''}UI / UX Audit &nbsp;·&nbsp; {audit_date_display}</div>
    <h1>{title}</h1>
    <div class="subtitle">{'A side-by-side comparison across audits — score deltas, severity counts, and finding-resolution status.' if is_comparative else 'A senior UX audit across nine usability dimensions with a regulated-banking lens.'}</div>
    <div class="meta-grid">
      <div class="meta-item"><div class="label">Audit Date{'s' if is_comparative else ''}</div><div class="value">{audit_date_display}</div></div>
      <div class="meta-item"><div class="label">Platform</div><div class="value">{meta.get('Platform', 'N/A')}</div></div>
      <div class="meta-item"><div class="label">Persona</div><div class="value">{meta.get('Auditor Persona', 'N/A')}</div></div>
      <div class="meta-item"><div class="label">{'Audits Compared' if is_comparative else 'Flow Scope'}</div><div class="value">{f'{len(audits)} audits' if is_comparative else meta.get('Flow Scope', 'N/A')}</div></div>
    </div>
  </div>

  <!-- Score Section -->
  <div class="score-section">
    {score_cards}
    {'<div class="score-arrow">→</div>' if is_comparative and len(audits) == 2 else ''}
  </div>

  {"" if not is_comparative else f'''
  <div class="improvement-banner">
    <div>
      <div class="delta">+{float(audits[-1]["score"]) - float(audits[0]["score"]):.1f}</div>
      <div class="delta-text">Score improvement</div>
    </div>
    <div style="flex:1;">
      <div style="font-family: var(--serif); font-size: 22px; font-weight: 500; color: var(--text); margin-bottom: 8px; letter-spacing: -0.01em;">
        {sum(1 for v in ["FIXED"] if True)} of {total_original} original findings addressed
      </div>
      <div style="color: var(--muted); font-size: 14px; line-height: 1.5;">
        Original: {total_original} findings ({audits[0]["sev_counts"].get("critical", 0)} critical, {audits[0]["sev_counts"].get("high", 0)} high) →
        Re-audit: {total_latest} findings ({audits[-1]["sev_counts"].get("critical", 0)} critical, {audits[-1]["sev_counts"].get("high", 0)} high)
      </div>
    </div>
  </div>
  '''}

  {severity_stats_html}

  {comparison_html}

  {audit_sections}

  <!-- Top 5 Recommendations (Latest) -->
  <div class="section">
    <h2>Top 5 Priority Recommendations {'(Current)' if is_comparative else ''}</h2>
    {top5_html}
  </div>

  <!-- What's Working Well -->
  <div class="section">
    <h2>What's Working Well</h2>
    {working_well_html}
  </div>

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
  const MARKER_OFFSET = 10;

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

        const sx = (imgRect.left - layoutRect.left) + x * scaleX;
        const sy = (imgRect.top  - layoutRect.top)  + y * scaleY;

        const badge = card.querySelector('.finding-badge');
        if (!badge) return;
        const bRect = badge.getBoundingClientRect();
        const ex = bRect.left - layoutRect.left;
        const ey = (bRect.top - layoutRect.top) + bRect.height / 2;

        // Pill bounds (in displayed pixels) — matches annotate.py pill dims.
        const numStr = (card.dataset.findingNumber || '0') + '';
        const pillWNative = Math.max(24, 8 * numStr.length + 14);
        const hw = (pillWNative / 2) * scaleX;
        const hh = 11 * scaleY;

        // Clip the line origin to the pill rectangle edge.
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
    print(f"Combined HTML report generated: {output_file} ({file_size:.1f} MB)")


if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: python3 generate_combined_html.py <output-file> <audit-dir-1> [<audit-dir-2> ...]")
        sys.exit(1)
    build_combined_html(sys.argv[1], sys.argv[2:])
