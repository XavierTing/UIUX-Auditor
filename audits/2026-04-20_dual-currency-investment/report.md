# UI/UX AUDIT REPORT: OCBC Dual Currency Investment (DCI)

**Audit Date:** 2026-04-20
**Figma File:** `https://www.figma.com/design/5bzUnCV6vs7GFHzPvohbbR/Dual-Currency-Investment?node-id=932-30701`
**Auditor Personas:**
- **Persona A — Novice Investor:** First-time corporate user exploring DCI. Understands basic banking (deposits, FX transfers) but has no experience with structured products, options, derivatives, or strike prices. Goal: "I heard DCI offers better returns than time deposits. I want to try it with USD 200,000."
- **Persona B — Experienced Investor:** Seasoned treasury professional at a Singapore corporate. Familiar with structured products, options terminology, currency pairs, and OCBC's platform. Uses DCI regularly for yield enhancement. Goal: "I want to quickly place a 1-month USD/SGD DCI and manage my existing portfolio."
**Platform:** Web desktop (1280px+)
**Flow Scope:** End-to-end DCI investment flow — landing page, investment configuration, account selection, review, confirmation, post-investment monitoring, reinvestment, and prerequisite account flows.
**Screens Reviewed:** Landing page (empty state + FAQ expanded), Investment Configuration (empty, partial, filled states), Currency/Tenor dropdowns, Account Selection (empty + filled x2), Funding Account dropdown, Review, Confirmation (collapsed + expanded), Active Investments list, Settled Investments list, Investment Details (x4 states: strike met, not met, settled, expiring soon), Reinvest Step 1 (strike met + not met), Reinvest Step 2 (x2), Reinvest Confirmation, T&C Modal, MCA Prerequisite Gate, SAO Account Application, Customer w/o Currency in MCA sub-flow — **28+ screens total**.

---

## Executive Summary

OCBC's Dual Currency Investment flow delivers a **well-structured investment configuration experience** with strong visual design foundations — the two-column input/outcome layout, colour-coded scenario panels, investment timeline stepper, and consistent button pairing create an effective decision-support interface. The post-investment monitoring dashboard with inline settlement outcome banners and reinvestment CTAs is a standout feature for portfolio management.

However, the product has **critical deficiencies in risk communication and novice onboarding** that create both user-safety and regulatory concerns. A novice investor can traverse the entire flow — from promotional landing page through final submission — without encountering a single risk warning, suitability check, or plain-language explanation of what DCI means for their capital. The landing page actively positions DCI as a yield-enhancement product ("higher potential returns", "turn your foreign currency needs into potential for better returns") while all risk disclosures are confined to a collapsed FAQ section. For a capital-at-risk structured product with embedded derivatives, this is a severe gap.

The experienced investor experience is meaningfully better — terminology is standard, the two-column layout supports rapid decision-making, and the settlement outcome design on investment details screens is clear and well-differentiated. However, even experienced users will notice the absence of a step progress indicator, the lack of explicit consent mechanisms, and several missing features (rate history, portfolio analytics, maker-checker workflow) that would elevate the product from functional to best-in-class.

**Audit Coverage:** 28+ screens across 6 flows (new investment, monitoring, reinvestment, account prerequisites, T&C, customer w/o currency). All 9 audit dimensions evaluated plus 6 banking/DCI-specific focus areas. Missing features analysis included per request.

**UX Health Scores:**
- **Novice Investor: 3.5 / 10** — Product is not safe for novice use. Missing: risk disclosure in flow, suitability assessment, terminology help, actual return display, and educational onboarding.
- **Experienced Investor: 6.5 / 10** — Functional and efficient for repeat use. Strong config layout and portfolio monitoring. Friction from missing stepper, no explicit consent, and absent power-user features (rate history, saved configs).
- **Combined Score: 4.5 / 10** — Solid visual/interaction design foundations undermined by critical risk communication and regulatory compliance gaps.

---

## Findings Table

| # | Screen / Component | Dimension | Severity | Finding | Novice Impact | Experienced Impact | Recommendation |
|---|---|---|---|---|---|---|---|
| 1 | Landing — Hero Banner & Value Props | 9. Trust | 🔴 CRITICAL | Landing page copy exclusively promotes upside — "Ready to invest?", "Turn your foreign currency needs into potential for better returns", "Maximise your investment returns", "higher than interest rates on an ordinary time deposit." Zero risk mention anywhere above the fold for a capital-at-risk structured product with embedded derivatives. | Forms expectation of guaranteed positive returns; no signal that principal could be converted to less favourable currency at maturity. | Notes absence of required risk disclaimers at product entry point; questions regulatory compliance. | Add mandatory risk disclaimer below hero: "Important: DCI is a structured investment product, not a deposit. Your principal may be converted to the alternate currency at maturity. Capital is at risk. Not covered by deposit insurance." |
| 2 | Entire Flow (Config → Accounts → Review → Submit) | 9. Trust | 🔴 CRITICAL | Risk disclosures exist only in collapsed FAQ on landing page. A user can click "Place investment", configure parameters, select accounts, review, and submit — committing real capital — without encountering any risk warning or acknowledgment step. | No opportunity to understand downside before committing capital. May not even realise currency conversion risk exists until after settlement. | Expects inline risk disclosures per industry standard; questions whether this meets MAS regulatory requirements for Specified Investment Products. | Insert risk summary card at top of Configuration screen. Add mandatory risk acknowledgment checkbox on Review screen before Submit is enabled. |
| 3 | Pre-Configuration (No gate) | 9. Trust | 🔴 CRITICAL | No suitability assessment or Customer Knowledge Assessment (CKA) before allowing investment in a structured product with embedded derivatives. Any authenticated corporate user can immediately invest. | Allowed to invest in a complex product they may fundamentally misunderstand, with no comprehension gate. Could lose significant capital. | Questions whether platform meets MAS Notice SFA 04-N12 requirements for Customer Knowledge Assessment. | Add suitability gate before configuration: 3-4 questions confirming user understands DCI is not a deposit, settlement may be in alternate currency, and principal is at risk. For returning users, allow annual re-certification bypass. |
| 4 | Review — Submit Section | 6. Forms | 🔴 CRITICAL | No explicit T&C consent checkbox. Only implicit consent via small-print text: "By clicking 'Submit', you confirm that you have read, understood and agree to the Terms and Conditions." For a structured product with embedded derivatives, implicit consent is insufficient and likely does not meet regulatory requirements. | May not read disclaimer; unknowingly consents to unreviewed terms for a capital-at-risk product. | Expects explicit consent mechanism per industry standard for structured products. Implicit consent erodes trust. | Add mandatory checkboxes: "☐ I have read and agree to the Terms and Conditions" and "☐ I understand this investment may settle in the alternate currency and my principal is at risk." Both required before Submit enables. |
| 5 | Config — Strike Price Selection | 8. Cognitive Load | 🟠 HIGH | Annualized yield (e.g. 6.50% p.a.) is the primary decision anchor and only yield format shown. For a 1-month tenor, actual return is ~0.54%; for 1-week, ~0.125%. Actual period return is never displayed. Users see "6.70%" next to the first strike price and perceive it as their return. | Perceives 6.50% as the actual return they'll receive. Dramatically inflated expectations lead to disappointment or misunderstanding at settlement. | Understands p.a. convention but would benefit from seeing actual period return for quick mental calculation. | Show both formats: "6.50% p.a. (~0.54% for 1 month)" or "Est. return: ~$1,083 USD". Display absolute dollar return prominently in the Potential Outcomes panel. |
| 6 | Config — Strike Price Selection | 8. Cognitive Load | 🟠 HIGH | Strike price list shows yield-risk tradeoff as purely better/worse yields — higher strike = lower yield, but this relationship to conversion probability is unexplained. A user naturally selects the highest yield without understanding it maximises their probability of alternate currency settlement. | Naturally selects 6.70% (highest yield) without understanding that strike price closer to spot means higher conversion probability. Makes uninformed risk decision. | Understands tradeoff implicitly from options knowledge but notes absence of novice guardrails. | Add explanatory note above strike prices: "Strike prices closer to the current spot rate offer higher yields but have a greater chance of your investment settling in the alternate currency." |
| 7 | Config — Investment Amount Field | 5. Components | 🟠 HIGH | Minimum amount helper text displays "$0,000.00 USD" on the empty state and "$0,000.00 USD" on the partially filled state — template placeholders never replaced with actual minimums. The filled state shows "Minimum amount: $0,000.00 USD" which looks broken. | Cannot determine minimum investment. "$0,000.00" looks like a system error; reduces trust in the platform. | Recognises placeholder; questions production readiness of the design. | Replace with actual dynamic minimum (e.g., "Minimum: 50,000.00 USD"). Make dynamic per currency pair. |
| 8 | Config — All Financial Terms | 8. Cognitive Load | 🟠 HIGH | Financial jargon without inline definitions or tooltips: "Tenor", "Strike Price", "Currency pair", "Current Spot Rate (Indicative)", "Fixing Rate", "Base Currency", "Alternate Currency". The ⓘ icons exist next to Currency pair, Tenor, Strike Price, and Potential Outcomes, but no tooltip content is shown in the design — unclear if implemented. FAQ definitions are on a separate page. | Cannot make informed decisions. Key terms undefined at point of decision. Novice comprehensibility estimated at 2.5/5. | No issue — standard terminology (4.8/5 comprehensibility). | Ensure ⓘ tooltip content is designed/specified. Use plain language alongside jargon: "Tenor (Investment Period)", "Strike Price (Target Exchange Rate)". Add tooltip definitions for every ⓘ icon. |
| 9 | Config — Scenario Panels | 4. Colour | 🟠 HIGH | Scenario A (Base Currency outcome) uses green background; Scenario B (Alternate Currency outcome) uses peach/orange. Creates unconscious bias: green = good/desired, orange = warning/bad. In reality, either scenario could be the user's preferred outcome depending on their currency needs. | Perceives Scenario A as the "correct" or "good" outcome regardless of their actual currency conversion needs. Biased decision-making. | Notices colour bias but not significantly affected by it. May note it's inconsistent with neutral product positioning. | Use neutral colours for both scenarios (e.g., light blue and light grey). Or allow user to declare their preferred outcome and highlight accordingly. |
| 10 | Reinvest Config — Strike Not Met | 8. Cognitive Load | 🟠 HIGH | After strike-not-met settlement (e.g., EUR/SGD settling in SGD), the reinvestment screen silently flips the currency pair to SGD/EUR — the base currency has changed from EUR to SGD without any explanation or contextual banner. The investment amount is pre-populated with the SGD settlement amount (280,735.90). | Deeply confused by currency change. "Why is my base currency now SGD when I started with EUR?" May abandon or make an error. | Understands the mechanics (settled in SGD, so reinvesting from SGD) but prefers explicit confirmation and context. | Add contextual banner: "Your previous investment settled in SGD. This reinvestment uses SGD as your base currency." Show original vs new currency pair side by side. |
| 11 | Config → Accounts → Review | 1. IA & Navigation | 🟠 HIGH | No step progress indicator across the 3-step investment flow (Configure → Account Selection → Review). The "REVIEW" sidebar label appears only on the review screen; no equivalent label on configuration or account selection steps. Users cannot gauge remaining steps or their position in the flow. | Uncertain how long process will take or how many more steps remain. May abandon if flow feels endless. | Minor friction — can infer step count from experience but expects a stepper in a financial flow as standard. | Add horizontal stepper bar: "1. Configure → 2. Accounts → 3. Review → Confirmation". Persist across all steps. |
| 12 | Config — Spot Rate & Yield | 7. Feedback | 🟡 MEDIUM | "Indicative" qualifier on spot rate and yield is unexplained. "Current Spot Rate (Indicative)" with a refresh icon appears, but users don't know if rates are guaranteed, estimated, or may change before submission. The timestamp ("As at 17 Nov 2025, 15:05:28") helps but doesn't clarify guarantee. | Anxious about whether displayed yield is what they'll actually receive. "Indicative" sounds uncertain — may hesitate to proceed. | Understands live quotes but notes lack of explicit "rates locked at submission" or "rates may change" disclosure. | Add tooltip: "Indicative rates are based on current market conditions and may change. Your final rate will be confirmed at submission." |
| 13 | Review — Full Page | 2. Visual Hierarchy | 🟡 MEDIUM | Review screen requires scrolling through 5 sections (Investment details, Accounts, Potential Outcomes, Investment Timeline, T&C disclaimer) before reaching the Submit button at the very bottom. No sticky CTA bar, floating summary, or collapsible sections. The page is approximately 3x viewport height. | May not find Submit button; extensive scrolling before a significant financial commitment increases anxiety and cognitive load. | Finds scrolling tedious for repeat investments; wants a quick-submit option. | Add sticky bottom bar with key summary (Amount, Pair, Yield) + Submit button. Or make sections collapsible with a summary card always visible. |
| 14 | T&C Modal | 3. Typography | 🟡 MEDIUM | T&C presented as undifferentiated wall of Lorem Ipsum-style text — no headings, bullets, numbered clauses, or section breaks. Users cannot scan for relevant clauses. Entire content is in the same font size with no visual hierarchy. | Will not read any T&C content. Loses the only opportunity (besides FAQ) to understand product risks and terms. | Cannot locate specific clauses (early termination, force majeure, calculation agent). Frustrating for due-diligence-oriented professionals. | Structure T&C with section headings, numbered clauses, and bullet points. Highlight 3-5 key risk clauses visually (bold or coloured background). Add a table of contents at top. |
| 15 | Confirmation — CTA Priority | 9. Trust | 🟡 MEDIUM | "Place Another Investment" is the primary CTA (filled dark button) immediately after placing an investment. "Back to Dual Currency Investment" is secondary (text link). This nudges impulsive repeat investment without reflection or portfolio review. | May feel pressured to invest again immediately without evaluating portfolio alignment or reflecting on the commitment just made. | Appreciates quick access for batch placement but recognises the behavioural nudge. | Make "Back to Dual Currency Investment" the primary CTA (view portfolio first). Move "Place Another Investment" to secondary (outline button). |
| 16 | Confirmation — Expanded vs Collapsed | 8. Cognitive Load | 🟡 MEDIUM | The expanded confirmation screen repeats nearly all review information (investment details, accounts, full scenario panels, timeline). At confirmation, users primarily need reassurance + reference number, not a full recap. The collapsed version exists but the expanded is the default. | May re-read everything looking for something different; cognitive load at what should be a relief moment. | Skips detail; wasted screen real estate. | Default to collapsed confirmation (summary + ref number + timeline). Provide expandable "View full details" for opt-in detail. |
| 17 | Investment Details — "Expiring Soon" | 7. Feedback | 🟡 MEDIUM | "Expiring Soon" investment detail screen shows no settlement outcome section, no Potential Outcomes panel, and no projected scenarios. Users approaching expiry have less information than when they placed the investment. No current rate context to help gauge likely outcome. | Anxious about approaching expiry with no indication of likely outcome. "What will happen to my money?" — no information to answer this. | Wants to see current spot vs strike to gauge probable outcome. Missing information that was available at configuration. | Add "Projected Outcome" section showing current spot rate vs strike price, with indication of which scenario is more likely. Show countdown to fixing date/time. |
| 18 | Landing — "Expiring soon" Status | 4. Colour | 🟡 MEDIUM | "Expiring soon" status badge uses red/orange text in the Active Investments list. Red in banking context signals error/danger, but expiry is a normal lifecycle event, not an error. Creates unnecessary anxiety. | Perceives "Expiring soon" as something going wrong. Alarm where none is warranted. | May briefly notice the colour but understands it's informational. Mildly misleading. | Use a neutral or amber badge for "Expiring Soon" — reserve red for errors, warnings, or actions required. Consider "Approaching Maturity" as clearer label. |
| 19 | Landing — Value Proposition Cards | 2. Visual Hierarchy | 🟡 MEDIUM | Three value proposition cards all present benefits without balanced risk context: "Maximise your investment returns", "Flexibility and control", "Great for currency conversion needs". Icons are generic and don't clearly relate to the text content. | Value props reinforce deposit-like expectations. "Maximise your investment returns" reads as guaranteed upside. Cards are promotional, not educational. | Skims past marketing content; value props don't provide useful information for decision-making. | Balance at least one card with risk context: "Understand the tradeoffs — Your investment may settle in a different currency depending on market movements." Replace generic icons with DCI-specific illustrations. |
| 20 | Account Selection — Page Layout | 2. Visual Hierarchy | 🟡 MEDIUM | Account selection page uses less than 40% of the viewport width. The funding account and two settlement account dropdowns are stacked vertically with large amounts of whitespace on the right side. No contextual information about why two settlement accounts are needed. | Wonders why they need two settlement accounts. Page feels sparse — uncertain if something is missing. | Understands the need for dual settlement but notes the wasted space could show helpful context. | Add right-side contextual panel explaining why two settlement accounts are needed: "Depending on market conditions at expiry, your investment will settle in either [Base] or [Alternate] currency. We need an account for each." |
| 21 | Config — Currency Selector | 5. Components | 🟡 MEDIUM | Investment Amount currency selector shows "N.A" as default state with a generic flag icon, which is unclear. After selection, the dropdown shows a well-designed list with flags, full names, and ISO codes — but the "N.A" initial state is confusing. | "N.A" — does this mean Not Applicable? Not Available? Why is there no default currency? Confusing initial state. | Minor — quickly selects currency. But "N.A" is non-standard for a currency selector default. | Change default to "Select Currency" or pre-populate with user's primary account currency (likely SGD for Singapore corporate). |
| 22 | Landing — FAQ Expansion | 3. Typography | 🟡 MEDIUM | FAQ section contains comprehensive DCI education including worked examples, risk disclosures, payoff tables, and milestone dates — but only visible when manually expanded. This critical content is buried below the fold, behind accordion toggles, on the landing page only. Not accessible during the investment flow. | FAQ is the only source of product education, but most users won't find or read it. If they do, they can't reference it during configuration without navigating away. | May reference FAQ for specific clauses but finds it inefficient to toggle between FAQ and investment flow. | Surface key FAQ content contextually: risk info on config screen, milestone definitions next to timeline, payoff examples next to scenario panels. Make FAQ searchable. |
| 23 | Post-Investment — Table Column Density | 2. Visual Hierarchy | 🟢 LOW | Active Investments table packs 7 columns (Currency Pair, Strike Price, Tenor, Status, Expiry Date/Time, Investment Amount, plus inline settlement banners) into a single row. On narrower desktop viewports, this may cause horizontal scrolling or truncation. | Dense table is overwhelming; many columns contain unfamiliar data. | Appreciates data density for quick scanning but notes some columns (Trade Date, Start Date) are redundant with detail view. | Consider progressive disclosure: show 5 key columns in table, expand to full detail on row click. Use responsive table pattern for narrower viewports. |
| 24 | All Screens — Yield "p.a." Label | 3. Typography | 🟢 LOW | "p.a." abbreviation is never expanded to "per annum" or "per year" anywhere in the flow. Used on config, review, confirmation, investment details, and portfolio list. Combined with annualised-only yield display, compounds the comprehension gap. | May not know what "p.a." means. Adds to the jargon burden. | No issue — standard abbreviation. | Expand on first use: "6.50% p.a. (per year)". Consider using "annual" in full where space permits. |
| 25 | Confirmation — Timeline Dates | 7. Feedback | 🟢 LOW | Confirmation shows "Trade Date: 17 Nov 2025" (the date of placement) but no indication of what happens between now and Start Date (19 Nov 2025). The 2-day gap is unexplained. | Wonders why investment doesn't start immediately. "Did something go wrong?" May check back anxiously. | Understands T+2 settlement convention but notes it's not explained for corporate users who may not be FX-savvy. | Add brief note: "Your investment will start 2 business days after placement (standard settlement)." |

---

## Missing Features Analysis

This section identifies features that are absent from the current DCI flow but would meaningfully improve the user experience. Categorised by impact area.

### Critical for Novice Safety

| Missing Feature | Description | Why It Matters | Effort |
|---|---|---|---|
| **Product Education Module** | Interactive onboarding tutorial explaining DCI mechanics before first investment — what it is, how scenarios work, what "strike price" means, worked example with visuals. | A novice arrives at the config screen and faces 6+ undefined financial terms. Without foundational understanding, every parameter choice is uninformed. The FAQ provides this content but it's buried and passive. | Medium Lift |
| **Risk Calculator / "What-If" Simulator** | Tool allowing users to model scenarios: "If I invest X in USD/SGD at strike Y, what are my possible outcomes?" with visual payoff chart. | Users choose parameters without understanding the concrete financial implications. A simulator would transform abstract numbers into tangible outcomes. | Large Effort |
| **Inline Glossary / Terminology Help** | Persistent, contextual tooltip definitions for every financial term on the configuration screen — not just ⓘ icons but actual designed tooltip content. | Tooltips exist as icons (ⓘ) but no tooltip content is shown in the design. Either the content isn't designed or it's not implemented. This is the single most impactful improvement for novice comprehension. | Quick Win |
| **Suitability Assessment Gate** | Pre-investment questionnaire to verify user understands DCI risks before allowing access to configuration. | MAS regulatory requirement for Specified Investment Products. Protects both the user and the bank. | Medium Lift |

### Experienced User Efficiency

| Missing Feature | Description | Why It Matters | Effort |
|---|---|---|---|
| **Saved Investment Templates** | Ability to save frequently-used DCI configurations (e.g., "Monthly USD/SGD 1M") and reuse them for repeat investments. | Treasury professionals place similar DCI investments regularly. Re-entering the same parameters each time is unnecessary friction. | Medium Lift |
| **Rate History Chart** | Historical exchange rate chart for the selected currency pair, shown alongside the strike price selection. | Experienced users want market context when choosing a strike price. "Is 1.2850 high or low relative to recent history?" Currently requires a separate tool. | Medium Lift |
| **Batch Investment Placement** | Ability to configure and submit multiple DCI investments in a single flow (e.g., ladder different tenors or strike prices). | Treasury professionals often place multiple DCI investments simultaneously as a yield strategy. Current flow supports only one at a time. | Large Effort |
| **Quick Reinvest** | One-click reinvestment from the portfolio list with same parameters, bypassing the full configuration flow. | For settled investments where the user wants to roll over with identical parameters, the current 3-step reinvest flow is unnecessarily long. | Medium Lift |

### Regulatory Compliance

| Missing Feature | Description | Why It Matters | Effort |
|---|---|---|---|
| **Explicit T&C Consent Checkbox** | Dedicated checkbox requiring active opt-in to terms, not implicit consent via "By clicking Submit..." disclaimer text. | Industry standard and likely regulatory requirement for structured products with embedded derivatives. Implicit consent is insufficient. | Quick Win |
| **Key Fact Sheet / Product Highlight Sheet** | Link to or inline display of the MAS-required product highlight sheet during the investment flow (currently only "Download Termsheet" on post-investment details). | MAS typically requires product highlight sheets to be provided before purchase of Specified Investment Products. Currently only available post-investment. | Quick Win |
| **Risk Acknowledgment Step** | Dedicated screen or section where users confirm they understand specific DCI risks before proceeding to submit. | Goes beyond T&C consent — specific acknowledgment of: not a deposit, principal at risk, may settle in alternate currency, not insured. | Medium Lift |
| **Cooling-Off Period Notice** | Information about whether a cooling-off period applies and how to exercise cancellation rights. | Standard for many investment products in Singapore. Absence may be a compliance gap. | Quick Win |

### Portfolio Management

| Missing Feature | Description | Why It Matters | Effort |
|---|---|---|---|
| **Portfolio Analytics Dashboard** | Aggregate view of DCI portfolio performance: total invested, total yield earned, currency exposure breakdown, average yield across investments. | Users with 4+ active investments (as shown in the portfolio list) have no aggregate view. Each investment is tracked individually with no portfolio-level insights. | Large Effort |
| **Expiry Alerts & Notifications** | Configurable notifications for approaching expiry dates, settlement outcomes, and rate movements relative to strike prices. | "Expiring Soon" badge on the list is the only alert mechanism. No push notifications, email alerts, or configurable thresholds. Users must manually check the dashboard. | Medium Lift |
| **Export / Reporting** | Ability to export investment data to CSV/Excel for treasury reporting and accounting reconciliation. | Corporate treasury teams need to report DCI positions in their own systems. Manual data entry from screen is error-prone and time-consuming. | Medium Lift |
| **Current Rate vs Strike Monitoring** | Real-time or near-real-time display of current exchange rate vs strike price for active investments, showing how close/far from settlement threshold. | The "Expiring Soon" detail screen shows no current rate information. Users can't gauge the likely outcome without checking rates externally. | Medium Lift |

### Maker-Checker Workflow (Corporate Banking)

| Missing Feature | Description | Why It Matters | Effort |
|---|---|---|---|
| **Checker/Approver Flow** | Complete approval workflow for the checker role — currently only the Maker confirmation screen exists. No design for how the checker reviews, approves, or rejects a DCI investment. | In corporate banking, maker-checker is mandatory for transaction authorization. The absence of a checker flow means only half the workflow is designed. | Large Effort |
| **Delegation & Authority Levels** | Configurable approval thresholds (e.g., investments > $500K require additional approval) and delegation for when the primary checker is unavailable. | Standard corporate banking requirement. Without it, investment placement may be blocked when the usual approver is unavailable. | Large Effort |
| **Audit Trail** | Visible history of who created, approved, modified, or cancelled each investment, with timestamps. | Regulatory and internal compliance requirement for corporate banking transactions. Not visible in current design. | Medium Lift |

---

## DCI Risk & Clarity Assessment

### Risk Disclosure
**Rating: INSUFFICIENT** — The product positions DCI as a yield-enhancement opportunity while isolating all risk information in a collapsed FAQ. The landing page hero ("Ready to invest? Turn your foreign currency needs into potential for better returns") and value proposition cards (3 benefits, 0 risks) create a deposit-like expectation. No in-flow risk warnings, no suitability check, no risk acknowledgment before submission. Findings #1, #2, #3.

### Suitability Assessment
**Rating: ABSENT** — No Customer Knowledge Assessment or suitability questionnaire exists in the flow. Any authenticated corporate user can immediately configure and submit a DCI investment regardless of their understanding of structured products, options, or currency risk. This likely does not meet MAS requirements for Specified Investment Products (Notice SFA 04-N12). Finding #3.

### Strike Price Comprehension
**Rating: PARTIAL** — Strike prices are presented with "% from spot" context and indicative yields, which helps experienced investors gauge the risk/reward tradeoff. The ⓘ icon exists but tooltip content is not designed/visible. No definition of "strike price" or explanation of the yield-risk tradeoff appears on the configuration screen. Findings #6, #8.

### Currency Pair Clarity
**Rating: NEEDS IMPROVEMENT** — Base and Alternate currencies are labelled in the pair selector, but the terms are never defined in-context. The reinvestment flow after strike-not-met silently flips the currency pair without explanation. Scenario colour coding (green for Base, peach/orange for Alternate) creates value judgment rather than neutral presentation. Findings #9, #10.

### Yield Presentation
**Rating: NEEDS IMPROVEMENT** — Annualized yield is the sole display format. For short tenors (1 week = 0.125% actual, displayed as 6.50% p.a.), this dramatically inflates perceived returns. Absolute dollar return is shown in Potential Outcomes panel but only after selecting all parameters. "p.a." abbreviation is never expanded. "Indicative" qualifier is unexplained. Findings #5, #12, #24.

### Regulatory Disclosures
**Rating: SIGNIFICANT GAPS** — No suitability assessment, no explicit T&C consent checkbox, no risk acknowledgment step, no cooling-off period notice, no Key Fact Sheet link during the investment flow (only "Download Termsheet" on post-investment details). Product classification as "capital at risk structured investment" is buried in FAQ. Findings #3, #4, #14.

---

## Novice Investor Journey Assessment

A novice corporate treasury user arriving at the DCI landing page encounters a **promotional experience** that reads like a premium deposit product. The hero banner invites them to "invest" with "better returns" and three value cards promise "maximise your investment returns", "flexibility and control", and "great for currency conversion needs". The empty state illustration cheerfully suggests "Start your first Dual Currency Investment and unlock higher potential returns." No risk context appears above the fold.

The FAQ section — the only place where DCI is explained, risks are disclosed, and a worked example is provided — is collapsed at the bottom of the page. A novice who expands it would find comprehensive content: a clear definition, indicative pricing parameters, a payoff table, and risk bullets. But this is passive education — most novice users won't find or read it.

Clicking "Place investment", the novice enters the configuration screen and faces a wall of undefined financial terms: **Tenor** (should be "Investment Period"), **Strike Price** (never defined), **Spot Rate (Indicative)** (unexplained), **Base Currency** and **Alternate Currency** (labelled but undefined). The ⓘ tooltip icons exist next to some terms but no tooltip content is visible in the design. Terminology audit scores novice comprehensibility at approximately **2.5 out of 5**.

The investment amount field shows a broken placeholder ("$0,000.00 USD") for the minimum, eroding trust. The currency selector defaults to "N.A" — a non-standard, confusing initial state.

Strike price selection displays attractive annualized yields (6.30%–6.70%) that dwarf typical deposit rates, but a novice doesn't know that "6.50% p.a." on a 1-month product means ~0.54% actual return. They also don't know that selecting a higher yield increases their probability of receiving the alternate currency — the yield-risk tradeoff is entirely unexplained.

The Potential Outcomes panel uses green (Scenario A / Base Currency) and peach (Scenario B / Alternate Currency), unconsciously framing one outcome as "good" and the other as "bad" — when either could be preferred depending on the user's currency needs.

Account selection asks for three accounts (funding, base settlement, alternate settlement) without explaining why two settlement accounts are needed. The review screen requires extensive scrolling with no sticky CTA. The T&C is a wall of placeholder text with no structure.

At no point does the user encounter: a risk warning, a suitability check, a definition of DCI, or an explicit consent mechanism.

**Novice Journey Score: 3.5 / 10** — The product is not safe for novice use in its current state.

---

## Experienced Investor Efficiency Assessment

For a seasoned treasury professional, the DCI product offers a **competent and efficient** configuration experience. The two-column layout (inputs left, outcomes right) enables real-time impact assessment — changing strike price immediately updates the scenario panels. The strike price radio buttons with yield percentages and "% from spot" context support quick comparison.

The Investment Timeline component is an excellent reusable pattern — four dates (Trade, Start, Expiry, Maturity) with plain-language descriptions, consistently applied across configuration, review, confirmation, and investment details.

The post-investment dashboard is well-designed: Active/Settled tabs with count badges, inline settlement outcome banners with colour-coded status (green check for strike met, orange warning for not met), and a "Reinvest" CTA directly on the settlement banner. The date filter on Settled tab enables historical lookup.

**Friction points for experienced users:**
- **No step progress indicator** — The 3-step flow (Config → Accounts → Review) lacks a stepper, forcing mental tracking of position
- **No rate history** — Strike price selection lacks historical exchange rate context; users must reference external tools
- **No saved configs/templates** — Repeat investors re-enter similar parameters every time
- **No quick reinvest** — Reinvestment requires traversing the full 3-step flow even for identical parameters
- **No explicit consent** — Implicit "By clicking Submit" feels incomplete for a structured product
- **No maker-checker** — Only the Maker confirmation exists; the Checker/Approver flow is undesigned
- **No portfolio analytics** — Multiple investments tracked individually with no aggregate view
- **"Expiring Soon" detail lacks rate context** — Can't see current spot vs strike to gauge likely outcome

**Reinvestment efficiency:** The pre-population of investment amount with previous settlement total (principal + yield) is a smart UX decision. However, the currency pair flip after strike-not-met (e.g., EUR/SGD → SGD/EUR) is silent and potentially confusing even for experienced users. The full 3-step flow for reinvestment could be streamlined.

**Time-to-task estimate:** A seasoned user can configure and submit a standard DCI in ~3-4 minutes. Reinvestment with pre-populated data takes ~2 minutes. Both are acceptable but could be faster with saved templates and quick-reinvest.

**Experienced Journey Score: 6.5 / 10** — Functional and efficient for repeat use, with strong configuration and monitoring design. Elevated by portfolio management features, rate context, and maker-checker workflow completion.

---

## Top 5 Priority Recommendations

### 1. Add In-Flow Risk Disclosure and Mandatory Acknowledgment
- **What to fix:** Insert risk summary card on the Configuration screen and mandatory risk acknowledgment checkboxes on the Review screen.
- **Why it matters:** Users currently commit capital to a capital-at-risk structured product with embedded derivatives without encountering any risk warning. This is a user-safety concern (novice users form deposit-like expectations) and a regulatory compliance risk (MAS requirements for Specified Investment Products). This is the single most impactful change for novice safety.
- **How to fix it:**
  1. Add a collapsible risk summary panel at the top of the Config screen: *"Important: DCI is a structured investment, not a deposit. Your principal may be returned in the alternate currency at maturity. This product is not covered by deposit insurance. Past performance is not indicative of future results."*
  2. On Review screen, replace implicit "By clicking Submit..." text with mandatory checkboxes:
     - *"☐ I have read and agree to the Terms and Conditions"*
     - *"☐ I understand this investment may settle in the alternate currency and my principal is at risk"*
  3. Disable Submit button until both checkboxes are checked.
- **Effort estimate:** Medium Lift (2-3 days)

### 2. Add Suitability Assessment Gate with Product Education
- **What to fix:** Insert a suitability/knowledge check and brief product education before first-time access to the DCI configuration screen.
- **Why it matters:** MAS Notice SFA 04-N12 typically requires a Customer Knowledge Assessment for Specified Investment Products. Beyond compliance, a suitability gate is the strongest novice protection mechanism — it ensures users understand what they're investing in before committing capital.
- **How to fix it:**
  1. First-time users see a brief DCI explainer screen (visual diagram of how DCI works, 2 scenarios illustrated).
  2. 3-4 suitability questions: *"Do you understand that DCI is not a deposit?"*, *"Do you understand your principal may be returned in a different currency?"*, *"Have you invested in structured products before?"*
  3. Correct answers required to proceed. Wrong answers trigger educational content.
  4. For returning users who have passed: annual re-certification or bypass with "I confirm my understanding is current."
- **Effort estimate:** Medium Lift (3-5 days)

### 3. Show Actual Period Return Alongside Annualized Yield
- **What to fix:** Display actual return (both percentage and dollar amount) next to the annualized yield for each strike price option and in the Potential Outcomes panel.
- **Why it matters:** Annualized yield is the primary decision driver but dramatically inflates perceived returns for short tenors. A 1-week DCI at 6.50% p.a. yields ~0.125% actual (~$250 on $200K). Users choosing between DCI and a time deposit need apples-to-apples comparison. This is especially critical for novice users who don't understand annualization.
- **How to fix it:**
  1. Strike price list: "6.50% p.a. ***(~$1,083 for 1 month)***"
  2. Potential Outcomes panel: Show "Yield" row as both p.a. and actual: "+1,083.33 USD (6.50% p.a.)"
  3. On first use, expand "p.a." to "per year" in parentheses.
- **Effort estimate:** Quick Win (1-2 days)

### 4. Design Complete Maker-Checker Workflow
- **What to fix:** Design the full Checker/Approver flow for DCI investments, including approval queue, review screen, approve/reject actions, and delegation settings.
- **Why it matters:** For Singapore corporate banking, maker-checker is a fundamental authorization requirement. Currently only the Maker flow is designed — the Checker experience is completely absent. Without this, the product cannot function in a real corporate banking environment where dual authorization is mandatory.
- **How to fix it:**
  1. **Checker dashboard:** List of pending DCI investments awaiting approval, with key details (amount, pair, yield, submitter).
  2. **Checker review screen:** Read-only version of the investment details with Approve/Reject buttons and comment field.
  3. **Notifications:** Email/push notification to checker when new investment is pending.
  4. **Delegation:** Allow checker to delegate approval authority when unavailable.
  5. **Authority levels:** Configurable thresholds (e.g., > $500K requires senior approval).
- **Effort estimate:** Large Effort (1-2 weeks)

### 5. Add Step Progress Indicator and Contextual Help Across Flow
- **What to fix:** Add a horizontal stepper bar across all investment flow steps and ensure ⓘ tooltip content is designed and functional.
- **Why it matters:** The absence of a stepper creates uncertainty about flow length (especially for novice users), and the missing tooltip content means the ⓘ icons are visual promises of help that are never delivered. Together, these create a flow that feels longer and more confusing than it needs to be.
- **How to fix it:**
  1. Add persistent stepper: "1. Configure Investment → 2. Select Accounts → 3. Review & Submit"
  2. Design tooltip content for every ⓘ icon:
     - Currency Pair: "The two currencies involved in your DCI. The base currency is what you invest; the alternate is what you may receive at maturity."
     - Tenor: "How long your money will be invested. Longer tenors typically offer higher yields."
     - Strike Price: "The exchange rate threshold that determines which currency you receive at maturity."
     - Potential Outcomes: "Two possible scenarios based on the exchange rate at expiry compared to your chosen strike price."
  3. Add contextual helper text on Account Selection explaining why two settlement accounts are needed.
- **Effort estimate:** Quick Win (2-3 days)

---

## Design System & Consistency Notes

### Strengths
- **Button pairing convention** — Back (outlined, left) + Primary (filled, right) applied consistently across all multi-step flows. Well-established pattern.
- **Investment Timeline stepper** — Reusable component with dot markers, connecting lines, and date labels. Consistent across config, review, confirmation, and detail screens. Plain-language helper text on each date.
- **Label-value pair layout** — Grey label above, bold value below, two-column grid. Identically applied across review, detail, and parameter screens.
- **Scenario A/B panel pattern** — Consistent structure (badge, condition, settlement currency, amounts) reused across config, review, confirmation, and details screens.
- **Status badge system** — Pill-shaped badges with semantic colours: green "Active", orange "Expiring soon", blue "Awaiting Settlement", grey "Settled". Consistent shape and sizing.
- **Settlement outcome banners** — Inline expandable banners on portfolio list with green check (strike met) and orange triangle (not met). Distinctive, informative, and well-integrated into the table layout.

### Inconsistencies
1. **Primary button colour variance:** OCBC red used for all CTAs (Next, Submit, Place Investment), but the SAO account application and OMC gate screen may use different button styles. The "Add" buttons on the SAO landing are grey (disabled state) vs the active teal "Add" on Multi-Currency Account.
2. **Navigation label inconsistency:** "FX and Investment" (config, landing) vs "FX and Treasury" (investment details) vs "FX and treasury" (lowercase, OMC gate). Three variants of the same navigation item across one product flow.
3. **Heading case conventions:** Mix of ALL CAPS letter-spaced ("DUAL CURRENCY INVESTMENT", "REVIEW", "INVESTMENT DETAILS") and title case ("Investment Parameters", "Potential Outcomes", "Settlement Outcome"). No clear system governing when to use which.
4. **Currency selector default state:** "N.A" with a generic flag vs a meaningful default or "Select Currency" placeholder. Non-standard and confusing.
5. **Minimum amount placeholder:** "$0,000.00 USD" appears to be a template placeholder never replaced with actual data. Appears on both empty and partially-filled states.
6. **Scenario colour semantics:** Green for "Base Currency" / Scenario A and peach/orange for "Alternate Currency" / Scenario B creates unintentional value judgment.

### Components to Standardise / Create
- **Risk disclaimer card** — Needed on Config screen; should be a reusable alert component with consistent styling (icon + text + optional dismiss).
- **Tooltip content** — ⓘ icons exist but tooltip content isn't designed. Need a tooltip component with financial term definitions.
- **Step progress indicator** — Missing entirely from the multi-step flow. Should be a reusable stepper component.
- **Consent checkbox** — Needed on Review screen; standard checkbox + label pattern with mandatory validation.
- **Contextual helper panel** — Right-side information panel pattern for Account Selection and other sparse screens.

---

## What's Working Well

1. **Two-column input/outcome layout on the configuration screen** creates an exceptional cause-and-effect relationship. Users can see how their parameter choices (strike price, tenor, currency pair) immediately affect the potential outcomes in the right panel. This is a best-in-class pattern for decision-support interfaces in financial products.

2. **Investment Timeline component** is a standout reusable pattern. Four dates (Trade, Start, Expiry, Maturity) with plain-language helper text ("When funds are deducted and investment starts") successfully translate financial jargon into actionable context. Consistently applied across all flow stages.

3. **Post-investment portfolio dashboard** with Active/Settled tabs, count badges, and inline settlement outcome banners is well-designed for ongoing portfolio management. The expandable settlement banners (green check for strike met, orange warning for not met) provide immediate status comprehension without navigating to detail screens.

4. **Reinvestment pre-population** automatically sets the investment amount to the previous settlement total (principal + yield), reducing data entry and creating a natural reinvestment path. Smart UX decision for returning investors.

5. **Settlement outcome design on investment details screens** effectively differentiates between strike met (green banner with check icon + explanatory text) and strike not met (orange banner with warning icon + conversion explanation). The settlement breakdown table (Principal + Yield = Total Settlement) is clear, scannable, and well-structured. Users can quickly understand what happened and what they'll receive.

6. **Currency selector dropdown design** with country flags, full currency names, and ISO codes provides excellent visual recognition. The search functionality enables quick lookup for users with many currency options. The selected state with checkmark is clear.

7. **FAQ content quality** — While poorly positioned (buried, collapsed), the actual FAQ content is excellent: comprehensive DCI explanation, worked example with indicative pricing parameters, payoff table, risk bullets, and milestone date definitions. If surfaced contextually throughout the flow, this content would dramatically improve novice comprehension.

---

## Suggested Next Audit Scope

1. **Maker-Checker / Approval Flow** — The Checker/Approver experience is completely undesigned. For a corporate banking product, this is the other half of the transaction flow and is critical for production readiness.

2. **Mobile / Responsive Breakpoints** — This audit covered desktop only. The two-column config layout, long review page, scenario panels, and dense portfolio table will require significant responsive adaptation for tablet/mobile viewports.

3. **FX Online Product Flow** — The sibling product under "FX and Investment" navigation. Likely shares design system components and may have similar risk disclosure gaps.

4. **Account Application (SAO) Full Flow** — Only the landing screen was visible. The full multi-step account opening flow should be audited for form design, document upload, and compliance patterns, especially since DCI users are redirected here when they lack a Multi-Currency Account.

5. **Error States & Edge Cases** — No error states are visible in the current designs: What happens when rate expires during review? What if account balance is insufficient? What if the system is unavailable? What if the user's session times out mid-flow? These critical states need to be designed and audited.
