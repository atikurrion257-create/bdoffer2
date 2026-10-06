# House Standard (fill this in)

**verified against:** template, 2026-10-06. **This file is yours to edit.** Every `TODO` below is a decision only you can make. Skills read this file and apply it as *your* convention rather than generic advice — this is what makes the plugin an agency asset instead of a generic assistant.

> Editing rule: fill in the TODOs, delete the ones that do not apply, and keep the file under ~400 lines. Never edit a copy inside a skill folder — edit here and rebuild.

## 1. Dialect defaults

- Default dialect for new client work: `TODO` (recommended: V4 atomic where the stack supports it, else V3 + containers).
- Do we allow hybrid pages? `TODO` (recommended: yes, at section level only, with a recorded exception).
- Do we migrate existing sites to V4 as part of a redesign? `TODO` (recommended: no — separate project).
- Minimum Elementor / Elementor Pro / WordPress / PHP we support: `TODO`.

## 2. Layout conventions

- Maximum container nesting depth for a simple section: `TODO` (recommended: 4).
- Wrapper-only containers allowed? `TODO` (recommended: no).
- Spacing source: `TODO` (recommended: container gap + padding tokens; Spacer widgets only for one-off vertical rhythm).
- Do we use sections/columns anywhere? `TODO` (recommended: legacy documents only).
- Standard breakpoints and any custom ones: `TODO` (record the exact px values; e.g. mobile ≤767, tablet ≤1024, plus any laptop/widescreen).

## 3. Design tokens

- Source of truth: `TODO` (options: Elementor global colours/fonts + Theme Style, atomic Classes/Variables, or theme.json synced to the Kit).
- Palette roles and hex values: `TODO`.
- Type scale (names + sizes + line-heights, responsive steps): `TODO`.
- Spacing scale: `TODO`.
- Radii / shadows / borders: `TODO`.
- Naming convention for classes and variables: `TODO` (examples: `btn--primary`, `card`, `text--lead`, `space/md`, `color/primary`).
- Fluid typography (clamp) policy: `TODO`.
- Do we allow per-element overrides of tokens? `TODO` (recommended: no, except one-off illustration).

## 4. Components and reuse

- Reuse mechanism preference: `TODO` (recommended: V4 Components for layout-level reuse; Loop for repeatable content; global widget only for a single shared element on V3 sites).
- Where do shared site parts live (header/footer/templates)? `TODO`.
- Rule for when a section becomes a component vs a template vs a loop: `TODO`.

## 5. Content model and ACF

- Naming conventions for CPTs, taxonomies, field groups: `TODO` (prefix style, singular/plural).
- ACF return formats: image → `TODO` (recommended: ID), date → `TODO`, link → `TODO`.
- Everything a client might change must be one of: post field / ACF field / option / menu — never a literal in settings. Exceptions: `TODO`.
- Options pages we use: `TODO` (e.g. Global settings: contact details, social links, footer copy).
- Repeater policy: `TODO` (recommended: model as a CPT + loop when the items deserve URLs or reuse; otherwise a third-party/custom tag with a documented cost).
- Who edits what (roles): `TODO`.

## 6. Code placement and exceptions

- Child theme vs small plugin vs must-use plugin rules: `TODO` (recommended: presentation in the child theme; CPTs/fields/behaviour in a small site plugin; hardening in mu-plugins).
- Is custom code ever allowed inside Elementor content? `TODO` (recommended: no, except a scoped documented embed).
- Required record for any exception — what / why / scope / exit condition: `TODO`.
- Custom widget policy: `TODO` (recommended: only when reused ≥2 places, needs real controls, and the team can maintain it).

## 7. Quality gates and budgets

- DOM / widget-count budget per page: `TODO`.
- Image policy (formats, max weight, required dimensions, LCP image handling): `TODO`.
- Font policy (self-hosted, `font-display`, subsets, max families/weights): `TODO`.
- An accessibility baseline: `TODO` (recommended: WCAG 2.1/2.2 AA behaviours; escalate to blockers for public-sector/education/health clients).
- Escalation rule for compliance-bound clients: `TODO`.
- Which quality findings are blockers at our agency: `TODO`.
- Cache/CDN/minification stack we must not fight: `TODO`.

## 8. Approval tiers (defaults — override if we differ)

| Tier | Our default |
|---|---|
| READ-ONLY | Analysis, plans, audits, research, local files |
| SAFE AUTOMATION | Local artifacts, scaffolds for review, snippets for review, reports |
| APPROVAL REQUIRED | Anything on staging; drafts; template creation; token changes on staging |
| HIGH-RISK | Production writes, deletions, global style changes, conditions changes, plugin installs, SEO/security config, PHP/DB changes, bulk edits |

Never acceptable without explicit approval: `TODO` (keep the master list; the plugin will enforce the tier list from the master instructions).

## 9. Client and confidentiality

- May client designs/content be uploaded to an AI tool? `TODO` (per-client consent rule).
- Anonymisation requirements: `TODO`.
- Are we willing to work from a competitor's site as a visual reference? `TODO` (recommended: pattern extraction yes, verbatim cloning no).

## 10. Output conventions

- Preferred deliverables per task type: `TODO` (blueprint, audit report, QA report, quality report, conditions matrix, field matrix).
- Language/tone: `TODO`.
- Do we include effort estimates? `TODO` (bands only, no hours, unless asked).
- Always include a verification plan? `TODO` (recommended: yes).
