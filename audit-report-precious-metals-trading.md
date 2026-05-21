# UI/UX AUDIT REPORT: Precious Metals Trading App

**Audit Date:** 9 March 2026
**URL:** `https://theory-round-48270233.figma.site`
**Auditor Persona:** Novice investor, new to precious metals
**Platform:** Web desktop (1280x1080)
**Flow Scope:** Buy & sell flows for Gold (XAU), Silver (XAG), Platinum (XPT), Palladium (XPD)
**Screens Reviewed:** Dashboard, Trade (x4 metals), Order Review, Order Confirmation, Order History, Products, 404

---

## EXECUTIVE SUMMARY

This is a well-structured precious metals trading prototype with a clean visual identity, logical information architecture, and a complete buy/sell flow covering all 4 metals. The app follows modern SaaS conventions (Tailwind + shadcn/ui) and provides a credible trading experience. However, for a **financial trading product used by novice investors**, there are significant gaps in **trust signalling, error prevention, educational scaffolding, and accessibility compliance** that would erode confidence and cause drop-off. The biggest risks are: (1) a novice user has no onboarding or guided first-trade experience, (2) critical accessibility failures in contrast, touch targets, and motion, (3) the sell flow allows zero-balance sells to reach the review screen before failing, and (4) currency conversion introduces confusion without adequate explanation.

**Overall UX Health Score: 6.5 / 10** -- Solid foundation, but unshipped for production without fixing trust, accessibility, and novice-friendliness gaps.

---

## FINDINGS TABLE

| # | Screen / Component | Dimension | Severity | Finding | User Impact | Recommendation |
|---|---|---|---|---|---|---|
| 1 | Trade -- Order Form | 6. Forms | CRITICAL | No onboarding or guided first-trade experience. A novice investor lands on the trade page and sees "Market" vs "Limit" order types, 5 currency options, bid/ask/spread data -- with zero explanation of what any of it means. | Novice users will feel overwhelmed and abandon. They don't know what a "Market Order" is, what "XAU" means, or why there's a spread. | Add contextual tooltips (?) next to "Order Type", "Bid", "Ask", "Spread". Add a first-time user banner: "New to trading? Here's how to place your first order" with a 3-step explainer. Consider defaulting to Market order and SGD to reduce decisions. |
| 2 | Trade -- Sell Flow | 5. Components | CRITICAL | All 4 PM account balances start at 0 oz. The sell toggle is fully accessible, but entering any amount will only fail at validation ("Cannot sell more than your holdings (0 oz)"). A novice user doesn't know they own nothing until they try to sell. | User attempts a sell, gets an error toast, doesn't understand why. Feels broken. | Disable the "Sell" button or show a clear inline message when holdings = 0: "You don't hold any [Metal] yet. Buy some first to start selling." Prevent the error path entirely. |
| 3 | Trade -- Order Form | 9. Cognitive Load | CRITICAL | The currency selector (SGD/USD/EUR/HKD/JPY) on the order form introduces massive cognitive load for a novice. Switching currencies changes the amount, the price display, and the debit account -- but there's no explanation of exchange rates, fees, or why you'd choose a non-SGD currency. | User accidentally selects JPY, sees a wildly different price, panics. Or enters "1000" thinking it's SGD when it's JPY. Currency confusion in financial apps causes real monetary mistakes. | Default to SGD and collapse the currency selector behind "Advanced options" or a "Change currency" link. Show the exchange rate prominently when non-SGD is selected. Add a warning: "You're trading in [Currency]. Amount will be debited from your [Currency] account." |
| 4 | Global | 8. Accessibility | HIGH | No `prefers-reduced-motion` support despite extensive animations (accordion, dialog slide-in, fade, zoom, pulse). WCAG 2.1 SC 2.3.3 violation. | Users with vestibular disorders or motion sensitivity experience discomfort. Some may be unable to use the app. | Add a global `@media (prefers-reduced-motion: reduce)` rule that disables/minimizes all animations and transitions. |
| 5 | Global | 4. Colour & Contrast | HIGH | `--muted-foreground` (#717182) on `--muted` (#ececf0) and `--accent` (#e9ebef) backgrounds fails WCAG AA at ~3.5:1 contrast (requires 4.5:1). This affects secondary labels, placeholder text, and metadata across the entire app. | Low-vision users cannot read secondary text. Even normally-sighted users in bright ambient light will struggle. | Darken muted foreground to at least #5e5e6e (or darker) to achieve 4.5:1 on all light backgrounds. |
| 6 | Global -- All interactive elements | 8. Accessibility | HIGH | Default button/input height is `h-9` (36px), below the WCAG 2.2 SC 2.5.8 minimum of 44px for touch targets. | Mobile or touch-screen users will mis-tap buttons and inputs frequently. Even on desktop, users with motor impairments struggle with small targets. | Increase all interactive element min-heights to 44px. At minimum, apply `min-h-11` (44px) for touch devices via `@media (pointer: coarse)`. |
| 7 | Dashboard -- Market Overview | 2. Visual Hierarchy | HIGH | All 4 metal cards have equal visual weight and size. A novice investor doesn't know which metal to start with. There's no "recommended for beginners" or "most popular" signal. Gold (the most common entry point) isn't visually prioritised. | User faces a 4-way equal-choice paralysis. Novice investors often start with gold but nothing guides them there. | Make the Gold card slightly larger or add a "Most Popular" or "Start Here" badge. Alternatively, add a "New to precious metals? Start with Gold" CTA above the grid. |
| 8 | Trade -- Order Form | 6. Forms | HIGH | The "Amount" field expects a currency amount, but the label says "Amount (SGD)" -- it's unclear whether this is the amount to spend or the value of metal to buy. The computed "Quantity" display below is the only way to understand what you're actually getting. | Novice user enters "100" thinking they're buying 100 oz. They're actually spending S$100 (~0.015 oz of gold). The mental model mismatch causes distrust. | Rename to "Spend Amount (SGD)" or offer a toggle: "I want to spend [amount]" vs "I want to buy [quantity] oz". Show the quantity computation more prominently, e.g., "You'll receive ~0.015 oz of Gold". |
| 9 | Order Review | 10. Trust | HIGH | No fee disclosure, no spread cost breakdown, and no "what you'll pay vs. what you get" summary. The review page shows the total but doesn't break down: metal cost + spread + any fees. For a financial product, this is a trust-eroding omission. | Novice investor doesn't understand what they're paying for. Post-purchase, they see a different P&L than expected because the spread cost wasn't made transparent. Feels like hidden fees. | Add a cost breakdown section: "Metal price: S$X, Spread (0.5%): S$Y, Total: S$Z". Even if there are no additional fees, state "No additional fees" explicitly -- absence of reassurance is itself a trust issue. |
| 10 | Order Review | 7. Feedback | MEDIUM | The "Confirm Buy/Sell" button has no loading state mentioned in the UI. After clicking, there's a direct navigation to the confirmation page. If the network is slow, the user may double-click or wonder if their order went through. | Double-submission risk. User anxiety during the most critical moment of the flow. | Add a loading spinner on the button with text "Processing..." and disable the button after first click. Show a brief processing overlay for market orders. |
| 11 | Dashboard -- Portfolio Holdings | 7. Feedback | MEDIUM | The empty state for holdings says "No holdings yet" with a link "Start trading to build your portfolio" -- but the link text isn't specific about WHERE it goes. It should clearly go to the trade page for the most accessible metal. | Novice user sees empty portfolio but isn't guided to a specific action. Generic "start trading" is vague. | Change to "Buy your first precious metal" with a button linking to `/trade/XAU`. Make it look like a CTA button, not a text link. |
| 12 | Trade -- Price Chart | 5. Components | MEDIUM | The price chart shows price history but has no Y-axis labels, no gridlines, and no volume data. The time interval buttons (1H, 1D, 1W, 1M, 1Y) don't explain what they represent. | Novice investor can't read the chart meaningfully. "Is S$6,588 high or low historically?" is unanswerable without Y-axis context. | Add Y-axis price labels, subtle gridlines, and labels under the time buttons ("Last hour", "Last day", etc.). Consider adding a simple annotation: "52-week range: S$X -- S$Y". |
| 13 | Trade -- Metal Tabs | 1. Info Architecture | MEDIUM | The metal tabs (Gold XAU, Silver XAG, Platinum XPT, Palladium XPD) use chemical/trading codes (XAU, XAG, XPT, XPD) that novice investors don't recognise. The codes are more prominent than the metal names. | User doesn't know what "XPT" means without prior knowledge. Creates an expert-oriented feel that excludes beginners. | Show the metal name first, code second, and in smaller text: "Gold (XAU)" instead of "Gold XAU". On the Products page, explain what the codes mean. |
| 14 | Order Confirmation | 10. Trust | MEDIUM | The order ID is a truncated UUID (first 8 chars). This looks like a system artifact, not a human-friendly order reference. There's no instruction to "save this for your records" or option to download/email a receipt. | User has no record of the trade. If they need to reference it for support or tax purposes, a truncated UUID is not user-friendly. | Display a full human-readable order reference (e.g., "PM-2026-0001"). Add "Download Receipt" and "Email Confirmation" buttons. |
| 15 | Navigation | 1. Info Architecture | MEDIUM | "Trade" nav link goes directly to `/trade/XAU` (Gold). There's no intermediate trade landing page showing all 4 metals with pricing. A user wanting to trade Silver must click "Trade" then switch tabs -- the nav doesn't reflect the sub-navigation. | If a user is looking for Silver, they land on Gold first and must discover the tab system. Mild friction but repeated across sessions. | Either: (a) make "Trade" a dropdown with all 4 metals, or (b) add a trade landing page showing all metals with "Trade" CTAs, or (c) remember the user's last-traded metal. |
| 16 | Products Page | 9. Cognitive Load | MEDIUM | The product info for each metal is comprehensive but presented as long-form text. A novice investor comparing metals has to read 4 separate tab views. There's no comparison view or summary table across metals. | User can't easily compare "Should I buy Gold or Silver?" -- they have to mentally hold information across tab switches. | Add a "Compare Metals" section/page with a side-by-side table: Price, Min Quantity, Volatility, Use Cases, Best For. |
| 17 | Global -- Footer | 2. Visual Hierarchy | LOW | The footer only contains a copyright line. No links to Help, Terms, Privacy Policy, Contact, FAQ, or regulatory information. For a financial product, this is a trust gap. | Novice investors look for regulatory info, help resources, and legal information in the footer. Absence reduces perceived legitimacy. | Add footer links: Help Center, Terms & Conditions, Privacy Policy, Contact Us, Regulatory Information. For a trading app, include the licence/regulatory body reference. |
| 18 | Dashboard -- Recent Orders | 2. Visual Hierarchy | LOW | The "Recent Orders" section shows 8 orders in a table. The table headers (Time, Metal, Side, Type, Quantity, Price, Total, Status) are dense for a novice. The table is the same component on the Dashboard and Orders page -- no progressive disclosure. | Novice sees a wall of data on the dashboard. The recent orders table is more useful for active traders than first-time users. | On the Dashboard, show only the 3 most recent orders in a simplified card format (not a table). Reserve the full table for the Orders page. |
| 19 | Trade -- Debit/Credit Accounts | 6. Forms | LOW | Account display format is "Current Account (501-100234-001) -- S$50,000.00". The account number is meaningless to the user in this context and adds noise. | User must parse a long string to find the relevant info (which account and how much is in it). | Simplify to "Current Account -- S$50,000.00" in the dropdown. Show account numbers only on hover/expand or on a dedicated accounts page. |
| 20 | Global | 8. Accessibility | LOW | No skip-navigation link is present. Keyboard-only users must tab through the entire nav bar on every page load. | Keyboard users waste time tabbing through 4 nav items + account info before reaching main content. | Add a visually hidden skip link: "Skip to main content" that appears on focus, jumping to the main content area. |
| 21 | 404 Page | 1. Info Architecture | LOW | The 404 page shows "404 / Page not found" with a "Go to Dashboard" button. No search, no suggested links, no explanation of what might have gone wrong. | Dead end. User who mistyped a URL or followed a broken link gets no helpful recovery path. | Add suggested links (Dashboard, Trade, Products) and a brief message: "The page you're looking for doesn't exist. Here are some places to start." |

---

## TOP 5 PRIORITY RECOMMENDATIONS

### 1. Add Novice Investor Onboarding & Contextual Education
- **What to fix:** Add tooltips, a first-trade walkthrough, and inline explanations for trading terminology (Market/Limit orders, Bid/Ask/Spread, XAU codes).
- **Why it matters:** The stated user is a novice investor. Every unexplained term is a drop-off point. Financial literacy cannot be assumed. A novice who doesn't understand what they're buying will not buy.
- **How to fix it:** (a) Add `(?)` tooltip icons next to "Order Type", "Bid", "Ask", "Spread" with 1-sentence plain-language definitions. (b) Show a dismissible first-visit banner on the Trade page: "New to precious metals? [Learn the basics] or [Place your first trade -- we'll guide you]". (c) Default the form to Market order + SGD to reduce initial decisions from 5 to 2 (metal + amount).
- **Effort estimate:** Medium Lift

### 2. Fix the Sell Flow for Zero-Balance Holdings
- **What to fix:** Prevent users from entering the sell flow when they hold 0 oz of a metal.
- **Why it matters:** Currently, a user can toggle to "Sell", enter an amount, and only discover they can't sell via a toast error. This is error-provoking rather than error-preventing. Nielsen's Error Prevention heuristic (H5) requires designing to prevent errors, not just recover from them.
- **How to fix it:** When holdings = 0, either (a) disable the Sell toggle with a tooltip "You don't hold any Gold yet", or (b) replace the sell form body with an inline message: "You don't have any Gold to sell. [Buy Gold now]" with a CTA. Show the user's current balance prominently in the "Your Holdings" sidebar card.
- **Effort estimate:** Quick Win

### 3. Add Cost Transparency on the Order Review Page
- **What to fix:** Break down the total cost into metal price, spread cost, and fees (or explicitly state "no fees") on the review screen before confirmation.
- **Why it matters:** This is a financial product. Regulatory standards (MAS, FCA, SEC) increasingly require clear cost disclosure before execution. Even without regulation, hiding the spread cost erodes trust. A novice who discovers their purchase price is 0.5% above spot after buying feels deceived.
- **How to fix it:** Add a "Cost Breakdown" section on the Order Review page: Metal Price per oz, Spread (0.5%) per oz, You Pay (Ask) per oz, multiplied by quantity, total, and fees (S$0.00 -- No additional fees).
- **Effort estimate:** Quick Win

### 4. Fix WCAG Accessibility Failures (Contrast, Touch Targets, Motion)
- **What to fix:** Three accessibility failures: (a) muted text contrast below 4.5:1, (b) touch targets below 44px, (c) no `prefers-reduced-motion` support.
- **Why it matters:** These are WCAG 2.1/2.2 Level AA violations. Beyond compliance, they affect real users: ~8% of men are colour-deficient, ~15% of the population has a disability, and many users access trading apps on mobile devices. For a financial product, accessibility failures can also be a legal liability.
- **How to fix it:** (a) Darken `--muted-foreground` from #717182 to #5a5a6a. (b) Add `@media (pointer: coarse) { button, input, select, a { min-height: 44px; } }`. (c) Add `@media (prefers-reduced-motion: reduce)` global rule to disable animations.
- **Effort estimate:** Quick Win

### 5. Simplify the Order Form for Novice Users
- **What to fix:** Reduce cognitive load by defaulting to Market order + SGD, clarifying the "Amount" field, and collapsing advanced options.
- **Why it matters:** The current form presents 5+ decisions simultaneously (Buy/Sell, Market/Limit, Currency, Amount, Account). For a novice, this is paralysing. Research shows that reducing form complexity increases completion rates by 20-30%.
- **How to fix it:** (a) Rename "Amount (SGD)" to "I want to spend (SGD)" and add a computed "You'll receive: ~X.XX oz" line below it in a highlight colour. (b) Hide the currency selector behind "Change currency" toggle -- 90%+ of SGD users will trade in SGD. (c) Hide Limit orders behind "Advanced: Limit Order" toggle. (d) Auto-select the user's SGD current account as debit.
- **Effort estimate:** Medium Lift

---

## DESIGN SYSTEM & CONSISTENCY NOTES

**Framework:** Tailwind CSS v4 + shadcn/ui (Radix UI primitives) -- a well-established, consistent component system.

**Consistency strengths:**
- Semantic colour tokens used throughout (--primary, --muted, --destructive, etc.)
- 4px spacing grid consistently followed
- Typography scale follows Tailwind's standard progression
- Focus indicators use the modern `:focus-visible` pattern with forced-colors fallback

**Inconsistencies flagged:**
1. **Metal colour system is ad-hoc:** Gold=amber, Silver=slate, Platinum=cyan, Palladium=violet. These aren't part of the semantic token system -- they're hardcoded. If the palette changes, these won't update.
2. **Button height inconsistency:** Some buttons are `h-8` (32px), some `h-9` (36px), some `h-10` (40px). The order form submit button, the nav links, and the product CTA buttons don't share a consistent height.
3. **Missing text-5xl:** The type scale jumps from `text-4xl` (36px) to `text-6xl` (60px). Only the 404 page uses `6xl` -- if an intermediate heading is ever needed, it doesn't exist.
4. **Toast component (Sonner) is external** to the shadcn/ui system. Its styling doesn't use the semantic tokens, creating a risk of visual inconsistency if the theme changes.

**Components that should be standardised:**
- The "metal price card" (used in Dashboard and Trade page) should be a documented component in the design system with consistent hover/active states.
- The "cost summary" pattern (used in Trade form, Order Review, and Order Confirmation) appears 3 times with slightly different layouts -- consolidate into one reusable component.

---

## ACCESSIBILITY SUMMARY

| WCAG Criterion | Level | Status | Details |
|---|---|---|---|
| 1.4.3 Contrast (Minimum) | AA | FAIL | `--muted-foreground` (#717182) on `--muted`/`--accent` backgrounds: ~3.5:1 (needs 4.5:1) |
| 2.3.3 Animation from Interactions | AAA | FAIL | No `prefers-reduced-motion` support; animations persist for all users |
| 2.5.8 Target Size (Minimum) | AA | FAIL | Interactive elements at 36px, below 44px minimum |
| 2.4.1 Bypass Blocks | A | MISSING | No skip-navigation link found |
| 1.3.1 Info and Relationships | A | UNCLEAR | Cannot verify form label associations from CSS/JS alone; needs HTML audit |
| 4.1.3 Status Messages | AA | LIKELY PASS | Toast notifications via Sonner likely use ARIA live regions |
| 2.1.1 Keyboard | A | PASS | Radix UI components provide keyboard support out of the box |
| 2.4.7 Focus Visible | AA | PASS | `:focus-visible` ring indicators present with forced-colors fallback |

**Overall Accessibility Risk Level: HIGH** -- Three AA-level failures (contrast, touch targets, motion) plus a missing Level A requirement (skip-nav). These must be fixed before production launch, especially for a financial product that may serve elderly or disabled users.

---

## WHAT'S WORKING WELL

1. **Logical, complete flow architecture.** The buy flow (Dashboard -> Trade -> Review -> Confirmation) is a well-structured 4-step funnel. Every step has a clear back path, and the confirmation page provides 3 clear next actions. This is textbook good flow design.

2. **Excellent product information content.** The Products page for each metal includes "About", "Why Invest", "Fun Facts", and FAQ -- written in accessible plain English. This is exactly the kind of educational content novice investors need. The content quality is high.

3. **Real-time price data with smart refresh intervals.** Prices refresh every 5 seconds, holdings every 10 seconds. The "Live" indicator (pulsing green dot) provides system status feedback. The bid/ask/spread display follows financial industry conventions.

4. **Multi-currency support is genuinely useful.** For a Singapore-based platform serving international investors, supporting 5 currencies with automatic account matching is a strong feature. The implementation (auto-selecting the matching currency account) reduces friction for experienced users.

5. **Modern, credible visual design.** The amber/gold brand identity is appropriate for a precious metals product. The clean, minimal shadcn/ui aesthetic feels professional and trustworthy -- this doesn't look like a scam or a toy. The typography is clean and the spacing is generous.

---

## SUGGESTED NEXT AUDIT SCOPE

1. **Mobile responsiveness audit** -- The current design is 1280px desktop. The app uses sm/md/lg breakpoints but no xl/2xl. A mobile walkthrough of the buy/sell flow would likely reveal significant layout and touch-target issues.

2. **Error state & edge case audit** -- Test: What happens with extremely large amounts? Network failure mid-order? Session timeout? Concurrent tab trading? The current audit found no error boundary or offline state handling.

3. **Localization audit** -- The app uses `en-SG` locale with SGD but supports 5 currencies. Are number formats, date formats, and currency symbols correct for each locale? Does JPY (zero decimal) display correctly?

4. **Post-trade experience audit** -- What happens after a user builds a portfolio? The Holdings table, P&L calculations, and order history filtering should be tested with realistic multi-metal, multi-currency portfolio data.
