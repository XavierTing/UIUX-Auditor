# UI/UX AUDIT REPORT: Precious Metal (Buy / Sell flow)

**Audit Date:** 2026-05-04
**Platform:** Web Desktop (OCBC Velocity — Business Banking, ≥1024 px)
**Auditor Persona:** Senior UX Auditor & Design Systems Expert (NN/g lens)
**Flow Scope:** Pre-Investment Landing → Buy / Sell forms → Review → Acknowledgement → Email confirmation → Post-Investment Landing → Order History → Price Alert (14 screens captured from Figma node `396:26081`)
**Source:** Figma file `pJuwdSGBCJvVtx6i77ytzM` ("Precious Metal")
**Domain Lens:** Banking / Investment (regulated)
**Personas:**
- **Novice retail investor** — first-time precious-metal buyer; needs plain language, risk clarity, fee transparency
- **Seasoned investor** — already understands spot price, premium, spread, allocated/unallocated; needs efficiency, transparent pricing, drill-down to execution detail

---

## EXECUTIVE SUMMARY

The Precious Metal flow is **visually polished and functionally complete for a happy path**, but it is **materially under-disclosed for a regulated investment product**. The most consequential issues are not aesthetic — they are economic and regulatory. Pricing is opaque (a single "Indicative Price" hides the bid/ask spread, fee, and FX rate; a *different* indicative price gets executed than the one shown on the chart), risk is invisible until it is too late (no risk panel, no Key Fact Sheet, no past-performance disclaimer near the chart, no allocated-vs-unallocated custody statement), and the entire failure / pending / maker-checker state matrix is undesigned despite a corporate-banking context that strongly implies maker-checker workflow.

Visually the product reads as conventional and trustworthy, but trust signals fail closer inspection: the disclaimer on the Review screen is plain grey body text (visually weaker than the marketing chip beside it), T&C consent is passive copy not a checkbox, and the disclaimer references a button label ("Submit") that doesn't exist on the page (the actual button reads "Confirm Buy/Sell Order"). Buy and Sell paths have visibly drifted (different field-labels for the same value, "Show available balance" only present on one path), and Order History is a dead-end (rows are not clickable, no order-detail screen exists).

**Per-persona scores:**
- **Novice:** **3.5 / 10** — opaque pricing, hidden risk, ambiguous terminology will lead to misinterpretation and complaint.
- **Seasoned:** **5.0 / 10** — fast and clean to operate, but missing the disclosure surface (bid/ask, fees, custody, status, drill-down) seasoned investors expect.
- **Combined:** **4.0 / 10** — adequate scaffolding, critical gaps in the regulated-domain disclosures and workflow integrity that must be closed before launch.

**Overall UX Health Score: 4.0 / 10** — *do not ship until the four critical pricing-transparency, risk-disclosure, maker-checker, and missing-state findings are resolved.*

---

## FINDINGS TABLE

| # | Screen | Dimension | Severity | Finding | Novice Impact | Seasoned Impact | Recommendation |
|---|---|---|---|---|---|---|---|
| 1 | Buy Review | Banking-domain — Pricing | 🔴 CRITICAL | Two distinct prices share the same label "Indicative Price" — chart shows 6,581.85 SGD/oz, executed Buy uses 6,128.50 (30,642.50 ÷ 5). | Will believe the headline = what they pay/receive; will feel misled when the executed price appears on the order history. | Recognises the gap as undisclosed spread/markup but cannot reconcile it without a breakdown. | Rename: "Live indicative price" on the chart vs "Executed price" on Review/Ack/Order History. Show both with delta on Review. |
| 2 | Buy Form (Filled) | Banking-domain — Pricing | 🔴 CRITICAL | No bid/ask spread anywhere — Buy and Sell transact off the same single number; spread, fee, and FX are all hidden inside one figure. | Cannot evaluate cost-of-trading. | Major credibility issue; assumes worst-case hidden spread; trades elsewhere. | Show a Buy quote and a Sell quote on every chart and form header. On Review, break out unit price × qty = subtotal, ± fee, ± FX, = total. |
| 3 | Buy Review | Banking-domain — Pricing | 🔴 CRITICAL | No fee / commission line at any commit point. "Fees and charges" sits in a *collapsed* FAQ on the landing — not point-of-sale disclosure. | Discovers fees retrospectively in statement; complaint risk. | Cannot model net P&L. | Add explicit "Fees & charges" row to Review summary, even if fee = 0 (state "0.00 SGD — included in price" if baked in). Disclose GST/VAT same row. |
| 4 | Buy Form (Filled) | 9. Trust & Emotional | 🔴 CRITICAL | No risk warning surfaced before commitment — risk content is in a collapsed "Things to look out for" FAQ at the bottom of the landing. | May invest without understanding precious metals are not capital-guaranteed; regulatory and complaint risk. | Notes asymmetry between marketing prominence and risk prominence; questions the product's regulatory posture. | Persistent risk panel above the chart on Buy/Sell forms: "Precious metal prices can fall as well as rise. Past performance is not indicative of future results. Holdings are not SDIC-insured." Plus KFS link. |
| 5 | Order History | 7. Feedback & System Status | 🔴 CRITICAL | Global header shows a "Tasks and Statuses" pill (implies maker-checker), yet no Submitted / Pending Approval / Awaiting Settlement / Rejected state designed in any flow. | If user is the maker, won't know trade is awaiting checker — may re-submit. | Same — ops will not trust a flow that hides workflow state. | Design 4 maker-checker states (Submitted / Pending Approval / Approved-Pending Settlement / Rejected) as Order History row statuses and detail-screen statuses. Ack should say "submitted for approval" when applicable. |
| 6 | Buy Form (Empty) | 5. Component & Interaction | 🔴 CRITICAL | No error / inline-validation, insufficient-balance, market-closed, price-stale, network-failure, or order-rejected states designed in any of 14 frames. | Hits raw browser-default errors or dead-ends; drops the trade or calls support. | Will not trust a trading product whose failure modes are invisible. | Design the full state matrix before launch (field-level + page-level). Each state needs a recovery action. |
| 7 | Pre-Investment Landing | 8. Cognitive Load & Clarity | 🟠 HIGH | "Indicative" — the most consequential word in the product — is never explained inline. | Reads "Indicative price" as "current price"; doesn't realise executed price will differ. | Understands the term but expects the bank to define it for compliance. | Inline info-icon next to every "Indicative" label opening a tooltip: "For reference only. The price you transact at is set at the moment of execution and may differ." |
| 8 | Buy Review | 9. Trust & Emotional | 🟠 HIGH | T&C consent is passive copy ("By clicking Submit you confirm…"), not an explicit checkbox. No scroll-to-bottom requirement; no in-flow link to full T&Cs. | Implicit consent — may not realise they are agreeing. | Below industry standard for regulated investment. | Replace with explicit unchecked checkbox: "☐ I have read and agree to the Terms and Conditions and the Key Fact Sheet". Disable Confirm CTA until checked. |
| 9 | Buy Review | Banking-domain — Risk | 🟠 HIGH | Disclaimer says "By clicking 'Submit'…" but the actual button reads "Confirm Buy Order" / "Confirm Sell Order". | Mild confusion; may wonder if there's a separate Submit step. | Reads as careless copy work; undermines trust. | Either rewrite disclaimer to reference the actual button label, or rename the button to "Submit". Keep consistent. |
| 10 | Buy Review | Banking-domain — Risk | 🟠 HIGH | No Key Fact Sheet (KFS) link, no suitability statement, no product-knowledge gate anywhere in the flow. | Direct compliance risk — has not been shown KFS before commitment. | Will expect KFS access on every regulated-investment screen. | Add KFS link to Review and Pre-Investment Landing. For first-time precious-metal investors, gate Confirm behind a 5-question suitability check. |
| 11 | Pre-Investment Landing | Banking-domain — Risk | 🟠 HIGH | Custody model (allocated vs unallocated) never disclosed. Tagline implies paper bullion, but bank balance-sheet exposure model is silent. SDIC status not stated. | May assume holding is physical or insured — major mis-selling risk. | Will demand to know allocated vs unallocated before opening a position. | Add "Custody and Protection" section: "Your holding is unallocated paper bullion — a contractual claim on OCBC, not segregated physical metal. Holdings are not SDIC-protected." |
| 12 | Buy Review | Banking-domain — Pricing | 🟠 HIGH | GST / tax treatment never mentioned at point of sale. SG IPM gold (≥99.5%) is GST-exempt; silver and non-IPM gold attract GST. | Won't know whether displayed price is GST-inclusive. | Will assume worst and trade elsewhere. | Add "GST treatment" line to Review: "GST: 0.00 SGD (IPM gold is GST-exempt)" or "+9% GST (XX SGD)" as appropriate. Same line in email. |
| 13 | Order History | 1. IA & Navigation | 🟠 HIGH | Order History rows are not clickable — no row chevron, no "View" action, no order-detail screen exists. | Cannot retrieve their own trade record beyond visible columns. | Cannot pull termsheet or execution detail for reconciliation/audit. | Make every row clickable to an Order Detail screen: full economics (price, qty, fee, FX, GST, total), settlement status, termsheet PDF link, maker/checker history. |
| 14 | Order History | 7. Feedback & System Status | 🟠 HIGH | No Status column on Order History — no way to distinguish filled / pending / cancelled / awaiting-approval / rejected. | Cannot tell if a recent order is settled or in flight. | Major operational gap — corp ops needs status to reconcile. | Add STATUS column with coloured pills (Filled / Pending Approval / Awaiting Settlement / Cancelled / Rejected); make filterable. |
| 15 | Buy Review | 4. Colour & Contrast | 🟠 HIGH | Risk / T&C disclaimer is plain ~12 px grey body text — no icon, no border, no tint. Visually weaker than the Buy chip beside it. | Eye skips the disclaimer entirely. | Reads it but notes weak treatment as below regulatory norms. | Wrap disclaimer in a tinted panel with left border (amber) + icon, immediately above Confirm CTA. Plus checkbox from #8. |
| 16 | Order History | 3. Typography & Readability | 🟠 HIGH | Numeric columns (QUANTITY, INDICATIVE PRICE, TOTAL) are left-aligned with proportional (not tabular) figures — decimals don't align vertically. | Readable but slower to scan. | Recognised as substandard finance-table styling. | Right-align all numeric columns; use tabular lining figures (`font-variant-numeric: tabular-nums`). Apply to Holdings Details and price tiles too. |
| 17 | Buy Form (Filled) | 2. Visual Hierarchy | 🟠 HIGH | Primary CTAs (`Review Buy Order`, `Confirm Buy Order`, `Create Alert`) are dark slate — the visually quietest element on the screen. | May not realise where to submit; eye lingers on the chart. | Less harmful but still slows action surface. | Promote primary CTA to a brand-coloured filled button (OCBC red or brand-blue). Use slate for secondary. |
| 18 | Buy Form (Filled) | Banking-domain — Pricing | 🟠 HIGH | No price-validity window communicated — slippage between Review and Confirm is invisible. | Will be surprised when executed price differs from the form price. | Expects a "quote held for X seconds" countdown. | Either lock the quote on Review with a visible countdown ("Price held for 30s"), or re-quote on Confirm with explicit "Price has updated — confirm new price?" interrupt. |
| 19 | Buy Form (Filled) | Banking-domain — Risk | 🟠 HIGH | No "Past performance is not indicative of future results" disclaimer near any price chart (Buy, Sell, Price Alert). | May extrapolate past trend into expected future. | Recognised as compliance gap. | Add boilerplate immediately under every chart. |
| 20 | Buy Form (Filled) | 2. Visual Hierarchy | 🟡 MEDIUM | Eye lands on the chart card on the left first — the form on the right (the actual task) is visually quieter than the chart. | Wastes attention before realising the form is the task. | Mild inefficiency. | Reduce chart visual weight (smaller header, less saturated chart fill); elevate the form (subtle shadow / accent border). Or invert columns. |
| 21 | Sell Form (Filled) | 8. Cognitive Load & Clarity | 🟡 MEDIUM | Buy = "Investment Amount", Sell = "Market Value", Sell email = "Investment Amount". Same value, three labels across the journey. | Cognitive load — re-learn labels per step. | Reads as careless copy work; questions whether values mean the same thing. | Pick one label — recommend "Cost (SGD)" for Buy and "Proceeds (SGD)" for Sell. Use the same in-app and in-email. |
| 22 | Buy Form (Filled) | 5. Component & Interaction | 🟡 MEDIUM | Swap icon between Investment Amount and Quantity to Buy is unlabelled — bi-directional auto-calc is implicit. | May type both fields manually and produce inconsistent values. | Will infer the behaviour quickly. | Tooltip on the swap icon: "Quantity and amount are linked — fill either, the other will calculate." Or remove the swap and auto-fill on blur. |
| 23 | Sell Form (Filled) | 6. Forms & Data Entry | 🟡 MEDIUM | "Show available balance" link appears on filled Buy form but not on empty Buy form, and absent from Sell form entirely. | Cannot quickly check balance/holding before deciding amount. | Same — and notes path inconsistency. | Show "Available balance: X SGD" inline under Credit Account on Buy form (empty + filled). Show "Available holding: X ounces" inline on Sell form. Mirrored. |
| 24 | Sell Form (Empty) | 6. Forms & Data Entry | 🟡 MEDIUM | Min/max guardrails asymmetric — Buy shows Min only; Sell shows Max only. | Trial-and-error into validation errors. | Mild annoyance — expects both bounds visible. | Show both Min and Max for every numeric field on both forms. Format: "Min 0.01 oz · Max 25.86 oz". |

---

## TOP 5 PRIORITY RECOMMENDATIONS

### 1. Make pricing transparent end-to-end

- **What to fix:** Today, a single "Indicative Price" hides the spread, fee, FX, and GST. The user sees one number on the chart (6,581.85 SGD/oz) and is silently transacted at a different one (6,128.50 SGD/oz on the order history). Buy and Sell trade off the same number.
- **Why it matters:** This is the single biggest mis-sell risk in the product. Novices feel deceived; seasoned investors trade elsewhere; compliance is exposed. (Findings #1, #2, #3, #12, #18.)
- **How to fix it:** On every chart, show **two** quotes: "Buy at X.XX SGD · Sell at Y.YY SGD" with the spread visible. On Review, break the cost into a 5-line table: `Unit price × Quantity = Subtotal | ± Fee | ± FX adjustment | ± GST | = Total`. Lock the quote on Review with a visible countdown timer ("Quote valid for 30s — refresh"). Rename the chart price "Live indicative" and the executed price "Executed price" so they cannot be confused.
- **Effort estimate:** **Large Effort** — pricing service must publish bid/ask separately; Review template must add the breakdown; quote-lock logic is new.

### 2. Surface risk and disclosure at decision time, not in a collapsed FAQ

- **What to fix:** All risk content lives inside a collapsed FAQ ("Things to look out for") at the bottom of the landing. The Review-screen disclaimer is grey body copy with no border or icon. There is no Key Fact Sheet, no suitability gate, no past-performance boilerplate near charts, and no statement of custody (allocated vs unallocated) or SDIC coverage.
- **Why it matters:** Regulated-investment products require risk visibility before commitment. Today's design buries every signal. (Findings #4, #8, #10, #11, #15, #19.)
- **How to fix it:** Add a persistent **Risk panel** above every chart on Buy/Sell forms with three lines: *"Precious metal prices can fall as well as rise. Past performance is not indicative of future results. Your holding is unallocated paper bullion — a contractual claim on OCBC, not SDIC-insured."* On the Review screen, replace passive consent copy with an explicit checkbox: *"☐ I have read and agree to the Terms and Conditions and the Key Fact Sheet"*; disable Confirm until both are checked; render the disclaimer in a tinted amber panel with an icon. Add a KFS link on the landing card and on Review.
- **Effort estimate:** **Medium Lift** — content + new component, but no new pricing logic.

### 3. Design the missing state matrix and the maker-checker workflow

- **What to fix:** Across 14 frames, no error, validation, insufficient-balance, market-closed, price-stale, network-failure, or order-rejected state exists. The global header shows "Tasks and Statuses" implying maker-checker — yet no Submitted / Pending Approval / Awaiting Settlement / Rejected state is designed.
- **Why it matters:** A real-money trading flow with no failure modes is a launch blocker. For corporate banking, maker-checker is the *fundamental* operational pattern. (Findings #5, #6, #14.)
- **How to fix it:** Catalogue the full state matrix and design each one: field-level validation, page-level errors (insufficient balance, insufficient holding, market closed, price stale > N seconds, network/API failure), order-rejected with reason. Add four maker-checker states (Submitted / Pending Approval / Approved-Pending Settlement / Rejected) — surfaced as row badges on Order History, as the acknowledgement variant after Confirm ("Order submitted for approval"), and as a status row on the order-detail screen.
- **Effort estimate:** **Large Effort** — net-new screens and a workflow integration.

### 4. Make Order History the single source of truth — and make rows drillable

- **What to fix:** Today's Order History is a static list. Rows are not clickable, there is no Status column, and no order-detail screen exists in the deck.
- **Why it matters:** Corporate users need to retrieve termsheets, reconcile statements, and audit trades. Without drill-down, the product has no audit trail. (Findings #13, #14.)
- **How to fix it:** Add a Status column with coloured pills (Filled / Pending Approval / Awaiting Settlement / Cancelled / Rejected). Make every row clickable to an Order Detail screen showing the full economic breakdown (price, qty, fee, FX, GST, total), settlement status, termsheet PDF download, and maker/checker history. Right-align all numeric columns and use tabular figures.
- **Effort estimate:** **Medium Lift** — Order Detail screen is new; rest is incremental.

### 5. Reconcile Buy and Sell — same value, same name, same component

- **What to fix:** Buy form labels the SGD field "Investment Amount"; Sell form calls the same field "Market Value"; the Sell email reverts to "Investment Amount". "Show available balance" appears on the Buy form (filled state only) but is missing from the empty state and from the Sell form. Min/max guardrails differ asymmetrically (Buy: min only; Sell: max only).
- **Why it matters:** Buy and Sell are mirrored journeys for the same user; inconsistencies erode trust and make muscle memory transfer poorly. (Findings #21, #23, #24.)
- **How to fix it:** Adopt one label each per direction — "Cost (SGD)" for Buy and "Proceeds (SGD)" for Sell — and use them in-app and in-email. Add an "Available balance / Available holding" inline read on both empty and filled states for both forms (mirrored component). Show both Min and Max on every numeric field on both forms.
- **Effort estimate:** **Quick Win** — copy and component-prop changes, no logic.

---

## DESIGN SYSTEM & CONSISTENCY NOTES

- **Inconsistent terminology for the same value.** "Investment Amount" (Buy) vs "Market Value" (Sell) vs "Investment Amount" (Sell email) — reconcile to a single label per direction.
- **Buy/Sell path drift.** "Show available balance" link present on Buy (filled) only; entirely absent on Sell. Symmetry is broken.
- **Two indicative prices, one label.** Live chart price and executed-trade price both appear under the heading "Indicative Price" — this is a labelling failure that the design system should explicitly disambiguate (different token / different colour / different prefix).
- **Underdesigned chip.** Buy/Sell pills on Order History rows and on the Review header are coloured text only — no padding, no pill background. Industry-standard convention is a tinted pill chip; bring this into the component library.
- **Numeric column alignment regression.** Numeric columns are left-aligned and use proportional figures. The design system should specify `text-align: right` and `font-variant-numeric: tabular-nums` for any numeric-typed table cell.
- **Layout anchoring drift.** Form/landing screens are left-anchored at max-width; Review and Acknowledgement are centred. Pick one.
- **Capitalisation drift in nav.** "Pay and transfer" (sentence case) on the Order History header vs "Pay and Transfer" (title case) on every other frame.
- **Y-axis tick rounding.** Price chart shows ticks like `6,666.65 / 6,578.83 / 6,491.00` — non-round values. Snap to round increments (`6,500 / 6,550 / 6,600 / 6,650`).
- **Two "pick one" patterns within the same screen family.** Time-range selector uses pill chips; section nav uses underlined tabs. Consolidate.
- **Empty `Settlement Date` quadrant.** Right column of every Buy/Sell form has ~200 px dead vertical space below `Settlement Date` — wasted canvas; could host a "What you'll pay / what you'll receive" calculator block.
- **CTA muting.** Primary CTAs are dark slate while the brand colour is reserved for the logo and Sell-toggle state. The product never feels like an OCBC product on the Buy path.

---

## DOMAIN-SPECIFIC ASSESSMENT — Banking / Investment

| Lens | Status | Notes |
|---|---|---|
| Risk presented with **equal weight** to upside | ❌ Missing | Gain in green is prominent (price tile, holdings P&L); no equivalent volatility / downside framing. |
| Risk warning **before** commitment | ❌ Missing | Risk content sits in a *collapsed* FAQ at the bottom of the landing only. |
| Past-performance disclaimer near charts | ❌ Missing | No boilerplate on any chart. |
| Key Fact Sheet (KFS) link | ❌ Missing | Not linked anywhere in 14 frames. |
| Suitability / product-knowledge gate | ❌ Missing | No 5-question check, no first-time gating. |
| T&C **checkbox** before Confirm | ❌ Missing | Passive consent copy only. |
| Bid / ask spread visible | ❌ Missing | One number for both Buy and Sell. |
| Fee / commission line at commit | ❌ Missing | Mentioned only in collapsed FAQ. |
| FX rate disclosed at commit | ❌ Missing | No explicit FX line on Buy/Sell Review. |
| GST / tax disclosed at commit | ❌ Missing | Silver vs IPM gold treatment not shown. |
| Custody (allocated/unallocated) disclosed | ❌ Missing | Tagline implies unallocated; never stated explicitly. |
| SDIC / deposit-protection statement | ❌ Missing | Holdings are not SDIC-protected; user is not told. |
| Settlement window / cancellability | 🟡 Partial | Settlement date shown ("28 Apr 2026 (Today)") but cancellability not stated. |
| Price-validity / quote-held window | ❌ Missing | No countdown, no re-quote interrupt. |
| Maker-checker / pending-approval state | ❌ Missing | Implied by global "Tasks and Statuses" pill, never designed. |

**Domain assessment:** the product is **not yet ready for a regulated launch**. Every fundamental disclosure (price, fee, FX, GST, custody, risk, suitability, deposit-protection) is absent or buried. This is the single biggest finding cluster of the audit and must be resolved holistically — not screen-by-screen.

---

## NOVICE INVESTOR JOURNEY ASSESSMENT

A first-time precious-metal buyer lands on the page, sees Gold at 6,581.85 with a green +2.80% one-day move, clicks "Trade Gold", types "5 ounces" into the form, ignores the "Indicative" word (it doesn't sound load-bearing), arrives at Review, glances past the grey 12-px disclaimer, clicks Confirm Buy Order, and gets a green-tick "filled successfully" celebration. They leave with the impression that they paid the price they saw. When the executed price (6,128.50, on the order history) appears in their statement they will feel deceived. They will not have read the FAQ. They will not have seen a KFS, a fee, a custody statement, or a "past performance" disclaimer. This is not a regulatory-compliant journey. **Score: 3.5 / 10.**

## SEASONED INVESTOR EFFICIENCY ASSESSMENT

A seasoned investor will execute the trade quickly — the form is short, the steps are minimal, and the acknowledgement is fast. But they will do it *with reservations*: they cannot see the bid/ask, cannot see the fee, cannot retrieve the termsheet from the order history, cannot drill into an individual trade for reconciliation, and have no maker-checker visibility. They will make small, exploratory trades to understand the spread, then move volume to a more transparent venue. The product feels like a *demo* of a precious-metal trading product, not the production article. **Score: 5.0 / 10.**

---

## ANNOTATED SCREENSHOTS

The annotated screenshots below pin every finding to its on-screen location. Severity colours: 🔴 Critical · 🟠 High · 🟡 Medium · 🟢 Low.

- **Pre-Investment Landing** — markers #7, #11
- **Buy Form (Empty)** — marker #6
- **Buy Form (Filled)** — markers #2, #4, #17, #18, #19, #20, #22
- **Buy Review** — markers #1, #3, #8, #9, #10, #12, #15
- **Sell Form (Empty)** — marker #24
- **Sell Form (Filled)** — markers #21, #23
- **Order History Dashboard** — markers #5, #13, #14, #16

(See `report.html` for the rendered annotated views with side-by-side findings and connector lines.)

---

## WHAT'S WORKING WELL

1. **Conventional Buy/Sell colour mapping is followed.** Buy = green, Sell = red, gain = green up-arrow, loss = red down-arrow. Internally consistent and matches Western finance convention. Helps both personas orient quickly.
2. **Acknowledgement screens are clean and emotionally well-pitched.** Green check + concise success message + drill-back-to-overview link + drill-into-order CTA is the right pattern; avoids over-celebration of what is in fact a routine financial transaction.
3. **Email confirmations are well-structured and tonally appropriate.** Subject lines clearly action-specific ("Your Gold (XAU) buy order is confirmed"), order details are complete, contact paths included. Good corporate-banking voice.
4. **Single design system and 8-px spacing scale, applied consistently.** Card, button, input, chip components are coherent across all 14 frames. Spacing scale is the same everywhere. This is a strong foundation to layer the disclosure improvements onto.
5. **Price Alert form is simple and well-considered.** "Rise Above / Falls Below" is plain language; quick-set chips (+2 / +5 / +10 / +20 %) are a thoughtful efficiency aid; expiry options ("Until triggered / 1 Week / 1 Month") are correctly scoped.

---

## SUGGESTED NEXT AUDIT SCOPE

1. **Maker-checker / approval flow** — once designed, audit it as a standalone flow with checker as a third persona.
2. **Order Detail / termsheet retrieval flow** — once the screen exists.
3. **Mobile (responsive) audit** — same flow on mobile-web. Touch targets, density, and the chart card will all behave very differently below 768 px.
4. **Edge-case state audit** — once error / loading / market-closed / insufficient-balance / order-rejected screens are designed.
5. **First-time-investor onboarding & suitability** — the gate before a novice's first precious-metal trade is its own UX problem worth a dedicated audit.

---

*End of audit report.*
