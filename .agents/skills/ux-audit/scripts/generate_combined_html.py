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
        "critical": "#DC2626", "high": "#EA580C",
        "medium": "#CA8A04", "low": "#16A34A",
    }.get(sev.lower() if sev else "", "#6B7280")


def severity_bg(sev):
    return {
        "critical": "#FEF2F2", "high": "#FFF7ED",
        "medium": "#FEFCE8", "low": "#F0FDF4",
    }.get(sev.lower() if sev else "", "#F9FAFB")


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
            "FIXED": "#16A34A", "PARTIALLY FIXED": "#CA8A04",
            "NOT FIXED": "#EA580C", "WORSE": "#DC2626",
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
        <p style="color: #6b7280; margin-bottom: 16px;">Cross-reference of original findings against the audited version.</p>
        <div style="overflow-x: auto;">
            <table class="findings-table">
                <thead><tr><th>#</th><th>Original Finding</th><th>Status</th><th>Notes</th></tr></thead>
                <tbody>{rows}</tbody>
            </table>
        </div>
    </div>"""


def build_combined_html(output_file, audit_dirs):
    audits = [parse_audit(d) for d in audit_dirs]

    # Determine if this is a comparative (2+ audits) or single
    is_comparative = len(audits) > 1
    product_name = audits[0]["title"].replace("UI/UX AUDIT REPORT: ", "")

    # Build score comparison
    score_cards = ""
    for i, a in enumerate(audits):
        label = a["meta"].get("Audit Date", f"Audit {i+1}")
        suffix = " (Original)" if i == 0 and is_comparative else (" (Re-audit)" if i > 0 else "")
        score_color = "#DC2626" if float(a["score"]) < 5 else ("#EA580C" if float(a["score"]) < 7 else ("#CA8A04" if float(a["score"]) < 8 else "#16A34A")) if a["score"] != "N/A" else "#6B7280"
        score_cards += f"""
        <div class="score-card">
            <div class="score-number" style="background: linear-gradient(135deg, {score_color}, {score_color}cc); -webkit-background-clip: text; -webkit-text-fill-color: transparent;">{a['score']}</div>
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
  :root {{
    --critical: #DC2626; --critical-bg: #FEF2F2; --critical-border: #FECACA;
    --high: #EA580C; --high-bg: #FFF7ED; --high-border: #FED7AA;
    --medium: #CA8A04; --medium-bg: #FEFCE8; --medium-border: #FEF08A;
    --low: #16A34A; --low-bg: #F0FDF4; --low-border: #BBF7D0;
  }}
  * {{ margin: 0; padding: 0; box-sizing: border-box; }}
  body {{ font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif; color: #1a1a2e; background: #f8f9fa; line-height: 1.6; }}
  .container {{ max-width: 1200px; margin: 0 auto; padding: 20px; }}
  .report-header {{ background: linear-gradient(135deg, #1a1a2e 0%, #16213e 100%); color: white; padding: 48px 40px; border-radius: 16px; margin-bottom: 32px; }}
  .report-header h1 {{ font-size: 28px; margin-bottom: 8px; font-weight: 700; }}
  .report-header .subtitle {{ opacity: 0.8; font-size: 16px; margin-bottom: 24px; }}
  .meta-grid {{ display: grid; grid-template-columns: repeat(auto-fit, minmax(200px, 1fr)); gap: 16px; margin-top: 20px; }}
  .meta-item {{ background: rgba(255,255,255,0.1); padding: 12px 16px; border-radius: 8px; }}
  .meta-item .label {{ font-size: 11px; text-transform: uppercase; letter-spacing: 1px; opacity: 0.7; }}
  .meta-item .value {{ font-size: 14px; font-weight: 500; margin-top: 2px; }}
  .score-section {{ display: flex; gap: 24px; margin-bottom: 32px; flex-wrap: wrap; }}
  .score-card {{ background: white; border-radius: 16px; padding: 32px; text-align: center; box-shadow: 0 1px 3px rgba(0,0,0,0.1); flex: 1; min-width: 150px; }}
  .score-number {{ font-size: 64px; font-weight: 800; }}
  .score-label {{ font-size: 14px; color: #6b7280; margin-top: 4px; }}
  .score-arrow {{ font-size: 48px; display: flex; align-items: center; color: #16A34A; font-weight: 700; }}
  .severity-stats {{ display: grid; grid-template-columns: repeat(4, 1fr); gap: 12px; margin-bottom: 32px; }}
  .stat-card {{ background: white; border-radius: 12px; padding: 20px; text-align: center; box-shadow: 0 1px 3px rgba(0,0,0,0.1); border-top: 4px solid; }}
  .stat-card.critical {{ border-color: var(--critical); }}
  .stat-card.high {{ border-color: var(--high); }}
  .stat-card.medium {{ border-color: var(--medium); }}
  .stat-card.low {{ border-color: var(--low); }}
  .stat-count {{ font-size: 36px; font-weight: 800; }}
  .stat-label {{ font-size: 12px; text-transform: uppercase; letter-spacing: 1px; color: #6b7280; margin-top: 4px; }}
  .section {{ background: white; border-radius: 16px; padding: 32px; margin-bottom: 24px; box-shadow: 0 1px 3px rgba(0,0,0,0.1); }}
  .section h2 {{ font-size: 22px; margin-bottom: 20px; padding-bottom: 12px; border-bottom: 2px solid #f3f4f6; }}
  .findings-table {{ width: 100%; border-collapse: collapse; font-size: 14px; }}
  .findings-table th {{ background: #f9fafb; padding: 12px 16px; text-align: left; font-size: 11px; text-transform: uppercase; letter-spacing: 0.5px; color: #6b7280; border-bottom: 2px solid #e5e7eb; }}
  .findings-table td {{ padding: 12px 16px; border-bottom: 1px solid #f3f4f6; vertical-align: top; }}
  .finding-row:hover {{ background: #f9fafb; }}
  .finding-num {{ font-weight: 700; white-space: nowrap; }}
  .recommendation {{ color: #4b5563; font-size: 13px; }}
  .severity-badge {{ display: inline-block; padding: 3px 10px; border-radius: 20px; font-size: 11px; font-weight: 700; letter-spacing: 0.5px; color: white; }}
  .severity-critical {{ background: var(--critical); }}
  .severity-high {{ background: var(--high); }}
  .severity-medium {{ background: var(--medium); }}
  .severity-low {{ background: var(--low); }}
  .status-badge {{ display: inline-block; padding: 3px 10px; border-radius: 20px; font-size: 11px; font-weight: 700; letter-spacing: 0.5px; }}
  .screen-section {{ margin-bottom: 40px; }}
  .screen-section h4 {{ font-size: 18px; margin-bottom: 16px; color: #1a1a2e; }}
  .screen-layout {{ display: flex; gap: 32px; position: relative; align-items: flex-start; }}
  .screenshot-col {{ flex: 0 0 58%; min-width: 0; }}
  .screenshot-container {{ border-radius: 12px; overflow: hidden; border: 1px solid #e5e7eb; }}
  .screenshot {{ width: 100%; height: auto; display: block; }}
  .connector-overlay {{ position: absolute; inset: 0; width: 100%; height: 100%; pointer-events: none; overflow: visible; z-index: 2; }}
  .screen-findings {{ flex: 1 1 42%; min-width: 0; display: flex; flex-direction: column; gap: 8px; }}
  .screen-finding {{ padding: 12px 16px; border-radius: 8px; display: flex; flex-wrap: wrap; align-items: flex-start; gap: 8px; position: relative; }}
  .finding-badge {{ display: inline-flex; align-items: center; justify-content: center; width: 28px; height: 28px; border-radius: 50%; color: white; font-size: 12px; font-weight: 700; flex-shrink: 0; }}
  .severity-tag {{ font-size: 10px; font-weight: 700; letter-spacing: 0.5px; padding: 2px 8px; border-radius: 4px; }}
  .severity-tag.severity-critical {{ background: var(--critical-bg); color: var(--critical); }}
  .severity-tag.severity-high {{ background: var(--high-bg); color: var(--high); }}
  .severity-tag.severity-medium {{ background: var(--medium-bg); color: var(--medium); }}
  .severity-tag.severity-low {{ background: var(--low-bg); color: var(--low); }}
  .finding-text {{ font-size: 14px; flex: 1; min-width: 200px; }}
  .recommendation-card {{ background: #f9fafb; border-radius: 12px; padding: 24px; margin-bottom: 16px; border-left: 4px solid #3b82f6; }}
  .recommendation-card h4 {{ font-size: 16px; margin-bottom: 12px; color: #1e40af; }}
  .rec-item {{ margin-bottom: 8px; font-size: 14px; }}
  .rec-item strong {{ color: #374151; }}
  .quick-win {{ background: #DCFCE7; color: #166534; padding: 2px 8px; border-radius: 4px; font-size: 12px; font-weight: 600; }}
  .medium-lift {{ background: #FEF3C7; color: #92400E; padding: 2px 8px; border-radius: 4px; font-size: 12px; font-weight: 600; }}
  .working-well-item {{ background: #F0FDF4; border-left: 4px solid #16A34A; padding: 16px 20px; border-radius: 8px; margin-bottom: 12px; }}
  .working-well-item h4 {{ color: #166534; font-size: 15px; margin-bottom: 4px; }}
  .working-well-item p {{ color: #374151; font-size: 14px; }}
  .report-footer {{ text-align: center; padding: 32px; color: #9ca3af; font-size: 13px; }}
  .improvement-banner {{ background: linear-gradient(135deg, #F0FDF4, #DCFCE7); border: 2px solid #BBF7D0; border-radius: 16px; padding: 24px 32px; margin-bottom: 32px; display: flex; align-items: center; gap: 24px; }}
  .improvement-banner .delta {{ font-size: 48px; font-weight: 800; color: #16A34A; }}
  .improvement-banner .delta-text {{ font-size: 16px; color: #166534; }}
  @media (max-width: 900px) {{
    .screen-layout {{ flex-direction: column; }}
    .screenshot-col, .screen-findings {{ flex: 1 1 auto; width: 100%; }}
    .connector-overlay {{ display: none; }}
  }}
  @media print {{
    body {{ background: white; }}
    .container {{ max-width: none; padding: 0; }}
    .section {{ box-shadow: none; border: 1px solid #e5e7eb; break-inside: avoid; }}
  }}
</style>
</head>
<body>
<div class="container">

  <div class="report-header">
    <h1>{title}</h1>
    <div class="subtitle">{'Comparative ' if is_comparative else ''}UI/UX Audit Report</div>
    <div class="meta-grid">
      <div class="meta-item"><div class="label">Audit Date{'s' if is_comparative else ''}</div><div class="value">{audit_date_display}</div></div>
      <div class="meta-item"><div class="label">Platform</div><div class="value">{meta.get('Platform', 'N/A')}</div></div>
      <div class="meta-item"><div class="label">Auditor Persona</div><div class="value">{meta.get('Auditor Persona', 'N/A')}</div></div>
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
      <div style="font-size: 18px; font-weight: 600; color: #166534; margin-bottom: 4px;">
        {sum(1 for v in ["FIXED"] if True)} of {total_original} original findings addressed
      </div>
      <div style="color: #4b5563; font-size: 14px;">
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
    critical: '#DC2626',
    high: '#EA580C',
    medium: '#CA8A04',
    low: '#16A34A'
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

        const color = SEVERITY_COLORS[card.dataset.severity] || '#6B7280';
        const dx = Math.max(40, (ex - sx) * 0.5);
        const d = 'M ' + sx + ' ' + sy +
                  ' C ' + (sx + dx) + ' ' + sy + ', ' +
                  (ex - dx) + ' ' + ey + ', ' +
                  ex + ' ' + ey;

        const path = document.createElementNS(SVG_NS, 'path');
        path.setAttribute('d', d);
        path.setAttribute('fill', 'none');
        path.setAttribute('stroke', color);
        path.setAttribute('stroke-width', '2');
        path.setAttribute('stroke-opacity', '0.7');
        path.setAttribute('stroke-linecap', 'round');
        svg.appendChild(path);

        const dot = document.createElementNS(SVG_NS, 'circle');
        dot.setAttribute('cx', sx);
        dot.setAttribute('cy', sy);
        dot.setAttribute('r', '3');
        dot.setAttribute('fill', color);
        svg.appendChild(dot);
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
