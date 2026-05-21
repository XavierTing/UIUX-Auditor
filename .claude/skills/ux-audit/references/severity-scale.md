# Severity Scale

Grade every finding on this scale. Be precise — do not default to MEDIUM when unsure. Consider the user impact and frequency.

---

## CRITICAL

**Blocks user task completion or causes major confusion.**

The user cannot achieve their primary goal, or the interface actively misleads them into making errors with real consequences.

**Indicators:**
- User cannot complete the core task at all
- User loses data, money, or makes irreversible mistakes
- The interface does the opposite of what the user expects
- A core screen or flow is broken or inaccessible

**Examples:**
- Submit button does nothing / leads to an error with no recovery path
- Form validation rejects valid input with no explanation
- A required step in a checkout flow is unreachable
- User can initiate a destructive action (sell, delete, transfer) on data they don't have
- Navigation completely breaks on mobile — user is trapped
- Critical information is hidden or misleading (wrong price displayed, incorrect totals)

---

## HIGH

**Significantly degrades the experience. Likely causes drop-off.**

The user can technically complete the task, but the friction is severe enough that many users will abandon, lose trust, or make mistakes.

**Indicators:**
- Significant number of users will fail or give up
- Creates distrust in the product or brand
- Causes measurable business impact (conversion drop, support tickets)
- Accessibility violation that excludes a user group

**Examples:**
- WCAG AA contrast failure affecting all secondary text (large user impact)
- No explanation of domain-specific terminology for the target audience
- Touch targets below 44px on mobile (mis-taps are frequent)
- Form field label is ambiguous — users enter wrong data type
- No cost breakdown before purchase confirmation (hidden fees perception)
- Empty state provides no guidance on what to do next
- No loading state on critical actions (user double-submits)

---

## MEDIUM

**Friction point. Reduces confidence or efficiency.**

The user can complete the task, but the experience is noticeably suboptimal. Creates friction that accumulates across repeated use.

**Indicators:**
- Slows users down or adds unnecessary steps
- Reduces confidence without blocking completion
- Inconsistency that causes momentary confusion
- Polish gap that makes the product feel unfinished

**Examples:**
- Chart has no Y-axis labels — user can see a trend but not interpret values
- Navigation requires extra clicks to reach a common destination
- Error messages are technically correct but not helpful ("Invalid input")
- Order confirmation shows a truncated ID instead of a human-readable reference
- Time zone not displayed alongside timestamps
- Progress indicator missing in a multi-step flow
- Tooltip content not discoverable — users don't know to hover

---

## LOW

**Polish issue. Minor inconsistency or nice-to-have improvement.**

The user is unlikely to notice or be bothered by this in isolation, but fixing it raises the overall quality bar.

**Indicators:**
- Cosmetic inconsistency
- Minor convenience improvement
- Best practice not followed but no measurable impact
- Only affects edge cases or power users

**Examples:**
- Inconsistent border radius between similar components (4px vs 6px)
- Footer missing standard links (Terms, Privacy) on a non-regulated product
- 404 page lacks suggested navigation links
- Account number shown in a dropdown where only account name matters
- Slight alignment mismatch between two adjacent elements
- Skip-nav link missing (affects keyboard users but tab order still works)
- Icon spacing slightly inconsistent across similar buttons
