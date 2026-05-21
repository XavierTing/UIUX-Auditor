# Content & Flow Audit — OCBC Dual Currency Investment (DCI)

**Audit Date:** 2026-03-13
**Product:** OCBC Business Banking — Dual Currency Investment
**Platform:** Web (Desktop)
**Auditor Role:** Agent 2 — Content & Flow Analysis

---

## Screen-by-Screen Content Inventory

### 1. DCI Landing Page (`renew-landing-uploaded-file.png`)

**Navigation State:** Top nav "FX and Investment" active (underlined). No breadcrumbs. No sub-navigation.

**Page Title:** "DUAL CURRENCY INVESTMENT" (all-caps, small text, positioned as section label)

**Hero Banner:**
- Heading: "Ready to invest?"
- Subtext: "Turn your foreign currency needs into potential for better returns"
- CTA Button: "Place investment" (white outline button on dark background)

**Value Proposition Cards (2 cards):**
- Card 1 — "Maximise your investment returns": "Strategically manage your excess cash with potentially higher returns compared to traditional deposits, making your capital work harder for you."
- Card 2 — "Great for currency conversion needs": "If you need to convert currencies to fund overseas suppliers, investments, or education, Dual Currency Investments give you the flexibility to hold and manage the alternate currency for conversions."

**Investment List Section:**
- Filter dropdowns: "All Currencies", "Status", "Tenor"
- Search field: magnifying glass icon with placeholder
- Empty state illustration with text: "Start your first Dual Currency Investment and unlock higher potential returns"
- Link: "Place investment" (with globe icon)

**FAQ Section:**
- Heading: "FREQUENTLY ASKED QUESTIONS" (all-caps)
- Accordion items (all collapsed by default):
  1. "What is a Dual Currency Investment (DCI)?"
  2. "How does it work?"
  3. "What are the risks involved in investing in Dual Currency Investment (DCI)?"
  4. "What are the key milestone dates when investing in Dual Currency Investment (DCI)?"

**Footer:** "OCBC. All Rights Reserved." | "Conditions of Access | Security & Privacy"

---

### 2. DCI Landing with FAQ Expanded (`renew-landing-uploaded-file-2.png`)

Same layout as above but with FAQ content visible:

**"What is a Dual Currency Investment (DCI)?" — expanded:**
"Dual Currency Investment product is a capital at risk currency linked structured investment which involves a currency option that offers potential enhanced interest to the investor. In addition, DCI provides investors the opportunity to receive the alternate currency that they need at a better exchange rate than the exchange rate on the day they invest."

**"How does it work?" — expanded:**
"Suppose an investor wants to invest USD 500,000 into a dual currency investment with a 3 month tenor, using SGD as the alternate currency."

Includes a table with:
- Indicative pricing parameters: Base currency (USD), Alternate currency (SGD), Tenor (3 months), Spot rate (1.3800), Strike (1.3660), Fixing date/time (2 business days before maturity, at 2pm Singapore time), DCI Yield (6.53% p.a.), USD/SGD exchange rate (Exchange rate on fixing date/time)
- Payoff at maturity table showing two conversion rate scenarios with principal plus enhanced yield calculations

**"What are the risks involved..." — expanded:**
Bullet points covering:
- DCI is not equivalent to Time Deposits; it is a structured product with embedded derivatives; not insured by Deposit Insurance and Policy Owners' Protection Schemes Act of Singapore
- The investor could lose all or a substantial part of their original amount invested in certain events
- If the Bank defaults on its obligations, recovery amount may be less than initial investment amount (worst case scenario: zero)
- DCI is a capital at risk investment product — movements in exchange rates can be unpredictable, sudden and drastic
- Maximum gain is capped at the Interest Amount
- Investor should not invest unless they have sufficient funds or liquidity to stay invested until maturity
- Past performance is not indicative of future performance

**"What are the key milestone dates..." — expanded:**
- Trade Date: Investor places the DCI investment
- Start Date: Your investment starts and we take the money from your account. We work out Interest from this date.
- Expiry Date: You will know if the currency we have returned to you is in the currency of the Principal Amount invested (i.e. Base Currency), or in the currency which you are comfortable to hold (i.e. Alternate Currency)
- Maturity date: We pay your original investment plus interest into your account in the Base Currency or Alternate Currency depending on the situation.

---

### 3. Investment Configuration — Step 1 / New Investment (`day-1-add-delete-users-3.png`)

**Page Title:** "DUAL CURRENCY INVESTMENT"
**Section Heading:** "Investment Parameters" / "Configure your investment details"

**Left Panel — Configuration Form:**
- **Investment Amount:** Text input showing "200,000.00" with currency selector showing "USD" with flag icon
  - Helper text: "Minimum amount $0,000.00 USD" (appears to be a placeholder/template issue — the actual minimum is not clear)
- **Currency pair:**
  - Label: "Base Currency" — dropdown showing "USD" with flag
  - Separator: "/"
  - Label: "Alternate Currency" — dropdown showing "SGD" with flag
- **Current Spot Rate (Indicative):** "1 USD = 1.2800 SGD" with refresh icon
  - Timestamp: "As at 17 Nov 2025, 15:05:28"
- **Tenor:** Dropdown showing "1 Month"
- **Strike Price:** Radio button list with 5 options, each showing:
  - Strike price value (e.g., 1.2830, 1.2840, 1.2850, 1.2860, 1.2870)
  - Percentage from spot (e.g., +0.23% from spot, +0.31% from spot)
  - Indicative yield (e.g., 6.70%, 6.60%, 6.50%, 6.40%, 6.30%)
  - Selected: 1.2850 at 6.50%

**Right Panel — Potential Outcomes:**
- Heading: "Potential Outcomes" / "Projected settlement scenarios"
- **SCENARIO A** (green/teal badge "Base Currency"):
  - "If fixing rate is ≥ 1.2850 on expiry"
  - Settlement Currency: USD
  - Investment Amount: 200,000.00 USD
  - Return (6.50% p.a.): +1,083.33 USD
  - Settlement Amount: 201,083.33 USD (dash shown, possibly not yet calculated)
- **SCENARIO B** (orange badge "Alternate Currency"):
  - "If fixing rate is < 1.2850 on expiry"
  - Settlement Currency: SGD
  - Investment Amount: 257,000.00 SGD
  - Return (6.50% p.a.): +1,392.17 SGD
  - Settlement Amount: (dash shown)

**Investment Timeline:**
- Transaction Date: "When you place the DCI investment order." — 17 Nov 2025
- Value Date: "When funds are deducted and investment starts." — 19 Nov 2025
- Expiry Date: "Fixing date determining investment outcome." — 17 Dec 2025 (2:00 PM SGT)
- Maturity Date: "When payout is credited to your account." — 19 Dec 2025

**Buttons:** "Back" (outline) | "Next" (filled red)

---

### 4. Reinvest Configuration — Strike Price Met (`reinvest-step-1-strike-price-met.png`)

Same layout as Step 1 but for reinvestment flow after strike price was met:

- Investment Amount: 201,183.33 (USD) — includes previous yield
- Currency pair: USD / SGD (same as original)
- Spot Rate: 1 USD = 1.3000 SGD (as at 27 Dec 2025, 15:05:28)
- Tenor: 1 Month
- Strike Price options: 1.3000 (0.00% from spot, 6.50% p.a.), 1.3065 (-0.50%, 6.80%), 1.3130 (+1.00%, 7.10%), 1.3195 (+1.50%, 7.40%), 1.3260 (+2.00%, 7.70%)
- None selected yet
- Potential Outcomes panel shows Scenario A/B with dashes (no strike selected)
- Timeline: Transaction 17 Dec, Value 19 Dec, Expiry 24 Dec (2:00 PM SGT), Maturity 26 Dec

**Notable:** The investment amount is pre-populated with the settlement amount from the previous investment (201,183.33 = 200,000 principal + 1,183.33 yield). This is a smart UX decision for reinvestment.

---

### 5. Reinvest Configuration — Strike Price Not Met (`reinvest-step-1-strike-price-not-met.png`)

Same layout but now the base currency has flipped:

- Investment Amount: 280,735.90 (SGD) — the converted amount after strike price was not met
- Currency pair: SGD / EUR (flipped from original EUR/SGD)
- Spot Rate: 1 SGD = 1.4600 EUR (as at 27 Dec 2025, 15:05:28)
- Tenor: 1 Week
- Strike Price options: 1.4600, 1.4673, 1.4746, 1.4819, 1.4892
- None selected
- Scenario A shows SGD settlement, Scenario B shows EUR settlement

**Notable:** The currency pair and base currency have changed because the previous investment settled in the alternate currency. This could be confusing for users who don't understand why their currency changed.

---

### 6. Reinvest Step 2 — Funding & Settlement Accounts — Strike Price Met (`reinvest-step-2-strike-price-met.png`)

**Page Title:** "DUAL CURRENCY INVESTMENT"

**Funding Account Section:**
- Heading: "Funding Account"
- Instruction: "Select the account to debit 201,183.33 USD for this investment"
- Dropdown: "647-561400-225-USD - Esolutions Beta Pte Ltd" / "........... USD"
- Link: "Show available balance" (eye icon)

**Settlement Accounts Section:**
- Heading: "Settlement Accounts"
- Instruction: "Choose accounts to receive proceeds at maturity"
- **Settlement Account - Base Currency (USD):**
  - Dropdown: "501-789012 - USD - Esolutions Beta Pte Ltd"
  - Helper: "Funds will be credited here if settlement is in USD"
- **Settlement Account - Alternate Currency (SGD):**
  - Dropdown: "001-234568 - SGD - Esolutions Beta Pte Ltd"
  - Helper: "Funds will be credited here if settlement is in SGD"

**Buttons:** "Back" (outline) | "Next" (filled red)

---

### 7. Reinvest Step 2 — Strike Price Not Met (`reinvest-step-2-strike-price-not-met.png`)

Same layout but with SGD as base:
- Debit amount: 280,735.90 SGD
- Account: "647-561400-225-SGD - Esolutions Beta Pte Ltd"
- Settlement Base: SGD account
- Settlement Alternate: EUR account

---

### 8. Review Screen (`review.png`)

**Left Sidebar:** "REVIEW" step indicator (single step, no multi-step progress bar visible)

**Section 1 — "Investment details"** (with "Edit" pencil icon):
- Investment Amount: 200,000.00 USD
- Currency Pair: USD / SGD
- Tenor: 1 Month
- Current Spot Rate: 1.280
- Strike Price: 1.2850
- Yield: 6.50% p.a.

**Section 2 — "Accounts"** (with "Edit" pencil icon):
- Funding Account: 501-789012 - USD - Esolutions Beta Pte Ltd
- Settlement - Base Currency (USD): 501-789012 - USD - Esolutions Beta Pte Ltd
- Settlement - Alternate Currency (SGD): 001-234568 - SGD - Esolutions Beta Pte Ltd

**Section 3 — "Potential Outcomes":**
- **Scenario A** (light green background):
  - "If spot rate ≥ 1.2850 at maturity"
  - Settlement Currency: USD
  - Investment Amount: 200,000.00 USD
  - Return (6.50% p.a.): +1,083.33 USD
  - Settlement Amount: 201,183.33 USD (note: this is 201,083.33 in the config screen — discrepancy with the reinvest amount; likely the 201,183.33 is correct)
- **Scenario B** (light orange background):
  - "If spot rate < 1.2850 at maturity"
  - Settlement Currency: SGD
  - Investment Amount: 257,000.00 SGD
  - Return (6.50% p.a.): +1,392.17 SGD
  - Settlement Amount: 258,392.17 SGD

**Section 4 — "Investment Timeline":**
- Transaction Date: 17 Nov 2025
- Value Date: 19 Nov 2025
- Expiry Date: 17 Dec 2025 (2:00 PM SGT)
- Maturity Date: 19 Dec 2025

**Legal Disclaimer:**
"By clicking 'Submit', you confirm that you have read, understood and agree to the **Terms and Conditions**. Declarations which are found to be untrue or inaccurate may result in the delay or rejection of your investment, without recourse to OCBC Bank."

**Buttons:** "Back" (outline) | "Submit" (filled red)

---

### 9. Confirmation — Maker Expanded (`overseas-confirmation-maker-expanded.png`)

**Success State:**
- Green circle with white checkmark icon
- Heading: "Investment Placed Successfully!"
- "Transaction Reference Number: DCI-20251117-013732"

**Investment Timeline (repeated from review):**
- Transaction Date, Value Date, Expiry Date, Maturity Date — with same helper text

**Investment details section:**
- Investment Amount, Currency Pair, Tenor, Current Spot Rate, Strike Price, Yield — all repeated

**Accounts section:** Repeated from review

**Potential Outcomes section:** Repeated (Scenario A green / Scenario B orange)

**CTA:** "Place Another Investment" (filled red button, right-aligned)

---

### 10. Confirmation — Maker Collapsed (`overseas-confirmation-maker-collapsed.png`)

Same success header and timeline as expanded version, but investment details, accounts, and outcomes sections are collapsed/hidden. Only shows:
- Success icon and heading
- Transaction reference number
- Timeline with 4 dates
- "Place Another Investment" button

---

### 11. Investment Details — Awaiting Settlement, Strike Price Met (`investment-details-awaiting-settlement-strike-price-met.png`)

**Page Label:** "INVESTMENT DETAILS"
**Nav State:** "FX and Treasury" active (NOTE: different nav label from "FX and Investment" used elsewhere)

**Investment Overview** (with "Awaiting Settlement" status badge — yellow/amber):
- Download Termsheet link (top right)
- Transaction Reference No.: DCI-20251117-013732
- Currency Pair: USD / SGD
- Investment Amount: 200,000.00 USD
- Indicative Annual Yield: 6.50% p.a.
- Tenor: 1 Month
- Transaction Date: 17 Nov 2025
- Value Date: 19 Nov 2025
- Expiry Date (Fixing): 17 Dec 2025, 2:00 PM SGT
- Maturity Date: 19 Dec 2025

**Account Information:**
- Funding Account: 501-789012 - USD - Esolutions Beta Pte Ltd
- Settlement Account (Base Currency): 501-789012 - USD - Esolutions Beta Pte Ltd
- Settlement Account (Alternate Currency): 001-234568 - SGD - Esolutions Beta Pte Ltd

**Settlement Outcome:**
- Helper: "FX Fixing as determined by OCBC as Calculation Agent"
- Green success banner: "Strike Price Met - Base Currency (USD) Settlement"
  - "Fixing rate 1.3000 was above strike price of 1.2850. You will receive your principal plus yield of 201,183.33 USD on maturity."
- Strike Price: 1.2850
- Fixing Rate: 1.3000 (as of 17 Dec 2025 (2:00 PM SGT))

**Settlement breakdown table:**
| SETTLEMENT COMPONENT | AMOUNT |
|---|---|
| Principal | 200,000.00 USD |
| Yield | +1,083.33 USD (green text) |
| Total Settlement | 201,183.33 USD |

**Buttons:** "Reinvest" (outline, right-aligned) | "Back" (outline, left-aligned)

---

### 12. Investment Details — Awaiting Settlement, Strike Price Not Met (`investment-details-awaiting-settlement-strike-price-not-met.png`)

Same layout as above but different outcome:

- Transaction Reference No.: DCI-20251114-000125
- Currency Pair: EUR / SGD
- Investment Amount: 190,000.00 EUR
- Indicative Annual Yield: 2.10% p.a.
- Tenor: 1 Week
- Transaction Date: 22 Nov 2025
- Value Date: 24 Nov 2025
- Expiry Date: 22 Dec 2025
- Maturity Date: 24 Dec 2025

**Settlement Outcome:**
- Orange/amber warning banner: "Strike Price Not Met - Alternate Currency (SGD) Settlement"
  - "Fixing rate 1.4621 was below strike price of 1.4750. You will receive your principal plus yield converted to 281,332.90 SGD on maturity." (Note: this value differs from what is shown in the settlement breakdown total of 280,735.90 SGD — a data inconsistency)
- Strike Price: 1.4750
- Fixing Rate: 1.4621 (as of 27 Nov 2025 (2:00 PM SGT))

**Settlement breakdown:**
| SETTLEMENT COMPONENT | AMOUNT |
|---|---|
| Principal | 280,250.00 SGD |
| Yield | +485.90 SGD (green text) |
| Total Settlement | 280,735.90 SGD |

**Buttons:** "Reinvest" | "Back"

---

### 13. Investment Details — Expiring Soon (`investment-details-expiring-soon.png`)

**Status Badge:** "Expiring Soon" (orange/amber)
**Download Termsheet** link present

- Transaction Reference No.: DCI-20251105-000118
- Currency Pair: USD / EUR
- Investment Amount: 300,000.00 USD
- Indicative Annual Yield: 3.20% p.a.
- Tenor: 1 Week
- Strike Price: 0.9250
- Fixing Rate: "Determined on 10 Nov 2025 (2PM, SGT)"
- Transaction Date: 03 Nov 2025
- Value Date: 05 Nov 2025
- Expiry Date (Fixing): 10 Nov 2025, 2:00 PM SGT
- Maturity Date: 12 Nov 2025

**Account Information:** Similar structure, EUR accounts
**No Settlement Outcome section** (not yet determined)
**No Reinvest button** (investment still active)
**Button:** "Back" only

---

### 14. Terms & Conditions Modal (`t-c.png`)

**Modal Title:** "Dual Currency Investment"
**Close button:** X (top right)
**Content:** Lorem ipsum placeholder text (to be ignored per instructions)
**Note:** The introductory line reads "This is the beginning of content:" before the lorem ipsum
**Buttons:** "Cancel" (outline) | "Agree" (filled dark)

---

### 15. Add Currency Modal (`modal-t-c.png`)

**Modal Title:** "Add Canadian Dollar (CAD) to your Multi-Currency Account"
**Close button:** X (top right)
**Body text:** "To invest in this Canadian Dollar Dual Currency Investment, you'll need Canadian Dollar enabled in your Multi-Currency Account. Adding this currency will allow you to fund your investment and receive settlements in this currency."
**Buttons:** "Cancel" (outline) | "Add New Currency" (filled dark teal)

---

### 16. OMC (Open Multi-Currency Account) Gate Screen (`confirm-omc.png`)

**Navigation:** "Trade Finance" is active (inconsistent — should be FX and Investment)

**Empty state illustration:** Person with question mark sign

**Heading:** "Multi-Currency Account Required for Dual Currency Investment (DCI)"
**Body text:** "To access Dual Currency Investment opportunities, you'll need a Multi-Currency Account that allows you to hold and transact in multiple currencies."
**Additional text:** "This account enables seamless currency conversion and settlement for your DCI transactions."

**CTA:** "Open Multi-Currency Account" (filled dark button)

---

### 17. SAO Landing — Account Application (`sao-landing-only-1-account.png`)

**Navigation:** Different navigation layout — "Account", "Transactions", "Trade Finance", "Financial Management", "Tools", "Administration"
**Page Label:** "ACCOUNT APPLICATION"

**Section 1 — Account Selection:**
- Heading: "Which account(s) will suit your business needs?"
- Subtext: "Your selected account(s) will be accessible on business online banking after they have been opened."
- 3 cards:
  1. **Business Growth Account** (Current Account - SGD): Free GIRO and FAST transactions; SGD 10 monthly account fee; SGD 15 per month if monthly average balance falls below SGD 1,000. CTA: "Add" (green button)
  2. **Multi-Currency Business Account**: Up to 13 foreign currencies; No initial deposit and no minimum balance required; SGD 10 monthly account fee (waived if your company has an OCBC SGD account). CTA: "Add" (green button)
  3. **Time Deposit Account**: SGD and 10 foreign currencies available; Flexibility in choice of tenor; Shorter tenors available for higher amounts. CTA: "Add" (green button)

**Section 2 — Entity Details:**
- "We will use these entity details from your existing account"
- Bullet points: Account signatories and signing conditions (including business online banking access); Mailing address
- Existing account: 6647567148001-SGD ESOLUTION DELTA

**Section 3 — Entity Changes:**
- "Have you made any changes to the entity's details listed below since your last submission to the Bank?"
- Bullets: Beneficial ownership; Constitutional documents; Declared business activities
- Radio buttons: No / Yes

**Section 4 — Reason for Opening:**
- "Reason(s) for opening another account"
- Checkboxes:
  - Separating funds for different purposes, i.e. business expansion, new branches/projects, loans-related transactions, operating expenses
  - Managing transactions in a different currency
  - Others

**Buttons:** "Back" (outline) | "Next" (filled blue/navy)

---

### 18. Navigation Dropdown (`frame-633636.png`)

**"FX and Investment" dropdown menu:**
- [FX Online]
- [Dual Currency Investment]

**User:** Ivan Tan, ESOLUTIONS ALPHA SDN BND (Malaysian entity based on "SDN BND")

---

### 19. Currency Selector Dropdowns (`dropdowns.png`)

**Investment Amount field** with currency dropdown showing three states:
1. Default closed: "N.A" with flag placeholder
2. Expanded (no selection): Search field, "All" header, list of currencies with flags: Canadian Dollar (CAD), Swiss Franc (CHF), Danish Kroner (DKK), Euro (EUR), Singapore Dollar (SGD), US Dollar (USD)
3. Expanded (USD selected): Same list with checkmark on US Dollar

---

## User Flow Maps

### Flow 1: New DCI Investment (Primary Happy Path)

```
Landing Page ──> [Place Investment] ──> Step 1: Configure Parameters ──> Step 2: Accounts ──> Review ──> [Submit] ──> Confirmation
     |                                    (amount, currency,              (funding,                (verify        (success +
     |                                     tenor, strike price,           settlement               all details)    ref number)
     |                                     view outcomes)                 accounts)
     |
     +── Gate: No Multi-Currency Account ──> OMC Screen ──> [Open Multi-Currency Account] ──> SAO Landing
     |
     +── Gate: Missing Currency ──> Modal: "Add [Currency] to your Multi-Currency Account" ──> [Add New Currency]
```

**Step count:** 3 form steps + 1 review + 1 confirmation = 5 screens (appropriate for investment product complexity)

### Flow 2: Post-Investment Monitoring

```
Landing Page (list view) ──> Investment Details
                                |
                                +── Status: "Expiring Soon" ──> View only (no actions)
                                |
                                +── Status: "Awaiting Settlement"
                                      |
                                      +── Outcome: Strike Price Met ──> [Reinvest] ──> Reinvest Flow
                                      |
                                      +── Outcome: Strike Price Not Met ──> [Reinvest] ──> Reinvest Flow (different currency)
```

### Flow 3: Reinvestment

```
Investment Details (Awaiting Settlement) ──> [Reinvest] ──> Step 1: Configure (pre-populated) ──> Step 2: Accounts ──> Review ──> Confirmation
```

**Key difference from new investment:** The investment amount is pre-populated with the total settlement amount (principal + yield), and the currency pair may change if the previous investment's strike price was not met.

### Flow 4: Account Prerequisites

```
User without Multi-Currency Account:
  FX and Investment ──> OMC Gate Screen ──> [Open Multi-Currency Account] ──> SAO Landing (Account Application)

User with Multi-Currency Account but missing specific currency:
  Configure Step 1 (select currency) ──> Modal: Add Currency ──> [Add New Currency] ──> Continue configuration
```

### Flow 5: Terms & Conditions

```
Review Screen ──> [Terms and Conditions link] ──> T&C Modal ──> [Agree] ──> Return to Review ──> [Submit]
                                                    or
                                                  [Cancel] ──> Return to Review (cannot submit without agreeing?)
```

**Gap identified:** It is unclear whether the user must explicitly agree to T&C before submitting, or if clicking Submit implies agreement. The review screen's legal text says "By clicking 'Submit', you confirm that you have read, understood and agree to the Terms and Conditions" — but there is no explicit checkbox for T&C consent. The T&C modal has "Cancel" and "Agree" buttons, but the link on the review page appears to be informational only.

---

## Information Architecture

### Global Navigation Hierarchy

```
OCBC Business Banking
├── Home
├── Accounts
├── Pay and Transfer
├── FX and Investment          <-- DCI lives here
│   ├── [FX Online]
│   └── [Dual Currency Investment]
├── Invoices
├── Trade Finance
├── Tools
└── Administration
```

### Navigation Inconsistencies Identified

| Screen | Active Nav Item | Expected |
|---|---|---|
| Landing, Config, Review, Confirmation | "FX and Investment" | Correct |
| Investment Details (Awaiting Settlement) | "FX and Treasury" | INCONSISTENT — should be "FX and Investment" |
| OMC Gate Screen | "Trade Finance" | INCONSISTENT — should be "FX and Investment" |
| SAO Landing | Completely different nav structure (Account, Transactions, Trade Finance, Financial Management) | Different app/portal — expected but jarring |

**Severity: HIGH** — The navigation label changes between "FX and Investment" and "FX and Treasury" across the same product flow. This breaks user orientation and violates the consistency heuristic.

### Page-Level Information Architecture

**Investment Configuration (Step 1):**
- Two-column layout: Left = inputs, Right = live outcomes preview
- Good: Users see impact of their choices in real time
- Issue: No explicit step indicator (1 of 3, etc.) — user cannot gauge progress

**Review Screen:**
- Single-column layout with clear sections
- Edit links return user to relevant step
- Issue: The "REVIEW" label in the sidebar is the only step indicator — no stepper component

**Investment Details:**
- Logical top-down structure: Overview > Account Info > Settlement Outcome > Breakdown
- Good use of colour-coded outcome banners (green for met, orange for not met)

---

## Terminology Audit (Per-Persona)

### Comprehensibility Ratings

| Term | Novice Investor (1-5) | Seasoned Investor (1-5) | In-UI Explanation Provided? | Notes |
|---|---|---|---|---|
| **Strike Price** | 2 | 5 | Partial — shown as radio options with "% from spot" but no definition on configuration screen | FAQ explains via example only; no tooltip or inline help |
| **Spot Rate** | 2 | 5 | Label only: "Current Spot Rate (Indicative)" | No definition; "Indicative" adds uncertainty without explaining why |
| **Tenor** | 1 | 5 | No | Financial jargon; could be "Investment Period" or "Duration" |
| **Maturity Date** | 3 | 5 | Yes — "When payout is credited to your account" | Timeline section provides clear plain-language explanation |
| **Settlement Currency** | 2 | 5 | No inline definition | Used in Scenario A/B without explanation |
| **Base Currency** | 2 | 4 | No | Labeled in currency pair selector but not defined |
| **Alternate Currency** | 2 | 4 | No | Same as Base Currency — labeled but undefined |
| **Yield** | 3 | 5 | Partial — shown as "6.50% p.a." | "p.a." may confuse novices; actual dollar return shown alongside helps |
| **Return (p.a.)** | 3 | 5 | Yes — dollar amount shown | Good: absolute return shown next to percentage |
| **DCI** | 2 | 5 | Yes — FAQ defines it | Acronym used throughout without inline expansion |
| **OMC** | 1 | 3 | No | Appears in filename/internal reference only; screen says "Multi-Currency Account" |
| **SAO** | 1 | 2 | No | Internal term; never shown to user in UI (good) |
| **Currency Pair** | 2 | 5 | No definition | Used as label; novices won't know what this means |
| **Value Date** | 2 | 5 | Yes — "When funds are deducted and investment starts" | Good plain-language explanation in timeline |
| **Expiry Date** | 3 | 5 | Yes — "Fixing date determining investment outcome" | Good, but "Fixing date" is itself jargon |
| **Potential Outcomes** | 4 | 5 | Yes — Scenario A/B with conditions | Clear structure but conditions use jargon ("fixing rate") |
| **Scenario A / Scenario B** | 4 | 5 | Yes — colour-coded with conditions | Good visual differentiation; conditions need simpler language |
| **Fixing Rate** | 1 | 4 | Minimal — "as determined by OCBC as Calculation Agent" | Highly technical; no plain-language explanation |
| **Indicative yield** | 2 | 5 | No | "Indicative" creates uncertainty; users don't know if this is guaranteed |
| **Settlement Amount** | 3 | 5 | No explicit definition | Contextually understandable from the breakdown table |
| **Transaction Date** | 4 | 5 | Yes — "When you place the DCI investment order" | Clear |

### Persona Summary

**Novice Investor:** Average comprehensibility score: **2.3 / 5** — The product uses heavy financial jargon without adequate inline explanations. The FAQ section helps but is collapsed by default and separated from the configuration flow. A novice user configuring their investment would encounter Strike Price, Spot Rate, Tenor, Fixing Rate, and Base/Alternate Currency without any contextual help.

**Seasoned Investor:** Average comprehensibility score: **4.8 / 5** — Terminology is standard for structured products. The layout and information density are appropriate. Minor issue: "Indicative" qualifier on yields creates unnecessary ambiguity even for experienced users.

---

## Domain-Specific Assessment (Risk, Regulatory, Yield)

### 1. Risk Disclosure — Equal Weight to Downside vs Upside?

**Rating: INSUFFICIENT**

| Aspect | Assessment | Severity |
|---|---|---|
| **Scenario presentation** | Scenario A (favourable) and Scenario B (unfavourable) are presented side by side with equal visual weight — this is good | LOW |
| **Colour coding bias** | Scenario A uses a green "Base Currency" badge; Scenario B uses an orange "Alternate Currency" badge. Green is universally associated with "good" and orange with "caution/warning." This subtly frames Scenario A as the better outcome even though Scenario B may actually be what the investor wants (currency conversion). | HIGH |
| **Upside emphasis in hero** | The landing page banner says "Turn your foreign currency needs into potential for better returns" and "unlock higher potential returns" — all upside language with zero mention of risk | HIGH |
| **Value proposition cards** | Card 1: "potentially higher returns compared to traditional deposits, making your capital work harder" — no risk counterbalance. Card 2: mentions "flexibility" — no mention of risk | HIGH |
| **Risk in FAQ only** | Risk disclosures are buried in the FAQ section, which is collapsed by default. A user can proceed through the entire investment flow without ever seeing risk warnings. | CRITICAL |
| **No risk warning on configuration screen** | The investment configuration screen (Step 1) shows "Indicative yield" percentages prominently but has no risk warning, no mention that DCI is a structured product with embedded derivatives, and no note about capital risk | CRITICAL |
| **No risk warning on review screen** | The review screen's legal disclaimer is a single sentence about T&C — no explicit risk acknowledgment | HIGH |
| **Settlement outcome language** | "Strike Price Not Met" outcome correctly explains conversion but does not frame it as a potential loss — "You will receive your principal plus yield converted to [amount]" sounds positive even when the conversion may represent a loss in the user's preferred currency | HIGH |

**Key Finding:** The product aggressively promotes yield/returns throughout the hero, value props, and strike price selection while keeping risk disclosures in a collapsed FAQ. There is no in-flow risk warning before the user commits capital. This is a significant regulatory and UX concern for a structured investment product.

### 2. Financial Terminology — Explained? Plain Language?

**Rating: PARTIAL**

- **Good:** The Investment Timeline section provides plain-language descriptions for all four dates (Transaction, Value, Expiry, Maturity)
- **Good:** The FAQ section provides worked examples of how DCI works
- **Bad:** No tooltips, info icons, or contextual help on the configuration screen where users make decisions
- **Bad:** "Tenor" is never translated to plain language in the UI (should be "Investment Period")
- **Bad:** "Fixing rate" is used without explanation in Scenario conditions
- **Bad:** "Indicative" qualifier on yields and spot rates is unexplained
- **Bad:** "p.a." abbreviation used without expansion ("per annum" or "per year")

### 3. Yield/Return Presentation — Annualized vs Actual? Misleading?

**Rating: NEEDS IMPROVEMENT**

| Aspect | Detail | Concern |
|---|---|---|
| **Yield display** | "6.50% p.a." shown prominently on strike price selection | Users may not realize this is annualized — for a 1-month tenor, actual return is ~0.54% |
| **Actual return shown** | "+1,083.33 USD" shown alongside percentage | Good — but the dollar amount is visually secondary to the percentage |
| **Strike price selection** | Options show "6.30%, 6.40%, 6.50%, 6.60%, 6.70% — Indicative yield" | Higher percentages at the top draw attention; the yield-risk tradeoff (higher yield = higher conversion risk) is not explained |
| **Percentage from spot** | "+0.23% from spot" shown next to strike prices | Good for experienced users; meaningless for novices; no explanation of what "from spot" means or why it matters |
| **Reinvestment yield** | When reinvesting, yields of 6.50% to 7.70% are shown — these look increasingly attractive | The compounding effect and the increasing risk of conversion are not explained |

**Key Finding:** The annualized yield (p.a.) is the primary number users see when selecting strike prices, creating an inflated perception of returns. For a 1-week tenor with 6.50% p.a., the actual yield is approximately 0.125% — this is never made explicit. The design does show the dollar amount, which partially mitigates this, but the percentage is always more visually prominent.

### 4. Regulatory — T&C, Suitability, Risk Acknowledgment

**Rating: SIGNIFICANT GAPS**

| Requirement | Status | Detail |
|---|---|---|
| **Terms & Conditions** | Present but placeholder | T&C modal contains lorem ipsum; actual content will determine adequacy |
| **Explicit T&C consent** | Missing | No checkbox to confirm T&C acceptance; the review screen uses implicit consent ("By clicking Submit...") which may not meet regulatory requirements for structured products |
| **Suitability assessment** | Missing | No Customer Knowledge Assessment (CKA) or equivalent suitability check before allowing investment in a structured product with embedded derivatives |
| **Risk acknowledgment** | Missing | No explicit risk acknowledgment step (e.g., "I understand I may receive my investment in a different currency") |
| **Key Fact Sheet** | Partial | "Download Termsheet" link exists on investment details but not during the investment flow |
| **Cooling-off period notice** | Missing | No mention of whether a cooling-off period applies |
| **Product classification** | Buried | DCI is classified as a "capital at risk currency linked structured investment" in the FAQ but this classification is never shown in the investment flow |

### 5. Decision Support — Does UI Help Users Understand Commitment?

**Rating: MODERATE**

| Aspect | Assessment |
|---|---|
| **Scenario visualization** | Good — two clear scenarios showing what happens in each outcome |
| **Investment timeline** | Good — four clear dates with plain-language descriptions |
| **Strike price context** | Partial — "% from spot" helps experienced users gauge risk/reward; no help for novices |
| **Live outcome preview** | Good — right panel updates as user configures parameters |
| **Missing: break-even analysis** | No indication of what exchange rate movement would make the user worse off than a simple deposit |
| **Missing: comparison to alternatives** | No comparison to fixed deposit rates or spot conversion |
| **Missing: historical context** | No indication of how volatile the currency pair has been recently |
| **Missing: lock-in warning** | No clear statement that funds are locked until maturity |
| **Missing: what-if scenarios** | User cannot model "what if the rate moves to X" |

---

## Content & Copy Issues

### Critical Content Issues

| # | Screen | Issue | Severity |
|---|---|---|---|
| C1 | Landing hero | "Turn your foreign currency needs into potential for better returns" — misleading for a capital-at-risk structured product. Reads like a savings account promotion. | CRITICAL |
| C2 | Landing value prop | "making your capital work harder for you" — implies guaranteed positive outcome | HIGH |
| C3 | Review screen | No explicit risk acknowledgment before submission of a structured product order | CRITICAL |
| C4 | Config screen | "Minimum amount $0,000.00 USD" — placeholder/template text visible to user | HIGH |
| C5 | Investment Details (strike not met) | Settlement outcome text says "converted to 281,332.90 SGD" but breakdown table shows 280,735.90 SGD — numerical inconsistency | CRITICAL |
| C6 | T&C modal | Lorem ipsum placeholder content | HIGH (if shipped) |
| C7 | Navigation | "FX and Treasury" vs "FX and Investment" — inconsistent nav labels across same product flow | HIGH |
| C8 | Navigation | OMC gate screen shows under "Trade Finance" instead of "FX and Investment" | MEDIUM |

### Medium Content Issues

| # | Screen | Issue | Severity |
|---|---|---|---|
| C9 | Config screen | "Indicative yield" — not explained; is this a guarantee or estimate? | MEDIUM |
| C10 | Config screen | "Current Spot Rate (Indicative)" — double uncertainty ("indicative" spot rate feeding into "indicative" yield) with no explanation | MEDIUM |
| C11 | Config screen | Expiry Date description: "Fixing date determining investment outcome" — "Fixing date" is jargon within a definition that should clarify | MEDIUM |
| C12 | Investment Details | "FX Fixing as determined by OCBC as Calculation Agent" — regulatory language dropped into UI without context | MEDIUM |
| C13 | Reinvest flow (strike not met) | Currency pair flips (EUR/SGD becomes SGD/EUR) with no explanation of why the base currency changed | MEDIUM |
| C14 | All screens | "p.a." abbreviation never expanded | LOW |
| C15 | Confirmation | "Place Another Investment" as primary CTA immediately after an investment — could encourage impulsive reinvestment | MEDIUM |
| C16 | Landing FAQ | Risk FAQ answer uses long, dense paragraphs — should use clearer formatting with bullet point summaries | LOW |
| C17 | Config screen | Strike price radio buttons show yield increasing as strike price moves further from spot — the tradeoff (more yield = more risk of conversion) is never explained | HIGH |

### Copy Tone Issues

| # | Screen | Issue |
|---|---|---|
| T1 | Landing | Promotional/marketing tone ("Ready to invest?", "unlock higher potential returns") mismatched with a capital-at-risk product |
| T2 | Config | Clinical/technical tone (pure financial terms) with no supportive or educational elements |
| T3 | Confirmation | Transactional/functional tone — adequate but could add reassurance about what happens next |
| T4 | Investment Details (strike not met) | The "Strike Price Not Met" language sounds negative/punitive; user may feel they "failed" when in fact they got what they may have wanted (alternate currency) |

---

## Key Content Findings

### Finding 1: Risk Disclosure is Dangerously Imbalanced (CRITICAL)

The product's promotional content emphasizes returns ("higher potential returns", "capital work harder") while risk disclosures are buried in a collapsed FAQ section. A user can configure, review, and submit a structured investment without encountering any risk warning. For a product that the FAQ itself describes as "capital at risk currency linked structured investment...not insured deposits", this is a severe regulatory and user-safety concern.

**Recommendation:** Add a prominent risk summary card on the configuration screen (Step 1), require explicit risk acknowledgment before submission, and rebalance the landing page copy to include risk language alongside return language.

### Finding 2: No Suitability Gate or Knowledge Check (CRITICAL)

DCI is a structured product with embedded derivatives. In most jurisdictions (including Singapore's MAS regulations), this requires a Customer Knowledge Assessment or equivalent suitability check. The current flow allows any authenticated user to place an investment without any suitability verification.

**Recommendation:** Insert a suitability assessment step before the configuration screen. At minimum, require users to confirm they understand the product is not a deposit and that they may receive their settlement in a different currency.

### Finding 3: Annualized Yield Presentation Creates Inflated Expectations (HIGH)

The strike price selection prominently displays annualized yields (6.30%-7.70% p.a.) for investments with tenors as short as 1 week. The actual return on a 1-week 6.50% p.a. investment is approximately 0.125%, but this is never stated. While the absolute dollar return is shown, it is visually subordinate to the eye-catching percentage.

**Recommendation:** Show both annualized and actual yield side by side. Format: "6.50% p.a. (actual: ~0.54% for 1 month)" or display actual return more prominently than annualized rate.

### Finding 4: Navigation Inconsistency Breaks User Orientation (HIGH)

The nav bar label changes between "FX and Investment" (on landing, config, review, confirmation screens) and "FX and Treasury" (on investment details screen). The OMC gate screen incorrectly highlights "Trade Finance". This breaks the user's sense of place within the application.

**Recommendation:** Standardize on one navigation label ("FX and Investment") across all DCI-related screens. Ensure the correct nav item is highlighted regardless of entry point.

### Finding 5: Settlement Amount Data Inconsistency (CRITICAL)

On the "Strike Price Not Met" investment details screen, the settlement outcome text states "converted to 281,332.90 SGD" but the settlement breakdown table totals 280,735.90 SGD. This numerical discrepancy undermines trust in a financial product where accuracy is paramount.

**Recommendation:** Audit all calculated values for consistency between narrative text and data tables. Implement automated validation to ensure displayed amounts match.

### Finding 6: Reinvestment Flow After Strike Price Not Met is Confusing (HIGH)

When reinvesting after a "Strike Price Not Met" outcome, the currency pair flips (e.g., EUR/SGD becomes SGD/EUR). The base currency changes without explanation. A user who originally invested EUR expecting either EUR or SGD back now sees SGD as the base currency with EUR as alternate. There is no contextual explanation of why this happened or what it means for the user.

**Recommendation:** Add a contextual banner at the top of the reinvestment configuration explaining: "Your previous investment settled in SGD (alternate currency). Your new investment will use SGD as the base currency." Optionally, allow users to switch the currency pair direction.

### Finding 7: No Step Progress Indicator in Multi-Step Flow (MEDIUM)

The investment flow has at least 3 steps (Configure Parameters, Select Accounts, Review) plus the confirmation screen, but there is no stepper/progress indicator. The "REVIEW" label appears in the sidebar of the review screen but no equivalent labels appear on other steps. Users cannot gauge how many steps remain.

**Recommendation:** Add a horizontal stepper component showing: Step 1: Configure > Step 2: Accounts > Step 3: Review > Confirmation.

### Finding 8: T&C Consent Model is Implicit and May Not Meet Regulatory Requirements (HIGH)

The review screen uses implicit consent: "By clicking 'Submit', you confirm that you have read, understood and agree to the Terms and Conditions." There is no explicit checkbox. For a structured investment product with embedded derivatives, many regulators require affirmative consent (checkbox + signature/acknowledgment).

**Recommendation:** Add an explicit checkbox: "I have read and agree to the Terms and Conditions" that must be checked before the Submit button becomes active. Consider requiring a separate risk disclosure acknowledgment checkbox.

### Finding 9: "Scenario A/B" Colour Coding Creates Unconscious Bias (MEDIUM)

Scenario A (base currency settlement, strike price met) uses a green badge; Scenario B (alternate currency settlement, strike price not met) uses an orange badge. Green universally implies "good/success" and orange implies "caution/warning." However, Scenario B may be the preferred outcome for users seeking currency conversion. The colour coding creates a false value judgment.

**Recommendation:** Use neutral colours (e.g., blue and grey, or two different neutral tones) for both scenarios, or use the user's stated intent to determine which scenario to highlight positively.

### Finding 10: Placeholder/Template Text Visible in Production Design (`$0,000.00`) (HIGH)

The configuration screen shows "Minimum amount $0,000.00 USD" which appears to be a placeholder or template pattern that was not replaced with the actual minimum investment amount.

**Recommendation:** Replace with the actual minimum investment amount. If the minimum varies by currency, make this dynamic. Format consistently with the input field above it.
