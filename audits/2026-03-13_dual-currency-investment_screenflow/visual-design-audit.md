# OCBC Dual Currency Investment (DCI) -- Visual & Design Audit

**Audit Date:** 2026-03-13
**Platform:** Web Desktop (1280px+)
**Auditor:** Senior UX Auditor (AI-Assisted)
**Scope:** Full DCI product flow -- placement, review, confirmation, landing/portfolio, investment details, reinvestment, T&C modal, multi-currency account gate
**Personas:** Novice corporate investor / Seasoned corporate investor
**Dimensions Covered:** 1-7, 9-10 (Accessibility/WCAG excluded per brief)
**Exclusions:** WCAG/accessibility analysis; lorem ipsum placeholder content in T&C modal

---

## Executive Summary

The OCBC DCI product delivers a functional end-to-end investment placement flow with a clean visual foundation and sensible two-column parameter/outcome layout. However, it suffers from several high-severity issues that compromise both novice comprehension and seasoned-user efficiency. Most critically, **risk disclosure is structurally subordinated to yield presentation**, the concept of "strike price" is never defined in plain language, and the dual-scenario outcome panel does not make it obvious which scenario represents a loss of principal currency. Navigation inconsistencies (label mismatches between screens, absence of step indicators, no breadcrumbs) erode wayfinding confidence. The design system has notable fragmentation: three distinct nav bar configurations, inconsistent status badge colors, and button hierarchy that shifts between screens. The landing/portfolio screen packs substantial information density but lacks visual hierarchy to separate investments requiring action from those that do not.

**Overall UX Health Score: 5.5 / 10** -- Structurally sound but with critical gaps in risk communication, navigation consistency, and information hierarchy that create real business and compliance exposure.

---

## Section 1: Visual & Layout Analysis

### 1.1 Typography

| Observation | Screens Affected | Severity |
|---|---|---|
| Page title treatment inconsistent: "DUAL CURRENCY INVESTMENT" uses all-caps spaced small-caps on parameter/landing screens, but "INVESTMENT DETAILS" uses the same style on detail screens while "REVIEW" uses a different weight/size treatment with a horizontal rule | Parameter, Review, Details | Medium |
| Strike price radio rows use small secondary text (~11px) for "from spot" percentages, making the risk/reward trade-off comparison difficult to scan at desktop distance | Investment Parameters (configured) | Medium |
| Potential Outcomes panel uses identical font weight for both scenario labels and monetary values, reducing scanability of the most important numbers (settlement amounts) | Investment Parameters, Review | Medium |
| The landing table compresses 7+ columns into a dense layout where text sizes drop below comfortable reading thresholds; the "Transaction Date / Value Date / Maturity Date" multi-line cells are especially hard to parse | Landing with investments | High |
| Yield values on strike price selector ("6.70%", "6.60%") right-aligned with "Indicative yield" sub-label are well-formatted but the "p.a." annotation is inconsistently sized vs. the review/details screens | Parameters vs. Review | Low |
| Investment Timeline uses adequate typographic hierarchy (bold date labels, regular descriptions, bold date values) -- this is well done | Parameters, Review, Confirmation | -- (positive) |

### 1.2 Color Semantics

| Observation | Screens Affected | Severity |
|---|---|---|
| **Green is overloaded with 5+ distinct meanings:** (1) success checkmark on confirmation, (2) "Base Currency" badge, (3) "Strike Price Met" outcome banner, (4) yield amount in settlement breakdown (+1,083.33), (5) "Active" status on landing table, (6) the OCBC brand logo. This creates ambiguity -- does green mean "good for you" or just "base currency"? Strike Price Met settlement in base currency green implies a favorable outcome, while Strike Price Not Met in amber/orange implies unfavorable, but in reality both scenarios produce yield | All screens | High |
| **"Alternate Currency" badge uses red/coral**, which carries a strong negative semantic in financial contexts. For a novice user, the red badge on Scenario B subconsciously signals "bad outcome" or "danger," when it should be a neutral alternate path. This biases perception and may not satisfy balanced disclosure requirements | Parameters, Review | High |
| "Expiring Soon" badge uses orange/amber which is appropriate for urgency. "Awaiting Settlement" uses green outline which is appropriate. "Settled" uses grey which is neutral. This status badge system is internally consistent | Details screens | -- (positive) |
| The "Strike Price Not Met" outcome banner uses an amber/warning triangle icon, reinforcing the false impression that alternate-currency settlement is inherently negative. In reality, the user receives principal + yield in the alternate currency, which may be their desired conversion outcome | Details (strike not met) | High |
| Link colors appear in teal/green ("Show available balance", "Place investment" on empty state, "Download Termsheet") -- reasonably consistent | Multiple | Low |

### 1.3 Spacing & Layout

| Observation | Screens Affected | Severity |
|---|---|---|
| The two-column layout (parameters left, outcomes right) on the Investment Parameters screen shifts to a single-column stacked layout on the Review screen. The Potential Outcomes cards on Review are full-width with a different visual treatment (light green/light amber background fills). This layout shift between steps may confuse users who built a mental model of left=input, right=output | Parameters vs. Review | Medium |
| Button bar spacing varies: Parameters screen has "Back" (outlined, left) and "Next" (filled red, right) with wide separation. Review screen has the same pattern with "Submit" instead of "Next". Confirmation has only "Place Another Investment" (filled red, centered). The inconsistent button positioning across steps weakens predictability | Parameters, Review, Confirmation | Medium |
| The landing page with active investments has a dense KPI summary bar (Active Investments, Expiring Soon, Total Invested Amount, Avg. Yield) immediately followed by tabs and filters, then the table. The vertical spacing between these sections is tight, making the visual hierarchy feel compressed | Landing (with investments) | Medium |
| Investment Details screens maintain consistent two-column field layout for the overview section, settlement breakdown is well-structured as a table. Good visual separation between overview, accounts, and settlement outcome sections | Details screens | -- (positive) |

### 1.4 Component Consistency

| Observation | Screens Affected | Severity |
|---|---|---|
| **Three different nav bar label configurations observed:** "FX and Investment" (parameters, landing, review, reinvest), "FX and Treasury" (investment details -- both settled and awaiting settlement), and "FX and treasury" / "Trade finance" (confirm-omc screen with different casing). This is a clear design system fragmentation | All screens | High |
| The currency dropdown on the investment amount field shows "NIL" as the default unselected state in the empty parameters screen and "N.A" in the dropdown component detail view -- two different labels for the same empty state | Parameters (empty), Dropdowns | Low |
| Status badges across screens: "Awaiting Settlement" (green outline), "Expiring Soon" (orange filled), "Settled" (grey filled) use different visual treatments (outline vs. filled). While the color coding is semantically reasonable, the inconsistent fill/outline treatment suggests these are not from a unified badge component | Details screens, Landing | Medium |
| The "Reinvest" button appears as a small outlined button in the settlement breakdown table on details screens, but the primary CTA on the landing page is "Place Investment" (filled red). The reinvest action -- arguably the highest-value conversion action post-maturity -- is visually demoted | Details vs. Landing | Medium |

---

## Section 2: Navigation & Information Architecture Assessment

### 2.1 Wayfinding

| # | Finding | Severity | Novice Impact | Seasoned Impact |
|---|---|---|---|---|
| N1 | **No step indicator or progress bar across the placement flow.** The user moves through Parameters -> (Account Selection) -> Review -> Confirmation with no visual indication of where they are in the process or how many steps remain. The only orientation cue is the page title changing. | High | Novice has no mental model of the journey length. "How many more screens until I commit?" is unanswered, increasing anxiety for a high-stakes financial action. | Seasoned user can infer the flow but still cannot confirm they are on the penultimate step before submission. |
| N2 | **No breadcrumbs.** From any Investment Details screen, the only navigation option is "Back" (which goes to the landing list). There is no breadcrumb trail showing Landing > Investment Details > [Reference Number]. | Medium | Novice may feel lost in the details view with no orientation to the overall product structure. | Seasoned user relies on browser back button anyway, so impact is lower. |
| N3 | **"FX and Investment" vs. "FX and Treasury" nav label mismatch.** The active nav item changes label between screens within the same product flow. This is disorienting -- the user may question whether they have navigated to a different section of the platform. | High | Novice may believe they accidentally left the DCI section and hesitate to proceed. | Seasoned user will notice the inconsistency and flag it as unprofessional but will not be blocked. |
| N4 | **Confirmation screen (collapsed) lacks clear next actions beyond "Place Another Investment."** After successful placement, the user's most likely next action is to return to the portfolio/landing to see their new investment. There is no "View My Investments" or "Go to Portfolio" link. The only CTA is to place another investment, which serves the bank's conversion goal but not the user's monitoring need. | Medium | Novice wants reassurance that their investment is now visible and trackable. Without a link to the portfolio, they must manually navigate via the top nav. | Seasoned user placing multiple investments benefits from "Place Another," but a portfolio link would still be useful. |
| N5 | **Landing page tabs "Active Investments" and "Settled" provide adequate top-level segmentation**, but within Active Investments, there is no sub-filtering by urgency. Investments requiring action (Expiring Soon, Strike Price Met/Not Met notifications) are mixed in with stable Active ones. | Medium | Novice may miss that an investment requires a reinvestment decision because it is visually buried in the table. | Seasoned user with many investments has to visually scan the full table for action-required items. |

---

## Section 3: DCI-Specific Focus Area Evaluation

### 3.1 Risk Disclosure

**Rating: CRITICAL concern**

- **Upside given disproportionate prominence over downside.** The Potential Outcomes panel on the parameters screen shows two scenarios, but the visual treatment creates an implicit hierarchy: Scenario A (Base Currency, green badge) appears first and is visually "positive," while Scenario B (Alternate Currency, red badge) appears second and is visually "negative." In reality, DCI risk is that the user may receive their principal back in a different currency at an unfavorable rate. This risk is never stated in plain language on the parameters or review screens.
- **No explicit risk warning before the Submit button.** The review screen shows a T&C agreement line but no standalone risk disclosure statement such as "You may receive your investment amount in [alternate currency] if the strike price is not met. This means your principal may be worth less in your base currency."
- **The "Strike Price Met / Not Met" language on post-settlement screens is the closest the product comes to explaining outcomes**, but this is after the fact. The pre-commitment screens rely entirely on the user understanding scenarios A and B without any narrative explanation.

| Severity | Novice Impact | Seasoned Impact |
|---|---|---|
| CRITICAL | Novice may not understand they could lose money in base-currency terms. The green/red color coding may falsely reassure them that Scenario A is the "normal" outcome. | Seasoned user understands the mechanics but may flag the lack of explicit risk language as a regulatory concern. |

### 3.2 Strike Rate Comprehension

**Rating: HIGH concern**

- **"Strike Price" is never defined anywhere in the visible flow.** The parameters screen presents a radio-button list of strike prices (e.g., 1.2830, 1.2840, 1.2850) with "from spot" percentages and "Indicative yield" values. A novice user has no way to understand what a strike price is, what "from spot" means, or why choosing a higher strike price reduces yield.
- **The relationship between strike price and risk is implicit**, embedded in the yield gradient (higher strike = lower yield), but never explained. A single sentence such as "The strike price determines the exchange rate at which your investment may convert to [alternate currency]. A rate closer to spot has higher conversion probability but offers higher yield." would dramatically improve comprehension.
- **The "from spot" percentage labels are helpful for seasoned users** but opaque for novices. "+0.23% from spot" means nothing without understanding what "spot" is.

| Severity | Novice Impact | Seasoned Impact |
|---|---|---|
| HIGH | Novice cannot make an informed strike price selection. They are essentially choosing blindly between yield levels without understanding the risk trade-off. | Seasoned user finds the strike price selector efficient and well-structured with the yield/spot trade-off visible at a glance. |

### 3.3 Currency Pair Clarity

**Rating: MEDIUM concern**

- **Base and Alternate currency labels are clearly presented** in the currency pair selector with flag icons, and the Potential Outcomes panel maps Scenario A to Base Currency and Scenario B to Alternate Currency. This is structurally sound.
- **However, the terms "Base Currency" and "Alternate Currency" are financial jargon.** A novice may not know which is which. The parameters screen does label them, and the selected flags help, but the outcome scenarios would benefit from using the actual currency names (e.g., "Settled in USD" / "Settled in SGD") rather than abstract labels.
- **The current spot rate is displayed** ("1 USD = 1.2800 SGD") which provides good context for evaluating strike prices.

| Severity | Novice Impact | Seasoned Impact |
|---|---|---|
| MEDIUM | Novice must mentally map "Base" and "Alternate" to actual currencies across two panels. Using currency names directly would reduce cognitive load. | Seasoned user has no issue with this terminology. |

### 3.4 Tenor/Maturity

**Rating: LOW concern (well handled)**

- **Tenor selection is a simple dropdown** (1 Week, 1 Month visible in screenshots), which is appropriate for the small number of options.
- **The Investment Timeline section explicitly maps tenor to actual dates** (Transaction Date, Value Date, Expiry Date, Maturity Date) with clear descriptions of what each date means. This is one of the best-designed elements in the flow.
- **Minor gap:** The tenor-yield relationship is not shown at the tenor selection step. The user must select a tenor, then observe how strike prices and yields change. A tenor comparison view (e.g., "1 Week: up to 6.50% p.a. / 1 Month: up to 7.70% p.a.") would help, but this is a nice-to-have.

| Severity | Novice Impact | Seasoned Impact |
|---|---|---|
| LOW | Timeline section is genuinely helpful for novice understanding of the investment lifecycle. | Seasoned user appreciates the date specificity but might want tenor comparison. |

### 3.5 Yield Presentation

**Rating: HIGH concern**

- **Yield is prominently displayed as "Indicative yield" next to each strike price** and as "Indicative Annual Yield" in the review/details screens. The "p.a." annotation is present, confirming annualization.
- **However, the actual dollar return is only shown in the Potential Outcomes panel**, not alongside the strike price selector. When choosing between strike prices, the user sees "6.70% p.a." but not "your actual return would be approximately $X over 1 month." For a 1-month tenor, 6.50% p.a. translates to roughly 0.54% actual return -- a significant perceptual difference that could mislead novice users.
- **Yield is given GREATER prominence than risk.** The strike price selector is essentially a yield picker -- the right column of bold red percentages draws the eye. The risk dimension (how far from spot, probability of conversion) is in smaller grey text on the left. This visual weighting inverts the appropriate hierarchy for a risk-bearing product.

| Severity | Novice Impact | Seasoned Impact |
|---|---|---|
| HIGH | Novice sees large yield numbers and may overestimate returns, not realizing 6.50% p.a. on a 1-month product is ~0.54% actual. The prominent red yield figures attract attention away from risk parameters. | Seasoned user understands annualization but may still appreciate actual-return figures for quick mental math. |

### 3.6 Regulatory Compliance Signals

**Rating: HIGH concern**

- **No suitability disclaimer visible** in the flow. For a structured product with principal risk, regulatory best practice (and MAS requirements for complex investment products) typically requires a suitability assessment or at minimum a disclaimer that the product may not be suitable for all investors.
- **Risk acknowledgment is bundled into the T&C agreement** on the review screen, not presented as a separate, prominent step. The single line "By clicking 'Submit', you confirm that you have read, understood and agree to the Terms and Conditions" does not specifically mention investment risk.
- **No cooling-off or cancellation information** is provided at any point.
- **The FAQ section on the landing page includes "What are the risks involved in investing in Dual Currency Investment (DCI)?"** which is helpful but is collapsed by default and positioned below the fold on the active investments view. Risk education should be surfaced proactively during the placement flow, not tucked into an FAQ.

| Severity | Novice Impact | Seasoned Impact |
|---|---|---|
| HIGH | Novice may commit to a product without understanding they are taking on FX risk. The lack of a prominent risk acknowledgment step creates both user-harm and regulatory exposure. | Seasoned user expects and would not be bothered by an additional risk acknowledgment step. |

---

## Section 4: Per-Screen Findings

### Screen: Investment Parameters -- Empty State
**File:** `day-1-add-delete-users.png`

| # | Dimension | Severity | Finding | Recommendation | Novice Impact | Seasoned Impact |
|---|---|---|---|---|---|---|
| 1 | Forms & Data Entry | Medium | The empty state shows "0.00" as the default investment amount with "NIL" as the currency. The minimum amount helper text reads "$0,000.00 USD" which appears to be a formatting template rather than an actual minimum. If the true minimum is e.g., $50,000, it should state that clearly. | Display the actual minimum amount with correct formatting (e.g., "Minimum amount: 50,000.00 USD"). Remove the "NIL" default and use a proper placeholder like "Select currency." | Novice needs to know the minimum investment upfront to decide whether to proceed. Ambiguous minimums waste time. | Seasoned user wants to know minimums immediately to size their investment. |
| 2 | Cognitive Load | Medium | The Potential Outcomes panel shows empty Scenario A and B with dashes. While structurally correct as a placeholder, it provides no explanatory text about what these scenarios represent. A novice seeing this for the first time has no context for why there are two scenarios. | Add a brief explanatory sentence: "DCI has two possible outcomes depending on the exchange rate at expiry. Configure your investment to see projected returns for each scenario." | Novice is confused by the dual-scenario structure with no explanation. | Seasoned user understands and ignores the empty state. |

### Screen: Investment Parameters -- Configured
**File:** `day-1-add-delete-users-3.png`

| # | Dimension | Severity | Finding | Recommendation | Novice Impact | Seasoned Impact |
|---|---|---|---|---|---|---|
| 3 | Trust & Emotional Design | CRITICAL | The Potential Outcomes panel uses color-coded badges -- green for "Base Currency" (Scenario A) and red/coral for "Alternate Currency" (Scenario B) -- that create an implicit value judgment. In financial product design, color should not bias the user toward one outcome. Both scenarios produce a positive yield; the difference is the settlement currency. | Use neutral colors for both scenario badges (e.g., both in navy/dark grey, or use the currency flag colors). Reserve green/red exclusively for gain/loss indicators in the settlement breakdown. | Novice unconsciously interprets green as "good outcome" and red as "bad outcome," potentially misunderstanding the product's risk profile. This is a disclosure fairness issue. | Seasoned user is not misled but may note the design as potentially non-compliant with fair disclosure principles. |
| 4 | Cognitive Load | HIGH | Strike price selection presents 5 options with yield and from-spot percentage but no plain-language explanation of what strike price means or how it affects their investment outcome. The term "strike price" is derivatives jargon unfamiliar to most corporate treasury staff who are not derivatives specialists. | Add a contextual tooltip or inline explainer: "Strike price is the exchange rate that determines your settlement currency. If the spot rate is above/below this rate at expiry, you receive your investment in [base/alternate] currency." Show a simple visual: "Spot now: 1.2800 | Your strike: 1.2850 | If rate goes above 1.2850, you get USD. Below, you get SGD." | Novice cannot make an informed selection. This is the most consequential decision in the flow and it is presented without explanation. | Seasoned user benefits from the compact layout and does not need explanation. A tooltip (not inline) would avoid cluttering their experience. |
| 5 | Visual Hierarchy | HIGH | The yield percentages (right-aligned, bold, red) in the strike price selector visually dominate the risk parameters (left-aligned, smaller, grey). The eye is drawn to yield first, risk second. For a risk-bearing product, the visual hierarchy should at minimum give equal weight to both dimensions. | Give the "from spot" percentage equal visual weight -- same font size, same weight. Consider reframing as "conversion probability: higher/lower" to make risk tangible. | Novice focuses on yield (the visually dominant element) and may select the highest yield without understanding they are also selecting the highest conversion probability. | Seasoned user reads both columns but would appreciate conversion probability language over "from spot" percentages. |
| 6 | Component Design | Medium | The Potential Outcomes panel on the right does not update with a loading state when strike price is changed. It is unclear whether the scenarios update in real-time or require a page refresh. If real-time, a brief transition/highlight animation would confirm the update. | Add a subtle highlight flash or transition animation when scenario values update in response to parameter changes. If data requires server fetch, show a skeleton loader in the outcomes panel. | Novice may not notice values changed after strike price selection if there is no visual feedback. | Seasoned user expects real-time updates and would appreciate visual confirmation. |

### Screen: Review
**File:** `review.png`

| # | Dimension | Severity | Finding | Recommendation | Novice Impact | Seasoned Impact |
|---|---|---|---|---|---|---|
| 7 | Trust & Emotional Design | CRITICAL | The Submit action commits the user to a financial investment, but the only pre-commitment safeguard is a single-line T&C acknowledgment. There is no explicit risk statement, no summary of "what could happen" in plain language, and no friction step (e.g., checkbox acknowledgment of specific risks). The T&C link opens the lorem-ipsum modal -- in production this must contain actual terms, but the flow itself should surface key risks inline, not hide them behind a link. | Add a visible risk summary box above the Submit button: "Important: If the strike price is not met at expiry, your principal of [amount] will be converted to [alternate currency] at the strike rate of [rate]. You will receive approximately [converted amount]." Require a checkbox: "I understand that my investment may be settled in [alternate currency]." | Novice may submit without understanding they could receive a different currency. This is the highest-risk moment in the flow for user harm. | Seasoned user would appreciate the explicitness as regulatory protection. |
| 8 | Visual Hierarchy | Medium | The review screen collapses the two-column layout into a single stacked layout. The Potential Outcomes cards now have colored backgrounds (light green for Scenario A, light amber for Scenario B) which is different from the parameters screen's white cards with colored badges. This visual treatment change between screens creates inconsistency. | Maintain the same visual treatment for the Potential Outcomes cards across all screens. If the review screen uses colored backgrounds, the parameters screen should too (or vice versa). | Novice may not recognize these as the same scenarios they configured on the previous screen. | Seasoned user adjusts but notices the inconsistency. |
| 9 | Navigation | Medium | The "Edit" links next to "Investment details" and "Accounts" on the review screen use a pencil icon. Clicking "Edit" presumably returns the user to the parameters screen, but it is unclear whether it preserves all other selections or resets the form. No confirmation is given about what happens when you go back to edit. | Add a tooltip or micro-copy: "Edit will return you to the parameters screen. Your other selections will be preserved." Alternatively, use inline editing on the review screen itself for simple field changes (like account selection). | Novice may be afraid to click Edit for fear of losing their work. | Seasoned user expects back-navigation to preserve state but would appreciate confirmation. |

### Screen: Confirmation -- Collapsed
**File:** `overseas-confirmation-maker-collapsed.png`

| # | Dimension | Severity | Finding | Recommendation | Novice Impact | Seasoned Impact |
|---|---|---|---|---|---|---|
| 10 | Feedback & System Status | Medium | The confirmation screen shows "Investment Placed Successfully!" with a green checkmark, transaction reference number, and the Investment Timeline. However, it does not summarize the key investment parameters (amount, currency pair, strike price, yield). The user must expand (via the chevron below the timeline) to see details. For a high-value financial transaction, immediate confirmation of the key terms provides reassurance. | Show a brief summary above the timeline: "USD 200,000.00 | USD/SGD | Strike: 1.2850 | Yield: 6.50% p.a. | Maturity: 19 Dec 2025". Keep the expandable section for full details. | Novice needs immediate reassurance that the correct investment was placed. Having to expand to verify creates unnecessary anxiety. | Seasoned user placing multiple investments wants to quickly confirm parameters without expanding. |
| 11 | Navigation | Medium | The only CTA is "Place Another Investment." There is no link to view the portfolio/landing page or the specific investment detail. After placing an investment, a common user need is to verify it appears in their portfolio. | Add a secondary link: "View My Investments" or "View Investment Details" alongside the "Place Another Investment" CTA. | Novice wants to verify their investment is tracked and visible in the system. | Seasoned user benefits from "Place Another" but also wants quick access to portfolio. |

### Screen: Landing -- Active Investments
**File:** `renew-landing-uploaded-file-3.png`

| # | Dimension | Severity | Finding | Recommendation | Novice Impact | Seasoned Impact |
|---|---|---|---|---|---|---|
| 12 | Visual Hierarchy | HIGH | The landing table mixes investments in different states (Active, Expiring Soon, Awaiting Settlement) with strike-price-met/not-met alert banners inline. The green and amber alert banners ("Strike Price Met - Base Currency (USD) Settlement" / "Strike Price Not Met - Alternate Currency (SGD) Settlement") appear between table rows, breaking the table structure. These are the most action-critical notifications in the entire product, but they compete visually with the dense table data above them. | Separate action-required investments into a prominent "Requires Your Attention" section at the top of the page, above the main table. Use card-based layouts for these items with clear CTAs (Reinvest / View Details). Keep the table for monitoring-only investments. | Novice may miss critical settlement notifications buried in the table. The inline banners are easy to overlook when scrolling through dense data. | Seasoned user with many investments needs a quick way to identify which ones need action. Scanning the full table is inefficient. |
| 13 | Information Architecture | Medium | The KPI summary bar shows "Active Investments: 4 | Expiring Soon: 1 | Total Invested Amount: 1,500,000.00 SGD | Avg. Yield: 2.7% p.a." The Total Invested Amount is labeled in SGD but the actual investments span multiple currency pairs (USD, EUR). It is unclear whether this is a converted-to-SGD equivalent or only SGD-denominated investments. | Clarify the KPI with a label like "Total Invested (SGD equivalent)" or show separate totals per base currency. The "Avg. Yield" should also clarify whether it is weighted by investment size or a simple average. | Novice may misinterpret the aggregate figures if currency conversion is implicit. | Seasoned user will question the accuracy of cross-currency aggregation. |
| 14 | Component Design | Low | The "Reinvest" button in the inline alert banners on the landing table uses a different visual treatment from the "Place Investment" CTA in the hero banner. The hero uses a white outlined button on a dark red background; the inline "Reinvest" uses a white outlined button on a green/amber background. Both are important CTAs but look different. | Standardize CTA button styles for primary investment actions. Use the same button component regardless of the container background color. | Minimal direct impact, but visual inconsistency subtly erodes trust in the product's polish. | Seasoned user notices component inconsistency as a sign of design system immaturity. |

### Screen: Landing -- Empty State
**File:** `renew-landing-uploaded-file.png`

| # | Dimension | Severity | Finding | Recommendation | Novice Impact | Seasoned Impact |
|---|---|---|---|---|---|---|
| 15 | Cognitive Load | Low | The empty state shows a hero banner ("Ready to invest?"), two value proposition cards, filter controls (with no data to filter), an empty state illustration, and an FAQ section. The filter controls appearing above the empty state is slightly awkward -- filters imply data exists. | Hide filter controls when there are no investments. Show them only when the user has at least one investment. The empty state illustration and "Place investment" link are well-designed. | Minor confusion: "Why are there filters if I have no investments?" | No impact; seasoned user knows they are starting fresh. |

### Screen: Investment Details -- Awaiting Settlement, Strike Price Met
**File:** `investment-details-awaiting-settlement-strike-price-met.png`

| # | Dimension | Severity | Finding | Recommendation | Novice Impact | Seasoned Impact |
|---|---|---|---|---|---|---|
| 16 | Feedback & System Status | Medium | The settlement outcome banner says "Strike Price Met - Base Currency (USD) Settlement" with an explanation "Fixing rate 1.3000 was above strike price of 1.2850. You will receive your principal plus yield of 201,183.33 USD on maturity." This is the best plain-language explanation in the entire product, but it only appears AFTER the fixing date. The same level of explanation should be available during the placement flow. | Back-port this explanatory pattern to the Investment Parameters screen. On the parameters screen, show: "If fixing rate is above [strike], you receive [base currency]. If below, you receive [alternate currency]." with projected amounts. | Novice would have benefited enormously from this explanation during placement, not just after settlement. | Seasoned user appreciates the confirmation clarity. |
| 17 | Navigation | Low | The "FX and Treasury" nav label on this screen differs from "FX and Investment" on the parameters/landing screens. (Repeated from Navigation finding N3 but noting the specific screen.) | Standardize to a single label across all screens in the DCI product. | See N3. | See N3. |

### Screen: Investment Details -- Awaiting Settlement, Strike Price Not Met
**File:** `investment-details-awaiting-settlement-strike-price-not-met.png`

| # | Dimension | Severity | Finding | Recommendation | Novice Impact | Seasoned Impact |
|---|---|---|---|---|---|---|
| 18 | Color & Semantics | HIGH | The "Strike Price Not Met" banner uses an amber/orange warning triangle icon. This implies the outcome is a problem or error, when in fact it is a normal, expected outcome of the product. For users who placed the DCI specifically for currency conversion purposes (as highlighted in the landing page value proposition), alternate-currency settlement may be the DESIRED outcome. | Use a neutral blue information icon instead of a warning triangle for "Strike Price Not Met." Change the banner language to be outcome-neutral: "Your investment will be settled in [alternate currency] at the strike rate." Reserve warning/amber for genuinely problematic states (e.g., settlement failure). | Novice sees the warning icon and panics: "Did something go wrong with my investment?" This creates unnecessary anxiety. | Seasoned user understands the outcome but may find the warning treatment patronizing or inaccurate. |

### Screen: Reinvest -- Strike Price Not Met
**File:** `reinvest-step-1-strike-price-not-met.png`

| # | Dimension | Severity | Finding | Recommendation | Novice Impact | Seasoned Impact |
|---|---|---|---|---|---|---|
| 19 | Cognitive Load | Medium | The reinvestment screen pre-fills the investment amount with the settlement amount from the previous investment (280,735.90 SGD) and pre-selects the currency pair (SGD/EUR). This is excellent for efficiency. However, the Potential Outcomes panel shows Scenario A with the pre-filled amount but Scenario B values are still showing dashes, suggesting the user needs to select a strike price first. The partially-filled state is slightly confusing. | Either pre-select a default strike price (e.g., the closest to spot) to show complete outcomes, or add a micro-copy note: "Select a strike price to see projected outcomes for Scenario B." | Novice may think the dashes indicate an error or missing data rather than an incomplete configuration. | Seasoned user understands the dependency but would appreciate faster configuration with a default strike price. |

### Screen: Multi-Currency Account Required
**File:** `confirm-omc.png`

| # | Dimension | Severity | Finding | Recommendation | Novice Impact | Seasoned Impact |
|---|---|---|---|---|---|---|
| 20 | Navigation | HIGH | This gate screen uses a completely different nav bar configuration -- "FX and treasury" (lowercase), "Trade finance" (lowercase, different from other screens), and the active state appears to be on "Trade finance" rather than "FX and Investment." A user arriving here from a DCI marketing link or product page would be disoriented by the navigation context shift. | Ensure this screen uses the same nav bar configuration and active state as the rest of the DCI flow ("FX and Investment"). The product context should remain consistent even for prerequisite/gate screens. | Novice may believe they have navigated to the wrong section entirely. Combined with the unfamiliar "Multi-Currency Account" requirement, they may abandon. | Seasoned user will be confused by the nav label discrepancy and may question whether they are in the right place. |
| 21 | Cognitive Load | Medium | The page explains that a Multi-Currency Account is required for DCI, with a clear CTA ("Open Multi-Currency Account"). However, it does not explain how long account opening takes, whether it can be done online, or when the user can return to place their DCI investment. | Add context: "Opening a Multi-Currency Account takes approximately [X minutes/days]. Once approved, you can return here to place your first Dual Currency Investment." Include a "Learn more about Multi-Currency Accounts" link. | Novice needs to know the effort and timeline to decide whether to proceed now or later. | Seasoned user may already have the account and could be seeing this erroneously; a "Check my accounts" link would help. |

### Screen: T&C Modal
**File:** `t-c.png`

| # | Dimension | Severity | Finding | Recommendation | Novice Impact | Seasoned Impact |
|---|---|---|---|---|---|---|
| 22 | Component Design | Low | The T&C modal has "Cancel" and "Agree" buttons. The "Agree" button is teal/dark, which is inconsistent with the red primary button used throughout the rest of the product. This color inconsistency may cause momentary hesitation. (Note: lorem ipsum content is expected placeholder and not flagged.) | Use the same primary button color (OCBC red) for the "Agree" button to maintain visual consistency with the rest of the product. | Minor: novice may briefly wonder if this is a different product or external page. | Negligible. |

---

## Section 5: Findings Summary Table (Sorted by Severity)

| # | Screen / Component | Dimension | Severity | Finding Summary |
|---|---|---|---|---|
| 3 | Investment Parameters | Trust & Emotional Design | CRITICAL | Green/red color coding on scenario badges biases perception of outcomes, creating unfair risk disclosure |
| 7 | Review | Trust & Emotional Design | CRITICAL | No explicit risk statement before Submit; risk buried in T&C link with no inline risk summary or acknowledgment checkbox |
| N1 | All flow screens | Navigation | HIGH | No step indicator or progress bar across the multi-step placement flow |
| N3 | All screens | Navigation | HIGH | "FX and Investment" vs. "FX and Treasury" nav label mismatch within the same product |
| 4 | Investment Parameters | Cognitive Load | HIGH | Strike price presented without any plain-language definition or explanation of its impact |
| 5 | Investment Parameters | Visual Hierarchy | HIGH | Yield visually dominates risk in the strike price selector, inverting appropriate hierarchy for a risk-bearing product |
| -- | All screens | Color & Semantics | HIGH | Green overloaded with 5+ meanings; "Alternate Currency" red badge carries negative connotation in financial context |
| -- | Parameters, Review | Yield Presentation | HIGH | Annualized yield prominently displayed without actual-return context; 6.50% p.a. on 1-month tenor is ~0.54% actual |
| 12 | Landing (active) | Visual Hierarchy | HIGH | Action-critical settlement notifications buried as inline banners within dense table |
| 18 | Details (strike not met) | Color & Semantics | HIGH | Warning icon on "Strike Price Not Met" implies error when it is a normal product outcome |
| 20 | Multi-Currency Account gate | Navigation | HIGH | Completely different nav bar configuration from rest of DCI flow |
| -- | Flow-wide | Regulatory | HIGH | No suitability disclaimer, no standalone risk acknowledgment step, no cooling-off information |
| 8 | Review | Visual Hierarchy | Medium | Potential Outcomes visual treatment changes between Parameters and Review screens |
| 9 | Review | Navigation | Medium | "Edit" link behavior unclear -- does it preserve other selections? |
| 10 | Confirmation | Feedback | Medium | Collapsed confirmation lacks key parameter summary; must expand for verification |
| 11 | Confirmation | Navigation | Medium | No "View My Investments" link; only "Place Another Investment" CTA |
| 13 | Landing (active) | Information Architecture | Medium | Cross-currency KPI aggregation unclear (SGD equivalent not labeled) |
| N2 | Details screens | Navigation | Medium | No breadcrumbs for orientation within product hierarchy |
| N5 | Landing (active) | Information Architecture | Medium | No sub-filtering or separation for action-required investments |
| -- | Parameters, Details | Typography | Medium | Dense table text, inconsistent title treatments across screens |
| -- | All screens | Component | Medium | Status badge outline/fill inconsistency; "Reinvest" button visually demoted vs. primary CTAs |
| 6 | Investment Parameters | Component Design | Medium | No loading/transition state when outcomes panel updates |
| 19 | Reinvest | Cognitive Load | Medium | Partially-filled outcomes panel (dashes in Scenario B) without explanation |
| 21 | Multi-Currency Account gate | Cognitive Load | Medium | No context on account-opening timeline or process |
| 1 | Parameters (empty) | Forms & Data Entry | Medium | Minimum amount formatting appears templated; "NIL" currency default unclear |
| 2 | Parameters (empty) | Cognitive Load | Medium | Empty Potential Outcomes panel provides no context for dual-scenario structure |
| 15 | Landing (empty) | Cognitive Load | Low | Filter controls visible when no data exists to filter |
| 22 | T&C Modal | Component Design | Low | "Agree" button color inconsistent with product's primary button color |
| -- | Multiple | Typography | Low | Minor inconsistencies in "p.a." sizing and value formatting across screens |
| 14 | Landing (active) | Component Design | Low | "Reinvest" button in alert banners styled differently from hero "Place Investment" CTA |
| -- | Parameters | Forms | Low | "NIL" vs. "N.A" for empty currency state |

---

## Section 6: Top 5 Priority Recommendations

### 1. Add Explicit Risk Disclosure Before Commitment
- **What to fix:** Add a visible risk summary box and acknowledgment checkbox on the Review screen, directly above the Submit button.
- **Why it matters:** Users committing significant capital to a product with principal currency risk must understand the downside scenario in plain language. This is both a user-protection and regulatory-compliance issue. The current flow buries risk in T&C and relies on the user interpreting abstract scenarios.
- **How to fix it:** Insert a bordered callout box: "Please note: If the fixing rate is [below/above] [strike price] on [expiry date], your investment of [amount] [base currency] will be converted to approximately [amount] [alternate currency] at the strike rate. Your return in [base currency] terms may be lower than your original investment." Add a required checkbox: "I understand my investment may be settled in [alternate currency]."
- **Effort estimate:** Quick Win (copy + one UI component)

### 2. Neutralize Scenario Color Coding
- **What to fix:** Replace the green "Base Currency" and red "Alternate Currency" badges with neutral, non-judgmental colors.
- **Why it matters:** The current green/red coding creates an implicit bias that Scenario A is positive and Scenario B is negative. For a product where either outcome includes positive yield, this misrepresents the risk profile and may not satisfy fair disclosure requirements.
- **How to fix it:** Use navy or dark grey badges for both scenarios, differentiated by currency flag icons and labels. Alternatively, use the currency's national color (e.g., blue for USD, red for SGD) if it does not create a positive/negative association. Apply the same treatment to the "Strike Price Met/Not Met" banners on details screens -- use a neutral blue info icon instead of green check / amber warning.
- **Effort estimate:** Quick Win (badge color change)

### 3. Add Step Indicator and Plain-Language Strike Price Explainer
- **What to fix:** (a) Add a step progress indicator across the placement flow. (b) Add a contextual explainer for strike price on the parameters screen.
- **Why it matters:** (a) Users committing to a multi-step financial transaction need orientation. (b) Strike price is the single most consequential parameter in DCI placement, and it is presented without explanation, making informed consent impossible for novice users.
- **How to fix it:** (a) Add a horizontal step indicator: "1. Configure Investment > 2. Select Accounts > 3. Review & Submit". (b) Add a tooltip icon next to "Strike Price" that opens: "The strike price is the exchange rate compared against the market rate at expiry. It determines whether you receive your investment back in [base currency] or [alternate currency]." Include a simple diagram showing the two outcome paths.
- **Effort estimate:** Medium Lift (step indicator is a new component; explainer is copy + tooltip)

### 4. Separate Action-Required Investments on Landing Page
- **What to fix:** Create a distinct "Requires Action" section at the top of the Active Investments view for investments with settlement outcomes (strike price met/not met) and expiring-soon investments.
- **Why it matters:** The most time-sensitive and financially consequential items (reinvestment decisions at maturity) are visually buried in a dense table. Missing a reinvestment window has direct financial impact.
- **How to fix it:** Above the main table, add a card-based section: "Action Required (2)" with individual cards for each investment needing attention. Each card shows: currency pair, amount, settlement outcome, and a prominent "Reinvest" or "View Details" CTA. The main table below retains all investments for monitoring purposes.
- **Effort estimate:** Medium Lift (new section component, data filtering logic)

### 5. Standardize Navigation Labels and Component System
- **What to fix:** Unify the nav bar label to a single term across all DCI screens and standardize status badge, button, and color component usage.
- **Why it matters:** Three different nav configurations ("FX and Investment", "FX and Treasury", "FX and treasury") across the same product flow erodes user confidence and suggests the product is stitched together from different systems. This is especially damaging for trust in a financial product.
- **How to fix it:** Audit all screens for nav label consistency; pick one label (recommend "FX and Investment") and apply it universally. Create a status badge component with consistent fill/outline treatment. Ensure all primary CTAs use the same red button component.
- **Effort estimate:** Quick Win (label text changes) to Medium Lift (component standardization)

---

## Section 7: Design System & Consistency Notes

| Issue | Details |
|---|---|
| **Nav bar fragmentation** | Three configurations observed: "FX and Investment" (most screens), "FX and Treasury" (details screens), "FX and treasury" / "Trade finance" (confirm-omc). Must be unified into a single component with consistent labels. |
| **Status badges** | "Awaiting Settlement" (green outline), "Expiring Soon" (orange filled), "Settled" (grey filled) use different visual treatments. Recommend a unified badge component with consistent shape and size, varying only color. |
| **Primary button color** | OCBC red used throughout main flow, but T&C modal uses teal/dark for "Agree." Should use the same primary color. |
| **Scenario badges** | "Base Currency" (green) and "Alternate Currency" (red) are custom badge components not seen elsewhere. These should be either added to the design system as a formal "currency indicator" component or replaced with neutral styling. |
| **Alert banners** | The "Strike Price Met" (green) and "Strike Price Not Met" (amber) banners on both landing and details screens use slightly different widths and padding. Should be a single alert-banner component. |
| **"Reinvest" button** | Appears in two contexts (details settlement breakdown, landing alert banner) with different sizes and visual prominence. Should be standardized. |
| **Currency selector** | The dropdown component shows "NIL" in one context and "N.A" in another for the empty state. Standardize to a single empty-state label. |

---

## Section 8: What is Working Well

1. **Investment Timeline component is excellent.** The vertical timeline with Transaction Date, Value Date, Expiry Date, and Maturity Date -- each with a plain-language description of what happens on that date -- is the single best-designed element in the product. It provides genuine clarity for both personas and should be used as a reference pattern for other complex concepts in the flow.

2. **Post-settlement explanation text is clear and specific.** The settlement outcome banners on the details screens (e.g., "Fixing rate 1.3000 was above strike price of 1.2850. You will receive your principal plus yield of 201,183.33 USD on maturity.") are well-written, specific, and use actual numbers. This quality of explanation should be brought forward into the placement flow.

3. **Currency pair selector with flag icons is intuitive.** The use of country flag icons alongside currency codes in both the base/alternate currency selectors and the investment amount currency selector provides strong visual recognition. The current spot rate display with refresh timestamp is also well-executed.

4. **Settlement breakdown table is well-structured.** The Principal / Yield / Total Settlement table on the details screen is clean, scannable, and uses appropriate formatting (green for positive yield, clear currency labels). This is a strong pattern.

5. **Landing page FAQ section addresses the right questions.** The four FAQ questions ("What is a DCI?", "How does it work?", "What are the risks?", "What are the key milestone dates?") are well-chosen for novice education. The collapsed accordion pattern is appropriate for supplementary content.

---

## Section 9: Suggested Next Audit Scope

1. **Maker-Checker Approval Flow:** The confirmation screen filename references "maker" suggesting a corporate banking dual-authorization model. The checker/approver experience -- what they see, what information they need to approve/reject, and how they communicate decisions -- should be audited as a separate flow.

2. **Reinvestment Flow (Full End-to-End):** The reinvest screens were partially captured. A full audit of the reinvestment decision flow -- from settlement notification through to new investment placement -- would reveal whether the re-engagement experience is optimized for conversion and clarity.

3. **Mobile/Responsive Breakpoints:** This audit covered desktop 1280px+. The dense landing table, two-column parameter layout, and strike price selector will require significant adaptation for tablet and mobile viewports.

4. **Error States and Edge Cases:** No error states were visible in the screenshots provided. A dedicated audit of validation errors, API failure states, session timeout during placement, and insufficient-balance scenarios would be valuable.

5. **Multi-Language Support:** The "EN" language selector in the nav bar suggests multi-language support. An audit of the Chinese/Malay language versions would reveal whether the layout accommodates varying text lengths and whether financial terminology is accurately translated.
