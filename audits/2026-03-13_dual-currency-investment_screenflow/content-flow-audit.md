# OCBC Dual Currency Investment (DCI) -- Content & User Flow Audit

**Audit Date:** 13 March 2026
**Product:** OCBC Business Banking -- Dual Currency Investment (DCI)
**Platform:** Web (Desktop)
**Auditor:** Senior UX Auditor (AI-assisted)
**Screens Reviewed:** 20 screens across landing, placement, review, confirmation, monitoring, settlement, and reinvestment flows

**Personas Under Evaluation:**
- **Novice Investor** -- Unfamiliar with structured FX products; needs education and guardrails
- **Seasoned Investor** -- Understands DCI mechanics; wants efficient, frictionless execution

---

## Executive Summary

The OCBC DCI product flow demonstrates competent structural foundations -- the investment timeline, dual-scenario outcome display, and account selection patterns are directionally sound. However, the product suffers from **critical content gaps that expose both OCBC and its users to risk**: no in-flow risk disclosure, annualised yield presented without period return context, silent currency pair swaps during reinvestment, and financial jargon used without explanation. For a product where the user can receive principal back in a different (potentially depreciated) currency, these are not polish issues -- they are informed consent failures.

The novice investor is particularly underserved: the flow assumes existing knowledge of structured FX products, offers no progressive education, and buries risk information in an FAQ accordion that most users will never expand. The seasoned investor, while better equipped to navigate the terminology, faces unnecessary friction from missing inline validation, absent progress indicators, and a confirmation page that dead-ends without a link to monitor the investment.

**Overall Content & Flow Health Score: 4.5/10**
Rationale: Sound structural skeleton undermined by dangerous content omissions, inconsistent terminology, and missing safeguards for a high-stakes financial product.

---

## 1. User Flow Mapping

### Flow A: First-Time Investment Placement (5-7 steps)

```
Landing Page (Empty State)
    |
    v
[Place Investment] CTA
    |
    v
Investment Parameters Screen
  - Select investment amount + currency
  - Select currency pair (base / alternate)
  - Select tenor
  - Select strike price (radio buttons with yield)
  - View potential outcomes (Scenario A / B sidebar)
  - View investment timeline
    |
    v
[Next]
    |
    v
Account Selection Screen (Funding + Settlement accounts)
    |
    v
[Next]
    |
    v
Review Screen
  - Investment details summary
  - Account details
  - Potential outcomes (both scenarios)
  - Investment timeline
  - T&C consent (inline link, no checkbox)
    |
    v
[Submit]
    |
    v
Confirmation Screen
  - Success message + reference number
  - Investment timeline (collapsed by default)
  - [Place Another Investment] -- ONLY action available
    |
    (NO link to portfolio / investment details)
```

**Decision Points:** Currency pair selection, strike price selection (risk-return tradeoff), tenor selection
**Missing Decision Support:** No risk/return comparison tool, no "what happens if" calculator, no tooltip on strike price tradeoff

### Flow B: Investment Monitoring (2-3 clicks)

```
Landing Page (With Active Investments)
    |
    v
Click investment row in table
    |
    v
Investment Details Screen
  - "Expiring Soon" status badge (pre-expiry)
  - "Awaiting Settlement" status badge (post-expiry)
  - Settlement Outcome section (post-fixing)
  - Settlement Breakdown table
  - [Reinvest] button (post-settlement only)
  - [Download Termsheet] link
    |
    v
[Back] to landing
```

**Decision Points:** Whether to reinvest (only surfaces post-settlement)
**Gap:** No proactive notification or visual cue on landing page when an investment is approaching expiry beyond the "Expiring Soon" badge in the table

### Flow C: Reinvestment (4-5 clicks)

```
Investment Details (Awaiting Settlement)
    |
    v
[Reinvest]
    |
    v
Investment Parameters Screen (pre-filled)
  - Amount pre-filled from settlement total
  - Currency pair MAY SILENTLY SWAP (see Finding #1)
  - New strike prices and yields shown
  - New timeline shown
    |
    v
[Next]
    |
    v
Account Selection Screen
    |
    v
[Next]
    |
    v
Review Screen
    |
    v
[Submit]
    |
    v
Confirmation Screen
```

**CRITICAL Decision Point:** Currency pair swap on "Strike Not Met" reinvestment is not flagged or explained

### Flow D: Account Setup Gate (Dead End)

```
User navigates to DCI without Multi-Currency Account
    |
    v
Gate Screen: "Multi-Currency Account Required"
    |
    v
[Open Multi-Currency Account] -- single CTA
    |
    (No timeline, no alternative path, no "learn more", no back navigation context)
```

---

## 2. Financial Terminology Audit

Each term is scored on a 1-5 comprehensibility scale (1 = requires specialist knowledge, 5 = plain language).

| Term | Score | Where Used | Issue | Recommendation |
|------|-------|-----------|-------|----------------|
| **Strike Price** | 1/5 | Parameters screen, Details screen, Settlement outcome | Core mechanic of the product but never defined in-flow. Presented as radio buttons with values like "1.2850" with no explanation of what selecting a different strike means for the user's risk. | Add tooltip: "The exchange rate that determines your investment outcome. If the market rate is above/below this rate at expiry, your settlement currency changes." Add contextual help icon next to the radio group header. |
| **Fixing Rate** | 1/5 | Details screen (post-settlement) | Appears only after settlement with no prior introduction. "Fixing Rate: 1.3000" tells the user nothing about what "fixing" means or who determines it. | Rename to "Market Rate at Expiry" with a subtitle "(Determined by OCBC as Calculation Agent)". The current label "FX Fixing as determined by OCBC as Calculation Agent" is buried above the outcome banner. |
| **Tenor** | 2/5 | Parameters screen, Details screen, Landing table | Financial jargon for "investment duration." Some users may guess from context (dropdown showing "1 Month", "1 Week") but the label itself is opaque. | Rename to "Investment Duration" or "Investment Period". Keep "Tenor" as a parenthetical for seasoned users: "Investment Period (Tenor)". |
| **Indicative Yield** | 2/5 | Parameters screen (strike price radio labels) | "6.50% Indicative yield" appears next to each strike price. "Indicative" implies it might change, but no explanation of when or why. Critically, this is an ANNUALISED figure shown alongside 1-week and 1-month tenors. | (a) Clarify "indicative" means rate may change before order confirmation. (b) Show BOTH annualised and period return: "6.50% p.a. (~0.54% for 1 month)". |
| **Indicative Annual Yield** | 2/5 | Details screen header | Same annualisation issue. "6.50% p.a." for a 1-month investment is technically correct but psychologically misleading -- it implies a return ~12x the actual period return. | Always pair with absolute period return in dollars: "6.50% p.a. (estimated return: ~USD 1,083 for this 1-month investment)". |
| **Base Currency / Alternate Currency** | 3/5 | Parameters screen, Details screen, Account selection | Reasonably clear from context (flags + currency codes help). However, the relationship to outcomes is not explicit -- user must infer that "Scenario A = stay in base" and "Scenario B = convert to alternate." | Add a one-line explainer below the currency pair: "If strike price is met, you receive base currency (USD). If not met, your funds are converted to alternate currency (SGD)." |
| **Value Date** | 2/5 | Timeline section | "When funds are deducted and investment starts" -- the description is helpful, but the term itself is banking jargon. The description text is small and easy to miss. | Rename to "Investment Start Date" with "(Value Date)" parenthetical. |
| **Expiry Date (Fixing)** | 2/5 | Timeline section, Details screen | "Fixing date determining investment outcome" -- again, the parenthetical "(Fixing)" adds jargon rather than clarity. Users must understand both "expiry" and "fixing" simultaneously. | Rename to "Outcome Determination Date" or simply "Expiry Date" and remove "(Fixing)". Explain in the description: "The date when the market rate is compared to your strike price to determine your payout currency." |
| **Maturity Date** | 3/5 | Timeline section | "When payout is credited to your account" -- reasonably clear. Term is widely understood. | Acceptable. Could simplify to "Payout Date" for maximum clarity. |
| **Settlement Amount** | 3/5 | Scenarios panel, Settlement breakdown | Clear in context but users need to understand this is principal + yield, not just yield. The breakdown table on the details screen makes this clear. | Acceptable on details screen. On the parameters screen scenarios, add a line showing the calculation: "200,000.00 + 1,083.33 = 201,083.33 USD". |
| **Current Spot Rate (Indicative)** | 2/5 | Parameters screen | "1 USD = 1.2800 SGD" is clear, but "(Indicative)" and the timestamp raise questions about rate validity and how often it refreshes. | Add "Refreshes every X minutes" or "Rate valid for approximately X minutes." Make the refresh icon more prominent. |

**Overall Terminology Score: 2.1/5** -- The product leans heavily on institutional finance vocabulary without adequate contextual explanation for a digital self-service channel.

---

## 3. Risk Disclosure Assessment

### DCI-Specific Risks That Must Be Communicated

| Risk | Disclosed In-Flow? | Location | Adequacy |
|------|-------------------|----------|----------|
| **Principal currency conversion risk** (receiving funds in depreciated alternate currency) | NO | FAQ accordion only ("What are the risks...") | CRITICAL gap. The core risk of the product -- that you may get back a different currency worth less than your original investment -- is never stated during the placement flow. |
| **Opportunity cost** (locked funds, cannot withdraw early) | NO | Not visible in any screen | Not disclosed anywhere in the reviewed screens. |
| **Yield is not guaranteed** ("indicative" qualifier) | PARTIAL | "Indicative" label on yield | The word "indicative" is used but its implications are not explained. |
| **No capital protection** | NO | Not visible in flow | Not disclosed. DCI is not a deposit and not protected by deposit insurance. This is a regulatory-grade omission. |
| **Counterparty risk** (OCBC as calculation agent) | MINIMAL | Small text on settlement screen | "FX Fixing as determined by OCBC as Calculation Agent" appears on the details screen but not during placement. |
| **Market risk on alternate currency** | NO | Not in flow | If strike is not met and user receives SGD, the SGD may further depreciate before they can convert back. Not mentioned. |

### Risk Disclosure Placement Recommendation

A risk acknowledgment step MUST be added to the placement flow, ideally between the Parameters screen and the Account Selection screen. This should:

1. Summarise the two possible outcomes in plain language with concrete numbers from the user's own investment parameters
2. Explicitly state: "If the market moves against you, you will receive [alternate currency] which may be worth less than your original [base currency] investment"
3. Require affirmative acknowledgment (checkbox, not just a scrollable T&C link)
4. For first-time DCI users, consider a mandatory educational interstitial

---

## 4. Form Analysis

### Parameters Screen (day-1-add-delete-users-3.png)

| Element | Current State | Issue | Severity |
|---------|--------------|-------|----------|
| **Investment Amount field** | Shows "200,000.00" with "Minimum amount $0,000.00 USD" below | The minimum amount displays "$0,000.00" which is clearly a formatting bug -- either the minimum is $0 (unlikely) or the template failed to populate. This undermines trust in a financial product. | HIGH |
| **Currency pair selection** | Base/Alternate dropdowns with flags | No explanation of what "base" and "alternate" mean in the DCI context. User must already know. | MEDIUM |
| **Strike Price radio buttons** | 5 options with "% from spot" labels and "Indicative yield" | No default selected on initial load (unconfirmed). The relationship between strike distance from spot and yield is shown numerically but not explained conceptually ("further from spot = higher yield but higher conversion risk"). | HIGH |
| **Tenor dropdown** | Shows "1 Month" | Only one option visible; unclear if other tenors are available without clicking. No explanation of how tenor affects risk/return. | MEDIUM |
| **Required field indicators** | None visible | No asterisks or other indicators for required fields. For a financial form, every field is presumably required, but this should be explicit. | LOW |
| **Inline validation** | None visible | No validation feedback shown. What happens if user enters amount below minimum? Above maximum? Non-numeric input? No designs for these states. | HIGH |
| **Potential Outcomes panel** | Shows Scenario A and B with amounts | Scenario B does NOT show the equivalent value in the base currency. User sees "257,000.00 SGD" but cannot assess whether this is a gain or loss versus their original 200,000 USD. | CRITICAL |

### Account Selection Screen (reinvest-step-2 screens)

| Element | Current State | Issue | Severity |
|---------|--------------|-------|----------|
| **Funding Account dropdown** | Pre-selected with account details | "Show available balance" link is present but collapsed -- balance should be visible by default for a financial transaction. | MEDIUM |
| **Settlement Account labels** | "Settlement Account - Base Currency (SGD)" / "Settlement Account - Alternate Currency (EUR)" | Labels are clear and correctly differentiated. Helper text ("Funds will be credited here if settlement is in SGD") is useful. | -- (Working well) |
| **No "Add Account" option** | Only existing accounts shown | If user doesn't have the right currency account, there's no path to create one from this screen. | LOW |

### Review Screen (review.png)

| Element | Current State | Issue | Severity |
|---------|--------------|-------|----------|
| **Edit links** | "Edit" pencil icons on Investment Details and Accounts sections | Good -- allows correction without restarting. | -- (Working well) |
| **T&C consent** | "By clicking 'Submit', you confirm that you have read, understood and agree to the Terms and Conditions." (inline link, no checkbox) | For a financial product with principal risk, passive consent (implied by clicking Submit) may not meet regulatory requirements. An active checkbox is standard practice. | HIGH |
| **Scenario display** | Both scenarios shown with amounts | Same issue as parameters screen: Scenario B shows only alternate currency amount without base currency equivalent. | CRITICAL |
| **Review screen terminology** | Uses "spot rate" in scenario conditions | Review says "If spot rate >= 1.2850 at maturity" but the parameters screen says "If fixing rate is >= 1.2850 on expiry." Different terms for the same concept on sequential screens. | MEDIUM |

---

## 5. Content Gaps

### 5.1 Missing Content (Not Designed)

| Gap | Impact | Priority |
|-----|--------|----------|
| **Error states for all form fields** | Users encountering validation errors will see no feedback, potentially submitting invalid data or getting stuck | CRITICAL |
| **Loading/processing states** | For a financial transaction, the absence of a processing state between Submit and Confirmation creates anxiety ("Did it go through?") | HIGH |
| **Session timeout handling** | Mid-flow timeout with no save state means users lose all input. For a multi-step financial form, this is a significant friction risk. | HIGH |
| **Rate expiry / staleness warning** | Spot rate shown is timestamped but there's no warning when the rate is stale or when the quoted yields may no longer be valid | HIGH |
| **Cancellation flow** | No cancel/exit confirmation. User clicking browser back or navigating away loses all progress silently. | MEDIUM |
| **Insufficient funds state** | No design for what happens if funding account has insufficient balance | HIGH |
| **Maximum investment amount** | Only minimum is shown (and it's bugged). No maximum limit communicated. | MEDIUM |
| **Print/save/email confirmation** | Confirmation screen shows reference number but no way to save or share the confirmation details | MEDIUM |
| **Investment amendment/cancellation post-submission** | No information about whether the investment can be cancelled after submission and before value date | MEDIUM |

### 5.2 Terminology Inconsistencies Across Screens

| Inconsistency | Screens Affected | Risk |
|---------------|-----------------|------|
| "Transaction Date" (timeline/details) vs "Trade Date" (FAQ) | Parameters, Review, Details vs FAQ accordion | User searching FAQ for "Transaction Date" won't find it; creates perception of different dates |
| "If fixing rate is >= 1.2850 on expiry" (parameters) vs "If spot rate >= 1.2850 at maturity" (review) | Parameters screen vs Review screen | Same condition described with different rate names ("fixing rate" vs "spot rate") AND different time references ("on expiry" vs "at maturity") |
| "Expiry Date (Fixing)" (timeline) vs "Expiry Date" (details header) | Timeline section vs Investment Details header | Inconsistent parenthetical usage |
| "FX and Investment" (most screens) vs "FX and Treasury" (details screens) | Navigation bar | Different nav labels across the same product flow |
| Landing page header shows "Earning Days: 1" but details show "Tenor: 1 Week" / "Tenor: 1 Month" | Landing table vs Details screen | "Earning Days" is a different concept from "Tenor" but their relationship is not explained |

### 5.3 Missing Educational Content

| Content Need | Where It Should Appear | Why |
|-------------|----------------------|-----|
| "What is a Dual Currency Investment?" -- 2-sentence plain-language explainer | Top of Parameters screen (first-time users) | The FAQ on landing has this, but once user enters the flow, all educational content disappears |
| Strike price selection guide | Above strike price radio buttons | User is making a risk-return decision with no guidance on what "further from spot" means practically |
| "How is my return calculated?" worked example | Below or within Potential Outcomes panel | Showing the math (principal x rate x tenor = yield) builds understanding and trust |
| "What happens next?" post-confirmation | Confirmation screen | User has just committed funds but has no idea what to expect (when funds debit, when they'll see the investment in their portfolio, how they'll be notified of outcome) |

---

## 6. Detailed Findings

### CRITICAL Findings

| # | Screen | Dimension | Severity | Finding | Novice Impact | Seasoned Impact | Recommendation |
|---|--------|-----------|----------|---------|---------------|-----------------|----------------|
| 1 | Reinvest Step 1 (Strike Not Met) | Content / Risk | CRITICAL | **Silent currency pair swap on reinvestment.** When strike price is NOT met (EUR/SGD investment settles in SGD), the reinvestment screen shows base currency as SGD and alternate as EUR -- the REVERSE of what the user originally invested. The user's original USD/SGD pair has been replaced with SGD/EUR. There is no banner, warning, or explanation that the currency pair has changed. | Novice will not notice the swap. They will believe they are "continuing" their original investment when they are actually entering a fundamentally different trade with different currency risk. Potential for significant unintended FX exposure. | Seasoned investor will likely notice but will find the silent swap presumptuous. They may have wanted to convert back to their original base currency rather than entering a new pair. Wastes time if they need to manually reconfigure. | (a) Add a prominent banner at the top of the reinvestment parameters screen: "Your settlement was in [SGD]. Your new investment will use [SGD] as the base currency. This is different from your original investment pair [USD/SGD]." (b) Offer a choice: "Reinvest in same pair (USD/SGD)" vs "Invest settlement proceeds (SGD/EUR)". (c) Pre-select the original pair by default if possible. |
| 2 | Parameters + Review | Content / Risk | CRITICAL | **Scenario B does not show base-currency equivalent value.** When the alternate currency outcome is shown (e.g., "257,000.00 SGD" or "258,392.17 SGD"), there is no comparison to the original investment amount in USD. The user cannot determine whether they are gaining or losing money in Scenario B without performing mental FX arithmetic. | Novice sees "258,392.17 SGD" and may interpret the large number as a gain, when in reality the USD equivalent could represent a loss. This is a fundamental informed consent issue -- the user cannot evaluate the risk of the product. | Seasoned investor can estimate the FX impact mentally but shouldn't have to. The absence of this comparison is a friction point and a trust issue -- it looks like the product is hiding the downside. | Add a line below Scenario B's settlement amount: "Equivalent to approximately ~USD [X] at current spot rate" with a note "(actual value will depend on exchange rate at maturity)". Flag in red if the equivalent is below the original investment amount. |
| 3 | Entire Placement Flow | Risk Disclosure | CRITICAL | **No explicit risk disclosure within the placement flow.** The only risk information is in an FAQ accordion on the landing page ("What are the risks involved in investing in DCI?") which users must (a) see, (b) choose to expand, and (c) read before entering the flow. Once inside the placement flow, there is zero risk language. The T&C link on the review screen is the only legal safeguard. | Novice will complete the entire investment placement without encountering a single explicit statement that they could receive their money back in a different, potentially less valuable currency. This is an informed consent failure. | Seasoned investor understands the risks but the absence of disclosure creates legal and regulatory exposure for OCBC. In a dispute, the bank cannot demonstrate that the user was warned during the transaction flow. | Insert a dedicated "Risk Acknowledgment" step between Parameters and Account Selection. Content should include: (a) plain-language statement of both outcomes with the user's actual numbers, (b) explicit statement that principal may be returned in a different currency, (c) statement that this is not a deposit and not capital-protected, (d) active checkbox: "I understand and accept these risks." |
| 4 | All Form Screens | Forms / System Status | CRITICAL | **No error states, validation feedback, or loading states designed.** Across all screens (parameters, account selection, review, confirmation), there are no designs for: inline field validation errors, form submission failures, network timeout states, processing/loading indicators, or session expiry warnings. For a financial transaction flow, this is a critical design gap. | Novice encountering an error will have no feedback about what went wrong or how to fix it. Could lead to duplicate submissions, abandoned transactions, or lost confidence. | Seasoned investor expects enterprise-grade reliability indicators. The absence of loading states during submission is anxiety-inducing when real money is at stake. | Design and implement: (a) inline validation for investment amount (min/max, numeric format), (b) a processing overlay with spinner for submission, (c) error state with retry option for submission failures, (d) session timeout warning with save/extend option, (e) insufficient funds error with link to fund account. |

### HIGH Findings

| # | Screen | Dimension | Severity | Finding | Novice Impact | Seasoned Impact | Recommendation |
|---|--------|-----------|----------|---------|---------------|-----------------|----------------|
| 5 | Parameters Screen | Content / Cognitive Load | HIGH | **Yield shown as annualised rate without period return.** "6.50% p.a." for a 1-month investment implies ~78% annual return to the casual reader. The actual period return is ~0.54%, or ~USD 1,083 on a USD 200,000 investment. This is industry-standard presentation but misleading in a self-service digital channel. | Novice reads "6.50%" and dramatically overestimates the return. May make investment decisions based on inflated expectations. When the actual dollar return appears in the scenario panel, the disconnect causes confusion. | Seasoned investor understands annualisation but still benefits from seeing the period return for quick mental math. The absence is an unnecessary cognitive burden. | Show both: "6.50% p.a. (~0.54% for 1 month)" on the strike price radio buttons. In the Potential Outcomes panel, add a line: "Estimated return: USD 1,083.33 (0.54% of principal)". |
| 6 | Parameters Screen | Forms / Content | HIGH | **"$0,000.00 USD" minimum amount display bug.** The minimum investment amount below the input field shows "$0,000.00 USD" which is clearly a template/formatting error. In a financial product, displaying a malformed monetary value undermines trust. | Novice may interpret this as "no minimum" or be confused by the formatting. Either way, trust in the platform's accuracy is damaged at the very first input field. | Seasoned investor immediately recognizes this as a bug and questions the reliability of other displayed values (spot rates, yields, settlement amounts). | Fix the data binding to display the actual minimum amount (e.g., "Minimum amount: USD 50,000.00"). Ensure the currency symbol and format are consistent with the selected currency. |
| 7 | Confirmation Screen | Navigation / Flow | HIGH | **Confirmation page is a dead end -- no link to portfolio or investment details.** After successfully placing an investment, the only CTA is "Place Another Investment." There is no link to "View Investment Details," "Return to Portfolio," or "View All Investments." The user must manually navigate back via the top navigation. | Novice wants reassurance that the investment is "in the system." Without a direct link to view it, they may feel uncertain and navigate around trying to find it, potentially getting lost. | Seasoned investor who has just placed an investment wants to immediately verify it in their portfolio. Being forced to navigate manually is a 2-3 click tax on every transaction. | Add at minimum two CTAs: (a) Primary: "View Investment Details" (links to the newly created investment's detail page), (b) Secondary: "Place Another Investment" (existing). Also add: "Return to DCI Portfolio" text link. |
| 8 | Review Screen | Content / Terminology | HIGH | **Scenario condition language differs between Parameters and Review screens.** Parameters screen: "If fixing rate is >= 1.2850 on expiry." Review screen: "If spot rate >= 1.2850 at maturity." These describe the same condition but use different rate names and different time references, potentially confusing users into thinking they are different conditions. | Novice may believe these are two different conditions and become confused about when and how the outcome is determined. | Seasoned investor will recognize they are the same but the inconsistency erodes confidence in the product's attention to detail. | Standardise language across ALL screens. Recommended: "If the market exchange rate is at or above [strike price] on the Expiry Date ([date])". Use this exact phrasing on parameters, review, and details screens. |
| 9 | Multi-Currency Account Gate | Navigation / Flow | HIGH | **Account gate is a dead end with no context.** The screen says "Multi-Currency Account Required" with a single CTA "Open Multi-Currency Account." There is no: estimated processing time, list of required documents, alternative paths, explanation of what a Multi-Currency Account is, or back/cancel navigation. | Novice encounters this wall with no information about what's needed, how long it takes, or whether they even want to proceed. High bounce probability. May abandon DCI interest entirely. | Seasoned investor is frustrated by the lack of timeline information. They need to plan around account opening before they can invest, but have no data to plan with. | Redesign the gate to include: (a) brief explanation of Multi-Currency Account purpose, (b) estimated opening time ("typically X business days"), (c) required documents list, (d) "Learn More About DCI" link to maintain interest, (e) "Back to FX and Investment" navigation link. |
| 10 | Parameters Screen | Content / Cognitive Load | HIGH | **Strike price selection provides no decision-support context.** Five strike price options are presented as radio buttons with "% from spot" and "Indicative yield" labels, but there is no explanation that selecting a strike further from spot increases yield but also increases the probability of currency conversion. The tradeoff is the core decision of the product. | Novice has no framework for choosing between 1.2830 and 1.2870. The only differentiator they can see is the yield percentage, which naturally biases them toward the highest yield (furthest strike) without understanding the increased conversion risk. | Seasoned investor understands the tradeoff but would benefit from probability estimates or historical context. The current presentation assumes knowledge that even experienced investors may not have for specific currency pairs. | (a) Add a header explainer: "A strike price closer to the current spot rate offers lower yield but lower chance of currency conversion. A strike further away offers higher yield with higher conversion chance." (b) Consider adding a visual risk-return spectrum. (c) Optionally show historical probability: "Based on the past 12 months, the fixing rate was below this strike X% of the time." |

### MEDIUM Findings

| # | Screen | Dimension | Severity | Finding | Novice Impact | Seasoned Impact | Recommendation |
|---|--------|-----------|----------|---------|---------------|-----------------|----------------|
| 11 | All Flow Screens | Navigation / Flow | MEDIUM | **No step/progress indicator in the placement flow.** The multi-step flow (Parameters > Account Selection > Review > Confirmation) has no progress bar, step counter, or breadcrumb. Users do not know how many steps remain. | Novice cannot estimate time commitment. May abandon mid-flow if they feel it's "going on too long" without knowing they're one step from completion. | Seasoned investor prefers efficiency signals. Not knowing whether "Next" leads to one more screen or three creates mild frustration. | Add a step indicator: "Step 1 of 3: Investment Parameters" / "Step 2 of 3: Account Selection" / "Step 3 of 3: Review & Submit". |
| 12 | Landing Page (Active) | Content / Terminology | MEDIUM | **Landing page table uses "Earning Days" column** alongside "Tenor" in other screens. These represent related but different concepts (earning days = actual calendar days the investment earns; tenor = the investment period label like "1 Month" or "1 Week"). The relationship is never explained. | Novice sees "Earning Days: 1" for a new investment and doesn't understand why a "1 Month" investment shows "1" earning day (likely because it was just placed). Confusing. | Seasoned investor can infer the meaning but finds the inconsistency with "Tenor" labels used elsewhere unnecessary. | Either (a) add "Tenor" as a column and remove "Earning Days," or (b) show both with a clear label: "Earning Days: 1 of 30 (1 Month Tenor)". |
| 13 | Landing Page (Active) | Visual Hierarchy / Content | MEDIUM | **"Expiring Soon" status in the table uses orange badge but no urgency context.** The investment row shows an orange "Expiring Soon" badge but provides no information about WHEN it expires. The user must click into the detail screen to find the expiry date. | Novice may not understand the urgency or what action (if any) they should take. | Seasoned investor wants to triage quickly without clicking into each investment. Missing expiry date in the table row forces unnecessary navigation. | Add the expiry date inline in the table row, or as a tooltip on the badge: "Expires 10 Nov 2025 (2 days)". |
| 14 | Account Selection Screen | Forms / Content | MEDIUM | **Funding account balance hidden behind "Show available balance" link.** The available balance in the funding account is not shown by default -- user must click to reveal it. For a financial transaction, knowing whether you have sufficient funds should not require an extra click. | Novice may not realize they need to check their balance and could proceed to submit only to encounter an error (which is itself not designed). | Seasoned investor routinely wants to verify balance. The extra click is a minor annoyance per transaction but compounds across repeated use. | Show the available balance by default below the account selector, with an option to hide it for security if needed. |
| 15 | Confirmation Screen | Content / Trust | MEDIUM | **No "what happens next" information on confirmation.** After submission, the user sees a green checkmark and a reference number but no information about: when funds will be debited, when the investment appears in their portfolio, how they'll be notified of the outcome, or what the next key date is. | Novice feels uncertain about what they've just committed to. "Investment Placed Successfully!" confirms the action but not the expectations. They may check their account repeatedly looking for the debit. | Seasoned investor knows the process but still appreciates a confirmation email/notification setup and timeline reinforcement. | Add below the success message: "What happens next: (1) Funds will be debited from your account on [Value Date]. (2) You can track your investment in the DCI Portfolio. (3) The outcome will be determined on [Expiry Date] at 2:00 PM SGT. (4) Settlement proceeds will be credited on [Maturity Date]." |
| 16 | Investment Details (Expiring Soon) | Content / Navigation | MEDIUM | **"Expiring Soon" details screen shows no action options.** The screen shows the investment is about to expire but offers no actions -- no "what to expect" content, no "prepare to reinvest" option, no reminder setup. Only a "Back" button and "Download Termsheet" link. | Novice doesn't know what happens when the investment expires. The screen is informational but not actionable, creating anxiety without resolution. | Seasoned investor may want to set a reinvestment preference or prepare settlement account allocations in advance. No affordance for this. | Add: (a) "What happens at expiry" explainer section, (b) "Set Reinvestment Preference" option (even if it's just a notification preference), (c) countdown or date prominence: "Expires in 2 days (10 Nov 2025, 2:00 PM SGT)". |
| 17 | Investment Details (Awaiting Settlement - Strike Not Met) | Content / Clarity | MEDIUM | **Settlement outcome banner uses "Strike Price Not Met" terminology without plain-language explanation.** The green/orange banner reads: "Fixing rate 1.4621 was below strike price of 1.4750. You will receive your principal plus yield converted to 281,332.90 SGD on maturity." This is technically accurate but frontloads jargon before the user impact. | Novice must parse three financial terms (fixing rate, strike price, converted) before understanding what happened to their money. Many will not fully comprehend the sentence. | Seasoned investor finds this acceptable but would prefer the key information (what currency, what amount) more prominently displayed. | Restructure to lead with the outcome: "Your investment will be settled in SGD (alternate currency). You will receive SGD 280,735.90 on [Maturity Date]." Then add the technical detail as a secondary line: "The market rate (1.4621) was below your strike price (1.4750), so your funds are converted to SGD." |
| 18 | Parameters Screen | Content / Trust | MEDIUM | **Spot rate timestamp format inconsistent and lacks refresh clarity.** "As at 17 Nov 2025, 15:05:28" -- the timestamp is precise but there's no indication of refresh frequency, whether the rate is live, or what happens if it becomes stale during the session. The small refresh icon is not labelled. | Novice doesn't know if this rate is "current enough" to be reliable. May worry that the rate will change between viewing and submitting. | Seasoned investor is accustomed to indicative rates but still wants confidence in freshness. In FX, seconds matter. | Add "Rate refreshes automatically" or "Live rate -- updates every 30 seconds" label. Make the refresh icon a clickable "Refresh Rate" button with timestamp. |
| 19 | Navigation Bar | Content / Consistency | MEDIUM | **Navigation label inconsistency: "FX and Investment" vs "FX and Treasury."** The top navigation shows "FX and Investment" on most screens but switches to "FX and Treasury" on the Investment Details screens (post-settlement). This suggests different underlying systems or page templates have leaked into the user-facing navigation. | Novice may think they've navigated to a different section of the platform, causing disorientation. | Seasoned investor notices the inconsistency and questions whether they're viewing the same product module. | Standardise to a single label across all DCI screens. Recommended: "FX and Investment" as it's more user-friendly than "Treasury." |

### LOW Findings

| # | Screen | Dimension | Severity | Finding | Novice Impact | Seasoned Impact | Recommendation |
|---|--------|-----------|----------|---------|---------------|-----------------|----------------|
| 20 | Landing Page | Content / Tone | LOW | **Landing page value propositions are generic and marketing-heavy.** "Maximise your investment returns" and "Great for currency conversion needs" are vague value props that don't differentiate DCI from a deposit or FX forward. | Novice doesn't learn anything specific about DCI from these cards. | Seasoned investor ignores marketing content. No impact. | Replace with specific, factual value props: "Earn yields of X-Y% p.a. on your idle foreign currency" and "Choose your preferred conversion rate and earn returns while you wait." |
| 21 | Landing Page (Active) | Content | LOW | **Summary metrics at top ("Active Investments: 4, Earning Days: 1, Total Invested Amount: 1,500,000.00 SGD, Avg. Yield: 2.7% p.a.") mix currencies without disclosure.** "Total Invested Amount" is shown in SGD but includes USD and EUR investments. The conversion basis is not stated. | Novice may not realize the total is a cross-currency aggregate and take it at face value. | Seasoned investor recognizes the aggregation issue but finds it sloppy. | Add "(SGD equivalent)" label and a note: "Converted at current indicative rates" or show totals per currency. |
| 22 | Currency Dropdown | Forms | LOW | **Currency dropdown shows limited selection (6 currencies) with no indication of completeness.** CAD, CHF, DKK, EUR, SGD, USD are shown. User doesn't know if this is the full list or if scrolling reveals more options. The "All" label at top is ambiguous. | Minimal impact -- most users will find their currency. | Seasoned investor dealing in GBP, JPY, AUD, or other major currencies may assume the product doesn't support their pair. | Add a count: "6 available currencies" or ensure the list is clearly complete. If more currencies exist, ensure the scrollbar is more visible. |
| 23 | Reinvest Step 2 (Account Selection) | Content | LOW | **Account selection help text says "Funds will be credited here if settlement is in EUR/SGD"** but doesn't explain the conditions under which each scenario occurs. | Novice knows WHERE funds go but not WHEN each account applies. | Minimal impact. | Add: "If strike is met, funds settle in [base currency] to this account. If not met, funds convert to [alternate currency] and settle to the other account." |

---

## 7. What's Working Well

1. **Investment Timeline component is excellent.** The vertical timeline showing Transaction Date, Value Date, Expiry Date, and Maturity Date with plain-language descriptions ("When funds are deducted and investment starts") is one of the best-designed elements in the flow. It provides temporal context that is essential for a time-bound product. It appears consistently across Parameters, Review, Confirmation, and Details screens.

2. **Dual-scenario outcome display is structurally sound.** Showing both Scenario A (base currency settlement) and Scenario B (alternate currency settlement) side-by-side is the correct design pattern for a DCI product. The colour-coded "Base Currency" / "Alternate Currency" badges provide quick visual differentiation. The structure is right even though the content within it (missing base-currency equivalent in Scenario B) needs improvement.

3. **Settlement breakdown table on the Details screen is clear and well-structured.** The table showing Principal + Yield = Total Settlement with green-highlighted yield amount makes the return calculation transparent. This is the kind of financial transparency that should be replicated earlier in the flow (on the Parameters and Review screens).

4. **Review screen with inline Edit links supports non-linear correction.** The ability to edit Investment Details or Account selection directly from the Review screen without restarting the flow respects the user's time. The pencil icon is a recognised affordance.

5. **Currency pair display with flags is effective.** Using country flags alongside currency codes (e.g., the US flag next to "USD", the Singapore flag next to "SGD") provides instant visual recognition and reduces the cognitive load of reading currency codes. This is well-implemented across all screens.

6. **Account selection clearly differentiates base and alternate currency settlement accounts.** The labels "Settlement Account - Base Currency (USD)" and "Settlement Account - Alternate Currency (SGD)" with helper text explaining which scenario triggers which account are well-designed and reduce confusion about fund flows.

7. **"Download Termsheet" link on Investment Details** provides a document trail for the investment, which is important for business banking users who need records for compliance or reporting.

---

## Appendix: Screen Inventory

| Screen | File | Key Content Elements |
|--------|------|---------------------|
| Landing (Empty) | renew-landing-uploaded-file.png | Value props, empty portfolio, FAQ accordion, Place Investment CTA |
| Landing (Active) | renew-landing-uploaded-file-3.png | Portfolio summary, investment table, status badges, filters |
| Parameters | day-1-add-delete-users-3.png | Investment amount, currency pair, tenor, strike price, scenarios, timeline |
| Review | review.png | Summary of all selections, scenarios, timeline, T&C, Submit |
| Confirmation | overseas-confirmation-maker-collapsed.png | Success message, reference number, timeline, Place Another CTA |
| MCA Gate | confirm-omc.png | Multi-Currency Account required message, Open Account CTA |
| Details (Expiring Soon) | investment-details-expiring-soon.png | Investment overview, no settlement data, no action options |
| Details (Strike Met) | investment-details-awaiting-settlement-strike-price-met.png | Settlement outcome (base currency), breakdown, Reinvest CTA |
| Details (Strike Not Met) | investment-details-awaiting-settlement-strike-price-not-met.png | Settlement outcome (alternate currency), breakdown, Reinvest CTA |
| Reinvest Step 1 (Strike Met) | reinvest-step-1-strike-price-met.png | Pre-filled parameters, USD/SGD pair maintained |
| Reinvest Step 1 (Strike Not Met) | reinvest-step-1-strike-price-not-met.png | Pre-filled parameters, SGD/EUR pair (SWAPPED from original) |
| Reinvest Step 2 (Strike Met) | reinvest-step-2-strike-price-met.png | Account selection for USD-based reinvestment |
| Reinvest Step 2 (Strike Not Met) | reinvest-step-2-strike-price-not-met.png | Account selection for SGD-based reinvestment |
| Currency Dropdown | currency-dropdown.png | 6 currencies with flags and search |

---

*Report generated: 13 March 2026 | Methodology: Senior UX Audit framework with dual-persona evaluation (Novice/Seasoned Investor)*
