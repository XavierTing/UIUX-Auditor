# Audit Framework — 9 Dimensions

Evaluate every dimension below. Do not skip any. For each dimension, identify specific findings and grade them using the severity scale.

---

## Dimension 1: Information Architecture & Navigation

Evaluate how information is organised and how users move through the product.

**Criteria:**
- Is the hierarchy of information logical and scannable?
- Are navigation labels clear and user-vocabulary aligned (not internal jargon)?
- Is the user always oriented — do they know where they are, where they came from, and where they can go?
- Are primary, secondary, and tertiary actions visually differentiated?
- Are there dead ends, orphan screens, or unclear exit paths?
- Does the URL structure (if web) reflect the information hierarchy?
- Is the sitemap/page structure discoverable (breadcrumbs, nav highlighting)?

**Common failures:**
- Navigation labels that use internal product terminology instead of user vocabulary
- No visual indicator of the current page/section in navigation
- Dead-end pages with no onward navigation
- Hamburger menus hiding critical navigation on desktop
- More than 7±2 items in a single navigation level

---

## Dimension 2: Visual Hierarchy & Layout

Evaluate how the visual design guides user attention and organises content.

**Criteria:**
- Does the layout guide the eye to the most important action or information first?
- Is there consistent use of spacing, alignment, and grid?
- Are components correctly sized relative to their importance?
- Is there visual noise or competing focal points on any screen?
- Does the layout adapt correctly across breakpoints (if applicable)?
- Is whitespace used intentionally to create breathing room and group related content?
- Are CTAs visually dominant and easy to find?

**Common failures:**
- Multiple elements competing for primary attention on the same screen
- Inconsistent spacing that breaks visual rhythm
- CTAs buried below the fold or visually indistinct from surrounding content
- Grid misalignment between sections
- Layout that doesn't reflow properly at common breakpoints

---

## Dimension 3: Typography & Readability

Evaluate the text presentation for readability and hierarchy.

**Criteria:**
- Are font sizes appropriate for the context and user environment?
- Is line length optimised for reading (45-75 characters per line)?
- Is line height appropriate (1.4-1.6 for body text)?
- Is letter spacing appropriate (not too tight, not too loose)?
- Is there a clear typographic hierarchy (H1 → H2 → H3 → Body → Caption)?
- Is text contrast sufficient for readability?
- Are truncation, overflow, and long-string edge cases handled?
- Is the font stack appropriate for the platform (system fonts vs web fonts)?

**Common failures:**
- Body text below 16px on mobile
- Line lengths exceeding 80 characters (hard to track to the next line)
- No visible difference between H2 and H3 (flat hierarchy)
- Low-contrast text on coloured backgrounds
- Text truncated without indication ("..." missing)

---

## Dimension 4: Colour & Contrast

Evaluate the colour system for meaning, consistency, and accessibility.

**Criteria:**
- Does the colour system communicate meaning consistently (red = error, green = success, amber = warning)?
- Are interactive elements (links, buttons, inputs) clearly distinguishable from static content?
- Is colour used as the sole differentiator anywhere (colour-blind risk)?
- Is the overall palette cohesive and purposeful?
- Do all text-background combinations have sufficient contrast for readability?
- Are status indicators (success, error, warning, info) distinguishable without colour alone?

**Common failures:**
- Using red and green as the only differentiator between positive and negative states
- Interactive text links that look identical to body text
- Decorative use of colour that conflicts with semantic meaning
- Muted/secondary text that fails contrast requirements
- Different shades of the same colour used inconsistently across screens

---

## Dimension 5: Component & Interaction Design

Evaluate interactive elements for clarity, consistency, and completeness.

**Criteria:**
- Are interactive affordances clear — does it look clickable/tappable?
- Are input fields, dropdowns, and controls following platform conventions?
- Are ALL states designed: hover, focus, active, error, disabled, loading?
- Are empty states, zero-data states, and skeleton loaders accounted for?
- Are micro-interactions meaningful and not decorative noise?
- Are destructive actions visually distinct (different colour, confirmation step)?
- Are toggles, checkboxes, and radio buttons used correctly for their data type?

**Common failures:**
- Flat text that is actually clickable but doesn't look like a link
- Missing hover/focus states (element looks static)
- No empty state design (blank screen when no data)
- Loading states that use generic spinners with no context ("Loading..." vs "Loading your orders...")
- Destructive buttons (Delete, Cancel order) styled identically to safe buttons

---

## Dimension 6: Forms & Data Entry

Evaluate form design for usability, efficiency, and error handling.

**Criteria:**
- Is the form length appropriate, or can fields be removed/deferred?
- Are field labels always visible (not just placeholder text)?
- Are inline validation messages timely, specific, and non-punitive?
- Is the error recovery path clear (what went wrong + how to fix it)?
- Are smart defaults, autofill, and progressive disclosure used?
- Are required fields marked clearly?
- Is the form grouped into logical sections for longer forms?
- Do inputs use the correct type (email, tel, number, date) for mobile keyboards?

**Common failures:**
- Labels inside input fields (placeholder-as-label) that disappear on focus
- Validation only on form submit, not inline as the user types
- Error messages that say "Invalid input" without explaining what's wrong
- No indication of which fields are required vs optional
- Asking for information the system already has or could infer
- No autofill support for common fields (name, email, address)

---

## Dimension 7: Feedback & System Status

Evaluate how the system communicates what is happening to the user.

**Criteria:**
- Does the system always inform the user of what is happening (loading, success, failure, progress)?
- Are confirmation states present after destructive or important actions?
- Are error messages written in human language, not system codes?
- Are toast/alert/notification patterns used appropriately and not overused?
- Is progress shown for multi-step processes?
- Are timeouts and session expirations communicated proactively?

**Common failures:**
- Click a button → nothing visible happens for 2+ seconds
- Error messages showing HTTP status codes or stack traces to users
- No confirmation before destructive actions (delete, cancel, discard)
- Toast messages that disappear before the user can read them
- No progress indicator for operations that take more than 1 second

---

## Dimension 8: Cognitive Load & Clarity

Evaluate the mental effort required to use the product.

**Criteria:**
- Does any screen ask the user to make too many decisions at once?
- Is jargon or technical language used where plain language should be?
- Are instructions or help text proactively surfaced, not only on error?
- Is the number of steps in a flow appropriate for the task complexity?
- Is progressive disclosure used where information density is high?
- Are defaults chosen intelligently to reduce decisions?
- Is the interface consistent enough that users can predict behaviour?

**Common failures:**
- Forms with 10+ fields visible at once (no grouping or progressive disclosure)
- Technical terminology without explanation (e.g., "XAU" without "Gold")
- Multi-step flows with no progress indicator or step count
- Asking users to choose between options they don't understand
- Help text hidden in tooltips that users don't discover

---

## Dimension 9: Trust & Emotional Design

Evaluate whether the design builds confidence and feels trustworthy.

**Criteria:**
- Does the design feel credible, professional, and appropriate for the context?
- Are there reassurance signals at high-anxiety moments (e.g., payment, data submission)?
- Is tone of voice consistent across all UI copy?
- Does the experience feel respectful of the user's time and attention?
- Are social proof elements present where appropriate (reviews, testimonials, trust badges)?
- Is pricing transparent with no hidden fees?
- Are regulatory/compliance signals present for regulated industries?

**Common failures:**
- No SSL/security indicators near payment forms
- Missing terms, privacy policy, or regulatory information
- Inconsistent tone (formal in one section, casual in another)
- No cost breakdown before final purchase confirmation
- Missing contact information or support options
- Generic stock photos that reduce credibility
