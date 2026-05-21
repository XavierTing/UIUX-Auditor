# Visual Design Audit -- OCBC Dual Currency Investment (DCI)

**Date:** 2026-03-13
**Screens Reviewed:** 17 screenshots across the DCI product flow
**Scope:** Typography, colour, spacing, component inventory, visual hierarchy, design system consistency

---

## Typography Analysis

### Font Family
- **Primary typeface:** Appears to be a sans-serif font consistent with OCBC's digital design system (likely Open Sans or a custom OCBC webfont). Used universally across all screens.
- **No serif or decorative fonts** observed anywhere in the product flow.

### Typographic Scale (Estimated from screenshots)

| Role | Approx Size | Weight | Usage |
|------|------------|--------|-------|
| Page title / Section heading | ~20-24px | Bold (700) | "DUAL CURRENCY INVESTMENT", "Investment Parameters", "Investment Overview" |
| Sub-section heading | ~16-18px | Semibold (600) | "Potential Outcomes", "Settlement Outcome", "Account Information", "Strike Price" |
| Scenario labels | ~14-16px | Semibold (600) | "SCENARIO A", "SCENARIO B", "Scenario A", "Scenario B" |
| Body text / Field values | ~14px | Regular (400) | Account numbers, dates, amounts, descriptions |
| Field labels | ~12-13px | Regular (400) | "Investment Amount", "Currency Pair", "Transaction Date", grey colour |
| Caption / Helper text | ~11-12px | Regular (400) | "Minimum amount: $0,000.00 USD", helper text below fields |
| Navigation items | ~14px | Regular (400) / Bold on active | "Home", "Accounts", "Pay and Transfer", etc. |
| Button text | ~14px | Semibold (600) | "Submit", "Next", "Back", "Place investment" |

### Typographic Hierarchy Observations

1. **Page title treatment is inconsistent.** The "DUAL CURRENCY INVESTMENT" label uses all-caps letter-spaced styling on the investment parameter screens and reinvest screens, but "Investment Overview" on the detail screens uses title case bold. The "REVIEW" sidebar label also uses all-caps tracking. These are two different titling conventions coexisting.

2. **"FREQUENTLY ASKED QUESTIONS" on the landing page** uses all-caps letter-spaced styling (similar to the page title), establishing a pattern for section-level labelling, but this pattern is not carried through to other screens where sub-section headings use title case.

3. **Scenario labels inconsistency:** On the `day-1-add-delete-users-3.png` (investment parameters with data), scenario labels read "SCENARIO A" and "SCENARIO B" in all-caps. On the empty-state `day-1-add-delete-users.png`, they also use all-caps. This is internally consistent within the Potential Outcomes panel.

4. **Field label hierarchy is clear.** Grey, smaller text for labels above bold/regular black values. This is consistently applied across review, investment details, and account selection screens.

5. **Yield values use colour + weight** to draw attention: the indicative yield percentages (e.g., "6.50% p.a.") appear in red/dark colour and bold on the strike price selection, effectively creating a visual anchor for the most decision-critical data.

### Typography Issues

- **T&C modal (`t-c.png`):** Dense body text in the modal with no clear heading hierarchy within the content. Appears to be a wall of text with minimal visual differentiation between paragraphs. Line spacing appears tight for a legal document.
- **Inconsistent case conventions:** Mix of ALL CAPS letter-spaced headers ("DUAL CURRENCY INVESTMENT", "INVESTMENT DETAILS", "ACCOUNT APPLICATION", "FREQUENTLY ASKED QUESTIONS") and title case headers ("Investment Overview", "Account Information", "Settlement Outcome"). These should follow one convention.
- **The "Indicative yield" label** on strike price radio options is right-aligned in a smaller, lighter weight -- good for scannability but the word "Indicative" may be missed by users scanning only the percentage.

---

## Colour Palette

### Primary Colours

| Colour | Hex (Approx) | Usage |
|--------|-------------|-------|
| OCBC Red | `#E5001A` / `#D0021B` | OCBC logo, header accent bar, top navigation bar background |
| Dark Charcoal / Near-Black | `#1A1A1A` / `#333333` | Primary body text, headings, field values |
| White | `#FFFFFF` | Page background, card backgrounds, modal backgrounds |
| Light Grey (Background) | `#F5F5F5` / `#F8F8F8` | Page background behind content cards, subtle section dividers |

### Secondary / Functional Colours

| Colour | Hex (Approx) | Usage |
|--------|-------------|-------|
| Medium Grey | `#666666` / `#999999` | Field labels, helper text, secondary text |
| Light Grey (Borders) | `#E0E0E0` / `#D9D9D9` | Card borders, dividers, input field borders, table row dividers |
| Blue (Link) | `#0066CC` / `#1A73E8` | "Download Termsheet" link, "Terms and Conditions" link, "Place investment" link, "Show available balance" link, edit icons |
| Dark Teal / Dark Slate | `#2D3E50` / `#384250` | Primary CTA button fill ("Add New Currency" modal), some button variants |

### Status / Semantic Colours

| Colour | Hex (Approx) | Usage |
|--------|-------------|-------|
| Green (Success) | `#00A651` / `#27AE60` | Success checkmark icon (confirmation screen), "Awaiting Settlement" badge background (light green), Scenario A background tint, yield values in settlement breakdown ("+1,083.33 USD") |
| Orange / Amber (Warning) | `#F5A623` / `#FF9800` | "Expiring Soon" status badge, warning triangle icon (strike price not met), "Alternate Currency" badge |
| Red (Primary CTA / Brand) | `#E5001A` / `#CF0A2C` | "Submit" button, "Next" button, "Place investment" button, "Add" buttons on account application, "Base Currency" badge, OCBC brand red |
| Light Green (Scenario A bg) | `#E8F5E9` / `#F0FAF0` | Scenario A card background (strike price met / base currency settlement) |
| Light Orange/Peach (Scenario B bg) | `#FFF3E0` / `#FEF6EE` | Scenario B card background (strike price not met / alternate currency settlement) |

### Colour Usage Observations

1. **Red is overloaded.** OCBC brand red is used simultaneously for: (a) primary CTA buttons (Submit, Next), (b) the "Base Currency" badge in Scenario A, (c) navigation accents. This creates potential confusion -- a "Base Currency" badge in red does not communicate the same intent as a "Submit" button in red. Red typically signals danger/error in banking UIs but here it is the brand primary.

2. **Scenario colour coding is effective.** Green tint for Scenario A (base currency / strike price met = favourable) and orange/peach tint for Scenario B (alternate currency / strike price not met = less favourable from a principal-preservation standpoint) provides intuitive colour semantics. However, this coding is subtle and not explicitly labelled with colour meaning.

3. **Status badges are well-differentiated.** "Awaiting Settlement" uses a green outline/badge, "Expiring Soon" uses an orange/amber badge. These are scannable and distinguishable.

4. **The green yield value (+1,083.33 USD, +485.90 SGD)** in the settlement breakdown effectively signals positive return. Consistent across both strike-price-met and not-met detail screens.

5. **Modal backdrop** uses a semi-transparent grey overlay (`rgba(0,0,0,0.5)` approximately), which is standard and functional.

6. **Dark teal/slate button** on the "Add New Currency" modal is a different button colour from the OCBC red used elsewhere. This introduces a second primary button colour into the system, breaking consistency.

---

## Spacing & Layout

### Page Structure

- **Max content width:** Approximately 900-1000px, centred on the page. Consistent across all DCI screens.
- **Header:** Fixed OCBC header with logo (left), user info (centre-right), language/notifications (right). Height approximately 60-70px.
- **Navigation bar:** Horizontal main nav below header with items: Home, Accounts, Pay and Transfer, FX and Investment, Invoices, Trade Finance, Tools, Administration. Active item indicated by bold text + red underline.
- **Left sidebar label:** "DUAL CURRENCY INVESTMENT" or "INVESTMENT DETAILS" or "REVIEW" appears as a left-aligned label with a short red horizontal rule above it. This acts as a breadcrumb/section identifier.
- **Footer:** Minimal footer with "Conditions of Access | Security & Privacy" (right) and copyright (left or centre).

### Spacing Patterns (Estimated)

| Element | Spacing |
|---------|---------|
| Header to nav bar | ~0px (flush) |
| Nav bar to content | ~24-32px |
| Section heading to content | ~16-20px |
| Between form field groups | ~20-24px |
| Card internal padding | ~20-24px |
| Between cards (Scenario A/B) | ~16-20px |
| Button group (Back/Next) spacing | ~16px between buttons, bottom-aligned |
| Page horizontal padding (left/right margins within content area) | ~40-60px |

### Layout Patterns

1. **Two-column layout on investment parameters screen:** Left column holds form inputs (Investment Amount, Currency pair, Tenor, Strike Price), right column holds the Potential Outcomes panel. Approximately 55/45 or 60/40 split. This is a strong pattern for showing input-output relationships.

2. **Single-column layout on review and detail screens:** Full-width content within the centred container. Two-column grid within sections for label-value pairs (e.g., "Currency Pair" on left, "Investment Amount" on right).

3. **Investment Timeline** uses a vertical stepper/timeline component with circular markers connected by a vertical line. Consistent across review, confirmation, and parameter screens.

4. **Button placement:** "Back" button is always bottom-left (outlined/ghost style), "Next"/"Submit" is always bottom-right (filled red). This left-right pattern for secondary/primary actions is consistent and follows convention.

5. **The landing page (`renew-landing-uploaded-file.png`)** uses a hero banner with dark background, value proposition cards below, filter bar, empty-state illustration, and FAQ accordion -- a well-structured landing page layout.

### Spacing Issues

- **The confirmation screen (collapsed view, `overseas-confirmation-maker-collapsed.png`)** appears cramped with the success icon, reference number, and timeline all compressed into a narrow vertical layout. Compared to the expanded confirmation view, the collapsed one feels rushed.
- **Review screen (`review.png`)** is very long vertically. The submit button is far below the fold, requiring significant scrolling. No sticky summary or floating CTA is present.
- **Account Application screen (`sao-landing-only-1-account.png`)** mixes multiple patterns: card selection at top, form fields in middle, radio buttons, checkboxes -- the vertical spacing between these different form sections is somewhat inconsistent (tighter between some groups than others).

---

## Component Inventory & Consistency

### Buttons

| Variant | Visual Style | Screens Used |
|---------|-------------|--------------|
| Primary CTA (Red filled) | Red background (`#E5001A`), white text, rounded corners (~4-6px), medium padding | Review (Submit), Parameters (Next), Landing (Place investment), Reinvest (Next) |
| Secondary (Outlined/Ghost) | White background, dark border, dark text, rounded corners | Review (Back), Parameters (Back), Reinvest (Back), Investment Details (Back, Reinvest) |
| Primary CTA (Dark teal filled) | Dark teal/slate background, white text, rounded corners | Modal (Add New Currency) |
| Text link button | Blue text, no border, sometimes with icon | Landing (Place investment link), Details (Download Termsheet) |
| Add button (Red filled, smaller) | Red background, white text, full-width within card | Account Application (Add) |

**Issue:** Two different filled-button colours (OCBC red and dark teal) are used for primary actions. The "Add New Currency" modal uses dark teal while all other CTAs use red. This should be unified.

### Form Inputs

| Component | Style | Notes |
|-----------|-------|-------|
| Text input | Bottom-border only (underline style), label above | Investment Amount field |
| Dropdown / Select | Bottom-border + chevron icon, label above | Currency pair, Tenor, Account selection |
| Currency selector (composite) | Input field with embedded currency dropdown (flag + code + chevron) on right side | Investment Amount field -- unique composite component |
| Radio buttons | Standard circular radio with label, description text below | Strike Price selection, Yes/No entity changes |
| Checkboxes | Standard square checkbox with label text | Account application reasons |
| Search input within dropdown | Standard input with search icon, inside dropdown panel | Currency selector dropdown |

**Observation:** The currency selector within the Investment Amount field is a well-designed composite component. It combines the amount input with an inline currency dropdown, showing flag icons + currency codes. The dropdown panel includes a search field and lists currencies with flags -- this is a polished, reusable component.

### Cards & Containers

| Component | Usage |
|-----------|-------|
| Scenario card (coloured background) | Potential Outcomes panel: green-tinted for Scenario A, orange-tinted for Scenario B |
| Account type card | Account Application: three side-by-side cards with bullet-point features and "Add" CTA |
| Settlement breakdown table | Investment Details: dark header row with white body rows, right-aligned amounts |
| Information section container | Light grey or white container with subtle border, used for Investment Overview, Account Information |
| Hero banner | Landing page: dark background with white text, CTA button right-aligned |
| Value proposition cards | Landing page: two side-by-side cards with icon, heading, description |
| FAQ accordion | Landing page: question rows with "Show" toggle |
| Empty state | Landing page: illustration with message and CTA link |

### Navigation & Structural Components

| Component | Description |
|-----------|-------------|
| Main header bar | OCBC logo + user info + language + notifications + icons |
| Primary navigation | Horizontal tab bar with text items, active state = bold + red underline |
| Section sidebar label | Left-aligned all-caps label with short red rule above (e.g., "INVESTMENT DETAILS") |
| Investment Timeline (stepper) | Vertical timeline with circular dot markers, connecting line, date labels |
| Status badge | Rounded pill badge: "Awaiting Settlement" (green outline), "Expiring Soon" (orange), "Base Currency" (red/green), "Alternate Currency" (orange) |
| Modal / Dialog | Centred overlay with white card, title, body text, Cancel + Primary action buttons |
| Breadcrumb / Progress indicator | The left sidebar label serves as a pseudo-breadcrumb but lacks true breadcrumb functionality (no clickable path) |

### Filter Components (Landing Page)

| Component | Description |
|-----------|-------------|
| Filter bar | Horizontal row of dropdown filters: "All Currencies", "Status", "Tenor" + Search input |
| Filter dropdown | Standard dropdown with chevron, grey border |
| Search field | Text input with search icon |

---

## Visual Hierarchy Assessment (Per Key Screen)

### Investment Parameters (day-1-add-delete-users-3.png)

**Eye flow:** Page title ("DUAL CURRENCY INVESTMENT") -> "Investment Parameters" heading -> Investment Amount input (large, prominent) -> Currency pair -> Strike Price radio group (right-aligned yields in red draw attention) -> Potential Outcomes panel (right column, colour-coded scenarios).

**Assessment:** The two-column layout effectively creates a cause-and-effect relationship between inputs (left) and outcomes (right). The strike price radio options with right-aligned yield percentages are the most decision-critical element and receive appropriate visual weight through bold text and positioning. The Potential Outcomes panel uses colour coding (green/orange badges, tinted backgrounds) to differentiate scenarios. **Well-structured for decision-making.**

**Issue:** The Investment Timeline at the bottom competes less for attention, which is appropriate, but it is separated from the outcomes by significant vertical distance. The timeline and the outcomes panel are both important for understanding the investment, yet they are in different visual zones.

### Review Screen (review.png)

**Eye flow:** "REVIEW" sidebar label -> "Investment details" heading + Edit link -> Key financial figures (Investment Amount, Currency Pair, Yield) -> Accounts section -> Potential Outcomes scenarios -> Investment Timeline -> T&C disclaimer -> Submit/Back buttons.

**Assessment:** This is a dense, long-scrolling page. The most critical information (amount, pair, yield) is at the top, which is correct. The Scenario cards with coloured backgrounds (green for A, orange for B) break up the page and draw attention to the outcome projections. The "Edit" pencil icons next to section headings provide clear editing affordance.

**Issues:**
- The page requires significant scrolling to reach the Submit button. No floating/sticky CTA is provided.
- The T&C disclaimer text just above the Submit button is small and easily skippable -- this is a regulatory risk.
- The visual hierarchy between "Investment details" and "Accounts" sections is weak; they use the same heading weight and there is minimal visual separation.

### Investment Details - Awaiting Settlement, Strike Price Met (investment-details-awaiting-settlement-strike-price-met.png)

**Eye flow:** "INVESTMENT DETAILS" label -> "Investment Overview" heading + "Awaiting Settlement" green badge -> Key financials (Ref No, Currency Pair, Amount, Yield) -> Account Information -> Settlement Outcome (green success banner) -> Settlement Breakdown table -> Reinvest button.

**Assessment:** The green "Awaiting Settlement" badge immediately communicates status. The Settlement Outcome section with the green check icon and explanatory text is the focal point of the lower half. The settlement breakdown table clearly presents Principal, Yield (green text), and Total Settlement. The "Reinvest" button is positioned at the bottom-right of the table, which is contextually appropriate.

**Issue:** The "Download Termsheet" link (top-right, blue text) has low visual prominence relative to its importance for compliance/record-keeping.

### Investment Details - Strike Price Not Met (investment-details-awaiting-settlement-strike-price-not-met.png)

**Eye flow:** Same as above, but the Settlement Outcome section uses an amber/orange warning triangle icon instead of a green check. The explanatory text describes alternate currency settlement.

**Assessment:** The orange icon and text effectively communicate a different outcome without being alarming. The settlement breakdown still shows positive yield (green "+485.90 SGD"), which is reassuring. The differentiation between "met" and "not met" states is handled well through icon and colour changes while maintaining the same layout structure.

### Confirmation - Expanded (overseas-confirmation-maker-expanded.png)

**Eye flow:** Large green checkmark circle icon -> "Investment Placed Successfully!" heading -> Reference number -> Investment Timeline -> Investment Details summary -> Accounts -> Potential Outcomes -> "Place Another Investment" CTA.

**Assessment:** The success state is immediately clear from the large green checkmark. The expanded view provides a comprehensive summary that mirrors the review screen structure. The "Place Another Investment" button uses dark/filled style.

**Issue:** The expanded confirmation contains a very large amount of information. Users at this point primarily need reassurance + reference number + next steps. The full investment recap, while thorough, may be information overload for a confirmation screen.

### Confirmation - Collapsed (overseas-confirmation-maker-collapsed.png)

**Eye flow:** Green checkmark -> "Investment Placed Successfully!" -> Reference number -> Timeline dates -> "Place Another Investment" button.

**Assessment:** This is the more appropriate confirmation pattern -- focused on confirmation + key dates + next action. Much more scannable than the expanded version.

### Landing Page (renew-landing-uploaded-file.png)

**Eye flow:** Navigation (FX and Investment active) -> "DUAL CURRENCY INVESTMENT" title -> Hero banner ("Ready to invest?" + CTA) -> Value proposition cards -> Filter bar -> Empty state illustration -> FAQ accordion.

**Assessment:** Well-structured landing page with clear visual hierarchy. The dark hero banner creates strong contrast and draws attention to the primary CTA. The value proposition cards provide quick-scan benefits. The empty state with illustration and CTA link guides users to take action.

**Issue:** When there are no investments to display, the page has a large empty zone between the filter bar and the FAQ section. The empty state illustration is helpful but the gap feels hollow on a desktop screen.

### T&C Modal (t-c.png)

**Eye flow:** Title ("Dual Currency Investment") -> Wall of body text -> Cancel/Agree buttons at bottom.

**Assessment:** The modal presents legal text with minimal formatting. There is no internal heading structure visible, making it difficult to scan for specific terms. The "Agree" button is the primary CTA (filled style).

**Issue:** Legal content in a modal is a common banking pattern, but the lack of internal headings, bullet points, or visual structure within the legal text makes it nearly impossible to read meaningfully. Users will simply scroll and click "Agree."

### Multi-Currency Account Required (confirm-omc.png)

**Eye flow:** Illustration (person with question mark) -> Heading text ("Multi-Currency Account Required for Dual Currency Investment") -> Explanatory paragraph -> "Open Multi-Currency Account" CTA button.

**Assessment:** Clean blocking state with clear explanation and single CTA. The illustration adds visual interest. The CTA is prominent (red filled button, full-width or near-full-width).

### Account Application (sao-landing-only-1-account.png)

**Eye flow:** "ACCOUNT APPLICATION" sidebar label -> Question heading -> Three account type cards (side-by-side, equal visual weight) -> Entity details section -> Change confirmation (radio buttons) -> Reasons for opening (checkboxes) -> Back/Next buttons.

**Assessment:** The three account type cards are well-structured with consistent formatting (title, subtitle, bullet points, CTA). The form below follows a logical progression.

**Issue:** The "Add" button on each account card is red (primary CTA colour), but adding an account is an intermediate step, not the final action. Having three identically-weighted red buttons competing for attention reduces the effectiveness of each.

---

## Design System Observations

### Consistent Patterns (Well-Established)

1. **Button pairing convention:** Back (outlined, left) + Primary (filled red, right) is applied consistently across all multi-step flows. This is a well-established pattern.

2. **Label-value pair layout:** Grey label above, bold/regular black value below. Used consistently across review, detail, and parameter screens. Two-column grid for paired data points.

3. **Investment Timeline stepper:** Consistent vertical timeline component with dot markers, date labels, and connecting lines. Used identically on parameter, review, and confirmation screens.

4. **Status badge system:** Pill-shaped badges with appropriate semantic colours (green = active/settled, orange = expiring/warning). Consistent shape and size.

5. **Scenario A/B colour coding:** Green tint for base currency scenario, orange tint for alternate currency scenario. Consistent across parameters, review, and confirmation screens.

6. **Page section identifier:** All-caps letter-spaced label with red rule above, left-aligned. Used for "DUAL CURRENCY INVESTMENT", "INVESTMENT DETAILS", "REVIEW", "ACCOUNT APPLICATION".

### Inconsistencies & Rogue Patterns

1. **Button colour inconsistency:** Primary CTAs are OCBC red across most screens, but the "Add New Currency" modal uses a dark teal/slate button. Two primary button colours exist in the system.

2. **Navigation label inconsistency:** The main nav item for the DCI section appears as "FX and Investment" on some screens and "FX and Treasury" on the investment detail screens. This is either a design inconsistency or reflects different sub-products, but from the user's perspective navigating within the same flow, it creates confusion.

3. **Header user info layout:** The header displays "Patrick Tan" + company name + last login across screens, but the exact layout (spacing, alignment) appears to shift slightly between screens.

4. **Case conventions for headings:** Mix of ALL CAPS tracking (page-level identifiers) and title case (section headings within pages). While there may be intentional hierarchy, the distinction is not documented or immediately obvious.

5. **Scenario badge styles vary:** "Base Currency" badge appears in red on some screens (matching OCBC brand red) and green on others. "Alternate Currency" badge appears in orange consistently. The red "Base Currency" badge is confusing because red typically signals caution in banking.

6. **The "confirm-omc" screen** has a slightly different header layout and navigation styling (the "Trade Finance" item appears active/underlined in red rather than "FX and Investment"), suggesting this screen may come from a different product or an older design iteration.

7. **Dropdown component:** The currency selector dropdown (`dropdowns.png`) uses a bottom-border-only input style with a dropdown panel that has a search field. The border turns blue when active/open. Other dropdowns (Tenor, Account selection) use a similar style but the bottom-border color treatment may differ (grey vs blue active state).

---

## Key Visual Issues Found

### Issue 1: Red Overload -- Brand Colour vs Semantic Meaning
- **Severity:** HIGH
- **Description:** OCBC brand red is used for primary CTA buttons, "Base Currency" scenario badges, navigation accents, and the "Add" buttons on account type cards. In a banking/investment context where red universally signals danger, error, or loss, using red as the primary action colour creates a subconscious tension. The "Base Currency" badge in red is particularly confusing -- it marks the favourable outcome (strike price met, return in base currency) but uses a colour that implies caution.
- **Impact (Novice):** May hesitate before clicking red buttons, especially on a financial submission. Red "Base Currency" badge may be misread as a warning.
- **Impact (Seasoned):** Less likely to be confused by button colour but may still find the "Base Currency" red badge semantically incorrect.

### Issue 2: Navigation Label Mismatch ("FX and Investment" vs "FX and Treasury")
- **Severity:** MEDIUM
- **Description:** The primary navigation label changes between "FX and Investment" (landing, parameters, reinvest, confirmation screens) and "FX and Treasury" (investment detail screens). This inconsistency may cause users to question whether they are still in the same product area.
- **Impact (Novice):** May think they have navigated to a different section, increasing disorientation.
- **Impact (Seasoned):** May recognise both terms but the inconsistency still erodes trust in the product's polish.

### Issue 3: Review Screen Length Without Sticky CTA
- **Severity:** MEDIUM
- **Description:** The review screen requires scrolling through Investment Details, Accounts, Potential Outcomes (two scenario cards), Investment Timeline, and T&C disclaimer before reaching the Submit button. No sticky/floating CTA or summary bar is provided.
- **Impact (Novice):** May not realise they need to scroll further to find the Submit button. The long page may feel overwhelming.
- **Impact (Seasoned):** May find the scrolling tedious for repeat investments.

### Issue 4: T&C Modal Lacks Internal Structure
- **Severity:** MEDIUM
- **Description:** The Terms and Conditions modal presents legal text as an undifferentiated wall of text with no visible headings, bullet points, or section breaks within the content. Users cannot scan for relevant sections.
- **Impact (Both):** Users will not read the T&C, which is common, but the lack of structure removes even the possibility of scanning. For a financial product, this is a missed opportunity to communicate key risk disclosures within the T&C.

### Issue 5: Two Primary Button Colour Systems
- **Severity:** LOW
- **Description:** The "Add New Currency" modal uses a dark teal/slate primary button, while all other screens use OCBC red. This introduces a second primary button colour into the design system.
- **Impact (Both):** Minor but creates a perception of design inconsistency. May confuse users about which colour represents the primary action.

### Issue 6: Confirmation Screen Information Overload (Expanded View)
- **Severity:** LOW
- **Description:** The expanded confirmation screen repeats nearly all information from the review screen (investment details, accounts, potential outcomes). For a confirmation/success state, this is excessive. Users at this stage need reassurance, a reference number, and next steps -- not a full recap.
- **Impact (Novice):** May re-read all information looking for something they missed, increasing cognitive load at a moment that should be relief.
- **Impact (Seasoned):** Will skip the detail, making the expanded view wasted screen real estate.

### Issue 7: Scenario A/B Outcome Panel -- No Default Selection Feedback
- **Severity:** LOW
- **Description:** On the reinvest step 1 screen, the Potential Outcomes panel shows Scenario A and B with dashes ("--") for all values before a strike price is selected. While the structure is present, the empty state provides no guidance about what will populate these fields.
- **Impact (Novice):** May not understand what "Scenario A" and "Scenario B" mean or why they are empty, especially before selecting a strike price.

### Issue 8: Landing Page Empty State Vertical Gap
- **Severity:** LOW
- **Description:** When no active investments exist, the landing page has a significant vertical gap between the filter bar and the FAQ accordion section. The empty state illustration helps but the page feels hollow on desktop viewports.
- **Impact (Both):** Primarily aesthetic. The page does not feel "wrong" but it lacks the density that banking users expect from a dashboard.

---

## Summary of Component Count

| Component Type | Count of Distinct Variants |
|---------------|--------------------------|
| Button styles | 4 (red filled, outlined/ghost, dark teal filled, text link) |
| Input types | 4 (text underline, dropdown underline, composite currency input, search) |
| Card types | 4 (scenario outcome, account type, settlement breakdown, value proposition) |
| Badge/Tag types | 4 (Awaiting Settlement, Expiring Soon, Base Currency, Alternate Currency) |
| Modal types | 2 (T&C scrollable content, action confirmation) |
| Navigation components | 3 (main header, primary nav bar, section sidebar label) |
| Timeline/Stepper | 1 (vertical investment timeline) |
| Illustration types | 2 (empty state, blocking state/OMC required) |
| Form control types | 3 (radio button, checkbox, dropdown/select) |
| Filter components | 2 (filter dropdown, search input) |
| Accordion | 1 (FAQ section) |
