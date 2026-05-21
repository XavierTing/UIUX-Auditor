# Report Template

Follow this exact structure for every audit report. Do not skip any section. Do not reorder sections.

---

## Section 1: Header

```markdown
# UI/UX AUDIT REPORT: {Product Name}

**Audit Date:** {YYYY-MM-DD}
**URL:** `{url}`
**Auditor Persona:** {Who you audited as — e.g., "Novice investor new to precious metals"}
**Platform:** {Web desktop / Mobile web / iOS / Android} ({resolution if known})
**Flow Scope:** {What flows were audited — e.g., "Buy & sell flows for all 4 precious metals"}
**Screens Reviewed:** {List of screens — e.g., "Dashboard, Trade (×4), Order Review, Confirmation, Orders, Products, 404"}
```

---

## Section 2: Executive Summary

- 3-5 sentence overall assessment of the experience
- State what the product does well at a high level
- State the biggest risks or gaps
- Audit coverage (screens reviewed, flow scope)
- **Overall UX Health Score: X/10** with a one-line rationale

The score should reflect:
- 9-10: Production-ready, minimal issues
- 7-8: Solid, some improvements needed
- 5-6: Functional but significant gaps
- 3-4: Major usability problems
- 1-2: Fundamentally broken

---

## Section 3: Findings Table

Present ALL findings in this exact table format:

```markdown
| # | Screen / Component | Dimension | Severity | Finding | User Impact | Recommendation |
|---|---|---|---|---|---|---|
```

**Rules:**
- Sort by severity: Critical → High → Medium → Low
- Number sequentially (1, 2, 3...)
- Every row must have ALL 7 columns filled
- "Screen / Component" must name the specific screen AND component (e.g., "Trade — Order Form", not just "Trade page")
- "Dimension" is the dimension number + short name (e.g., "6. Forms")
- "Severity" uses the labels: CRITICAL, HIGH, MEDIUM, LOW
- "Finding" is a specific, factual observation (not an opinion)
- "User Impact" explains the consequence from the user's perspective
- "Recommendation" is a concrete, implementable fix

**Target: 15-25 findings** for a thorough audit. Fewer than 10 suggests insufficient depth. More than 30 suggests insufficient prioritisation.

---

## Section 4: Annotated Screenshots

Group findings by screen. For each screen that has findings, include:

```markdown
### {Screen Name}

![{Screen Name} — Annotated](screenshots/{screen-name}-annotated.png)

**Findings on this screen:**
- **[#1] CRITICAL** — {Brief finding description} → {Brief recommendation}
- **[#7] HIGH** — {Brief finding description} → {Brief recommendation}
- **[#18] LOW** — {Brief finding description} → {Brief recommendation}
```

**Rules:**
- Order screens by flow sequence (e.g., Dashboard → Trade → Review → Confirmation)
- Within each screen, list findings by severity (Critical first)
- Reference finding numbers that match the Findings Table in Section 3
- The marker numbers on the screenshot MUST match the finding numbers in the table
- If a finding is global (applies to all screens), show its marker on the most representative screen
- Include both the annotated image path AND a brief summary of findings per screen

---

## Section 5: Top 5 Priority Recommendations

Pick the 5 highest-leverage improvements. For each:

```markdown
### {Number}. {Title}
- **What to fix:** Specific change required
- **Why it matters:** User impact and/or business impact
- **How to fix it:** Concrete, implementable recommendation with example if possible
- **Effort estimate:** Quick Win / Medium Lift / Large Effort
```

**Effort definitions:**
- **Quick Win** — Can be done in < 1 day by a single developer. CSS changes, copy updates, adding a tooltip.
- **Medium Lift** — 2-5 days. New component, form restructuring, adding a flow step.
- **Large Effort** — 1+ weeks. Architectural changes, new features, redesigning a core flow.

---

## Section 6: Design System & Consistency Notes

- Flag any inconsistencies with established design system conventions
- Identify rogue components, off-brand patterns, or one-off solutions
- Note components that should be standardised (used 3+ times with slight variations)
- Comment on the design system's strengths (token system, spacing grid, etc.)

---

## Section 7: What's Working Well

- 3-5 specific things done well
- Credit good design decisions, not just surface polish
- Be specific — "Clean visual design" is too vague. "The amber/gold brand identity is appropriate for a precious metals product and the generous whitespace creates a premium feel" is specific.

---

## Section 8: Suggested Next Audit Scope

- Recommend 2-4 areas or flows to audit next based on what you observed
- Brief rationale for each (1 sentence)
- Prioritise by risk — what's most likely to have hidden issues?
