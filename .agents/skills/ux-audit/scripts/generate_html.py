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
        "critical": "#DC2626",
        "high": "#EA580C",
        "medium": "#CA8A04",
        "low": "#16A34A",
    }.get(sev, "#6B7280")


def severity_bg(sev):
    return {
        "critical": "#FEF2F2",
        "high": "#FFF7ED",
        "medium": "#FEFCE8",
        "low": "#F0FDF4",
    }.get(sev, "#F9FAFB")


def severity_border(sev):
    return {
        "critical": "#FECACA",
        "high": "#FED7AA",
        "medium": "#FEF08A",
        "low": "#BBF7D0",
    }.get(sev, "#E5E7EB")


def build_html(audit_dir, output_file):
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
  :root {{
    --critical: #DC2626; --critical-bg: #FEF2F2; --critical-border: #FECACA;
    --high: #EA580C; --high-bg: #FFF7ED; --high-border: #FED7AA;
    --medium: #CA8A04; --medium-bg: #FEFCE8; --medium-border: #FEF08A;
    --low: #16A34A; --low-bg: #F0FDF4; --low-border: #BBF7D0;
  }}
  * {{ margin: 0; padding: 0; box-sizing: border-box; }}
  body {{ font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif; color: #1a1a2e; background: #f8f9fa; line-height: 1.6; }}
  .container {{ max-width: 1200px; margin: 0 auto; padding: 20px; }}

  /* Header */
  .report-header {{ background: linear-gradient(135deg, #1a1a2e 0%, #16213e 100%); color: white; padding: 48px 40px; border-radius: 16px; margin-bottom: 32px; }}
  .report-header h1 {{ font-size: 32px; margin-bottom: 8px; font-weight: 700; }}
  .report-header .subtitle {{ opacity: 0.8; font-size: 16px; margin-bottom: 24px; }}
  .meta-grid {{ display: grid; grid-template-columns: repeat(auto-fit, minmax(200px, 1fr)); gap: 16px; margin-top: 20px; }}
  .meta-item {{ background: rgba(255,255,255,0.1); padding: 12px 16px; border-radius: 8px; }}
  .meta-item .label {{ font-size: 11px; text-transform: uppercase; letter-spacing: 1px; opacity: 0.7; }}
  .meta-item .value {{ font-size: 14px; font-weight: 500; margin-top: 2px; }}

  /* Score card */
  .score-section {{ display: grid; grid-template-columns: 200px 1fr; gap: 24px; margin-bottom: 32px; }}
  .score-card {{ background: white; border-radius: 16px; padding: 32px; text-align: center; box-shadow: 0 1px 3px rgba(0,0,0,0.1); }}
  .score-number {{ font-size: 64px; font-weight: 800; background: linear-gradient(135deg, #EA580C, #CA8A04); -webkit-background-clip: text; -webkit-text-fill-color: transparent; }}
  .score-label {{ font-size: 14px; color: #6b7280; margin-top: 4px; }}
  .summary-card {{ background: white; border-radius: 16px; padding: 32px; box-shadow: 0 1px 3px rgba(0,0,0,0.1); }}
  .summary-card h2 {{ font-size: 20px; margin-bottom: 16px; }}
  .summary-card p {{ color: #374151; }}

  /* Severity stats */
  .severity-stats {{ display: grid; grid-template-columns: repeat(4, 1fr); gap: 12px; margin-bottom: 32px; }}
  .stat-card {{ background: white; border-radius: 12px; padding: 20px; text-align: center; box-shadow: 0 1px 3px rgba(0,0,0,0.1); border-top: 4px solid; }}
  .stat-card.critical {{ border-color: var(--critical); }}
  .stat-card.high {{ border-color: var(--high); }}
  .stat-card.medium {{ border-color: var(--medium); }}
  .stat-card.low {{ border-color: var(--low); }}
  .stat-count {{ font-size: 36px; font-weight: 800; }}
  .stat-card.critical .stat-count {{ color: var(--critical); }}
  .stat-card.high .stat-count {{ color: var(--high); }}
  .stat-card.medium .stat-count {{ color: var(--medium); }}
  .stat-card.low .stat-count {{ color: var(--low); }}
  .stat-label {{ font-size: 12px; text-transform: uppercase; letter-spacing: 1px; color: #6b7280; margin-top: 4px; }}

  /* Section */
  .section {{ background: white; border-radius: 16px; padding: 32px; margin-bottom: 24px; box-shadow: 0 1px 3px rgba(0,0,0,0.1); }}
  .section h2 {{ font-size: 22px; margin-bottom: 20px; padding-bottom: 12px; border-bottom: 2px solid #f3f4f6; }}

  /* Findings table */
  .findings-table {{ width: 100%; border-collapse: collapse; font-size: 14px; }}
  .findings-table th {{ background: #f9fafb; padding: 12px 16px; text-align: left; font-size: 11px; text-transform: uppercase; letter-spacing: 0.5px; color: #6b7280; border-bottom: 2px solid #e5e7eb; }}
  .findings-table td {{ padding: 12px 16px; border-bottom: 1px solid #f3f4f6; vertical-align: top; }}
  .finding-row:hover {{ background: #f9fafb; }}
  .finding-num {{ font-weight: 700; white-space: nowrap; }}
  .recommendation {{ color: #4b5563; font-size: 13px; }}

  /* Severity badges */
  .severity-badge {{ display: inline-block; padding: 3px 10px; border-radius: 20px; font-size: 11px; font-weight: 700; letter-spacing: 0.5px; color: white; }}
  .severity-critical {{ background: var(--critical); }}
  .severity-high {{ background: var(--high); }}
  .severity-medium {{ background: var(--medium); }}
  .severity-low {{ background: var(--low); }}

  /* Screenshots */
  .screen-section {{ margin-bottom: 40px; }}
  .screen-section h3 {{ font-size: 18px; margin-bottom: 16px; color: #1a1a2e; }}
  .screen-layout {{ display: flex; gap: 32px; position: relative; align-items: flex-start; }}
  .screenshot-col {{ flex: 0 0 58%; min-width: 0; }}
  .screenshot-container {{ border-radius: 12px; overflow: hidden; border: 1px solid #e5e7eb; }}
  .screenshot {{ width: 100%; height: auto; display: block; }}
  .connector-overlay {{ position: absolute; inset: 0; width: 100%; height: 100%; pointer-events: none; overflow: visible; z-index: 2; }}
  .screen-findings {{ flex: 1 1 42%; min-width: 0; display: flex; flex-direction: column; gap: 8px; }}
  .screen-findings h4 {{ font-size: 14px; color: #6b7280; margin-bottom: 4px; }}
  .screen-finding {{ padding: 12px 16px; border-radius: 8px; display: flex; flex-wrap: wrap; align-items: flex-start; gap: 8px; position: relative; }}
  .finding-badge {{ display: inline-flex; align-items: center; justify-content: center; width: 28px; height: 28px; border-radius: 50%; color: white; font-size: 12px; font-weight: 700; flex-shrink: 0; }}
  .severity-tag {{ font-size: 10px; font-weight: 700; letter-spacing: 0.5px; padding: 2px 8px; border-radius: 4px; }}
  .severity-tag.severity-critical {{ background: var(--critical-bg); color: var(--critical); }}
  .severity-tag.severity-high {{ background: var(--high-bg); color: var(--high); }}
  .severity-tag.severity-medium {{ background: var(--medium-bg); color: var(--medium); }}
  .severity-tag.severity-low {{ background: var(--low-bg); color: var(--low); }}
  .finding-text {{ font-size: 14px; flex: 1; min-width: 200px; }}
  .finding-rec {{ width: 100%; font-size: 13px; color: #4b5563; padding-left: 36px; margin-top: 4px; }}
  @media (max-width: 900px) {{
    .screen-layout {{ flex-direction: column; }}
    .screenshot-col, .screen-findings {{ flex: 1 1 auto; width: 100%; }}
    .connector-overlay {{ display: none; }}
  }}

  /* Recommendations */
  .recommendation-card {{ background: #f9fafb; border-radius: 12px; padding: 24px; margin-bottom: 16px; border-left: 4px solid #3b82f6; }}
  .recommendation-card h4 {{ font-size: 16px; margin-bottom: 12px; color: #1e40af; }}
  .rec-item {{ margin-bottom: 8px; font-size: 14px; }}
  .rec-item strong {{ color: #374151; }}
  .quick-win {{ background: #DCFCE7; color: #166534; padding: 2px 8px; border-radius: 4px; font-size: 12px; font-weight: 600; }}
  .medium-lift {{ background: #FEF3C7; color: #92400E; padding: 2px 8px; border-radius: 4px; font-size: 12px; font-weight: 600; }}
  .large-effort {{ background: #FEE2E2; color: #991B1B; padding: 2px 8px; border-radius: 4px; font-size: 12px; font-weight: 600; }}

  /* Accessibility table */
  .a11y-table {{ width: 100%; border-collapse: collapse; font-size: 14px; }}
  .a11y-table th {{ background: #f9fafb; padding: 10px 14px; text-align: left; font-size: 11px; text-transform: uppercase; letter-spacing: 0.5px; color: #6b7280; }}
  .a11y-table td {{ padding: 10px 14px; border-bottom: 1px solid #f3f4f6; }}
  .a11y-status {{ padding: 3px 10px; border-radius: 20px; font-size: 11px; font-weight: 600; }}
  .a11y-fail {{ background: #FEF2F2; color: #DC2626; }}
  .a11y-missing {{ background: #FFF7ED; color: #EA580C; }}
  .a11y-unclear {{ background: #FEFCE8; color: #CA8A04; }}
  .a11y-pass {{ background: #F0FDF4; color: #16A34A; }}
  .a11y-likely {{ background: #F0FDF4; color: #16A34A; }}

  /* Working well */
  .working-well-item {{ background: #F0FDF4; border-left: 4px solid #16A34A; padding: 16px 20px; border-radius: 8px; margin-bottom: 12px; }}
  .working-well-item h4 {{ color: #166534; font-size: 15px; margin-bottom: 4px; }}
  .working-well-item p {{ color: #374151; font-size: 14px; }}

  /* Footer */
  .report-footer {{ text-align: center; padding: 32px; color: #9ca3af; font-size: 13px; }}

  @media print {{
    body {{ background: white; }}
    .container {{ max-width: none; padding: 0; }}
    .section {{ box-shadow: none; border: 1px solid #e5e7eb; break-inside: avoid; }}
    .screen-section {{ break-inside: avoid; }}
  }}
</style>
</head>
<body>
<div class="container">

  <!-- Header -->
  <div class="report-header">
    <h1>{title}</h1>
    <div class="subtitle">Comprehensive UI/UX Audit Report</div>
    <div class="meta-grid">
      <div class="meta-item"><div class="label">Audit Date</div><div class="value">{meta.get('Audit Date', 'N/A')}</div></div>
      <div class="meta-item"><div class="label">Platform</div><div class="value">{meta.get('Platform', 'N/A')}</div></div>
      <div class="meta-item"><div class="label">Auditor Persona</div><div class="value">{meta.get('Auditor Persona', 'N/A')}</div></div>
      <div class="meta-item"><div class="label">Flow Scope</div><div class="value">{meta.get('Flow Scope', 'N/A')}</div></div>
    </div>
  </div>

  <!-- Score + Summary -->
  <div class="score-section">
    <div class="score-card">
      <div class="score-number">{score}</div>
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
    <p style="color: #6b7280; margin-bottom: 24px;">Each screenshot is annotated with numbered markers corresponding to findings above. Markers are colour-coded by severity.</p>
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
    critical: '#DC2626',
    high: '#EA580C',
    medium: '#CA8A04',
    low: '#16A34A'
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
    print(f"HTML report generated: {output_file} ({file_size:.1f} MB)")


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python3 generate_html.py <audit-dir> <output-file>")
        sys.exit(1)
    build_html(sys.argv[1], sys.argv[2])
