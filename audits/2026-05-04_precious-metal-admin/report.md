# UI/UX AUDIT REPORT: Precious Metal — Account-Creation, Cross-Currency Sell & Acknowledgement Variants

**Audit Date:** 2026-05-04
**Platform:** Web Desktop (OCBC Velocity — Business Banking, ≥1024 px)
**Auditor Persona:** Senior UX Auditor & Design Systems Expert (NN/g lens)
**Flow Scope:** Figma node `693:15517` — 14 screens captured: Overview (empty + populated), Buy form (new-account variant), Buy form (existing-account variant), Sell form (insufficient holdings + cross-currency), Buy/Sell review (3 variants), Acknowledgement (3 variants including new-account-opened), Email confirmation (Buy + Sell).
**Source:** Figma file `pJuwdSGBCJvVtx6i77ytzM` ("Precious Metal")
**Domain Lens:** Banking / Investment (regulated, corporate customer)
**Personas:**
- **Novice precious-metal investor (corporate customer)** — first time buying paper bullion through their company account; needs plain-language, fee/risk clarity, certainty about what they are committing to.
- **Experienced precious-metal investor (corporate customer)** — already understands spot/indicative/spread; needs transparent execution price, FX rate visibility, status visibility, audit trail.

---

## EXECUTIVE SUMMARY

The Figma frame names in this section (`Day 1 - Add/delete users`, `Renew landing - uploaded file`) are template/working titles that do **not** describe the actual content. The 14 captured frames are in fact a **variant set of the Precious Metals Buy/Sell trade flow** — with genuinely new content for (a) opening a Precious Metals account on a customer's first buy, (b) selling XAU against a USD credit account (cross-currency), (c) an insufficient-holdings warning on Sell, and (d) an acknowledgement variant that confirms both the trade and the new account in a single screen. The audit reports what is in the pixels.

The dominant problem cluster is **build readiness**: literal CMS placeholder tokens (`[Precious Metal Account]`, `[paper gold]`, `[Esolutions Alpha Pte Ltd]`) and email merge tokens (`<Salutation>`, `<Surname>`, etc) appear unresolved in production-feeling screens — and on the new-account-opened acknowledgement, the entity name is `Esolutions Beta Pte Ltd` while the session header is `Esolutions Alpha Pte Ltd`. Any one of these would erode trust on a regulated investment commit; all three together cannot ship.

The **second cluster is pricing transparency**. Cross-currency Sell (XAU → USD) is shown with no FX rate, no markup, and no timing — the customer commits to a USD figure with no idea how the FX leg is priced. The on-screen "Indicative" price is never reconciled with an "Executed" price on the acknowledgement, so the user never sees what they actually paid. Terms and Conditions are referenced in the commit disclaimer but not hyperlinked.

The **third cluster is workflow integrity**. The global header carries a `Tasks and Statuses` pill with a red-dot indicator on every screen — strongly implying a maker-checker queue — but no pending-approval, awaiting-checker, or rejected-by-checker state is designed anywhere. The acknowledgement copy says "filled successfully", treating the commit as terminal, which would mislead novices in any flow that actually requires a second-eye approval. The Recent orders table has no Status column.

**Per-persona scores:**
- **Novice (corporate customer):** **4.0 / 10** — opaque pricing, buried risk, unresolved placeholders, and "filled successfully" copy on a possibly-not-yet-final order will mislead and frustrate.
- **Experienced (corporate customer):** **4.5 / 10** — flow is fast and clean operationally, but the cross-currency FX gap, missing T&C link, missing executed-price disclosure, and absent status/audit-trail surfaces will be flagged by treasury/compliance.
- **Combined:** **4.0 / 10** — adequate scaffolding, critical build and disclosure gaps that must be closed before launch.

**Overall UX Health Score: 4.0 / 10** — *do not ship until the four critical build-readiness findings (placeholders, merge tokens, entity mismatch) and the four critical pricing/regulatory findings (FX rate, executed price, T&C link, risk disclosure) are resolved.*

---

## FINDINGS TABLE

| # | Screen | Dimension | Severity | Finding | Novice Impact | Experienced Impact | Recommendation |
|---|---|---|---|---|---|---|---|
| 1 | Buy Form (new-account) | 9. Trust & Emotional | 🔴 CRITICAL | Unresolved CMS placeholders (`[Precious Metal Account]`, `[paper gold]`, `[Esolutions Alpha Pte Ltd]`) leak as literal UI copy on the Buy form and the Review banner. | Confidence in tooling drops at the moment of commit. | Will not commit a trade against UI that shows bracketed tokens. | Resolve every `[…]` token before launch; add a build-time lint that fails on any visible bracketed placeholder. |
| 2 | Email — Buy confirmation | 9. Trust & Emotional | 🔴 CRITICAL | Email templates ship with unresolved merge tokens `<Salutation> <Surname>`, `<Name>`, `<Designation/rank>`, `<Department name>`. | Reads `Dear <Salutation> <Surname>` as phishing or a system error. | Compliance requires fail-closed personalisation. | Personalise all tokens; fail-closed if any remains; render `Dear Customer` fallback when no personal name is available. |
| 3 | Buy Ack — account-opened | 9. Trust & Emotional | 🔴 CRITICAL | Entity mismatch: session header is `ESOLUTIONS ALPHA PTE LTD` but the "account has been opened" panel attributes the new account to `Esolutions Beta Pte Ltd`. | Will believe the bank opened an account for the wrong entity. | Treasury/compliance will treat as a real entity-confusion incident. | Bind every entity reference to the session's customer-ID at render time; add a contract test asserting consistency. |
| 4 | Sell Form (cross-currency) | Banking-domain — Pricing | 🔴 CRITICAL | Cross-currency Sell (XAU → USD) shows no FX rate, no markup, no FX timing. User commits to a USD figure with no idea how the FX leg is priced. | Will not realise FX is silently bundled into the trade. | Cannot reconcile P&L; likely to refuse cross-currency for compliance. | Add a dedicated FX panel to Review whenever debit and credit currencies differ. Lock the FX quote with a countdown. |
| 5 | Buy Review | Banking-domain — Pricing | 🔴 CRITICAL | "Indicative" prices on the form/Review are never reconciled with an "Executed" price on the Acknowledgement — the ack repeats the indicative figure as if it were the fill. | Discovers any slippage retrospectively in the statement. | Cannot reconcile; will not trust the venue. | On the ack and confirmation email, surface "Executed unit price", "Quantity", "Total paid" as the canonical record. Rename on-chart figure "Live indicative". |
| 6 | Buy Review | Banking-domain — Regulatory | 🔴 CRITICAL | "Terms and Conditions" referenced in the Review disclaimer but not hyperlinked. | Click-through consent with no opportunity to read. | Compliance-flag — no audit trail of "document was made available". | Hyperlink "Terms and Conditions" to the actual document. Track view-timestamp. Add a separate Key Fact Sheet link. |
| 7 | Buy Review — new-account | 8. Cognitive Load & Clarity | 🟠 HIGH | Account-creation-on-first-buy messaging is split across 3 screens with 3 different phrasings (form: "New […] will be created with your order"; Review: "A new […] will be opened with this order"; Ack: "Your […] account has been opened"). | Cognitive load — must reconcile three phrasings to confirm one event. | Reads as careless copy work. | Pick one canonical phrase and use it in all three places. Lift the message out of the Credit-account block into a top-of-form info panel. |
| 8 | Buy Form (new-account) | 1. IA & Navigation | 🟠 HIGH | New-account-on-first-buy is communicated only inside the Credit-account block as plain text. Easy to overlook that the form will open a brand-new account. | May not realise they are doing two things at once. | Will spot but expects more prominence. | Surface as a top-of-form info panel with an icon. Repeat on Review and Acknowledgement. |
| 9 | Sell Form (insufficient holdings) | Banking-domain — Regulatory | 🟠 HIGH | No risk disclosure or product-suitability statement anywhere in flow. Empty-state copy markets upside ("hedge against inflation"); only counter-weight is the legalese "without recourse to Bank X". | May invest without understanding paper PM is non-capital-guaranteed. | Treats marketing-vs-risk asymmetry as a compliance gap. | Persistent risk panel above the chart on Buy/Sell forms; KFS link; "past performance" boilerplate near charts. |
| 10 | Overview (empty) | 8. Cognitive Load & Clarity | 🟠 HIGH | "Indicative" is used in four different ways without an inline definition (price, market value, market value (Indicative), quantity (Indicative)). | Reads as "current"; misses that executed price may differ. | Knows the term but expects bank to define it for compliance. | Inline info-icon → tooltip on every "Indicative". Standardise on one canonical noun phrase per concept. |
| 11 | Buy Ack (expanded) | 7. Feedback & System Status | 🟠 HIGH | "Filled successfully" reads as terminal — yet the global "Tasks and Statuses" pill has a red-dot suggesting pending second-eye approval. If maker-checker is invisible, novices will believe the trade is final when it may not be. | May take downstream actions on a not-yet-final order. | Cannot determine actual status from the screen. | If maker-checker applies, change copy to "Order submitted for approval. Awaiting Checker." Only show "Filled successfully" once both legs complete. |
| 12 | Overview (empty) | 1. IA & Navigation | 🟠 HIGH | `Tasks and Statuses` utility pill is present on every screen — likely the checker queue — but its overlay/page is never shown. No tooltip, no inline indication of what it means. | Doesn't know what the badge means; ignores it. | Knows it matters but cannot infer state. | Tooltip on hover. Design and audit the overlay. Surface pending counts in-context on order/acknowledgement screens, not only in the global header. |
| 13 | Overview (populated) | 7. Feedback & System Status | 🟠 HIGH | Recent orders table has no Status column. | Cannot tell whether a recent order has settled. | Major operational gap for reconciliation. | Add STATUS column with coloured pills (Filled / Pending / Settled / Cancelled / Rejected); filterable. |
| 14 | Buy Ack (expanded) | 7. Feedback & System Status | 🟠 HIGH | Acknowledgement gives no "what happens next" copy beyond a single forward-looking line. | Doesn't know when to expect settlement / statement / email. | Missing operational data needed to track through to reconciliation. | Add "What happens next" panel with email-dispatched, settlement cutoff, statement-availability, dispute path. |
| 15 | Buy Form (new-account) | 6. Forms & Data Entry | 🟠 HIGH | Sell has an amber insufficient-holdings warning; Buy has no equivalent insufficient-funds warning. Buy users can compose over-budget orders with no live feedback. | Trial-and-error into a server-side rejection. | Mild annoyance; expects parity. | Mirror Sell's warning on Buy: "Investment amount exceeds available balance (X SGD). Reduce to proceed." |
| 16 | Overview (empty) | 1. IA & Navigation | 🟠 HIGH | FAQ (fees, "things to look out for") sits below the fold. User clicks Trade before seeing fees or risk. | Buys without knowing the fee or the risk. | Treats burying these in a collapsed accordion as regulatory weakness. | Surface a fee headline and a risk headline *above* the per-metal trade CTAs. Keep full FAQ below. |
| 17 | Overview (empty) | 5. Components | 🟡 MEDIUM | Empty-state primary CTA "Start trading" is a blue text link, not a button. Every other primary CTA is a slate filled button. | May not realise where to start; eye gets pulled to metal cards. | Mild friction. | Replace link with standard slate primary button. |
| 18 | Buy Review | Banking-domain — Authorization | 🟡 MEDIUM | Confirm-Buy/Sell-order button is the only confirmation gate. No 2FA / SCA / signing step between Review and order placement. | Accidental clicks become orders. | Compliance flag — corp-banking trade execution typically requires a second factor at commit. | Insert 2FA / SCA prompt between Review and Confirm. |
| 19 | Buy Ack (collapsed) | 5. Components | 🟡 MEDIUM | Collapse chevron is unlabelled — no "Show details" / "Hide details" text. | May not realise more information is available. | Mild friction. | Add text label alongside chevron. |
| 20 | Sell Review | 8. Cognitive Load & Clarity | 🟡 MEDIUM | Buy uses "Investment amount" for the SGD field; Sell uses "Market value". Sell email reverts to "Investment amount". Same value, three labels. | Re-learn the layout per direction. | Reads as careless copy work. | Single label per direction — "Cost (SGD)" for Buy, "Proceeds (SGD)" for Sell — in-app and in-email. |
| 21 | Overview (populated) | 3. Typography | 🟡 MEDIUM | Numerics in Holdings details and Recent orders tables are not tabular; decimals don't align vertically. | Slower scanning but readable. | Recognised as substandard finance-table styling. | `font-variant-numeric: tabular-nums`; right-align numeric columns. |
| 22 | Buy Form (new-account) | design system inconsistency | 🟡 MEDIUM | Nav label inconsistent: "FX and Investment" on most screens vs "FX and Treasury" on the trade-form variants. | Quiet confusion. | Spotted immediately; reads as build defect. | Pick one (recommend "FX and Investment") and unify. |

---

## TOP 5 PRIORITY RECOMMENDATIONS

### 1. Block launch on the three "build-readiness" defects

- **What to fix:** Three production-feeling screens show unresolved tokens — `[Precious Metal Account]` / `[paper gold]` / `[Esolutions Alpha Pte Ltd]` on the Buy form and Review banner (Finding #1); `<Salutation>` / `<Surname>` / `<Name>` / `<Designation/rank>` / `<Department name>` in both email templates (#2); and an entity-name mismatch on the account-opened acknowledgement (`Esolutions Beta Pte Ltd` shown when the session is `Esolutions Alpha Pte Ltd`) (#3).
- **Why it matters:** Any single one of these would erode customer trust on a regulated investment commit. For a banking product the credibility cost is non-recoverable in real time — a customer who sees "Dear `<Salutation> <Surname>`" treats the email as phishing and may never re-open the product.
- **How to fix it:** (a) Add a pre-launch lint that scans every rendered UI string and email template for `\[[^\]]+\]` and `<[^>]+>` patterns and fails the build if any are found in visible copy. (b) Bind every entity reference on the acknowledgement to the session's customer-ID. (c) Add a contract test that asserts entity-name consistency between header context and any per-screen entity label.
- **Effort estimate:** **Quick Win** — instrumentation and binding only.

### 2. Make cross-currency pricing transparent

- **What to fix:** The Sell form's cross-currency variant (XAU → USD credit account) shows no FX rate, no markup, no FX timing (#4). The form, Review, and Acknowledgement all use "Indicative" figures but never disclose the executed unit price (#5). Terms and Conditions are referenced in the commit disclaimer but not hyperlinked (#6).
- **Why it matters:** Cross-currency settlement is two pricing decisions disguised as one. Hiding the FX leg is a regulatory and credibility failure simultaneously. The "Indicative → fill" gap is the same root issue as the live/executed price ambiguity flagged in the prior Buy/Sell audit.
- **How to fix it:** On Review whenever debit and credit currencies differ, surface a 4-line FX panel: `XAU/SGD reference price | SGD/USD rate (with markup) | All-in unit price | Total USD`. On the Acknowledgement, replace the indicative figure with `Executed unit price · Quantity · Total paid`. Hyperlink T&Cs on Review with a view-timestamp tracker; add a Key Fact Sheet link.
- **Effort estimate:** **Medium Lift** — Review template extension + pricing service publishes the executed unit price.

### 3. Surface risk, fees, and disclosure at decision time

- **What to fix:** Risk content lives below the fold in a collapsed FAQ ("Things to look out for") (#16). Disclaimer copy uses "without recourse to Bank X" without a plain-language counterbalance (#9). No KFS, no "past performance" boilerplate near any chart, no custody (allocated/unallocated) statement.
- **Why it matters:** Regulated investment requires risk visibility *before* commitment. Today's empty-state markets upside; the only downside language is buried legalese.
- **How to fix it:** Add a persistent risk panel above the chart on Buy/Sell forms with three lines covering price volatility, past-performance disclaimer, and custody/SDIC status. Add a fee headline + risk headline above the per-metal trade CTAs on the Overview. Add a KFS link.
- **Effort estimate:** **Medium Lift** — new component, no new logic.

### 4. Reconcile the maker-checker workflow with the acknowledgement copy

- **What to fix:** Every screen carries a "Tasks and Statuses" pill with a red-dot, implying a maker-checker queue, but no pending-approval / awaiting-checker / rejected state is designed anywhere. The acknowledgement says "filled successfully" — terminal language (#11, #12, #13).
- **Why it matters:** For a regulated corporate trading product, the maker-checker pattern is the operational floor. If it exists invisibly the novice user will misinterpret "filled successfully" as final. If it doesn't exist, treasury/compliance will refuse the product.
- **How to fix it:** (a) Decide the policy: maker-checker or single-control. (b) If maker-checker, change ack copy to "Order submitted for approval. Awaiting Checker." Only show "Filled successfully" once both legs complete. Surface a STATUS column on Recent orders with `Filled / Pending Approval / Awaiting Settlement / Cancelled / Rejected`. (c) Design and audit the `Tasks and Statuses` overlay. (d) If single-control, explicitly state on the ack: "No further approval required — order is final."
- **Effort estimate:** **Large Effort** — new screens and workflow integration.

### 5. Tighten the account-creation-on-first-buy branch

- **What to fix:** The fact that completing this form will open a brand-new Precious Metals account is communicated only inside the Credit-account block as plain text (#8). Across three screens the messaging is written three different ways (#7).
- **Why it matters:** Opening an account is a separate decision from placing a trade — it carries its own statement, tax treatment, and reporting implications. A novice corporate customer must not blunder into it.
- **How to fix it:** Pick one canonical phrase ("A Precious Metals account will be opened") and use it identically on form, Review, and Acknowledgement. Lift it out of the Credit-account block into a top-of-form info panel with an icon. Add a tickbox or inline acknowledgement: "I understand a new account will be opened for this purpose."
- **Effort estimate:** **Quick Win** — copy unification + one new info panel.

---

## DESIGN SYSTEM & CONSISTENCY NOTES

- **Bracketed placeholder tokens** (`[Precious Metal Account]`, `[paper gold]`, `[Precious Metals]`, `[Esolutions Alpha Pte Ltd]`) appear in production-looking copy. Either the design tooling is leaking template syntax, or the strings have not been bound. Add a lint.
- **Email merge syntax** (`<Salutation>`, `<Surname>`, `<Name>`, `<Designation/rank>`, `<Department name>`) appears literally in both email templates. Production-blocking; harden the merge pipeline.
- **Entity-name binding** is not consistent — the account-opened acknowledgement shows `Esolutions Beta Pte Ltd` while the session shows `Esolutions Alpha Pte Ltd`. Bind every entity reference to a single source-of-truth at render.
- **Buy / Sell pill chip vs coloured-word treatment.** Recent orders renders Buy/Sell as coloured pill chips; the Review header renders the same semantics as a coloured word with no pill. Standardise to the pill.
- **Primary CTA inconsistency.** Most primary CTAs are slate filled buttons (`Review buy order`, `Confirm buy order`, `View order`). The empty-state primary on the Overview is a blue text link (`Start trading`). Promote to the standard slate button.
- **Nav label drift.** `FX and Investment` vs `FX and Treasury` for the same nav item. Pick one.
- **Per-row Trade button vs link.** The empty Overview uses a blue text link for `Trade Gold (XAU)`; the populated Overview's Holdings row uses an outlined `Trade` button. Same intent, different affordance.
- **Numeric typography.** Holdings details and Recent orders tables use a proportional sans for numerics. Switch to tabular figures.
- **Disclaimer typography.** Review disclaimer is centred light-grey small body text — the lowest visual weight on the page, despite being a regulated consent. Promote to body weight with an amber-tinted icon panel.
- **Account-creation messaging.** Three different phrasings across three screens for a single event. Pick one canonical sentence.

---

## DOMAIN-SPECIFIC ASSESSMENT — Banking / Investment (regulated, corporate)

| Lens | Status | Notes |
|---|---|---|
| Risk presented **before** commitment | ❌ Missing | Collapsed FAQ only. |
| Risk with **equal weight** to upside | ❌ Missing | Gain in green is prominent; no equivalent downside. |
| Past-performance disclaimer near charts | ❌ Missing | No boilerplate on any chart. |
| Key Fact Sheet (KFS) link | ❌ Missing | Not present. |
| Suitability / product-knowledge gate | ❌ Missing | No 5-question check. |
| T&C **hyperlink** before Confirm | ❌ Missing | Referenced but not linked. |
| T&C **checkbox** | ❌ Missing | Passive copy. |
| Bid/ask spread | ❌ Missing | Single number ("Indicative"); same as prior audit. |
| Fee / commission line at commit | ❌ Missing | Mentioned only in collapsed FAQ. |
| **FX rate at commit (cross-currency Sell)** | ❌ Missing | New finding; XAU→USD has no FX disclosure. |
| GST / tax disclosed at commit | ❌ Missing | Same as prior audit. |
| Custody (allocated/unallocated) disclosed | ❌ Missing | Tagline implies paper bullion; never stated. |
| SDIC / deposit-protection statement | ❌ Missing | Holdings not SDIC; user not told. |
| Executed price disclosure | ❌ Missing | Ack repeats "Indicative" amount as if it were the fill. |
| Settlement window / cancellability | 🟡 Partial | "(Today)" stated; cancellability not. |
| 2FA / SCA / signing at commit | ❌ Missing | Single-click Confirm only. |
| Maker-checker / pending-approval state | ❌ Missing | Implied by "Tasks and Statuses" pill, never designed. |
| Order status on Order History | ❌ Missing | No Status column on Recent orders. |
| Account-creation prominence on first buy | 🟡 Partial | Mentioned but buried inside Credit-account block. |
| Entity-name consistency on confirmation | ❌ Missing | Beta vs Alpha mismatch on the new-account ack. |

**Verdict:** the product is **not yet ready for a regulated launch**. The findings cluster around build readiness (placeholders, merge tokens, entity binding), cross-currency pricing, and workflow integrity. These must be resolved holistically — not screen by screen.

---

## NOVICE CORPORATE CUSTOMER JOURNEY ASSESSMENT

A first-time corporate paper-bullion buyer lands on the Overview, sees Gold at 6,581.85 with a +2.80% green delta, clicks `Start trading` (a blue text link — they have to look for it), arrives on the Buy form, and at the Credit-account row reads "New `[Precious Metal Account]` will be created with your order" — the brackets read as broken or unfinished, and the account-creation event itself is buried. They proceed to Review; the same `[…]` brackets appear in the info banner. They glance past the small grey disclaimer that references unlinked Terms and Conditions, click Confirm Buy Order, and arrive on an acknowledgement that says "filled successfully and your Precious Metals account is now created" — except the account-holder line reads `Esolutions Beta Pte Ltd` and they work for `Esolutions Alpha Pte Ltd`. They phone-in. They open the email and find `Dear <Salutation> <Surname>`. They escalate. **Score: 4.0 / 10.**

## EXPERIENCED CORPORATE CUSTOMER ASSESSMENT

An experienced corporate customer (treasury / authorized trader) will execute the trade quickly — the form is short, the steps are minimal, the acknowledgement is fast. They will not be misled by `Indicative` or `filled successfully` — they understand the vocabulary. But the moment they try a cross-currency Sell they will not see an FX rate, and the moment they try to reconcile against a statement they will not find an Executed price. They will scroll the Recent orders table and find no Status column. They will look for a Tasks and Statuses overlay and not find it. They will tell their compliance team. The product feels like a serviceable demo with the disclosure surface left as a follow-up. **Score: 4.5 / 10.**

---

## ANNOTATED SCREENSHOTS

The annotated screenshots below pin every finding to its on-screen location. Severity colours: 🔴 Critical · 🟠 High · 🟡 Medium · 🟢 Low.

- **Overview (empty)** — markers #10, #12, #16, #17
- **Overview (populated)** — markers #13, #21
- **Buy Form (new-account)** — markers #1, #8, #15, #22
- **Sell Form (insufficient holdings)** — marker #9
- **Sell Form (cross-currency)** — marker #4
- **Buy Review** — markers #5, #6, #18
- **Buy Review (new-account)** — marker #7
- **Sell Review** — marker #20
- **Buy Acknowledgement (expanded)** — markers #11, #14
- **Buy Acknowledgement (account-opened)** — marker #3
- **Buy Acknowledgement (collapsed)** — marker #19
- **Email — Buy confirmation** — marker #2

(See `report.html` for the rendered annotated views with side-by-side findings and connector lines.)

---

## WHAT'S WORKING WELL

1. **Insufficient-holdings warning on Sell is well-designed.** Amber tint, clear icon, specific message ("Reduce the quantity to 25.86 ounces or less to proceed"), CTA disabled until resolved. This is the right pattern; mirror it for Buy insufficient-funds.
2. **Account-opened acknowledgement panel concept is good** — combining the trade success with the new-account success into one screen avoids a multi-page "wizard" feel. The entity-binding bug aside, the design intent is correct.
3. **Acknowledgement collapse pattern reduces cognitive load** for repeat users who don't need to re-read order details. (Chevron labelling aside.)
4. **Email subject lines are clear and action-specific** ("Your Gold (XAU) buy/sell order is confirmed").
5. **Cross-currency Sell support exists in the design at all** — many bank products skip this. The architectural decision is right; only the disclosure layer needs to catch up.

---

## SUGGESTED NEXT AUDIT SCOPE

1. **The actual Add User / Delete User flow** — once it exists, audit it with Maker / Checker personas.
2. **The Tasks and Statuses overlay** — once designed.
3. **The real Renewal upload flow** — once designed (today's "renew landing" screens are not renewal screens).
4. **Order Detail screen / drill-down** — once it exists.
5. **Edge cases** — error / loading / market-closed / insufficient-balance / order-rejected.

---

*End of audit report.*
