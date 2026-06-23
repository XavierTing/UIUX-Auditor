# UI/UX AUDIT REPORT: OCBC Precious Metals Module

**Audit Date:** 2026-06-23
**URL:** `https://www.figma.com/design/pJuwdSGBCJvVtx6i77ytzM/Precious-Metal?node-id=1106-21058`
**Auditor Personas:** (A) Novice — new to precious-metal investment · (B) Experienced precious-metal investor
**Platform:** Web desktop — OCBC business/corporate internet banking (OCBC Velocity-style), 1600px; with email (702px) and mobile push (375px) notification mockups
**Flow Scope:** End-to-end Precious Metals journey — Overview/market landing, Buy & Sell trade input, Review, T&C/account opening, Acknowledgement, Confirmation, Trade detail, Trade history, Dashboard/holdings, Manage & set price alerts, error/edge states, email & push notifications
**Screens Reviewed:** 19 de-duplicated representative screens covering all 49 frames (currency/state variants consolidated): Overview (SGD/USD), Buy input (empty/filled), Sell input, Review, T&C modal, Acknowledgement modal, Confirmation success, Trade detail, Trade history, Dashboard/holdings, Post-investment landing, Set price alert, Price-alert list, Error-banner specs, Exceed-market-value, Email confirmation, Push alert

---

## EXECUTIVE SUMMARY

The OCBC Precious Metals module is a competently structured corporate-banking trading flow with several genuine strengths: persistent field labels, a thoughtful amount↔quantity dual-input, well-written and non-punitive error-recovery copy, sensible sell-side guardrails (caps to holdings), proper empty states, and clear cross-channel reference numbers. The bones of a trustworthy trading tool are present.

However, for a regulated investment product the audit surfaces serious gaps concentrated in risk disclosure, system feedback, and production polish. There is no investment-risk disclosure, Key Fact Sheet, or suitability check before a customer commits to a five-figure order; the first-time Terms & Conditions modal asks the user to agree to four documents it never lets them open. The displayed "Indicative price" silently differs from the actual execution price (6,581.85 quoted vs 6,128.50 executed in the sample data) with no caveat. Multiple customer-facing surfaces ship unfilled template tokens (`[6:00 AM SGT]`, `<Salutation> <Surname>`, `<7,000.00 SGD/ounce>`, a stale "© 2024"). Price freshness is contradictory across screens with no refresh indicator, there is no loading state on order submission (double-submission risk), and the validation/error states exist only as isolated spec frames rather than on the live trade screen.

The experience diverges sharply by persona. The novice is under-served at exactly the high-stakes moments — undefined jargon (XAU/XAG, troy ounce, "Filled", "Credit account"), risk buried in a collapsed FAQ, and cold liability-only copy at the point of commitment. The experienced investor is better served for core trading but is blocked by efficiency gaps (no "place another trade", dead-end trade detail) and a data-integrity bug in the alerts list (count vs rows mismatch).

Audit coverage: all 9 usability dimensions plus a banking/investment domain lens (risk disclosure, terminology comprehension, yield/price presentation, regulatory disclosures), across the full buy/sell/alerts journey.

**Overall UX Health Score: 4.5/10 (Combined)** — solid structure undermined by critical risk-disclosure gaps and trust-eroding production defects that a regulated product cannot ship with. Per-persona: **Novice 3.5/10**, **Experienced 6.0/10**.

---

## Findings Table

26 findings — 2 Critical, 11 High, 11 Medium, 2 Low. Severity = the worst impact across the two personas. Per-persona impact columns and persona classification (Both / Novice-critical / Seasoned-critical / Conflicting) included.

| # | Screen / Component | Dimension | Severity | Finding | Novice Impact | Experienced Impact | Classification | Recommendation |
|---|---|---|---|---|---|---|---|---|
| 1 | T&C modal / Confirm | 9. Trust & Risk Disclosure | CRITICAL | No risk disclosure / KFS / suitability check before buy; T&C modal lists 4 agreements with no openable documents yet requires "Agree" | Commits to 30,642.50 SGD with zero risk disclosure; agrees to unreadable docs | Expects a KFS as standard; absence is regulatory exposure | Both | Add a risk-disclosure step with explicit acknowledgement; make all T&Cs openable |
| 2 | Buy/Sell input / Error specs | 5. Component & Interaction | CRITICAL | Validation/error states exist only as spec frames, not on the live trade screen; timing & CTA-gating unverified | If validation fires late/silently, blocked at submit with no recovery | Slows expert expecting immediate field feedback | Both | Integrate field-anchored inline errors, on-blur validation, gated CTA with reason; design all states |
| 3 | Review / Buy input | 7. Feedback & System Status | HIGH | Indicative price (6,581.85) vs actual execution price (6,128.50) gap never disclosed | Perceives bait-and-switch; loses trust | Expected but undocumented = compliance gap | Both | Tooltip on "Indicative price" + execution caveat; show executed price on confirm |
| 4 | Overview / Landing | 9. Trust & Risk Disclosure | HIGH | Upside-only marketing copy; no "value can fall" statement before CTA | Forms unbalanced optimistic risk model | Recognises as spin; low impact | Novice-critical | Add equally-weighted risk statement beside the value proposition |
| 5 | Overview / Landing | 8. Cognitive Load & Clarity | HIGH | Only risk content ("Things to look out for") is collapsed, below fold, after CTA, euphemistic | Risk hidden when deciding to invest | Minor | Novice-critical | Rename to "Risks", surface above fold, expand by default for first-timers |
| 6 | Maintenance modal / Email / Push | 7. Feedback & System Status | HIGH | Unfilled template tokens shipped: `[6:00 AM SGT]`, `<Salutation> <Surname>`, `<7,000.00 SGD/ounce>`, "© 2024" | Reads as broken; undermines trust | Looks like a QA failure | Both | Purge all merge/placeholder tokens; dynamic times; fix copyright |
| 7 | Buy input / Overview | 7. Feedback & System Status | HIGH | Conflicting price timestamps (23 Apr vs 28 Apr) and no refresh/expiry indicator on a live-priced commodity | Can't tell if quote is stale | Stale quote unacceptable for active trading | Both | Single live timestamp + auto-refresh with countdown/refresh control |
| 8 | Review / Confirmation | 7. Feedback & System Status | HIGH | No loading/processing state between Confirm and success | May double-click in uncertainty | Double-submission risk on a real order | Both | Add explicit processing state; disable button; block resubmission |
| 9 | Review vs Trade detail | 1. Information Architecture | HIGH | Review (pre-commit) and Trade-detail (executed) are near-identical; unclear if money moved | May think order placed and abandon/resubmit | Risks misread on fast scan | Both | Differentiate with status banner + step indicator; make pre-commit unmistakable |
| 10 | Buy / Sell input | 4. Colour & Contrast | HIGH | Buy/Sell and gain/loss rely on colour (red/green); brand red overloaded as brand + Sell + loss | Colour-blind novice can confuse Buy/Sell on real money | Same a11y risk; muddied action priority | Both | Add non-colour redundancy (icons/labels); fix one meaning for red |
| 11 | Overview / History / Alerts | 1. Information Architecture | HIGH | Currency can switch silently (SGD/USD/EUR across overview, history, alerts) | May transact in a different currency than read | Needs persistent unmistakable currency indicator | Both | Persistent prominent currency indicator; warn on switch; align units |
| 12 | Review | 9. Trust & Risk Disclosure | HIGH | At the 30,642.50 SGD confirm moment, only cold liability copy ("without recourse to OCBC Bank"); no reassurance | Coldest copy on most consequential screen raises anxiety | Reassurance on debit/settlement still useful | Novice-critical | Pair legal text with plain-language reassurance (settlement/debit timing, security) |
| 13 | Manage price alerts | 7. Feedback & System Status | HIGH | Filter counter vs table disagree ("All (5)" but 7 rows) | Confusing, lower stakes | Power users rely on data accuracy; breaks trust | Seasoned-critical | Reconcile counts with rendered rows; treat as data-integrity defect |
| 14 | Buy/Sell input | 2. Visual Hierarchy & Layout | MEDIUM | Primary CTA weak/buried (grey, below divider, invisible when disabled); chart out-weighs the form | May miss next-step button / why disabled | Minor friction locating action | Both | Elevate CTA; give disabled state a reason ("Enter an amount to continue") |
| 15 | Trade detail / Buy input | 8. Cognitive Load & Clarity | MEDIUM | Jargon undefined inline: XAU/XAG, troy ounce, Indicative price, Credit/Debit account, "Filled", "Market value (Indicative)"; FAQ only on Overview | Multiple terms ≤2/5 comprehension, no help where shown | Comfortable; no impact | Novice-critical | Inline tooltips on first use; carry FAQ definitions onto transactional screens (progressive disclosure) |
| 16 | Review / Overview | 1. Information Architecture | MEDIUM | Header/eyebrow inconsistent (inline vs gutter vs absent); no step indicator in a multi-step money flow | Weakened "where am I" orientation | Minor | Novice-critical | Standardise one eyebrow+H1; add step indicator to buy/sell flow |
| 17 | Buy/Sell input | 6. Forms & Data Entry | MEDIUM | Amount↔quantity swap control unlabeled, no chrome/tooltip | Won't grasp the two fields are one decision | Will infer; still ambiguous | Novice-critical | Add button container + tooltip ("Switch between amount and quantity") |
| 18 | Buy input / T&C modal | 1. Information Architecture | MEDIUM | Account creation messaged twice & inconsistently (inline vs modal) | Unclear if/when account exists | Minor redundancy | Novice-critical | One consistent account-creation message at a single point |
| 19 | Error specs | 5. Component & Interaction | MEDIUM | Blocking errors and soft warnings share identical amber styling; 3 banner variants coexist | Can't tell a stop from a heads-up | Same ambiguity; slows triage | Both | Distinct error vs warning styles; consolidate to one banner component |
| 20 | Buy input | 3. Typography & Readability | MEDIUM | Grey-on-grey labels likely fail AA; placeholder "0.00" indistinguishable from entered zero | Hard-to-read labels; value-entered confusion | Minor readability friction | Both | Raise contrast to AA; distinguish placeholder vs entered/focus states |
| 21 | Trade detail / Confirmation | 1. Information Architecture | MEDIUM | Trade detail is a dead end; success offers no "place another trade" | Lower impact, fewer repeats | Must re-navigate for every order | Seasoned-critical | Add contextual next-actions (sell/download/alert) + "Place another trade" |
| 22 | Trade history / multiple | Design System & Consistency | MEDIUM | Number/unit/account format drift ("ounce" vs "ounces", account formats, "Holding(s) details") | Small friction reconciling same data | Notices inconsistency; questions integrity | Both | Enforce one formatting standard for units, accounts, pluralisation, labels |
| 23 | Review | 6. Forms & Data Entry | MEDIUM | "Back" on Review ambiguous — discard or edit? | Fears losing/discarding order | Minor hesitation | Novice-critical | Label intent ("Edit order"/"Cancel"); confirm before destructive discard |
| 24 | Confirmation / Trade detail | Design System & Consistency | MEDIUM | Primary-button system unsystematised (grey, never red); Back as link vs button; two confirmation layouts differ | Inconsistent affordances less predictable | Reads as low polish | Both | Define one primary/secondary/tertiary treatment; unify confirmation layouts |
| 25 | Dashboard / global | Design System & Consistency | LOW | Nav label drift ("FX and Investment" vs "FX and treasury"); header chrome differs; spec frames mixed into product | Negligible per screen | Negligible | Both | Reconcile nav taxonomy & header chrome; keep specs out of production flow |
| 26 | Confirmation | 2. Visual Hierarchy & Layout | LOW | Success sentence under-emphasised (light grey, smaller than figures) | Reassurance under-weighted at closure | Negligible | Novice-critical | Promote success sentence to strongest text on the screen |

---

## Annotated Screenshots

Screens are ordered by flow sequence. Each marker number maps to the findings table above.

### Overview / Market Landing (SGD)
![Overview SGD — Annotated](screenshots/01-landing-overview-sgd-annotated.png)
**Findings on this screen:**
- **[#4] HIGH** — Upside-only marketing, no "value can fall" statement → Add balancing risk statement beside the value proposition.
- **[#5] HIGH** — Risk buried in a collapsed, euphemistic FAQ after the CTA → Rename to "Risks", surface above the fold, expand for first-timers.

### Overview / Market Landing (USD)
![Overview USD — Annotated](screenshots/02-landing-overview-usd-annotated.png)
**Findings on this screen:**
- **[#11] HIGH** — Currency unit can switch silently (SGD/USD/EUR) → Persistent currency indicator; warn on switch.

### Buy Trade Input (empty)
![Buy input — Annotated](screenshots/03-buy-trade-input-annotated.png)
**Findings on this screen:**
- **[#2] CRITICAL** — Error/validation states not present on the live screen → Integrate field-anchored inline errors and gated CTA.
- **[#7] HIGH** — Stale/conflicting price timestamp, no refresh → Single live timestamp + auto-refresh.
- **[#14] MEDIUM** — Weak, buried grey primary CTA, invisible when disabled → Elevate CTA; give disabled state a reason.
- **[#17] MEDIUM** — Unlabeled amount/quantity swap control → Add button chrome + tooltip.

### Buy Trade Input (filled)
![Buy input filled — Annotated](screenshots/18-buy-input-filled-annotated.png)
**Findings on this screen:**
- **[#18] MEDIUM** — Redundant/conflicting account-creation message → One consistent message at one point.
- **[#20] MEDIUM** — Grey-on-grey labels; "0.00" placeholder ambiguity → Raise contrast; distinguish placeholder vs entered.

### Sell Trade Input
![Sell input — Annotated](screenshots/19-sell-trade-input-annotated.png)
**Findings on this screen:**
- **[#10] HIGH** — Buy/Sell colour-only; brand red overloaded as brand + Sell + loss → Add non-colour redundancy; fix one meaning for red.

### Review Buy Order
![Review — Annotated](screenshots/04-review-buy-order-annotated.png)
**Findings on this screen:**
- **[#9] HIGH** — Near-identical to Trade-detail; unclear money state → Status banner + step indicator.
- **[#3] HIGH** — Indicative vs execution price gap → Tooltip + execution caveat.
- **[#16] MEDIUM** — No step indicator / header inconsistency → Standardise eyebrow+H1; add steps.
- **[#12] HIGH** — Cold liability-only copy at the confirm moment → Pair with plain-language reassurance.
- **[#23] MEDIUM** — Ambiguous "Back" (discard or edit?) → Label intent; confirm destructive discard.
- **[#8] HIGH** — No loading state on submit → Add processing state; block resubmission.

### Terms & Conditions / Account Opening
![T&C — Annotated](screenshots/15-terms-and-conditions-annotated.png)
**Findings on this screen:**
- **[#1] CRITICAL** — Agree to 4 T&Cs with no openable documents; no risk disclosure/KFS → Make T&Cs openable; add a real risk-disclosure step.
- **[#18] MEDIUM** — Duplicate account-creation messaging → One consistent message.

### Acknowledgement / Maintenance Modal
![Maintenance modal — Annotated](screenshots/10-modal-acknowledgement-annotated.png)
**Findings on this screen:**
- **[#6] HIGH** — Unfilled template token "[6:00 AM SGT]" / "[6:00 AM]" → Fill dynamically; one timezone format.

### Confirmation — Buy Order Filled
![Confirmation — Annotated](screenshots/16-confirmation-success-annotated.png)
**Findings on this screen:**
- **[#8] HIGH** — No processing state precedes this success → Add explicit pending state.
- **[#26] LOW** — Success sentence under-emphasised → Promote to strongest text.
- **[#24] MEDIUM** — Back link vs button inconsistency → One back pattern.
- **[#21] MEDIUM** — No "place another trade" → Add repeat-trade shortcut.

### Trade Detail (Filled)
![Trade detail — Annotated](screenshots/05-trade-detail-confirmation-annotated.png)
**Findings on this screen:**
- **[#9] HIGH** — Looks like Review; can't tell money moved → Differentiate executed vs pre-commit.
- **[#15] MEDIUM** — Jargon undefined ("Filled", "Credit account") → Inline glosses/tooltips.
- **[#21] MEDIUM** — Dead end: no sell/download/alert next-actions → Add contextual actions.

### Trade History
![Trade history — Annotated](screenshots/06-trade-history-annotated.png)
**Findings on this screen:**
- **[#11] HIGH** — SGD/USD/EUR mixed in rows → Unambiguous per-row currency.
- **[#22] MEDIUM** — Number/unit/account format drift → Enforce one standard.

### Dashboard / Holdings
![Dashboard holdings — Annotated](screenshots/07-dashboard-holdings-annotated.png)
**Findings on this screen:**
- **[#13] HIGH** — Alert filter count vs rows mismatch → Reconcile as data-integrity defect.

### Dashboard (default)
![Dashboard default — Annotated](screenshots/08-dashboard-default-annotated.png)
**Findings on this screen:**
- **[#25] LOW** — Nav label drift ("FX and treasury") → Reconcile nav taxonomy.

### Error / Edge-State Specs
![Error banners — Annotated](screenshots/11-error-banner-specs-annotated.png)
**Findings on this screen:**
- **[#2] CRITICAL** — Error states exist only as spec frames → Integrate into the live flow.
- **[#19] MEDIUM** — Blocking errors vs warnings look identical → Distinct styles; one banner component.

### Push Notification — Rate Reached
![Push noti — Annotated](screenshots/12-push-noti-rate-reached-annotated.png)
**Findings on this screen:**
- **[#6] HIGH** — Leaked delimiters "<7,000.00 SGD/ounce>" → Strip template syntax.

### Email — Buy Order Confirmed
![Email — Annotated](screenshots/13-email-noti-annotated.png)
**Findings on this screen:**
- **[#6] HIGH** — Unfilled merge fields "<Salutation> <Surname>", "<Name>"; "© 2024" → Fill/strip merge fields; fix year.

---

## Banking & Investment Domain Assessment

This is a regulated investment product, so it is held to a higher bar for risk clarity, error prevention, and trust signals.

**Risk disclosure — FAIL (Critical).** Downside is not given equal weight to upside. There is no risk-warning statement, Key Fact Sheet, or suitability/appropriateness check anywhere before a customer commits a five-figure order (#1, #4, #5). The single pre-commitment artifact is a liability declaration that protects the bank, not the customer (#12). The first-time T&C modal requires agreement to four documents it never lets the user open (#1) — a recognised regulatory/dark-pattern weakness.

**Terminology comprehension — WEAK for novices.** Six core terms score ≤2/5 for novice comprehensibility with no inline help where they appear: "Indicative price", "ounce" (never stated as *troy* ounce — a material accuracy gap), "Credit account"/"Debit account" (a buy's "Credit account – Gold (XAU)" reads as being *given credit*), "Order status: Filled", "Market value (Indicative)", and the bare ISO codes "XAU/XAG" (#15). The only glossary is the Overview FAQ — absent from the input, review, detail, and sell screens where the jargon actually appears.

**Yield / price presentation — MISLEADING.** Gains render prominently while the indicative-vs-execution price gap is undisclosed (#3): sample data shows a 6,581.85 SGD/ounce indicative quote executing at 6,128.50 SGD/ounce. Price freshness is contradictory across screens with no refresh affordance (#7), so a customer cannot tell whether they are transacting on a live or stale quote.

**Regulatory disclosures — INSUFFICIENT.** No KFS, no risk acknowledgement, no suitability gate; openable T&Cs absent. Recommendation: introduce a compliant disclosure step before "Confirm buy order" with an explicit risk acknowledgement and openable, versioned documents.

---

## Novice Investor — Journey Assessment

The novice is under-served precisely at the highest-stakes moments. The journey *starts* well — the empty holdings state and the "without holding the physical metal" gloss are genuinely helpful — but from the trade screen onward the scaffolding disappears. Undefined jargon (#15) means the novice cannot fully parse the form they are filling; the unlabeled amount↔quantity swap (#17) hides that the two fields are one decision; risk is buried (#4, #5) and the indicative-price caveat is missing (#3). At the moment of committing 30,642.50 SGD they receive cold liability copy and no reassurance (#12), no step indicator to confirm where they are (#16), and an ambiguous "Back" (#23). If anything is wrong, the error states are not on the screen (#2). The novice can complete a happy-path trade, but cannot make a *well-informed* one, and is one mistake away from confusion with no recovery. **Novice score: 3.5/10.**

## Experienced Investor — Efficiency Assessment

The experienced investor is well-served for the core mechanic: the dual-input, sell-side caps to holdings, persistent labels, and the data-dense trade-history and alerts tables all suit a power user. Their friction is at the edges. The trade-detail screen is a dead end and the success screen offers no "place another trade", forcing re-navigation for every order (#21) — a real tax on anyone who batches trades. The alerts list shows a count/row mismatch (#13) that directly erodes confidence in the data a power user depends on. Stale/contradictory price timestamps with no refresh (#7) and no submit loading state (#8) are unacceptable for active trading. The shipped template artifacts and the missing KFS (#1, #6) read as an immature product to an experienced eye. **Experienced score: 6.0/10.**

## Conflicting Needs & Progressive Disclosure

Where novice and expert needs diverge (notably jargon glossing #15, the swap-control affordance #17, and risk/education content), resolve via **progressive disclosure** rather than sacrificing either persona: inline tooltips and a first-run risk-education layer that the expert can dismiss/collapse, and a "place another trade" shortcut that doesn't clutter the novice's first journey. No finding requires helping one persona at the other's expense.

---

## TOP 5 PRIORITY RECOMMENDATIONS

### 1. Add a compliant risk-disclosure step before "Confirm buy order"
- **What to fix:** Insert a Key Fact Sheet / risk-warning statement with an explicit "I understand precious-metal values can fall" acknowledgement, and make the four agreements in the T&C modal genuinely openable (links or expandable text). Separate the customer-facing risk disclosure from the bank's liability declaration. (Resolves #1, #4, #5, #12.)
- **Why it matters:** For a regulated investment product this is the single biggest gap — currently a customer commits a five-figure order with no risk disclosure and agrees to documents they cannot read. It is both a user-protection and a regulatory exposure.
- **How to fix it:** A dedicated step (or expandable panel) before confirm: concise plain-language risks + openable versioned KFS/T&Cs + a required checkbox. Log acknowledgement against the order reference.
- **Effort estimate:** Large Effort

### 2. Make price honesty explicit — indicative vs execution, and freshness
- **What to fix:** Add an "Indicative price" tooltip and an execution caveat at input and review ("Final price is set at execution and may differ from the indicative price shown"); show the executed price prominently on confirmation; reconcile the conflicting timestamps and add an auto-refresh with a visible countdown/refresh control. (Resolves #3, #7.)
- **Why it matters:** The displayed price silently differs from the charged price and freshness is contradictory — a novice perceives bait-and-switch and an expert cannot trust the quote.
- **How to fix it:** Tooltip component + a live price ticker with "updated Xs ago / refresh" and an expiry on the quote used at confirm.
- **Effort estimate:** Quick Win (copy/tooltip) + Medium Lift (live refresh)

### 3. Purge all template artifacts and add the missing submit/loading states
- **What to fix:** Strip/fill every leaked token (`[6:00 AM SGT]`, `<Salutation> <Surname>`, `<Name>/<Designation>/<Department>`, `<7,000.00 SGD/ounce>`), fix "© 2024", and add an explicit processing state between Confirm and success that disables the button and prevents resubmission. (Resolves #6, #8.)
- **Why it matters:** Shipped placeholders read as broken on a bank; the missing loading state risks double-submitting a real order. Both are high-ROI trust fixes.
- **How to fix it:** Wire merge fields to data with safe fallbacks; add a submitting/pending state with optimistic disable + server confirmation.
- **Effort estimate:** Quick Win (artifacts) + Medium Lift (loading state)

### 4. Differentiate pre-commit from completed, and warm up the confirm moment
- **What to fix:** Visually separate Review (not yet submitted) from Trade-detail (Filled) with distinct headers, a clear status banner, and a step indicator; replace the cold liability-only declaration with plain-language reassurance (debit/settlement timing, security) kept alongside (not instead of) the legal text. (Resolves #9, #12, #16.)
- **Why it matters:** Users currently cannot reliably tell whether money has moved, and the most consequential screen has the coldest copy — a direct hit to novice confidence and a misread risk for experts.
- **How to fix it:** Status banner component ("Review — not yet submitted" vs "Completed · Filled"), a 3-step progress indicator, and a reassurance block above the declaration.
- **Effort estimate:** Medium Lift

### 5. Glossed jargon + efficiency shortcuts via progressive disclosure
- **What to fix:** Add inline tooltips/glosses on first use for novice-hostile terms ("troy ounce", "Filled = completed", define XAU/XAG, clarify Credit/Debit account) and carry FAQ definitions onto transactional screens; add a "Place another trade" shortcut and contextual next-actions (sell/download/set alert) on trade detail; label the swap control. (Resolves #15, #17, #21, #23.)
- **Why it matters:** Closes the novice comprehension gap and the expert efficiency gap simultaneously without sacrificing either — the core dual-persona resolution.
- **How to fix it:** Reusable tooltip/term component (collapsible for experts), labelled swap button, and contextual action bar on detail/success screens.
- **Effort estimate:** Medium Lift

---

## Design System & Consistency Notes

- **Primary action colour is unsystematised (#24):** slate-grey is the de-facto primary while OCBC red is never used for a primary action — red is instead spent on the Sell toggle and loss values, so the brand's most recognisable "this is the action" cue never marks the actual action. Decide one meaning for red and one consistent primary/secondary/tertiary button system.
- **Header/eyebrow component behaves three ways (#16):** inline top-left, in the left gutter with a red rule, or absent (overview). Standardise one eyebrow+H1 pattern.
- **Two divergent layouts for the same order-confirmation content (#9, #24):** success (grey page + white card + green check + blue "Back" link) vs trade-detail (white page, no card, outlined "Back" button, extra fields). Unify.
- **Three warning/banner treatments (#19):** tight field banner, large padded container, page banner with ×. Collapse to one banner component with size + severity variants, and visually separate blocking errors from soft warnings.
- **Formatting drift (#22):** "ounce" vs "ounces"; account numbers as `410-212232-201 - XAU` vs `XAU-410-212232-201` vs `647561400225-SGD`; "SGD/ounce" vs "SGD / ounce"; "Holdings details" vs "Holding details". Define and lint a single standard.
- **Rogue currency-flag usage (#10/#22):** the currency flag chip appears only inside the amount input, nowhere else. Apply consistently or remove.
- **Global chrome drift (#25):** nav reads "FX and Investment" vs "FX and treasury"; Search pill and help icon present on some screens only; design-spec frames mixed into the product set. Reconcile to one nav taxonomy and one header chrome; keep specs out of the production flow.

---

## WHAT'S WORKING WELL

1. **Persistent, top-aligned field labels** No placeholder-only labels in the trade panels — every input keeps its label visible, which is exactly right for a high-stakes form.
2. **Non-punitive, specific error-recovery copy** The spec'd errors tell the user *what* and *how to fix* with concrete thresholds ("Increase the investment amount to 24.59 SGD or more to proceed"; three recovery paths for insufficient balance). Once integrated on the live screen, this is exemplary.
3. **Sell-side guardrails** The sell flow pre-fills the XAU account and caps inputs to actual holdings ("Maximum 25.86 ounces / 158,484.99 SGD") — strong error prevention.
4. **The "without holding the physical metal" gloss and the empty holdings state** The one genuinely good plain-language explanation, paired with a proper illustrated zero-state and a clear "Start trading" CTA.
5. **Plain-language confirmation across channels** Success screen, trade detail, and email explain the mechanics in human terms ("the paper gold has been credited… the SGD amount has been debited") and share a consistent transaction reference number — good for trust and traceability.

---

## Suggested Next Audit Scope

1. **Live interaction & states audit (highest value):** the static frames can't confirm validation timing, focus/hover/keyboard accessibility, loading/skeleton states, or the live price refresh — audit a clickable prototype or staging build to verify the gaps flagged here (#2, #8, #20).
2. **Accessibility deep-dive (WCAG 2.2 AA):** formal contrast testing on the grey-on-grey labels (#20), colour-blind verification of Buy/Sell and gain/loss (#10), keyboard/screen-reader pass on the trade form, chart, and modals.
3. **Mobile/responsive audit:** this audit covered desktop; the notification mockups imply a mobile surface — audit the responsive Precious Metals trade flow on mobile web/app.
4. **Sell + alert end-to-end flows:** the live Sell review/confirm/success screens and the full set-price-alert creation flow (the captured artifacts were partly spec frames) deserve their own pass, including the alerts data-integrity bug (#13).
