# OCBC Corporate Banking - Dual Currency Investment (DCI)
# Content & User Flow Audit Report

**Date:** 2026-03-13
**Auditor:** Senior UX Auditor (AI-assisted)
**Platform:** Web Desktop (1280px+)
**Domain:** Corporate Banking (HIGH STAKES)
**Screens Analyzed:** 21

---

## 1. COMPLETE UI TEXT INVENTORY

### 1.1 Landing Page (Empty State) -- `renew-landing-uploaded-file.png`

**Navigation Bar:**
- Home | Accounts | Pay and Transfer | FX and Investment | Invoices | Trade Finance | Tools | Administration

**Header Area:**
- User: "Patrick Tan" | "ESOLUTIONS ALPHA PTE LTD" | "Last login: 12 May 2025, 13:58:31"
- Globe icon: "EN" (dropdown)
- "Tasks and Statuses" (button)

**Page Title:**
- "DUAL CURRENCY INVESTMENT"

**Hero Banner:**
- "Ready to invest?"
- "Turn your foreign currency needs into potential for better returns"
- Button: "Place investment"

**Value Proposition Cards:**
- Card 1: "Maximise your investment returns" / "Strategically manage your excess cash with potentially higher returns compared to traditional deposits, making your capital work harder for you."
- Card 2: "Great for currency conversion needs" / "If you need to convert currencies to fund overseas suppliers, investments, or education, Dual Currency Investments give you the flexibility to hold and manage the alternate currency for conversions."

**Filters:**
- "All Currencies" (dropdown)
- "Status" (dropdown)
- "Tenor" (dropdown)
- Search icon with text field: "Search"

**Empty State:**
- Illustration of person with briefcase
- "Start your first Dual Currency Investment and unlock higher potential returns"
- Link: "Place investment" (with globe icon)

**FAQ Section:**
- Section header: "FREQUENTLY ASKED QUESTIONS"
- Q1: "What is a Dual Currency Investment (DCI)?" / "Show"
- Q2: "How does it work?" / "Show"
- Q3: "What are the risks involved in investing in Dual Currency Investment (DCI)?" / "Show"
- Q4: "What are the key milestone dates when investing in Dual Currency Investment (DCI)?" / "Show"

**Footer:**
- "(c) OCBC. All Rights Reserved."
- "Conditions of Access | Security & Privacy"

---

### 1.2 Landing Page (FAQs Expanded) -- `renew-landing-uploaded-file-2.png`

**FAQ 1 Answer - "What is a Dual Currency Investment (DCI)?":**
- "Dual Currency Investment product is a capital at risk currency-linked structured investment which involves a currency option that offers potential enhanced interest to the investor. In addition, DCI provides investors the opportunity to receive the alternate currency that they need at a better exchange rate than the exchange rate on the day they invest."

**FAQ 2 Answer - "How does it work?":**
- "Suppose an investor wants to invest USD 500,000 into a dual currency investment with a 3-month tenor, using SGD as the alternate currency."
- **Indicative pricing parameters** table:
  - Base currency: USD 500,000
  - Alternate currency: SGD
  - Tenor: 3 months
  - Spot rate: 1.2800
  - Strike: ~
  - Fixing date/time: 3 business days before maturity, at 2pm Singapore time
  - DCI Yield: 6.50% p.a.
  - USD/SGD exchange rate: Exchange rate on fixing date/time
- **Payoff at maturity** table:
  - Conversion rate / What you will receive
  - USD/SGD exchange rate >=1.2850: Principal plus enhanced yield in USD of USD 508,215.28 [USD 500,000 + (6.5% x (91 Days x 500,000)]
  - USD/SGD exchange rate <1.2850: Principal plus enhanced yield in SGD of SGD 653,856.43 [SGD 561.25 * (1.2850)]

**FAQ 3 Answer - "What are the risks involved in investing in Dual Currency Investment (DCI)?":**
- "DCI is not equivalent to Time Deposits. DCI is a structured product embedded with derivatives. DCI is not an insured deposit for the purposes of the Deposit Insurance and Policy Owners' Protection Schemes Act of Singapore. The investor could lose all or a substantial part of your original amount invested in certain events."
- "If the Bank defaults on its obligations under the investment, the recovery amount that you will receive might be substantially less than the initial investment amount, and in the worst case scenario, zero."
- "DCI is a capital at risk investment product and you could lose all of your investment. Movements in exchange rates can be unpredictable, sudden and drastic, and affected by complex political and economic factors. You must be prepared to incur loss as a result of depreciation in the value of the alternate currency of the redemption amount is converted to the alternate currency at maturity. Such loss may offset any interest earned on the DCI and could even lead to a net loss."
- "The maximum gain of the DCI is capped at the Interest Amount."
- "DCI is not a listed financial instrument. You should not make a DCI unless you have sufficient funds or liquidity so as to enable you to stay invested in the DCI with OCBC until maturity and accept that the DCI shall remain illiquid until maturity."
- "You should understand that past performance is also not indicative of future performance of such investments."

**FAQ 4 Answer - "What are the key milestone dates when investing in Dual Currency Investment (DCI)?":**
- "Trade Date: Investor places the DCI instruction"
- "Start Date: Your investment starts and we will take the money from your account. We work out interest from this date."
- "Expiry Date: You will know if the currency we have returned to you is in the currency of the Principal Amount invested (i.e. Base Currency), or in the currency which you are comfortable buying (i.e. Alternate Currency)"
- "Maturity date: We pay your original investment plus yield to your account in the Base Currency or Alternate Currency depending on the situation."

---

### 1.3 Landing Page (Active Investments) -- `renew-landing-uploaded-file-3.png`

**Summary Dashboard:**
- "Active Investments: 4"
- "Expiring Soon: 1" / "Within 5 days"
- "Total Invested Amount: 1,500,000.00 SGD" / "Approximate SGD equivalent"
- "Avg. Yield: 2.7% p.a." / "Indicative Return"
- "Last updated: 15 Nov 2025, 11:36 AM (UTC+08:00)" / Refresh icon

**Tab Navigation:**
- "Active Investments" (selected, count: 4)
- "Settled" (count: 2)

**Table Headers:**
- CURRENCY PAIR (REFERENCE NUMBER)
- STRIKE PRICE
- TENOR
- STATUS
- EXPIRY DATE
- INVESTMENT AMOUNT

**Investment Row 1:**
- "AUD / SGD" / "DCI-20251111-001 12"
- "0.8900" / "Fixing Rate: Strike/Fixed on 02 Dec 2025, (PM) SGD"
- "1 Month"
- "Active"
- "26 Nov 2025 (2PM, SGT)" / "Maturity Date: 01 Dec 2025" / "Value Date: 17 Nov 2025"
- "700,000.00 AUD" / "5.89% p.a."

**Investment Row 2:**
- "USD / EUR" / "DCI-20251111-001 14"
- "0.9250" / "Fixing Rate: Strike/Fixed on..." (truncated)
- "1 Week"
- "Expiring soon" (orange badge)
- "19 Nov 2025 (2PM, SGT)" / (dates partially visible)
- "300,000.00 USD" / "3.20% p.a."

**Investment Row 3:**
- "USD / SGD" / "DCI-20251115-INVEST01"
- "1.2850" / "Fixing Rate: 1.830"
- "1 Month"
- "Awaiting Settlement"
- "17 Dec 2025 (2PM, SGT)" / "Maturity Date: 19 Dec 2025" / "Value Date: 19 Nov 2025"
- "200,000.00 USD" / "6.50% p.a."

**Strike Price Met Banner (green):**
- "Strike Price Met - Base Currency (USD) Settlement"
- "Fixing rate 1.3000 was above strike price of 1.2850. You will receive your principal plus yield of $201,183.33 USD on maturity."
- Button: "Reinvest"

**Investment Row 4:**
- "EUR / SGD" / "DCI-20251121319002"
- "1.4750" / "Fixing Rate: 1.4621"
- "1 Week"
- "Awaiting Settlement"
- "27 Nov 2025 (2PM, SGT)" / "Maturity Date: 29 Nov 2025"
- "190,000.00 EUR" / "1.0% p.a."

**Strike Price Not Met Banner (amber/red):**
- "Strike Price Not Met - Alternate Currency (SGD) Settlement"
- "Fixing rate 1.4621 was below strike price of 1.4750. You will receive your principal plus yield converted to SGD 281,322.90 SGD on maturity."
- Button: "Reinvest"

---

### 1.4 Landing Page (Settled Tab) -- `renew-landing-uploaded-file-4.png`

**Tab:** "Settled" (selected, count: 2)
**Date filter:** "Jan 2025" (dropdown)

**Settled Row 1:**
- "USD / SGD" / "DCI-20251202-000101"
- "1.3R2" / "Fixing Rate: 1.361"
- "1 Week"
- Status: "Settled"
- "07 Dec 2025 (2PM, SGT)" / "Maturity Date: 09 Dec 2025" / "Value Date: 02 Dec 2025"
- "280,000.00 USD" / "3.25% p.a."

**Strike Price Met Banner:**
- "Strike Price Met - Base Currency (USD) Settlement"
- "Fixing rate 1.3612 was above strike price of 1.3250. You will receive your principal plus yield of 280,174.52 USD on maturity."

**Settled Row 2:**
- "EUR / SGD" / "DCI-20251121310002"
- "1.4750" / "Fixing Rate: 1.4621"
- "1 Month"
- Status: "Settled"
- "27 Nov 2025 (2PM, SGT)" / "Maturity Date: 29 Nov 2025"
- "190,000.00 EUR" / "1.0% p.a."

**Strike Price Not Met Banner:**
- "Strike Price Not Met - Alternate Currency (SGD) Settlement"
- "Fixing rate 1.4621 was below strike price of 1.4750. You will receive your principal plus yield converted to SGD 281,322.90 SGD on maturity."

---

### 1.5 Multi-Currency Account Required -- `confirm-omc.png`

**Navigation Bar (DIFFERENT):**
- Home | Accounts | Pay and transfer | FX and treasury | Invoices | Trade finance | Tools | Administration

**Content:**
- Illustration with question mark
- "Multi-Currency Account Required for Dual Currency Investment (DCI)"
- "To access Dual Currency Investment opportunities, you'll need a Multi-Currency Account that allows you to hold and transact in multiple currencies."
- "This account enables seamless currency conversion and settlement for your DCI transactions."
- Button: "Open Multi-Currency Account"

---

### 1.6 Investment Parameters (Empty) -- `day-1-add-delete-users.png`

**Page Title:** "DUAL CURRENCY INVESTMENT"
**Section Title:** "Investment Parameters" / "Configure your investment details"

**Form Fields:**
- "Investment Amount" / placeholder "0.00" / currency dropdown showing flag + "NIL"
- "Currency pair" / "Base Currency" (dropdown) / "/" / "Alternate Currency" (dropdown)
- "Tenor" (dropdown)

**Right Panel - "Potential Outcomes":**
- "Projected settlement scenarios"
- "SCENARIO A" / green badge "Base Currency"
  - Settlement Currency: -
  - Investment Amount: -
  - Return: -
  - Settlement Amount: -
- "SCENARIO B" / red badge "Alternate Currency"
  - Settlement Currency: -
  - Investment Amount: -
  - Return: -
  - Settlement Amount: -

**Navigation:** "Back" (outline) | "Next" (solid red)

---

### 1.7 Investment Parameters (Amount Filled) -- `day-1-add-delete-users-2.png`

Same as above with:
- Investment Amount: "200,000.00" / "USD" flag
- "Minimum amount: $0,000.00 USD" (helper text - likely "$50,000.00")
- Base Currency: "USD" (selected, with flag)
- Alternate Currency: still showing placeholder
- Scenario A partially populated:
  - Settlement Currency: USD
  - Investment Amount: 200,000.00

---

### 1.8 Investment Parameters (Fully Configured) -- `day-1-add-delete-users-3.png`

**Form filled:**
- Investment Amount: 200,000.00 USD
- Minimum amount: $0,000.00 USD
- Base Currency: USD / Alternate Currency: SGD
- "Current Spot Rate (Indicative): 1 USD = 1.2800 SGD" / refresh icon
- "As at 17 Nov 2025, 15:05:28"
- Tenor: "1 Month"

**Strike Price Section:**
- Five radio options:
  - 1.2830 / ~0.23% from spot / 6.70% Indicative yield
  - 1.2840 / ~0.31% from spot / 6.60% Indicative yield
  - **1.2850 (selected)** / ~0.39% from spot / 6.50% Indicative yield
  - 1.2860 / ~0.47% from spot / 6.40% Indicative yield
  - 1.2870 / ~0.55% from spot / 6.30% Indicative yield

**Potential Outcomes (Right Panel - now populated):**
- "SCENARIO A" / "Base Currency" badge
  - "If fixing rate is >= 1.2850 on expiry"
  - Settlement Currency: USD
  - Investment Amount: 200,000.00 USD
  - Return (6.50% p.a.): +1,083.33 USD
  - Settlement Amount: 201,083.33 USD
- "SCENARIO B" / "Alternate Currency" badge
  - "If fixing rate is < 1.2850 on expiry"
  - Settlement Currency: SGD
  - Investment Amount: 257,000.00 SGD
  - Return (6.50% p.a.): +1,392.17 SGD
  - Settlement Amount: 258,392.17 SGD

**Investment Timeline:**
- "Key dates for your DCI investment"
- Transaction Date: "When you place the DCI investment order." / "17 Nov 2025"
- Value Date: "When funds are deducted and investment starts." / "19 Nov 2025"
- Expiry Date: "Fixing date determining investment outcome." / "17 Dec 2025 (2:00 PM SGT)"
- Maturity Date: "When payout is credited to your account." / "19 Dec 2025"

---

### 1.9 Funding Account (Empty) -- `day-1-add-delete-users-4.png`

**Section Title:** "Funding Account"
- "Select the account to debit 200,000.00 USD for this investment"

**Form Fields:**
- "Funding account" (dropdown, empty)

**Section Title:** "Settlement Accounts"
- "Choose accounts to receive proceeds at maturity"
- "Settlement Account - Base Currency (USD)" (dropdown)
  - Helper: "Funds will be credited here if settlement is in USD"
- "Settlement Account - Alternate Currency (SGD)" (dropdown)
  - Helper: "Funds will be credited here if settlement is in SGD"

---

### 1.10 Funding Account (Filled) -- `day-1-add-delete-users-5.png`

- Funding account: "647-561400-225-USD - Esolutions Beta Pte Ltd" / "........... USD"
- Link: "Show available balance" (eye icon)
- Settlement Account - Base Currency (USD): "501-789012 - USD - Esolutions Beta Pte Ltd"
  - Helper: "Funds will be credited here if settlement is in USD"
- Settlement Account - Alternate Currency (SGD): "001-234568 - SGD - Esolutions Beta Pte Ltd"
  - Helper: "Funds will be credited here if settlement is in SGD"

---

### 1.11 Review Screen -- `review.png`

**Page Label:** "REVIEW" (left sidebar label)

**Section: "Investment details"** / "Edit" (pencil icon)
- Investment Amount: 200,000.00 USD
- Currency Pair: USD / SGD
- Tenor: 1 Month
- Current Spot Rate: 1.280
- Strike Price: 1.2850
- Yield: 6.50% p.a.

**Section: "Accounts"** / "Edit" (pencil icon)
- Funding Account: 501-789012 - USD - Esolutions Beta Pte Ltd
- Settlement - Base Currency (USD): 501-789012 - USD - Esolutions Beta Pte Ltd
- Settlement - Alternate Currency (SGD): 001-234568 - SGD - Esolutions Beta Pte Ltd

**Section: "Potential Outcomes"**
- Scenario A: "If spot rate >= 1.2850 at maturity"
  - Settlement Currency: USD
  - Investment Amount: 200,000.00 USD
  - Return (6.50% p.a.): +1,083.33 USD
  - Settlement Amount: 201,183.33 USD
- Scenario B: "If spot rate < 1.2850 at maturity"
  - Settlement Currency: SGD
  - Investment Amount: 257,000.00 SGD
  - Return (6.50% p.a.): +1,392.17 SGD
  - Settlement Amount: 258,392.17 SGD

**Section: "Investment Timeline"**
- Same 4 dates as parameters screen

**Disclaimer:**
- "By clicking 'Submit', you confirm that you have read, understood and agree to the **Terms and Conditions**. Declarations which are found to be untrue or inaccurate may result in the delay or rejection of your investment, without recourse to OCBC Bank."

**Navigation:** "Back" | "Submit" (red)

---

### 1.12 Terms & Conditions Modal -- `t-c.png`

- Title: "Dual Currency Investment"
- "This is the beginning of content."
- Lorem ipsum placeholder text (NOT actual T&C content)
- Buttons: "Cancel" | "Agree"

---

### 1.13 Confirmation (Collapsed) -- `overseas-confirmation-maker-collapsed.png`

- Green checkmark icon
- "Investment Placed Successfully!"
- "Transaction Reference Number: DCI-20251117-013732"
- Investment Timeline (same 4 dates)
- Chevron down (expand indicator)
- Button: "Place Another Investment"

---

### 1.14 Confirmation (Expanded) -- `overseas-confirmation-maker-expanded.png`

Same as collapsed plus:
- "Investment details" section (same as review)
- "Accounts" section (same as review)
- "Potential Outcomes" (same as review)
- Button: "Place Another Investment"

---

### 1.15 Investment Details - Awaiting Settlement, Strike Price Met -- `investment-details-awaiting-settlement-strike-price-met.png`

**Navigation (DIFFERENT):**
- Home | Accounts | Pay and Transfer | FX and Treasury | Invoices | Trade Finance | Tools | Administration

**Page Label:** "INVESTMENT DETAILS"

**Investment Overview** / Badge: "Awaiting Settlement" (yellow)
- "Download Termsheet" link (with download icon)
- Transaction Reference No.: DCI-20251117-013732
- Currency Pair: USD / SGD
- Investment Amount: 200,000.00 USD
- Indicative Annual Yield: 6.50% p.a.
- Tenor: 1 Month
- Transaction Date: 17 Nov 2025
- Value Date: 19 Nov 2025
- Expiry Date (Fixing): 17 Dec 2025 / "2:00 PM SGT"
- Maturity Date: 19 Dec 2025

**Account Information:**
- Funding Account: 501-789012 - USD - Esolutions Beta Pte Ltd
- Settlement Account (Base Currency): 501-789012 - USD - Esolutions Beta Pte Ltd
- Settlement Account (Alternate Currency): 001-234568 - SGD - Esolutions Beta Pte Ltd

**Settlement Outcome:**
- "FX Fixing as determined by OCBC as Calculation Agent"
- Green banner: "Strike Price Met - Base Currency (USD) Settlement"
  - "Fixing rate 1.3000 was above strike price of 1.2850. You will receive your principal plus yield of 201,183.33 USD on maturity."
- Strike Price: 1.2850 / Fixing Rate: 1.3000

**Settlement breakdown:**
- Header: SETTLEMENT COMPONENT / AMOUNT
- Principal: 200,000.00 USD
- Yield: +1,083.33 USD (green)
- Total Settlement: 201,183.33 USD
- Button: "Reinvest"

**Navigation:** "Back"

---

### 1.16 Investment Details - Awaiting Settlement, Strike Price Not Met -- `investment-details-awaiting-settlement-strike-price-not-met.png`

Same structure as above with:
- Currency Pair: EUR / SGD
- Investment Amount: 190,000.00 EUR
- Indicative Annual Yield: 2.10% p.a.
- Tenor: 1 Week
- Amber/warning banner: "Strike Price Not Met - Alternate Currency (SGD) Settlement"
  - "Fixing rate 1.4621 was below strike price of 1.4750. You will receive your principal plus yield converted to 281,322.90 SGD on maturity."
- Strike Price: 1.4750 / Fixing Rate: 1.4621
- Settlement breakdown in SGD:
  - Principal: 280,250.00 SGD
  - Yield: +485.90 SGD
  - Total Settlement: 280,735.90 SGD
- Button: "Reinvest"

---

### 1.17 Investment Details - Settled -- `investment-details-settled.png`

Same structure with:
- Badge: "Settled" (grey)
- Currency Pair: USD / SGD
- Green banner: "Strike Price Met - Base Currency (USD) Settlement"
  - "Fixing rate 1.3612 was above strike price of 1.3525. You will receive your principal plus yield of 280,248.63 USD on maturity."
- NO "Reinvest" button (settled state)
- Only "Back" button

---

### 1.18 Investment Details - Expiring Soon -- `investment-details-expiring-soon.png`

- Badge: "Expiring Soon" (orange)
- Currency Pair: USD / EUR
- Fixing Rate: "Determined on 10 Nov 2025 (2PM, SGT)" (future date, not yet determined)
- NO Settlement Outcome section (not yet expired)
- NO Settlement breakdown
- Only Account Information and key dates shown

---

### 1.19 Reinvest Step 1 (Strike Price Met) -- `reinvest-step-1-strike-price-met.png`

Same layout as Investment Parameters screen with:
- Investment Amount: 201,183.33 USD (pre-populated with settlement amount)
- Base Currency: USD / Alternate Currency: SGD
- Current Spot Rate: 1 USD = 1.3000 SGD (updated rate)
- Tenor: 1 Month
- Five strike price options (different rates from original):
  - 1.3000 / 0.00% from spot / 6.50% p.a.
  - 1.3065 / ~0.50% from spot / 6.80% p.a.
  - 1.3130 / +1.00% from spot / 7.10% p.a.%
  - 1.3195 / +1.50% from spot / 7.40% p.a.
  - 1.3260 / +2.00% from spot / 7.70% p.a.
- Investment Timeline with new dates

---

### 1.20 Reinvest Step 2 (Strike Price Met) -- `reinvest-step-2-strike-price-met.png`

Same as Funding Account screen with:
- Pre-populated accounts from original investment
- Amount: 201,183.33 USD

---

### 1.21 Reinvest Step 1 (Strike Price Not Met) -- `reinvest-step-1-strike-price-not-met.png`

Same layout with:
- Investment Amount: 280,735.90 SGD (alternate currency settlement amount)
- Base Currency: SGD / Alternate Currency: EUR (currencies swapped from original)
- Current Spot Rate: 1 SGD = 1.4600 EUR
- Tenor: 1 Week
- Strike prices around 1.46xx range

---

## 2. FINANCIAL TERMINOLOGY AUDIT (Novice Persona Lens)

| Term | Comprehensibility (1-5) | Assessment | Recommendation |
|---|---|---|---|
| "Dual Currency Investment" | 2 | The name itself does not communicate the product mechanism. A novice would not understand that "dual" means settlement could happen in either currency depending on market movement. | Add a subtitle: "An investment where your returns may be paid in your chosen currency or an alternate currency, depending on exchange rate movement." |
| "Strike Price" | 1 | This is options trading jargon. A corporate treasurer unfamiliar with derivatives would not know this is the exchange rate threshold that determines settlement currency. | Rename to "Target Exchange Rate" or "Settlement Rate Threshold" with inline explanation: "The exchange rate that determines which currency you receive at maturity." |
| "Fixing Rate" | 1 | Extremely opaque. "Fixing" sounds like manipulation to a layperson. Even sophisticated investors may not immediately connect this to the market reference rate at expiry. | Rename to "Market Rate at Expiry" or "Reference Rate" with helper: "The official exchange rate observed at 2:00 PM SGT on the expiry date, used to determine your settlement currency." |
| "Base Currency" | 3 | Somewhat intuitive -- the currency you start with. But the relationship to "what you invest in" vs "what you might receive" is not clarified. | Add helper: "The currency you invest" on first use. |
| "Alternate Currency" | 3 | Paired with Base Currency, it is moderately clear. But "alternate" sounds optional, when in fact it is the currency you MAY be forced to receive. | Consider "Conversion Currency" and add: "The currency you may receive if the target exchange rate is not met." |
| "Settlement Currency" | 3 | Fairly clear in context (what you get paid in), but a novice may not understand why it changes between scenarios. | Add inline note: "The currency your investment proceeds will be paid in." |
| "Settlement Amount" | 4 | Relatively clear -- the total amount you receive. | Acceptable, but ensure "principal + yield" breakdown is always visible alongside. |
| "Indicative Yield" | 2 | "Indicative" is vague -- does it mean estimated, approximate, or subject to change? A novice would not know if this is guaranteed. | Clarify: "Estimated yield (not guaranteed, for illustration only)" or add a tooltip explaining that the actual yield is locked at placement. |
| "Indicative Annual Yield" | 2 | Same issue as above, compounded by annualization. A novice seeing "6.50% p.a." on a 1-month investment will likely think they earn 6.5% in total, not ~0.54% for the period. | CRITICAL: Show both annualized and actual period return side by side. E.g., "6.50% p.a. (~0.54% for 1 month)". |
| "Tenor" | 2 | Financial jargon for investment duration. Many corporate users outside treasury will not know this word. | Replace with "Investment Period" or "Duration" throughout. Keep "Tenor" only as a parenthetical: "Investment Period (Tenor)". |
| "Current Spot Rate (Indicative)" | 2 | "Spot rate" is FX jargon. Adding "Indicative" makes it even more uncertain-sounding. | Rename: "Current Exchange Rate (approximate)" with helper: "This rate changes in real time. The actual rate used will be determined at expiry." |
| "Scenario A / Scenario B" | 3 | Neutral labels. They do not communicate which is favorable or unfavorable. The color coding (green/red badges) helps, but the labels themselves carry no meaning. | Rename to "Scenario A: You keep your base currency" / "Scenario B: You receive the alternate currency" or use descriptive headers like "If rate moves in your favor" / "If rate moves against you." |
| "Value Date" | 2 | Standard banking term but unclear to non-treasury staff. Sounds like "the date it has value" rather than "the date funds are debited." | Rename: "Funding Date" or "Investment Start Date" with helper: "The date your funds are deducted and the investment begins." |
| "Expiry Date (Fixing)" | 2 | Two jargon terms stacked. "Expiry" suggests the investment ends, but it actually refers to the observation date. "Fixing" is unexplained. | Rename: "Rate Observation Date" with helper: "The date and time when the exchange rate is checked to determine your settlement currency." |
| "Maturity Date" | 3 | Reasonably well-known banking term. Most corporate users would understand this. | Acceptable. Helper text "When payout is credited to your account" is good. |
| "Transaction Date" | 4 | Clear and standard. | Good as is. |
| "FX Fixing as determined by OCBC as Calculation Agent" | 1 | Dense legal/financial language. "Calculation Agent" is a derivatives market term that will confuse almost all non-specialist users. | Simplify: "The exchange rate was determined by OCBC at the scheduled fixing time." |
| "p.a." | 3 | Common abbreviation but some users may not know it means "per annum" (per year). | Spell out on first use: "per year (p.a.)" |
| "Approximate SGD equivalent" | 3 | Reasonably clear. | Fine. |

**Overall Terminology Score: 2.3 / 5** -- The product uses heavy financial derivatives terminology that would be impenetrable to a novice corporate investor. Even a reasonably sophisticated corporate treasurer who has not specifically dealt with structured FX products would struggle with terms like "Strike Price," "Fixing Rate," and "Tenor."

---

## 3. USER FLOW MAPPING

### Flow 1: First Investment (New User)

```
Step 1: Landing Page (empty state)
   - User sees hero banner "Ready to invest?" and empty portfolio
   - Decision: Read FAQs or proceed directly?
   - Click: "Place investment" (banner CTA or empty state link)

Step 2: [IF no Multi-Currency Account] Account Required Gate
   - User sees blocker: "Multi-Currency Account Required"
   - Click: "Open Multi-Currency Account"
   - EXIT FLOW (external process to open account)
   - CONFUSION RISK: How long does account opening take?
     No timeline given. User has no idea if this is 5 minutes or 5 days.

Step 3: Investment Parameters (empty form)
   - User must configure:
     a. Investment Amount (manual entry + currency selection)
     b. Currency Pair (Base + Alternate from dropdowns)
     c. Tenor (dropdown)
     d. Strike Price (radio selection from 5 options)
   - Right panel updates dynamically with Scenario A/B
   - Timeline appears at bottom
   - DECISIONS: 4 distinct choices, all requiring financial knowledge
   - CONFUSION RISK (HIGH): Strike price selection shows % from spot
     and indicative yield -- user must understand the risk/return tradeoff.
     No guidance on how to choose.
   - Click: "Next"

Step 4: Funding Account
   - Select funding account (dropdown)
   - Select 2 settlement accounts (Base Currency + Alternate Currency)
   - "Show available balance" link available
   - CONFUSION RISK: Why are TWO settlement accounts needed? This is
     not explained until you notice the helper text.
   - Click: "Next"

Step 5: Review
   - Full summary of all selections
   - "Edit" links to go back to specific sections
   - Scenarios A and B displayed
   - Investment Timeline
   - T&C disclaimer with link
   - DECISION: Submit or go back
   - Click: "Submit"

Step 6: [IMPLICIT] T&C Modal
   - Lorem ipsum placeholder -- CRITICAL: No actual T&C content
   - Buttons: "Cancel" or "Agree"
   - NOTE: It is unclear if this modal appears BEFORE or AFTER clicking
     Submit, or if clicking the T&C link triggers it. The review screen
     disclaimer says "By clicking Submit, you confirm..." suggesting the
     modal may only appear when the user clicks the T&C link.

Step 7: Confirmation
   - Success message with reference number
   - Timeline recap
   - Expandable details section
   - CTA: "Place Another Investment"
   - NO link to go to portfolio/dashboard
   - NO "View investment details" link
```

**Total Steps:** 5-7 (depending on account status and T&C interaction)
**Total Decisions:** 6+ (amount, currency pair, tenor, strike price, accounts, submit)
**Estimated Time:** 5-10 minutes for experienced user; 15-30+ minutes for novice (if they can complete at all)

**Key Confusion Points:**
1. Strike price selection has no guidance for novices
2. No progress indicator -- user does not know how many steps remain
3. Multi-Currency Account gate provides no timeline or process visibility
4. T&C content is placeholder (lorem ipsum)
5. Confirmation page has no direct link to view the investment or return to portfolio

---

### Flow 2: Investment Monitoring

```
Step 1: Landing Page (Active Investments tab)
   - Summary dashboard: count, expiring soon, total amount, avg yield
   - Table with all active investments
   - Inline banners for awaiting-settlement items showing outcome
   - Filter by: Currencies, Status, Tenor, Search

Step 2: Click investment row -> Investment Details
   - Full details: overview, accounts, settlement outcome
   - Status badge: Active / Expiring Soon / Awaiting Settlement
   - If awaiting settlement: shows strike met/not met banner
   - Settlement breakdown table
   - "Download Termsheet" link
   - "Reinvest" button (if awaiting settlement)

Step 3: Return via "Back" button
   - Returns to portfolio listing
```

**Total Steps:** 2-3 clicks
**Confusion Points:**
1. "Back" button is the ONLY way to return -- no breadcrumbs
2. On the "Settled" tab, there is a date filter ("Jan 2025") but it is unclear what date range it filters on
3. Navigation bar CHANGES between landing and details screens (see Section 8)
4. "Expiring Soon" label does not explain what action is needed (if any)

---

### Flow 3: Reinvestment

```
Step 1: Investment Details (Awaiting Settlement)
   - User sees settlement outcome and breakdown
   - Click: "Reinvest" button

Step 2: Investment Parameters (pre-populated)
   - Amount pre-filled with settlement amount (principal + yield)
   - Currency pair pre-filled based on settlement:
     * Strike Met: same base/alternate as original
     * Strike Not Met: currencies SWAP (base becomes what was alternate)
   - New spot rate displayed
   - User selects new tenor and strike price
   - CONFUSION RISK (HIGH - Strike Not Met): The currencies swap silently.
     A user who invested USD/SGD and received SGD settlement now sees
     SGD/EUR as the reinvestment pair. This is a MAJOR conceptual shift
     that is not explained.
   - Click: "Next"

Step 3: Funding Account (pre-populated)
   - Accounts carried over from original investment
   - Click: "Next"

Step 4: Review -> Submit -> Confirmation
   - Same as initial investment flow
```

**Total Steps:** 4-5 clicks minimum
**Key Confusion Points:**
1. Currency pair swapping on "Strike Not Met" reinvestment is unexplained and potentially alarming
2. No explanation of why the reinvestment amount differs from the original investment
3. No option to partially reinvest (only full settlement amount)
4. No side-by-side comparison with the original investment terms

---

## 4. RISK DISCLOSURE ASSESSMENT

### Where is risk communicated?

| Location | Screen | Risk Content | Adequacy |
|---|---|---|---|
| Landing Page FAQ | `renew-landing-uploaded-file-2.png` | FAQ 3: "What are the risks involved..." -- 6 bullet points covering capital risk, counterparty risk, illiquidity, exchange rate risk | MODERATE -- Good content but buried in an FAQ accordion. User must actively expand it. |
| Investment Parameters - Scenario B | `day-1-add-delete-users-3.png` | Shows alternate currency settlement with red "Alternate Currency" badge | LOW -- Shows the NUMBERS but does not explain the RISK. A novice seeing "257,000.00 SGD" does not know if that is good or bad relative to 200,000 USD. |
| Review Screen - Scenario B | `review.png` | Same as above | LOW -- No explicit risk warning. |
| T&C Modal | `t-c.png` | Lorem ipsum placeholder -- NO ACTUAL RISK DISCLOSURE | CRITICAL FAILURE -- No real content. |
| Review Screen Disclaimer | `review.png` | "By clicking Submit, you confirm you have read, understood and agree to the Terms and Conditions..." | LEGAL BOILERPLATE -- Not a risk disclosure. |

### Is the downside scenario given equal visual weight?

**PARTIALLY.** Scenario A and Scenario B are given equal screen real estate on the parameters and review screens. However:

- Scenario A has a GREEN badge ("Base Currency") -- positive connotation
- Scenario B has a RED badge ("Alternate Currency") -- negative connotation
- The color coding is appropriate but the labels are neutral rather than explicitly stating risk
- **CRITICAL GAP:** Scenario B does NOT show the equivalent value in the base currency. A user investing 200,000 USD who might receive 258,392.17 SGD has NO way to assess whether that SGD amount is MORE or LESS than their original USD investment in USD terms. There is no "equivalent to approximately X USD at current rates" calculation shown.

### Is there a clear statement about potential loss in home-currency terms?

**NO.** This is the single most critical content gap in the entire product. At no point in the placement flow does the UI explicitly state:

> "If the exchange rate moves against you, you will receive your proceeds in [alternate currency]. When converted back to [base currency], this amount may be LESS than your original investment."

The FAQ mentions "You must be prepared to incur loss as a result of depreciation in the value of the alternate currency" but this is:
1. Buried in an accordion
2. On the landing page, not in the investment flow
3. Uses passive, legalistic language

### Is risk disclosure positioned BEFORE the user commits?

**INADEQUATELY.** The risk information in the FAQ is on the landing page (before the flow), but:
- It is not surfaced again during the investment parameters step
- It is not shown on the review screen before "Submit"
- The T&C modal (which should contain final risk disclosure) has lorem ipsum placeholder text
- There is NO risk acknowledgment checkbox or interstitial warning

### Are there appropriate warning signals?

**PARTIAL:**
- Red badge on "Alternate Currency" scenario -- good
- Amber/warning banner on "Strike Price Not Met" in portfolio -- good
- Green banner on "Strike Price Met" -- good
- **MISSING:** No warning icon, caution triangle, or explicit risk callout box anywhere in the placement flow
- **MISSING:** No risk rating indicator (e.g., "This is a HIGH RISK investment product")

### Risk Disclosure Severity Rating: CRITICAL

For a regulated banking product involving structured derivatives, the risk disclosure is dangerously insufficient. A novice investor could complete the entire placement flow without ever understanding that they might lose money in home-currency terms.

---

## 5. DCI-SPECIFIC CONTENT GAPS

### 5.1 Is the strike rate relationship to spot rate explained?

**PARTIALLY.** On the Investment Parameters screen (`day-1-add-delete-users-3.png`):
- The current spot rate is shown: "1 USD = 1.2800 SGD"
- Strike price options show "~X% from spot" (e.g., "~0.39% from spot")
- This implies a relationship but does NOT explain it

**MISSING explanation:** "The strike price is the exchange rate threshold. If the market rate at expiry is ABOVE the strike price, you keep your base currency. If BELOW, your investment is converted to the alternate currency. A higher strike price means higher yield but greater chance of conversion."

**MISSING:** Direction of risk. The percentage labels ("~0.39% from spot") do not indicate whether a higher or lower strike price is riskier. A novice cannot determine which option is more conservative.

### 5.2 Is the yield clearly labeled as annualized vs actual period return?

**NO -- CRITICAL GAP.** Throughout the product:
- Yield is consistently shown as "6.50% p.a." (annualized)
- The actual dollar return for the period IS shown in Scenario calculations (e.g., "+1,083.33 USD")
- But the actual PERCENTAGE return for the period is NEVER shown
- On the portfolio table, "6.50% p.a." is displayed next to investment amounts, creating the strong impression of a 6.5% return on a 1-month investment

**Example of the problem:**
- A user sees "200,000 USD at 6.50% p.a. for 1 Month"
- The actual period return is approximately 0.54% (~USD 1,083)
- Without explicit period yield, users may expect to earn USD 13,000 (6.5% of 200K)

**Recommendation:** Always display: "6.50% p.a. (approximately 0.54% for this 1-month period)" and show both the annualized and period returns in the Potential Outcomes panel.

### 5.3 Are the 4 key dates all explained?

**YES -- one of the strongest content elements.** The Investment Timeline on the parameters screen and review screen provides:

| Date | Label | Explanation |
|---|---|---|
| Transaction Date | "When you place the DCI investment order" | Clear |
| Value Date | "When funds are deducted and investment starts" | Clear |
| Expiry Date | "Fixing date determining investment outcome" | Moderately clear -- "Fixing" is jargon |
| Maturity Date | "When payout is credited to your account" | Clear |

The timeline visual is well-structured with a vertical stepper design.

**GAP:** The FAQ uses different date labels ("Trade Date" vs "Transaction Date," "Start Date" vs "Value Date") -- terminology inconsistency that could confuse users cross-referencing FAQ with the actual flow.

### 5.4 Is there a "how it works" diagram or visual explanation?

**NO.** The FAQ answer for "How does it work?" provides a NUMERICAL EXAMPLE (worked calculation with a table) but:
- There is NO visual diagram showing the decision tree / branching outcome
- There is NO infographic showing "invest X -> at expiry -> if rate above strike: get Y in base currency / if rate below strike: get Z in alternate currency"
- The worked example in the FAQ uses specific numbers that may not match the user's actual investment parameters
- There is NO interactive calculator or "try it" feature on the landing page

**Recommendation:** Add a simple flowchart/diagram above the FAQ:
```
You invest [Base Currency] -> At Expiry:
  Rate >= Strike Price -> You receive [Base Currency] + Yield
  Rate < Strike Price  -> You receive [Alternate Currency] + Yield
```

### 5.5 Does the FAQ content adequately cover a novice's likely questions?

**PARTIALLY.** Current FAQ covers:
1. What is DCI -- Yes, but definition is dense and jargon-heavy
2. How does it work -- Yes, but only via worked example, no visual
3. What are the risks -- Yes, comprehensive but legalistic
4. Key milestone dates -- Yes, but uses different labels than the product flow

**MISSING FAQ topics that a novice would likely ask:**
- "What is the minimum investment amount?" (mentioned on the form as helper text but not in FAQ)
- "Can I withdraw/cancel my investment before maturity?" (illiquidity mentioned in risk FAQ but not as standalone question)
- "What currencies are available?"
- "How is the yield calculated?"
- "What happens if I need the money before the maturity date?"
- "Who determines the fixing rate and how?"
- "What is the difference between the spot rate and the strike price?"
- "Can I lose more than my original investment?"
- "How do I choose the right strike price for my needs?"
- "What are the tax implications?"
- "Is this covered by deposit insurance?" (briefly mentioned in risk section but deserves prominent standalone answer: NO)

---

## 6. FORM ANALYSIS

### 6.1 Investment Parameters Form

| Field | Label | Type | Validation Visible | Helper Text | Smart Default | Novice-Friendly |
|---|---|---|---|---|---|---|
| Investment Amount | "Investment Amount" | Text input with currency dropdown | Minimum amount shown below field | "Minimum amount: $0,000.00 USD" (appears to be a formatting bug -- likely $50,000) | No default amount; currency defaults to NIL | NO -- "NIL" as default currency is confusing; no guidance on typical amounts |
| Base Currency | "Base Currency" | Dropdown | None visible | None | Populates when currency selected in amount field | PARTIAL -- linked to amount currency which is logical |
| Alternate Currency | "Alternate Currency" | Dropdown | None visible | None | No default | NO -- no guidance on common pairs |
| Tenor | "Tenor" | Dropdown | None visible | None | No default | NO -- term is jargon; no explanation of available options |
| Strike Price | (Section heading "Strike Price") | Radio buttons (5 options) | N/A (pre-calculated options) | Each option shows "~X% from spot" and "Indicative yield" | Middle option appears pre-selected | NO -- no explanation of tradeoff between strike levels |

**Issues:**
1. The minimum amount shows "$0,000.00 USD" which appears to be a display bug or placeholder
2. Currency starts at "NIL" instead of a sensible default (e.g., USD or SGD for OCBC Singapore)
3. No step/progress indicator visible -- user does not know this is step 1 of N
4. Required vs optional distinction: ALL fields appear required but none are marked with asterisks or "required" labels
5. No inline validation is visible in any state shown
6. The strike price radio buttons require significant financial knowledge to use correctly

### 6.2 Funding Account Form

| Field | Label | Type | Validation Visible | Helper Text | Smart Default | Novice-Friendly |
|---|---|---|---|---|---|---|
| Funding Account | "Funding account" | Dropdown | None visible | None in empty state | No default | PARTIAL -- clear label, but "funding" is slightly jargon |
| Settlement Account (Base) | "Settlement Account - Base Currency (USD)" | Dropdown | None visible | "Funds will be credited here if settlement is in USD" | No default | YES -- helper text is excellent |
| Settlement Account (Alt) | "Settlement Account - Alternate Currency (SGD)" | Dropdown | None visible | "Funds will be credited here if settlement is in SGD" | No default | YES -- helper text is excellent |

**Issues:**
1. "Show available balance" link is only visible after account selection -- should be visible during selection to help the user choose
2. No indication if the funding account has sufficient balance BEFORE selection
3. The two settlement accounts could be pre-populated if the user only has one account per currency
4. No explanation of WHY two settlement accounts are needed (because outcome is uncertain)

### 6.3 Review Screen

- NOT a form but an editable summary
- "Edit" links provided for Investment details and Accounts sections -- GOOD
- No edit link for Potential Outcomes (correctly, as these are calculated) -- GOOD
- The T&C link is a text hyperlink, not a checkbox -- user does not explicitly acknowledge risk

**Critical Issue:** No checkbox for T&C acknowledgment. The disclaimer says "By clicking Submit, you confirm..." but best practice for high-stakes financial products is an explicit checkbox: "I have read and understood the Terms and Conditions and the risks of this investment."

---

## 7. EMPTY STATES & EDGE CASES

### 7.1 Empty Portfolio State

**Screen:** `renew-landing-uploaded-file.png`

**Quality: GOOD.**
- Friendly illustration (person with briefcase/money)
- Clear message: "Start your first Dual Currency Investment and unlock higher potential returns"
- Clear CTA: "Place investment" link
- Filters still visible (Currencies, Status, Tenor, Search) -- these should ideally be hidden or disabled in empty state since there is nothing to filter

**Issue:** The empty state shows the same hero banner as the populated state. This is fine for consistency, but the banner message "Ready to invest?" is generic and does not specifically address a first-time user.

### 7.2 No Multi-Currency Account

**Screen:** `confirm-omc.png`

**Quality: MODERATE.**
- Clear blocker message with illustration
- Explains WHY a Multi-Currency Account is needed
- Single CTA: "Open Multi-Currency Account"

**Issues:**
1. No estimate of how long account opening takes
2. No link to learn more about Multi-Currency Accounts
3. No alternative path (e.g., "Contact your relationship manager")
4. The page is a dead end -- after clicking "Open Multi-Currency Account," the user's journey is opaque
5. No "Back" button or breadcrumb to return to previous page

### 7.3 Error States

**NOT DESIGNED.** No error states are visible in any of the 21 screens:
- No "insufficient balance" error on funding account
- No "market closed" or "rate expired" warning
- No network error / timeout state
- No server error state
- No validation error states on form fields (e.g., amount below minimum)
- No "session expired" handling
- No "investment no longer available" state (if rates change during flow)

**CRITICAL for banking:** Rate quotes are time-sensitive. There MUST be a state for "This quote has expired. Please refresh to get current rates."

### 7.4 Loading States

**NOT DESIGNED.** No loading states visible:
- No skeleton loader for portfolio table
- No loading spinner for rate refresh
- No loading state for the "Potential Outcomes" panel (which depends on API calculation)
- No loading state for account dropdowns

### 7.5 Other Edge Cases Not Addressed

- What happens if the user has only ONE account per currency? (Auto-populate?)
- What happens if all strike prices have the same yield? (Display issue?)
- What if the user tries to invest more than their available balance?
- What if market hours have ended and rates are stale?
- What if the user has pending investments that would exceed their balance?
- Currency pair unavailable or restricted?
- Weekend/holiday handling for dates?

---

## 8. NAVIGATION & IA CONSISTENCY

### 8.1 Navigation Bar Inconsistencies

This is a SIGNIFICANT information architecture issue. Three distinct navigation configurations were observed:

**Configuration A** (Landing page, Parameters, Funding, Review, Confirmation):
> Home | Accounts | Pay and Transfer | **FX and Investment** | Invoices | Trade Finance | Tools | Administration

**Configuration B** (Multi-Currency Account Required page):
> Home | Accounts | Pay and transfer | **FX and treasury** | Invoices | **Trade finance** | Tools | Administration

**Configuration C** (Investment Details - Awaiting Settlement, Settled):
> Home | Accounts | Pay and Transfer | **FX and Treasury** | Invoices | Trade Finance | Tools | Administration

**Specific Inconsistencies:**

| Element | Config A | Config B | Config C |
|---|---|---|---|
| FX section label | "FX and Investment" | "FX and treasury" | "FX and Treasury" |
| "Trade Finance" casing | "Trade Finance" | "Trade finance" | "Trade Finance" |
| "Pay and Transfer" casing | "Pay and Transfer" | "Pay and transfer" | "Pay and Transfer" |
| Active/highlighted item | "FX and Investment" | "Trade finance" (WRONG) | "FX and Treasury" |

**Critical Issues:**
1. The section name changes between "FX and Investment" and "FX and Treasury" -- this is a fundamental IA inconsistency. The user landed on "FX and Investment" but after placing an investment, the details screen shows "FX and Treasury." This creates disorientation.
2. The Multi-Currency Account page highlights "Trade finance" in the nav -- this is the WRONG section. DCI should be under FX, not Trade Finance.
3. Capitalization inconsistency ("Trade Finance" vs "Trade finance") suggests these screens were built by different teams or at different times.
4. Some screens show "Accounts" (plural), consistently, which is fine.

### 8.2 Breadcrumbs / Progress Indicators

**ABSENT.** No breadcrumbs are used anywhere in the product. No step indicators (e.g., "Step 1 of 3") are used in the investment placement flow.

**Impact:**
- User cannot tell how many steps remain in the placement flow
- User cannot navigate back to a specific step (only sequential "Back" button)
- On investment detail pages, user cannot see path context (e.g., "FX and Investment > Dual Currency Investment > DCI-20251117-013732")

The Review screen has a left-aligned "REVIEW" label which hints at step naming, but this is the only screen with such a label. The Investment Parameters and Funding Account screens have NO equivalent step label.

### 8.3 Navigation Back to Portfolio

**From Investment Details:** Only a "Back" button at the bottom of the page.
- No breadcrumb navigation
- No "Return to portfolio" explicit link
- The "DUAL CURRENCY INVESTMENT" page title present on other screens is replaced with "INVESTMENT DETAILS" -- which is fine but provides no clickable navigation

**From Confirmation Page:** No link to portfolio or to view the newly placed investment.
- Only CTA is "Place Another Investment"
- User must use the top navigation ("FX and Investment") to return to portfolio
- This is a missed opportunity for a "View my investments" or "Go to portfolio" link

### 8.4 Page Title Consistency

| Screen | Page Title |
|---|---|
| Landing | "DUAL CURRENCY INVESTMENT" |
| Parameters | "DUAL CURRENCY INVESTMENT" |
| Funding Account | "DUAL CURRENCY INVESTMENT" |
| Review | "REVIEW" (left label) + no page title |
| Confirmation | None (just success message) |
| Details | "INVESTMENT DETAILS" (left label) |

The title treatment is inconsistent. Some screens use the product name as a top-level heading, while others use a screen-specific label. The Review and Details screens use a left-aligned sidebar-style label, while others use a standard page heading position.

---

## EXECUTIVE SUMMARY

### Overall Assessment

The OCBC DCI product flow demonstrates competent structural design with a logical step-by-step placement process, well-organized portfolio views, and a thoughtful settlement outcome presentation (the strike-met/not-met banners are effective). However, the product suffers from **critical deficiencies in risk communication, financial terminology accessibility, and content completeness** that are unacceptable for a regulated structured investment product.

The most dangerous gap is the absence of explicit, plain-language risk disclosure within the investment placement flow. A novice corporate investor can place a $200,000 investment in a currency-linked derivative without ever being clearly told: "You may receive your money back in a different currency at a loss." The T&C modal containing lorem ipsum placeholder text is a showstopper that must be resolved before any production deployment.

The navigation inconsistencies (three different nav configurations across the product) indicate fragmented design system governance and would undermine user confidence in a banking platform where trust is paramount.

### UX Health Score: 5.0 / 10

Functional structure is solid but critical risk disclosure, terminology accessibility, and navigation consistency issues make this product unsafe for novice users and non-compliant with banking UX best practices.

### Top 5 Priority Recommendations

**1. Add explicit risk disclosure within the placement flow**
- **What:** Add a risk callout box on the Investment Parameters screen (before strike selection) and on the Review screen (before Submit) that plainly states: "This investment carries currency risk. If the exchange rate moves unfavorably, you will receive your proceeds in [alternate currency], which when converted back to [base currency] may result in a loss."
- **Why:** A corporate customer could place a six-figure investment without understanding the core risk. Regulatory exposure and customer harm potential is extreme.
- **How:** Insert a yellow/amber warning banner with a caution icon between the Potential Outcomes panel and the Strike Price section. On Review, add a risk acknowledgment checkbox before the Submit button.
- **Effort:** Quick Win

**2. Replace lorem ipsum T&C with actual content and add risk acknowledgment checkbox**
- **What:** Populate the T&C modal with real terms and conditions. Add a mandatory checkbox on the Review screen: "I acknowledge that this is a capital-at-risk product and I may receive my proceeds in a currency different from my investment currency."
- **Why:** Placeholder T&C in a banking product is a regulatory compliance failure. Explicit acknowledgment provides audit trail and forces user engagement with risk.
- **How:** Work with Legal/Compliance to finalize T&C content. Implement checkbox as blocking requirement for Submit button.
- **Effort:** Medium Lift

**3. Show actual period return alongside annualized yield**
- **What:** Everywhere "X% p.a." is displayed, also show the actual period return: "6.50% p.a. (~0.54% for 1 month)" and the equivalent base-currency value for Scenario B.
- **Why:** Novice users will misinterpret annualized yield as period yield, leading to incorrect return expectations. For a 1-week investment at 6.5% p.a., the actual return is ~0.125%, which is materially different from user expectations.
- **How:** Add calculated period yield next to every p.a. display. In Scenario B, add a line: "Equivalent to approximately [X] [Base Currency] at current exchange rate."
- **Effort:** Medium Lift

**4. Unify navigation bar across all screens**
- **What:** Standardize the navigation bar to a single configuration. Choose either "FX and Investment" or "FX and Treasury" (recommend "FX and Investment" as it directly describes DCI). Ensure consistent capitalization and correct section highlighting.
- **Why:** Three different navigation configurations across the same product flow creates disorientation and erodes trust. The Multi-Currency Account page highlighting "Trade finance" is a mislabeled entry point.
- **How:** Audit all screens against a single nav component from the design system. Fix the active state logic for each page.
- **Effort:** Quick Win

**5. Add progress indicator and breadcrumbs to the placement flow**
- **What:** Add a horizontal stepper showing "1. Investment Parameters > 2. Funding Account > 3. Review > 4. Confirmation" at the top of each placement screen. Add breadcrumbs on detail pages: "FX and Investment > Dual Currency Investment > [Reference Number]."
- **Why:** Users have no sense of progress during a multi-step financial transaction. This increases anxiety and abandonment, especially for high-value transactions.
- **How:** Implement a standard stepper component (common in OCBC's existing design patterns for other flows). Add breadcrumb component to detail pages.
- **Effort:** Quick Win

---

### Design System & Consistency Notes

1. **Navigation bar is NOT a single component** -- at least 3 variants exist with different labels and capitalization
2. **Status badge colors are inconsistent:**
   - "Active" = no badge/color (implied default)
   - "Expiring Soon" = orange text badge (some screens) / orange pill badge (others)
   - "Awaiting Settlement" = yellow pill badge
   - "Settled" = grey pill badge
   - These need standardization
3. **Button hierarchy is inconsistent:**
   - "Place investment" appears as: red solid button (banner), blue text link (empty state), red outline button (not seen but implied)
   - "Reinvest" appears as: grey outline button (details page), red solid button (portfolio banner)
4. **The "DUAL CURRENCY INVESTMENT" title uses ALL CAPS SPACED SMALL CAPS style** on main pages but "INVESTMENT DETAILS" and "REVIEW" use a different left-sidebar label style. These should be unified.
5. **Scenario cards:** Green background for Scenario A, amber/light orange for Scenario B is effective and should be standardized as a reusable component.
6. **Settlement outcome banners:** The green (strike met) and amber (strike not met) banners are well-designed. Ensure these are reusable design system components with consistent icon usage.
7. **Footer inconsistency:** Some screens show "(c) OCBC. All Rights Reserved." on the left with "Conditions of Access | Security & Privacy" on the right. The Multi-Currency Account page reverses this layout.

---

### Accessibility Summary

**WCAG Violations Identified (from visual inspection only):**

1. **1.4.3 Contrast (Minimum):** Several light grey helper text elements (e.g., "Funds will be credited here if settlement is in USD") appear to use low-contrast grey on white. Needs contrast ratio testing.
2. **1.3.1 Info and Relationships:** The Scenario A/B panels use color (green/red badges) as the primary differentiator. While labels also exist, the color carries significant semantic weight.
3. **1.1.1 Non-text Content:** The empty state illustration and value proposition card icons have no visible alt text (cannot verify from screenshot).
4. **2.4.6 Headings and Labels:** Form field labels are visible and persistent (not placeholder-only) -- GOOD. However, the strike price radio buttons lack descriptive labels explaining the tradeoff.
5. **2.4.8 Location:** No breadcrumbs or step indicators to communicate user location within the flow.
6. **3.3.2 Labels or Instructions:** The Investment Amount field shows "0.00" as placeholder and "NIL" as currency default -- these are not helpful instructions.
7. **3.3.5 Help:** No contextual help (tooltips, info icons, "learn more" links) on any form field in the placement flow.

**Overall Accessibility Risk Level: MEDIUM-HIGH**
The product appears to follow basic form labeling practices but lacks contextual help, has potential contrast issues, and provides no mechanism for screen reader users to understand the risk/return tradeoff in the strike price selection.

---

### What's Working Well

1. **Settlement outcome banners are clear and well-designed.** The green "Strike Price Met" and amber "Strike Price Not Met" banners on portfolio rows and detail pages use color, icons, and plain language to communicate outcomes. The inline explanation ("Fixing rate 1.3000 was above strike price of 1.2850. You will receive...") is one of the best content elements in the product.

2. **Investment Timeline is excellent.** The 4-date vertical stepper with plain-language descriptions for each date is well-structured and provides clear temporal context. This component appears consistently across the parameters, review, and confirmation screens.

3. **Settlement breakdown table is transparent.** The Principal / Yield / Total Settlement structure on detail pages is clear, uses green coloring for the yield line, and provides a complete accounting of the payout. This builds trust.

4. **Dual settlement account UX is thoughtful.** The Funding Account screen's approach of collecting both a base-currency and alternate-currency settlement account upfront -- with helper text explaining when each is used -- is proactive design that avoids a confusing post-maturity account selection step.

5. **Portfolio summary dashboard is information-dense but scannable.** The four metrics (Active Investments, Expiring Soon, Total Invested, Avg Yield) with the last-updated timestamp provide a useful at-a-glance overview. The tab separation of Active vs Settled investments is logical.

---

### Suggested Next Audit Scope

1. **Mobile responsiveness audit** -- This product was analyzed at desktop resolution only. Given that corporate banking users increasingly access platforms on tablets and mobile devices, a responsive design audit is essential.
2. **Maker-Checker approval flow** -- The confirmation screen filename references "overseas-confirmation-maker," implying a maker-checker workflow. The checker/approver experience was not included in these screens and needs separate audit.
3. **Error state and edge case design** -- Zero error states, loading states, or timeout handling were present in the 21 screens reviewed. These must be designed and audited.
4. **Accessibility testing** -- A full WCAG 2.2 AA audit with automated tools (axe, Lighthouse) and screen reader testing (NVDA/JAWS) on the implemented product.
5. **Reinvestment flow for "Strike Not Met" currency swap** -- The currency pair swap on reinvestment after an alternate-currency settlement needs dedicated UX research to validate that users understand and expect this behavior.
