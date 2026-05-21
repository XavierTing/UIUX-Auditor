# UIUX Auditor

An agentic AI-powered Senior UX Auditor and Design Systems Expert that conducts end-to-end UI/UX audits with deep knowledge of interaction design, information architecture, usability heuristics, and conversion-focused design.

Built as a [Claude Code](https://docs.claude.com/en/docs/claude-code) skill — invoke `/ux-audit` with a Figma URL, a live site URL, or a set of screenshots and the auditor produces an annotated, dual-persona, dimension-by-dimension audit report.

---

## What it does

- **Audits 9 UX dimensions** — Information Architecture, Visual Hierarchy, Typography, Colour & Contrast, Components, Forms, Feedback, Cognitive Load, Trust
- **Applies domain lenses** — extra scrutiny for regulated domains (banking/investment, healthcare, legal)
- **Captures screenshots automatically** — Figma MCP, Figma REST API (with PAT), or Playwright for live URLs
- **Annotates findings on the screenshots** — severity-coded pill markers with dotted SVG connectors linking each marker to a finding card
- **Produces a dated HTML report** — self-contained, base64-embedded images, light-mode Anthropic-Research aesthetic (cream `#FAF9F5`, Source Serif 4 / Inter / JetBrains Mono, earthy severity palette)
- **Supports dual-persona audits** — e.g. novice vs experienced, with per-persona impact and a combined score

## Quick start

### 1. Install the skill

Clone into a location your Claude Code project can see:

```bash
git clone https://github.com/XavierTing/UIUX-Auditor.git
cd UIUX-Auditor
```

The skill lives at [`.claude/skills/ux-audit/`](.claude/skills/ux-audit/). To use it in another project, copy that directory into the target project's `.claude/skills/` folder, or invoke it from this directory.

### 2. Install dependencies

```bash
pip install -r requirements.txt
# For live-URL captures (optional):
cd .claude/skills/ux-audit/scripts && npm install playwright && npx playwright install chromium
```

### 3. Run an audit

In Claude Code:

```
/ux-audit https://www.figma.com/design/<file-key>/<file-name>?node-id=<n>
```

Or for a live URL:

```
/ux-audit https://example.com
```

The skill will:
1. Ask you 4 framing questions (target user/goal, known pain points, platform, domain)
2. Capture screenshots via MCP / REST API / Playwright
3. Spawn parallel visual + content analysis agents
4. Synthesise 20–30 findings with severity grades
5. Annotate screenshots and generate the report

### 4. Open the report

```
audits/{audit-date}_{product-name}/reports/{generation-date}/report.html
```

Each regeneration creates a new dated folder; the audit folder itself stays as the canonical source.

## Report visual style

The HTML reports use an editorial light-mode aesthetic inspired by Anthropic's research papers and the Stripe Press / Geist design ecosystems:

- Cream background, near-black body text, generous whitespace, hairline dividers
- Serif display headings, sans body, monospaced numerics
- Earthy severity palette (terracotta / ochre / olive / moss) — calmer than the typical traffic-light red/orange/yellow/green
- Pill-shaped annotation markers (matching the in-page badge), bold Menlo digits, cream hairline ring
- Dotted SVG connector lines from each marker to its finding card, clipped to the pill edge

## Project structure

```
.
├── README.md
├── CLAUDE.md                         # Project instructions for Claude Code (audit methodology + agent rules)
├── AGENTS.md
├── requirements.txt
├── .claude/
│   └── skills/
│       └── ux-audit/
│           ├── SKILL.md               # Skill definition (invoke with /ux-audit)
│           ├── references/            # Audit framework, severity scale, report template
│           ├── scripts/
│           │   ├── annotate.py        # PIL screenshot annotation (severity-coded pill markers)
│           │   ├── capture.js         # Playwright-based live URL capture
│           │   ├── figma_export.py    # Figma REST API frame export
│           │   ├── generate_html.py   # Self-contained HTML report
│           │   ├── generate_pptx.py   # PPTX deck
│           │   ├── generate_combined_html.py  # Comparative report (multiple audits)
│           │   └── generate_combined_pptx.py
│           └── examples/              # Worked audit examples
└── audits/                            # Saved audits (dated folders per audit)
    └── {audit-date}_{product-name}/
        ├── report.md
        ├── findings.json
        ├── screenshots/
        └── reports/                   # Per-regeneration HTML archive
            └── {generation-date}/
                └── report.html
```

## Severity scale

| Symbol | Severity | Meaning |
|---|---|---|
| 🔴 | **CRITICAL** | Blocks user task completion or causes major confusion |
| 🟠 | **HIGH** | Significantly degrades experience, likely causes drop-off |
| 🟡 | **MEDIUM** | Friction point, reduces confidence or efficiency |
| 🟢 | **LOW** | Polish issue, minor inconsistency, nice-to-have |

## Tech stack

- Python 3.9+
- [Pillow](https://pillow.readthedocs.io/) for screenshot annotation
- [Playwright](https://playwright.dev/) for live URL capture
- [python-pptx](https://python-pptx.readthedocs.io/) for PPTX generation
- [Figma MCP](https://www.figma.com/developers/mcp) / REST API for Figma file access
- Designed to run inside [Claude Code](https://docs.claude.com/en/docs/claude-code) with the [Anthropic Claude API](https://docs.claude.com/en/api/overview)

## Author

Built by [Xavier Ting](https://github.com/XavierTing).

## Licence

Internal — see file headers.
