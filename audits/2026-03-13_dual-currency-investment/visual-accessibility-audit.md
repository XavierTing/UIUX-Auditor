# OCBC Corporate Banking -- Dual Currency Investment (DCI)
## Visual & Accessibility Audit Report
**Date:** 13 March 2026
**Screens Reviewed:** 13 Figma exports covering the full DCI lifecycle
**Platform:** Web Desktop (Corporate Banking Portal)

---

## 1. Typography System

### 1.1 Font Sizes Observed

| Role | Estimated Size | Screens Where Used |
|---|---|---|
| Page section label (e.g. "DUAL CURRENCY INVESTMENT") | ~11-12px, uppercase, letter-spaced | All main screens |
| Page heading (e.g. "Investment Parameters", "Funding Account") | ~20-22px, bold | Parameters, Funding, Review, Investment Details |
| Section heading (e.g. "Potential Outcomes", "Settlement Outcome") | ~16-18px, semibold | Parameters (filled), Review, Investment Details |
| Sub-heading (e.g. "SCENARIO A", "SCENARIO B") | ~12-13px, uppercase, semibold | Parameters, Review, Confirmation expanded |
| Body text / values (e.g. "200,000.00 USD", "1.2850") | ~14-16px, regular/semibold | All data screens |
| Form labels (e.g. "Investment Amount", "Currency pair") | ~12-13px, regular | Parameters, Funding Account |
| Helper/description text (e.g. "Projected settlement scenarios") | ~12-13px, regular, gray | Parameters, Funding, Review |
| Small meta text (e.g. "Minimum amount 50,000.00 USD", timestamps) | ~11-12px, regular, gray | Parameters (filled), Landing (active) |
| FAQ questions | ~14px, regular | Landing pages |
| Banner heading ("Ready to invest?") | ~18-20px, bold, white | Landing pages |
| Banner body text | ~13-14px, regular, white | Landing pages |
| Navigation items | ~14px, regular | All screens (top nav) |
| Footer text | ~12px, regular, gray | All screens |
| Button text ("Next", "Submit", "Back") | ~14-15px, semibold | All form screens |
| "FREQUENTLY ASKED QUESTIONS" label | ~11px, uppercase, letter-spaced | Landing pages |
| Table header row (landing with investments) | ~11-12px, uppercase, gray | Landing (active investments) |
| Status badges ("Awaiting Settlement", "Active", "Expiring Soon") | ~11-12px, regular | Landing (active), Investment Details |
| Settlement breakdown labels ("Principal", "Yield") | ~14-15px, regular/semibold | Investment Details |
| Yield positive value ("+1,083.33 USD") | ~14-15px, semibold, green | Investment Details |
| Modal title ("Dual Currency Investment") | ~18-20px, bold | T&C modal |
| Modal body (Lorem ipsum placeholder) | ~13-14px, regular | T&C modal |

### 1.2 Font Weights Observed

- **Bold (700):** Page headings, banner title, modal title, confirmation success heading, monetary values in settlement breakdown
- **Semibold (600):** Section headings, scenario labels, button text, key data values (amounts, rates), "Strike Price" section heading
- **Regular (400):** Body text, form labels, helper text, navigation items, FAQ text, timeline descriptions
- **Light consideration:** The small meta text and helper descriptions appear to use regular weight but at reduced opacity or lighter gray color, creating a visual "light" effect

### 1.3 Line Heights & Letter Spacing

- **Line heights** appear generally appropriate (~1.4-1.5x for body text, ~1.2-1.3x for headings)
- **Letter spacing:** Uppercase labels ("DUAL CURRENCY INVESTMENT", "FREQUENTLY ASKED QUESTIONS", "SCENARIO A/B", "SETTLEMENT COMPONENT", "AMOUNT") use increased letter-spacing (~1-2px tracking), which is correct for uppercase text
- The T&C modal body text has adequate line-height for readability of long-form content
- Timeline descriptions have comfortable line-height for multi-line helper text

### 1.4 Typography Issues

| # | Issue | Severity | Screen(s) | Details |
|---|---|---|---|---|
| T1 | Inconsistent page title treatment | MEDIUM | All screens | "DUAL CURRENCY INVESTMENT" uses uppercase + letter-spacing as a breadcrumb-like label, but "Investment Parameters" uses sentence case bold as the true heading. The visual hierarchy between these two is unclear -- the smaller uppercase label appears above the larger heading, creating ambiguity about which is the page title. |
| T2 | Small text may fail minimum size for banking | MEDIUM | Landing (active), Investment Details | Table header text and status badges at ~11px are at the threshold of readability. For a banking product used by corporate treasurers (potentially older users), 12px should be the absolute minimum for any text. |
| T3 | Placeholder Lorem Ipsum in T&C modal | CRITICAL | t-c.png | The Terms & Conditions modal contains Lorem Ipsum placeholder text. For a banking product, this is a critical gap -- users are asked to "Agree" to nonsensical Latin text. |
| T4 | Dense information in landing table | MEDIUM | renew-landing-uploaded-file-3.png | The active investments table packs Currency Pair, Strike Price (with "Fixing Rate" subtitle), Tenor, Status, dates (Transaction/Expiry/Maturity), and Investment Amount into a single row. At the observed font sizes, this creates a very dense reading experience. |
| T5 | Inconsistent value formatting emphasis | LOW | Review, Confirmation expanded | On the Review screen, key values like "200,000.00 USD" appear in the same weight as surrounding text in some sections but bold in others (e.g., the Potential Outcomes cards vs. the Investment Details section). |
| T6 | "REVIEW" label styling inconsistent | LOW | review.png | The "REVIEW" label in the left margin uses a different treatment (vertical orientation suggestion, uppercase) that does not match the page label pattern used on other screens ("DUAL CURRENCY INVESTMENT"). |

---

## 2. Color Palette

### 2.1 Complete Color Inventory

#### Brand Colors
| Color | Estimated Hex | Usage |
|---|---|---|
| OCBC Red (primary) | `#D6001C` / `#E3001B` | OCBC logo, primary nav active indicator (underline), "DUAL CURRENCY INVESTMENT" accent line, red horizontal rule |
| OCBC Red (dark) | `#B8001A` | Active nav underline, header accent bar |

#### Background Colors
| Color | Estimated Hex | Usage |
|---|---|---|
| White | `#FFFFFF` | Page background, card backgrounds, form fields, modal background |
| Light Gray (page) | `#F5F5F5` / `#F7F7F7` | Outer page background (visible on some screens), empty state area, landing filter section background |
| Light Gray (section) | `#F8F8F8` / `#FAFAFA` | Potential Outcomes panel background, Settlement breakdown section |
| Dark charcoal (banner) | `#2D2D2D` / `#333333` | "Ready to invest?" banner background |
| Green tint (Scenario A) | `#E8F5E9` / `#EDF7EE` | Scenario A card background (base currency outcome) |
| Orange/Amber tint (Scenario B) | `#FFF3E0` / `#FEF4E6` | Scenario B card background (alternate currency outcome) |
| Green tint (strike met alert) | `#E8F5E9` | "Strike Price Met" alert banner background |
| Amber tint (strike not met alert) | `#FFF8E1` / `#FEF4E6` | "Strike Price Not Met" alert banner background |
| Green tint (settlement row) | `#E8F5E9` | Strike Price Met row highlight on landing table |
| Amber tint (settlement row) | `#FFF8E1` | Strike Price Not Met row highlight on landing table |
| Modal overlay | `rgba(100,110,120,0.6)` approx | T&C modal backdrop (gray-blue overlay) |

#### Text Colors
| Color | Estimated Hex | Usage |
|---|---|---|
| Near-black | `#1A1A1A` / `#222222` | Primary headings, key values, body text |
| Dark gray | `#333333` / `#444444` | Secondary text, form values |
| Medium gray | `#666666` / `#777777` | Labels, descriptions, helper text |
| Light gray | `#999999` / `#AAAAAA` | Placeholder text, meta text, timestamps, disabled text |
| White | `#FFFFFF` | Banner heading text, text on dark backgrounds |
| OCBC Red | `#D6001C` | "Place investment" link text on landing empty state |
| Green (positive) | `#2E7D32` / `#1B8C1B` | Yield values ("+1,083.33 USD"), "2.7% p.a." on landing |
| Blue (link) | `#0066CC` / `#1A73E8` | "Download Termsheet" link, "Terms and Conditions" link on Review |
| Teal/Dark cyan | `#00838F` / `#007B83` | "Place investment" icon on landing empty state, T&C modal close button |

#### Interactive Element Colors
| Color | Estimated Hex | Usage |
|---|---|---|
| Red (primary button) | `#D6001C` / `#E3001B` | "Next" button, "Submit" button, "Place Another Investment" button, "Agree" button in modal, "Open Multi-Currency Account" button |
| White (button text) | `#FFFFFF` | Text on red primary buttons |
| Dark gray (outline button) | `#333333` border | "Back" button, "Cancel" button (outline style) |
| Green (badge - Base Currency) | `#2E7D32` bg, `#FFFFFF` text | "Base Currency" badge in Scenario A |
| Orange/Red (badge - Alt Currency) | `#E65100` / `#D84315` bg, `#FFFFFF` text | "Alternate Currency" badge in Scenario B |
| Amber/Orange (status badge) | `#FF8F00` / `#F57C00` text | "Expiring Soon" status on landing |
| Green (status) | `#2E7D32` | "Active" status text on landing |
| Amber (status badge bg) | `#FFF3E0` bg with `#E65100` text | "Awaiting Settlement" badge on Investment Details |
| Green (success icon) | `#4CAF50` / `#43A047` | Checkmark circle on Confirmation screen |
| Green (strike met icon) | `#4CAF50` | Checkmark icon in "Strike Price Met" alert |
| Amber (strike not met icon) | `#FF9800` / `#F57C00` | Warning triangle icon in "Strike Price Not Met" alert |

#### Border & Divider Colors
| Color | Estimated Hex | Usage |
|---|---|---|
| Light gray border | `#E0E0E0` / `#EEEEEE` | Card borders, form input borders, table row dividers, section dividers |
| Medium gray border | `#CCCCCC` / `#D0D0D0` | Dropdown borders, more prominent dividers |
| Red accent line | `#D6001C` | Short horizontal rule under "DUAL CURRENCY INVESTMENT" heading |

#### Radio Button / Selection Colors
| Color | Estimated Hex | Usage |
|---|---|---|
| Dark gray (selected radio) | `#333333` / `#222222` | Selected strike price radio button fill |
| Light gray (unselected radio) | `#CCCCCC` | Unselected strike price radio buttons |
| Timeline active dot | `#333333` | Filled circle for Transaction Date in timeline |
| Timeline inactive dot | `#CCCCCC` / `#E0E0E0` | Empty circles for future dates in timeline |

### 2.2 Color Inconsistencies

| # | Issue | Details |
|---|---|---|
| C1 | "Awaiting Settlement" badge color varies | On the landing table (renew-landing-uploaded-file-3.png) vs. Investment Details screens, the badge appears to use slightly different background tints and text colors. |
| C2 | Green usage is overloaded | Green is used for: (1) positive yield values, (2) "Active" status, (3) success confirmation checkmark, (4) "Base Currency" badge, (5) "Strike Price Met" alert, (6) yield percentage on landing. This overloading means green simultaneously signals "status: active", "outcome: favorable", and "scenario A". These are semantically different. |
| C3 | Red brand color doubles as primary action | The OCBC brand red is used for primary CTA buttons, which is standard for OCBC but may create tension if red is ever needed for error states. Currently no red error states are visible in these screens, suggesting errors have not been designed. |
| C4 | Inconsistent link color | "Place investment" on the empty landing uses a teal/cyan color, while "Download Termsheet" and "Terms and Conditions" use blue. Links should use a single, consistent color. |

---

## 3. Contrast Ratios (WCAG AA Evaluation)

### 3.1 Evaluation by Element Type

| Element | Foreground (est.) | Background (est.) | Est. Ratio | WCAG AA Requirement | Pass/Fail |
|---|---|---|---|---|---|
| **Body text on white** | `#333333` | `#FFFFFF` | ~12.6:1 | 4.5:1 | PASS |
| **Page headings on white** | `#1A1A1A` | `#FFFFFF` | ~16.8:1 | 3:1 (large) | PASS |
| **Helper text (gray) on white** | `#999999` | `#FFFFFF` | ~2.8:1 | 4.5:1 | FAIL |
| **Helper text (medium gray) on white** | `#777777` | `#FFFFFF` | ~4.5:1 | 4.5:1 | BORDERLINE |
| **Placeholder text in form fields** | `#AAAAAA` | `#FFFFFF` | ~2.3:1 | 4.5:1 | FAIL |
| **Red button text** | `#FFFFFF` | `#D6001C` | ~5.8:1 | 4.5:1 | PASS |
| **Banner text on dark bg** | `#FFFFFF` | `#2D2D2D` | ~13.2:1 | 4.5:1 | PASS |
| **"Active" status (green text)** | `#2E7D32` | `#FFFFFF` | ~5.2:1 | 4.5:1 | PASS |
| **"Expiring Soon" (amber text)** | `#F57C00` | `#FFFFFF` | ~3.0:1 | 4.5:1 | FAIL |
| **"Awaiting Settlement" badge** | `#E65100` | `#FFF3E0` | ~3.9:1 | 4.5:1 | FAIL |
| **Scenario A values on green bg** | `#333333` | `#E8F5E9` | ~10.5:1 | 4.5:1 | PASS |
| **Scenario B values on amber bg** | `#333333` | `#FFF3E0` | ~11.0:1 | 4.5:1 | PASS |
| **Yield green values on white** | `#2E7D32` | `#FFFFFF` | ~5.2:1 | 4.5:1 | PASS |
| **Table header gray uppercase** | `#999999` | `#FFFFFF` | ~2.8:1 | 4.5:1 | FAIL |
| **"Base Currency" badge** | `#FFFFFF` | `#2E7D32` | ~5.2:1 | 4.5:1 | PASS |
| **"Alternate Currency" badge** | `#FFFFFF` | `#E65100` | ~4.0:1 | 4.5:1 | BORDERLINE/FAIL |
| **Blue link text on white** | `#0066CC` | `#FFFFFF` | ~5.3:1 | 4.5:1 | PASS |
| **Teal link text on white** | `#007B83` | `#FFFFFF` | ~5.0:1 | 4.5:1 | PASS (borderline) |
| **Meta text (timestamps) on white** | `#AAAAAA` | `#FFFFFF` | ~2.3:1 | 4.5:1 | FAIL |
| **Footer text** | `#999999` | `#FFFFFF` | ~2.8:1 | 4.5:1 | FAIL |
| **"indicative yield" label (gray)** | `#999999` | `#FFFFFF` | ~2.8:1 | 4.5:1 | FAIL |
| **Strike Price Met alert text** | `#333333` | `#E8F5E9` | ~10.5:1 | 4.5:1 | PASS |
| **Strike Price Not Met alert text** | `#333333` | `#FFF8E1` | ~11.8:1 | 4.5:1 | PASS |
| **"Reinvest" button (outline)** | `#333333` | `#FFFFFF` | ~12.6:1 | 4.5:1 | PASS |
| **Modal body text** | `#333333` | `#FFFFFF` | ~12.6:1 | 4.5:1 | PASS |
| **Small "from spot" labels** | `#999999` | `#FFFFFF` | ~2.8:1 | 4.5:1 | FAIL |

### 3.2 Summary of Contrast Failures

| # | Severity | Element | Screen(s) | Est. Ratio | Required |
|---|---|---|---|---|---|
| CR1 | HIGH | Helper/description text (~#999 on white) | Parameters, Funding, Review, Landing | ~2.8:1 | 4.5:1 |
| CR2 | HIGH | "Expiring Soon" status text (amber on white) | Landing (active investments) | ~3.0:1 | 4.5:1 |
| CR3 | HIGH | "Awaiting Settlement" badge text | Landing (active investments), Investment Details | ~3.9:1 | 4.5:1 |
| CR4 | MEDIUM | Form placeholder text | Parameters (empty), Funding Account | ~2.3:1 | 4.5:1 |
| CR5 | HIGH | Table column headers (uppercase gray) | Landing (active investments) | ~2.8:1 | 4.5:1 |
| CR6 | MEDIUM | Timestamp/meta text | Landing (active investments), Parameters (filled) | ~2.3:1 | 4.5:1 |
| CR7 | MEDIUM | Footer text | All screens | ~2.8:1 | 4.5:1 |
| CR8 | HIGH | "indicative yield" and "from spot" labels | Parameters (filled), Reinvest step 1 | ~2.8:1 | 4.5:1 |
| CR9 | MEDIUM | "Alternate Currency" badge (white on orange) | Parameters, Review, Confirmation | ~4.0:1 | 4.5:1 |

**Total contrast failures: 9 distinct patterns**, affecting virtually every screen in the flow. This is the single largest accessibility risk in the design.

---

## 4. Spacing & Alignment

### 4.1 Grid System

- The content area appears to use a **centered container** of approximately **960-1040px** width on most screens
- The landing page with active investments uses a **wider table layout** that extends closer to the edges
- The Investment Parameters screen uses a **two-column layout**: left column (~55%) for form inputs, right column (~45%) for the Potential Outcomes panel
- The Review screen and Investment Details screens use a **single-column layout** with a centered content area
- The Confirmation screen is **center-aligned** with a narrower content column

### 4.2 Padding Patterns

| Element | Observed Padding | Consistency |
|---|---|---|
| Card/panel padding | ~24px internal padding | Generally consistent |
| Scenario A/B cards (Potential Outcomes) | ~16-20px padding | Consistent within panel |
| Form input fields | ~12-16px horizontal, ~10-12px vertical | Consistent |
| Banner ("Ready to invest?") | ~24-32px vertical, ~32-40px horizontal | Consistent |
| Section spacing (between sections) | ~32-40px | Generally consistent but varies |
| FAQ accordion items | ~16-20px vertical padding | Consistent |
| Investment Timeline items | ~12-16px vertical spacing | Consistent |
| Settlement breakdown table rows | ~12-16px vertical padding | Consistent |
| Navigation bar padding | ~12-16px vertical | Consistent |
| Footer padding | ~16-24px | Consistent |
| Modal padding | ~24-32px | Appears adequate |

### 4.3 Gap Patterns

| Context | Observed Gap | Notes |
|---|---|---|
| Between filter dropdowns (landing) | ~16px | Consistent |
| Between FAQ items | ~0px (dividers used) | Consistent |
| Between form label and input | ~4-8px | Tight but acceptable |
| Between investment rows in table | Divider-separated | Consistent |
| Between Scenario A and B cards | ~16px | Consistent |
| Between strike price radio options | ~12-16px | Consistent |
| Between Investment Timeline steps | ~16-20px | Consistent |
| Between "Back" and "Next" buttons | Full width separation (left-right aligned) | Consistent |
| Between sections on Review page | ~24-32px | Consistent |

### 4.4 Alignment Issues

| # | Issue | Severity | Screen | Details |
|---|---|---|---|---|
| S1 | Two-column data alignment inconsistency | MEDIUM | Review, Investment Details | In the Investment Overview / Investment Details sections, the left and right columns (e.g., "Investment Amount" / "Currency Pair") appear to use a two-column grid, but the right column start position shifts between screens. On the Review screen, "Currency Pair" aligns roughly at center. On Investment Details, "Investment Amount" (right) aligns further right. |
| S2 | Potential Outcomes panel vertical alignment | LOW | Parameters (empty vs. filled) | On the empty state (day-1-add-delete-users.png), the Potential Outcomes panel top-aligns with the form section. On the filled state (day-1-add-delete-users-3.png), the panel has grown significantly taller than the form, creating uneven bottom edges. This is not necessarily wrong but makes the layout feel unbalanced. |
| S3 | Strike Price radio list left alignment | LOW | Parameters (filled), Reinvest step 1 | The strike price values (e.g., "1.2830") and the "indicative yield" percentages (e.g., "6.70%") are left-aligned and right-aligned respectively within the strike price card, but the "from spot" helper text sits beneath each value in a smaller size, creating an inconsistent visual rhythm. |
| S4 | Button alignment across screens | MEDIUM | All form screens | "Back" is consistently left-aligned and "Next"/"Submit" is right-aligned. This is a common pattern, but the vertical spacing between the last content element and the button row varies: tighter on the Funding Account screen, more spacious on the Parameters screen. |
| S5 | Landing table column alignment | LOW | renew-landing-uploaded-file-3.png | The table is information-dense. Currency pair and dates columns appear to have inconsistent column widths, with the "DATES" column squeezed and the "INVESTMENT AMOUNT" column having extra right padding. |
| S6 | "REVIEW" label position | MEDIUM | review.png | The "REVIEW" step label appears in the far left margin, disconnected from the main content. This label placement does not match the heading pattern on other screens and could confuse users about where they are in the flow. There is no step indicator or breadcrumb showing the multi-step progress (Step 1: Parameters > Step 2: Accounts > Step 3: Review). |

---

## 5. WCAG 2.2 Accessibility Assessment

### 5.1 Criterion-by-Criterion Analysis

#### 1.1.1 Non-text Content (Level A)

| Finding | Severity | Screen | Details |
|---|---|---|---|
| Decorative illustrations lack alt text consideration | LOW | Landing (empty), Confirm OMC | The briefcase/investor illustration and the question-mark illustration are decorative. In implementation, they should use `alt=""` or `role="presentation"`. No issue if implemented correctly, but the design does not indicate this. |
| Currency flags lack text alternatives | MEDIUM | Parameters (filled), Reinvest | Small flag icons (US, Singapore, EUR) next to currency codes need alt text. The currency code text ("USD", "SGD") is adjacent, so flags could be decorative, but this should be specified in design annotations. |
| OCBC logo needs alt text | LOW | All screens | Standard requirement -- should be `alt="OCBC"` or `alt="OCBC - Home"`. |
| Globe/language icon | LOW | All screens | The globe icon next to "EN" in the header needs an accessible label. |
| Status icons (checkmark, warning triangle) | MEDIUM | Investment Details, Landing | The green checkmark and amber warning icons in the strike price alerts convey meaning and need text alternatives. The adjacent text does describe the status, so these may be decorative, but should be explicitly annotated. |

#### 1.3.1 Info and Relationships (Level A)

| Finding | Severity | Screen | Details |
|---|---|---|---|
| Form structure needs semantic markup | HIGH | Parameters, Funding Account | The "Investment Amount", "Currency pair", "Tenor" fields must use proper `<label>` elements associated with inputs via `for`/`id`. The design shows labels above inputs, which is correct visually, but implementation must preserve the programmatic association. |
| Strike Price as radio group | HIGH | Parameters (filled), Reinvest | The strike price selection must be implemented as a `<fieldset>` with `<legend>` ("Strike Price") and radio `<input>` elements. The design shows radio buttons, which is good, but the group heading and the structure need explicit annotation. |
| Table structure on landing | HIGH | Landing (active) | The investments list must be a proper `<table>` with `<thead>`, `<th>` headers, and `<tbody>` rows. The visual design implies a table but uses what appears to be a card/list hybrid. |
| Settlement breakdown table | MEDIUM | Investment Details | The "Settlement breakdown" section with "SETTLEMENT COMPONENT" and "AMOUNT" headers must be a proper `<table>`. |
| Investment Timeline structure | MEDIUM | Parameters (filled), Confirmation, Review | The timeline should use an ordered list `<ol>` with appropriate ARIA roles to convey sequence. |
| Scenario A/B structure | MEDIUM | Parameters, Review, Confirmation | The two scenarios should be clearly related and potentially grouped with headings that indicate they are mutually exclusive outcomes. |

#### 1.4.1 Use of Color (Level A)

| Finding | Severity | Screen | Details |
|---|---|---|---|
| "Expiring Soon" uses color as sole differentiator | HIGH | Landing (active) | The "Expiring Soon" status is differentiated from "Active" and "Awaiting Settlement" primarily by its amber/orange color. While the text label itself provides differentiation, the visual weight of color as the primary scanning mechanism means users with color vision deficiencies may struggle to quickly identify which investments need attention. An icon (e.g., clock/warning) should accompany the text. |
| Scenario A (green) vs. Scenario B (orange) | MEDIUM | Parameters, Review, Confirmation | The two scenarios rely on green vs. orange background tinting to differentiate them. The text labels "SCENARIO A" / "SCENARIO B" and "Base Currency" / "Alternate Currency" badges provide redundant cues, which is good. However, the "Base Currency" badge (green) and "Alternate Currency" badge (red-orange) on white could be confused by users with red-green color deficiency. Adding icons or patterns would improve differentiation. |
| Strike Price Met (green) vs. Not Met (amber) alerts | MEDIUM | Investment Details, Landing | The green and amber alert banners use color plus icon (checkmark vs. warning triangle) plus text to convey status. The icon + text provides adequate redundancy. However, the green vs. amber background tinting on landing table rows relies heavily on color. |
| Positive yield shown in green | MEDIUM | Investment Details | The "+1,083.33 USD" yield value is displayed in green to indicate positive return. No secondary indicator (e.g., "+" sign alone is good, but adding a label "Yield earned" or an upward arrow icon would strengthen accessibility). The "+" prefix does provide a non-color cue, which partially addresses this. |

#### 1.4.3 Contrast (Minimum) (Level AA)

**See Section 3 for detailed contrast analysis.** Summary: **9 distinct contrast failure patterns** identified, primarily in helper text, status badges, table headers, and meta text.

**Overall risk: HIGH.** The most critical failures are:
- Helper/description text across all screens (~2.8:1 against 4.5:1 required)
- "Expiring Soon" and "Awaiting Settlement" status indicators (~3.0-3.9:1)
- Table column headers (~2.8:1)
- "indicative yield" and "from spot" labels in strike price selection

#### 1.4.11 Non-text Contrast (Level AA) -- 3:1 required

| Element | Est. Ratio | Pass/Fail | Screen |
|---|---|---|---|
| Form input borders (light gray on white) | ~2.5-3.0:1 | BORDERLINE/FAIL | Parameters, Funding |
| Dropdown borders | ~3.0:1 | BORDERLINE | Parameters, Funding, Landing |
| Radio button (unselected) border | ~3.5:1 | PASS | Parameters (filled) |
| Radio button (selected) fill | >7:1 | PASS | Parameters (filled) |
| Card borders | ~2.5:1 | FAIL | Landing, Parameters |
| Timeline inactive dots | ~2.5:1 | FAIL | Parameters (filled), Confirmation, Review |
| Chevron/expand icons in FAQ | ~3.0:1 | BORDERLINE | Landing |
| Red primary button | N/A (solid fill) | PASS | All form screens |
| Outline button border | ~4.0:1 | PASS | All form screens |
| Tab underline (active) | N/A (red) | PASS | Landing (active investments) |

**Form input borders are a significant concern.** The light gray borders (~#E0E0E0) on white backgrounds produce approximately 2.5:1 contrast, below the 3:1 WCAG 1.4.11 requirement. This affects every form field across the Parameters and Funding Account screens.

#### 2.1.1 Keyboard (Level A)

| Finding | Severity | Screen | Details |
|---|---|---|---|
| No keyboard interaction design visible | HIGH | All screens | The designs do not show any keyboard interaction states. There is no evidence of focus ring design, tab order specification, or keyboard navigation patterns. For a banking product, this is a significant gap. |
| Strike price radio selection | HIGH | Parameters (filled) | The radio button group must be keyboard navigable with arrow keys. No keyboard behavior is specified. |
| FAQ accordion | MEDIUM | Landing | FAQ expand/collapse must be keyboard operable. No keyboard state shown. |
| Dropdown fields | HIGH | Parameters, Funding, Landing | All dropdowns must be keyboard operable with standard select behavior. |
| "Place investment" link in empty state | MEDIUM | Landing (empty) | Must be keyboard reachable and have clear focus indication. |
| Modal (T&C) | HIGH | T&C modal | Modal must trap focus, be dismissible with Escape, and return focus to trigger on close. No keyboard specification visible. |

#### 2.4.6 Headings and Labels (Level AA)

| Finding | Severity | Screen | Details |
|---|---|---|---|
| Heading hierarchy unclear | MEDIUM | All screens | "DUAL CURRENCY INVESTMENT" appears as a page-level label but is visually smaller than section headings like "Investment Parameters". The heading hierarchy should be: H1: "Dual Currency Investment" (or the specific page like "Investment Parameters"), H2: sections like "Potential Outcomes", "Strike Price", "Investment Timeline". Currently the visual hierarchy does not map cleanly to heading levels. |
| Generic heading "Investment details" | LOW | Review, Confirmation (expanded) | On the Review screen, "Investment details" is used as a section heading alongside an "Edit" link. On the Confirmation expanded screen, the same heading appears. These are descriptive enough. |
| "Accounts" heading adequate | PASS | Review, Confirmation | Clear, descriptive heading. |
| "Settlement Outcome" heading | PASS | Investment Details | Clear, descriptive heading. |

#### 2.4.7 Focus Visible (Level AA)

| Finding | Severity | Screen | Details |
|---|---|---|---|
| No focus indicators designed | CRITICAL | All screens | None of the 13 screens show focus indicator designs. For a banking product that may be used via keyboard (especially by users with motor disabilities or power users), this is a critical omission. Every interactive element (buttons, links, inputs, dropdowns, radio buttons, accordion triggers, tabs) needs a visible focus indicator. The recommended pattern is a 2px offset outline in a high-contrast color (e.g., the OCBC red or a blue/black). |

#### 2.5.8 Target Size (Minimum) (Level AA -- WCAG 2.2)

| Element | Est. Size | Meets 24x24px? | Meets 44x44px? | Screen |
|---|---|---|---|---|
| "Next" / "Submit" button | ~140x44px | YES | YES | All form screens |
| "Back" button | ~100x44px | YES | YES | All form screens |
| Radio buttons (strike price) | ~20x20px click target (visual), but row likely ~48px tall | Row: YES | Row: YES (if whole row is clickable) | Parameters (filled) |
| FAQ accordion rows | Full width, ~48px height | YES | YES | Landing |
| "Show" expand links in FAQ | ~50x20px visual target | YES | Likely NO (if only text is clickable) | Landing |
| Filter dropdowns on landing | ~140x36px | YES | NO (height ~36px) | Landing |
| "Place investment" button (banner) | ~160x44px | YES | YES | Landing |
| "Place investment" link (empty state) | Text link, ~140x20px | YES | NO | Landing (empty) |
| Search input | ~180x36px | YES | NO (height ~36px) | Landing |
| Tab switches ("Active Investments" / "Settled") | ~150x36px | YES | NO (height) | Landing (active) |
| "Edit" pencil icon links | ~60x20px | YES | NO | Review |
| "Reinvest" button | ~80x36px | YES | NO (height ~36px) | Investment Details |
| Close button (X) on T&C modal | ~24x24px | YES | NO | T&C modal |
| "Download Termsheet" link | Text link ~160x20px | YES | NO | Investment Details |
| Navigation menu items | ~80x48px | YES | YES | All screens |
| "Agree" / "Cancel" modal buttons | ~100x40px | YES | BORDERLINE | T&C modal |

**Summary:** Several interactive elements fall below the 44x44px minimum recommended for touch targets, though this is primarily a desktop product. The more critical WCAG 2.2 minimum of 24x24px is met by most elements. The "Show" links in FAQ, "Edit" links on Review, and the modal close button are the most concerning.

#### 3.3.2 Labels or Instructions (Level A)

| Finding | Severity | Screen | Details |
|---|---|---|---|
| "Investment Amount" label always visible | PASS | Parameters | The label sits above the input field, not as a placeholder. Good. |
| "Currency pair" labels visible | PASS | Parameters | "Base Currency" and "Alternate Currency" labels are persistent. |
| "Tenor" label visible | PASS | Parameters | Above the dropdown. |
| Funding Account field uses placeholder-as-label | HIGH | Funding Account | "Funding account" appears inside the dropdown as placeholder text. When a value is selected, does the label persist? The helper text "Select the account to debit..." is above the section, not directly associated with the field. The dropdown should have a persistent label above it. |
| Settlement Account fields have visible labels | PASS | Funding Account | "Settlement Account - Base Currency (USD)" and "Settlement Account - Alternate Currency (SGD)" are visible labels. |
| Helper text below settlement fields | PASS | Funding Account | "Funds will be credited here if settlement is in USD/SGD" provides clear instruction. |
| Filter dropdowns on landing use label-as-value | MEDIUM | Landing | "All Currencies", "Status", "Tenor" are shown as the current value/default. When a filter is selected, the label may disappear. These should have persistent labels. |
| Minimum amount instruction | PASS | Parameters (filled) | "Minimum amount 50,000.00 USD" is shown below the input. |

#### 4.1.2 Name, Role, Value (Level A)

| Finding | Severity | Screen | Details |
|---|---|---|---|
| No ARIA annotations in design | HIGH | All screens | The designs do not include any ARIA annotation specifications. For implementation, the following need explicit ARIA roles/labels: |
| -- Status badges | HIGH | Landing, Investment Details | Badges like "Awaiting Settlement", "Active", "Expiring Soon" need `role="status"` or be within elements with appropriate ARIA labels. |
| -- Investment Timeline | MEDIUM | Parameters, Review, Confirmation | Should use `aria-current="step"` for the active step, with appropriate list semantics. |
| -- Potential Outcomes scenarios | MEDIUM | Parameters, Review | Scenario A and B cards should have `aria-label` attributes describing the scenario (e.g., "Settlement in base currency if fixing rate is at or above strike price"). |
| -- Modal dialog | HIGH | T&C modal | Must use `role="dialog"`, `aria-modal="true"`, `aria-labelledby` pointing to the title. |
| -- Expand/collapse (FAQ, Confirmation) | MEDIUM | Landing, Confirmation | Must use `aria-expanded`, `aria-controls` for accordion behavior. |
| -- Strike Price radio group | HIGH | Parameters | Must have `role="radiogroup"` with `aria-labelledby` pointing to "Strike Price" heading. |

### 5.2 WCAG 2.2 Compliance Summary

| Criterion | Level | Status | Risk |
|---|---|---|---|
| 1.1.1 Non-text Content | A | Partially met (design gaps) | MEDIUM |
| 1.3.1 Info and Relationships | A | Not specified in design | HIGH |
| 1.4.1 Use of Color | A | Partially met (some redundancy, some gaps) | MEDIUM |
| 1.4.3 Contrast (Minimum) | AA | FAIL -- 9 patterns below threshold | CRITICAL |
| 1.4.11 Non-text Contrast | AA | FAIL -- form borders, timeline dots | HIGH |
| 2.1.1 Keyboard | A | Not designed | CRITICAL |
| 2.4.6 Headings and Labels | AA | Partially met | MEDIUM |
| 2.4.7 Focus Visible | AA | Not designed | CRITICAL |
| 2.5.8 Target Size | AA | Partially met (some undersized) | MEDIUM |
| 3.3.2 Labels or Instructions | A | Mostly met (one failure on Funding) | MEDIUM |
| 4.1.2 Name, Role, Value | A | Not specified in design | HIGH |

**Overall Accessibility Risk Level: CRITICAL**

The combination of widespread contrast failures, absent keyboard/focus design, and missing ARIA specifications represents a critical accessibility risk for a banking product. Banking products are subject to heightened regulatory scrutiny and serve users who may rely on assistive technology.

---

## 6. Component Consistency

### 6.1 Button Styles

| Button Type | Visual Style | Screens Used | Consistency |
|---|---|---|---|
| **Primary (red filled)** | Red bg (#D6001C), white text, rounded corners (~4-6px), ~44px height | "Next" (Parameters, Funding), "Submit" (Review), "Agree" (T&C modal), "Place Another Investment" (Confirmation), "Open Multi-Currency Account" (Confirm OMC), "Place investment" (Landing banner) | CONSISTENT -- same red, same border radius, same height |
| **Secondary (outline)** | White bg, dark gray border, dark gray text, rounded corners (~4-6px), ~44px height | "Back" (Parameters, Funding, Review, Investment Details), "Cancel" (T&C modal) | CONSISTENT |
| **Tertiary (outline, small)** | White bg, gray border, dark text, smaller (~36px height) | "Reinvest" (Investment Details), "Renew" (Landing active) | MOSTLY CONSISTENT -- slightly smaller than primary/secondary, appears on data screens only |
| **Text link button** | Teal/cyan text with icon, no border | "Place investment" (Landing empty state) | ONE-OFF -- uses a different color than standard links |
| **Ghost/icon button** | "Edit" with pencil icon, no border | "Edit" (Review screen, next to "Investment details" and "Accounts") | CONSISTENT with each other but unique to Review screen |

**Button Issues:**
- B1 (LOW): The "Reinvest" and "Renew" buttons appear slightly shorter (~36px) than the standard ~44px primary/secondary buttons. For consistency and touch target compliance, these should match the standard button height.
- B2 (MEDIUM): The "Place Another Investment" button on the Confirmation screen is red (primary), which is correct for the primary action, but its width is larger than typical CTAs, creating visual inconsistency with the narrower "Next"/"Submit" buttons on prior screens.
- B3 (LOW): The "Download Termsheet" link on Investment Details uses a blue text link style with a download icon, which is different from any button pattern. This is appropriate for a secondary action but should be documented as a distinct component.

### 6.2 Input Field Styles

| Input Type | Visual Style | Screens Used | Consistency |
|---|---|---|---|
| **Text input** | White bg, light gray border (~1px), rounded corners (~4px), ~44px height | "Investment Amount" (Parameters) | CONSISTENT |
| **Dropdown/Select** | White bg, light gray border, chevron icon right-aligned, rounded corners, ~44px height | Currency pair, Tenor (Parameters), Funding/Settlement accounts (Funding), Filters (Landing) | MOSTLY CONSISTENT -- the filter dropdowns on the landing page appear slightly shorter |
| **Radio buttons** | Standard circular radio, dark fill when selected | Strike Price options (Parameters, Reinvest) | CONSISTENT |
| **Search input** | White bg, light gray border, search icon left-aligned | Search field on Landing | ONE-OFF but appropriate |

**Input Issues:**
- I1 (MEDIUM): Filter dropdowns on the landing page ("All Currencies", "Status", "Tenor") appear shorter (~36px) than the form dropdowns on the Parameters screen (~44px). These should be unified to a single height.
- I2 (LOW): The "Investment Amount" input shows a currency flag + code ("NIL" or "USD") inside the input on the right side. This inline currency indicator is a nice pattern but should be documented as a specific input variant.

### 6.3 Card/Panel Styles

| Card Type | Visual Style | Screens Used | Consistency |
|---|---|---|---|
| **Potential Outcomes panel** | Light gray bg (#F8F8F8), subtle border or shadow, contains Scenario A/B cards | Parameters (empty/filled), Review, Confirmation (expanded) | CONSISTENT across flow |
| **Scenario A card** | Light green bg (#E8F5E9), "Base Currency" badge (green) | Parameters, Review, Confirmation | CONSISTENT |
| **Scenario B card** | Light amber/orange bg (#FFF3E0), "Alternate Currency" badge (orange-red) | Parameters, Review, Confirmation | CONSISTENT |
| **Strike Price card** | White bg, light border, contains radio options | Parameters (filled), Reinvest | CONSISTENT |
| **Settlement breakdown card** | White bg, visible border, table-like layout | Investment Details (both) | CONSISTENT |
| **Alert banner (success/green)** | Light green bg, green checkmark icon, descriptive text | Investment Details (strike met), Landing (active) | CONSISTENT |
| **Alert banner (warning/amber)** | Light amber bg, warning triangle icon, descriptive text | Investment Details (strike not met), Landing (active) | CONSISTENT |
| **Info banner ("Ready to invest?")** | Dark charcoal bg, white text, red CTA button | Landing (both) | CONSISTENT |
| **Value proposition cards** | White bg, subtle border, icon + text | Landing (empty) -- "Maximise your investment returns" and "Great for currency conversion" | ONE-OFF -- only appears on landing |

### 6.4 Navigation Consistency

| Screen | Nav Item Highlighted | Nav Text | Issue |
|---|---|---|---|
| Landing (empty) | "FX and Investment" (underlined red) | "FX and Investment" | -- |
| Landing (active investments) | "FX and Investment" (underlined red) | "FX and Investment" | -- |
| Parameters (empty) | "FX and Investment" | "FX and Investment" | -- |
| Parameters (filled) | "FX and Investment" | "FX and Investment" | -- |
| Funding Account | "FX and Investment" | "FX and Investment" | -- |
| Review | "FX and Investment" | "FX and Investment" | -- |
| Confirmation (collapsed) | "FX and Investment" | "FX and Investment" | -- |
| Confirmation (expanded) | "FX and Investment" | "FX and Investment" | -- |
| **Investment Details (strike met)** | **"FX and Treasury"** | **"FX and Treasury"** | **INCONSISTENT** |
| **Investment Details (strike not met)** | **"FX and Treasury"** | **"FX and Treasury"** | **INCONSISTENT** |
| T&C modal | N/A (modal overlay) | N/A | -- |
| **Confirm OMC** | **"Trade finance"** (underlined) | **"Trade finance"** (also note: lowercase) | **INCONSISTENT** |
| Reinvest step 1 | "FX and Investment" | "FX and Investment" | -- |

**Navigation Issues:**

| # | Severity | Issue | Details |
|---|---|---|---|
| N1 | HIGH | "FX and Investment" vs. "FX and Treasury" | The Investment Details screens (accessed after placement) show "FX and Treasury" as the active nav item, while all placement flow screens show "FX and Investment". This is either (a) a Figma error, (b) an intentional rename that was not applied consistently, or (c) two different sections with the same product appearing under different nav labels. Any of these is problematic. Users clicking "FX and Investment" to place a DCI and then seeing "FX and Treasury" when viewing details will be disoriented. |
| N2 | HIGH | Confirm OMC screen navigation mismatch | The "confirm-omc.png" screen shows "Trade finance" highlighted in the nav, with different text casing ("Pay and transfer" vs "Pay and Transfer", "FX and treasury" vs "FX and Investment"). This screen also shows "Trade finance" as the active section, suggesting the Multi-Currency Account prerequisite screen was placed under the wrong navigation section, or is from a different version of the nav. |
| N3 | MEDIUM | Nav item casing inconsistency | On the Confirm OMC screen, nav items use sentence case ("Pay and transfer", "FX and treasury", "Trade finance") while all other screens use title case ("Pay and Transfer", "FX and Investment", "Trade Finance"). This indicates the Confirm OMC screen is from a different design version or component library. |
| N4 | LOW | "Tasks and Statuses" button styling varies | The "Tasks and Statuses" button in the top-right header appears with slightly different styling (icon, badge presence) across screens, suggesting it was not componentized consistently. |

### 6.5 Status Badge Styles

| Badge | Background | Text Color | Border | Screens |
|---|---|---|---|---|
| "Awaiting Settlement" | Light amber (#FFF3E0) | Dark amber/orange (#E65100) | Rounded pill, subtle border | Investment Details, Landing |
| "Active" | None/transparent | Green (#2E7D32) | None visible | Landing |
| "Expiring Soon" | None/transparent | Amber (#F57C00) | None visible | Landing |
| "Base Currency" | Green (#2E7D32) | White | Rounded pill | Parameters, Review, Confirmation |
| "Alternate Currency" | Orange-red (#E65100) | White | Rounded pill | Parameters, Review, Confirmation |

**Status Badge Issues:**
- SB1 (MEDIUM): "Active" and "Expiring Soon" on the landing page appear to use text-only styling (no background pill), while "Awaiting Settlement" uses a pill badge. The inconsistency between text-only statuses and pill-badge statuses reduces scannability. All statuses should use a consistent badge pattern.
- SB2 (LOW): There is no visible "Settled" badge in the reviewed screens (the "Settled" tab exists but no settled investment detail screen was provided).

---

## Executive Summary

The OCBC Dual Currency Investment product demonstrates a generally well-structured information architecture with clear step-by-step flow progression. The visual design is clean and professional, appropriate for a corporate banking product. However, the audit reveals **significant accessibility deficits** that must be addressed before production deployment.

**The three most critical issues are:**

1. **Widespread contrast failures (9 patterns)** -- helper text, status badges, table headers, and meta text across virtually every screen fail WCAG AA requirements. For a banking product subject to accessibility regulations, this is the highest-priority fix.

2. **No keyboard/focus interaction design** -- None of the 13 screens specify focus indicators, tab order, or keyboard navigation behavior. This is a critical gap for a corporate banking product where power users rely on keyboard navigation and users with motor disabilities require keyboard access.

3. **Navigation label inconsistency ("FX and Investment" vs. "FX and Treasury")** -- Users navigating between the placement flow and investment details will encounter different navigation labels for what appears to be the same product area, creating disorientation in a high-stakes financial context.

**UX Health Score: 6.0 / 10** -- The visual design foundation is solid, but accessibility compliance gaps and navigation inconsistencies significantly reduce the score. Addressing contrast, keyboard access, and navigation consistency would raise this to 7.5-8.0.

---

*Report generated: 13 March 2026*
*Screens analyzed: 13 Figma exports*
*Audit scope: Visual design, typography, color, contrast, spacing, WCAG 2.2 accessibility, component consistency*
