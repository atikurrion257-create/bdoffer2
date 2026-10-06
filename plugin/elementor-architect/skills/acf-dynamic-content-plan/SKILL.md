---
name: acf-dynamic-content-plan
description: >
  Design the content model and its Elementor rendering so non-developers can edit safely:
  ACF field groups, field types, location rules, return formats, naming contracts,
  dynamic-tag mapping per element, loop strategies for repeatable content, options pages,
  empty-state fallbacks, and explicit workarounds for field types Elementor cannot render
  natively (repeater, flexible content, gallery, clone). Use when the user asks about ACF
  architecture, dynamic content, making something editable, repeater or flexible-content
  strategy, options pages versus per-post fields, dynamic tags, or "why does ACF show --?".
  Do NOT use for site-level content modelling and templates (use
  wordpress-site-architecture), for auditing artifacts (use elementor-structure-audit), or
  for page layout planning (use design-to-elementor-plan).
---

# ACF + Dynamic Content Plan

The goal is not "use ACF everywhere". It is: **the person who owns this content after launch can change it, safely, without a developer.**

## When to use

- ACF field-group design; field types and return formats.
- "Make this editable", "the client must be able to change X".
- Repeater / flexible content / gallery / clone strategy.
- Dynamic tag mapping and fallbacks.
- Diagnosing why a dynamic value renders empty or as `--`.

## When NOT to use

Site-level content modelling, templates and conditions (→ `wordpress-site-architecture`); artifact auditing; page layout plans.

## Inputs

- The content requirements per section (or the blueprint/element tree).
- ACF type installed: **free or Pro** (Repeater, Flexible Content, Clone, Gallery are Pro).
- Elementor and Elementor Pro versions; dialect (V3/V4).
- Editor roles: who changes what, and how technical they are.
- Existing field groups if this is not a greenfield site.

## Workflow

1. **Classify every content item** into exactly one bucket:
   - **Design decision** → not a field (goes to tokens/classes).
   - **Global site content** → options page (contact details, social links, footer copy, legal text).
   - **Per-post content** → ACF fields / post fields.
   - **Repeatable collection** → CPT + loop (preferred) or a documented alternative.
   - **Classification** → taxonomy.
   - **Static by exception** → state why (e.g. legally fixed copy).
2. **Design field groups.** Name (stable, prefixed), label (human, client's words), type, **return format**, location rules, instructions, required/optional, validation.
3. **Map each element to a data source.** Produce the element↔field table. Every text/image/link that a client will change must appear.
4. **Handle unsupported field types explicitly** using `references/playbook.md` §3. Never promise native rendering for repeater / flexible content / gallery / clone.
5. **Define fallbacks and empty states** for every dynamic field: hide the element, show a default, or show a preview-only placeholder.
6. **Preview-context requirements.** Which preview post must have data for the template to render meaningfully? Record it — the `--` symptom is usually missing values or a location-rule mismatch, not an Elementor bug.
7. **Editor contract.** What each role can change, what is locked, what needs a developer. Keep field groups small and named in the client's language.
8. **Capability/security notes** for anything requiring a custom dynamic tag or code (sanitisation, capability checks, escaping).
9. **Verification steps.** Test with a missing value, a very long value, and the real preview post.
10. **Output** per the contract below.

## Output contract

1. Field-group specification (name / type / return format / location / purpose / who edits).
2. Element ↔ data-source mapping table.
3. Field-type capability matrix with the strategy and fallback for each type in use.
4. Empty-state and fallback policy.
5. Editor roles and locked fields.
6. Risks (including version/ACF-type limitations).
7. Verification steps.
8. Confidence ledger.

## Hard rules

- **Never claim Elementor renders a field type natively without verification.** Mark capability claims LIKELY and version-scoped; Repeater/Flexible Content/Gallery/Clone are reported as not natively supported.
- **Return formats are a contract.** Fix them (image → ID is the usual choice), record them, and keep them consistent.
- **No design decisions in fields.** Exposing "headline colour" to an editor breaks the design system.
- **Prefer CPT + loop over repeaters** whenever the items deserve their own URL, querying, reuse, or independent editing.
- **Every dynamic element gets a defined empty state.**
- **Field names are forever; labels are not.** Name for the code, label for the human.
- Do not build forms of content access that bypass roles/capabilities.

## References

- `references/playbook.md` — field-type matrix, dynamic-tag mapping, fallback patterns, diagnosing empty values, anti-patterns.
- `references/verification-taxonomy.md`, `references/house-standard.md`, `references/dialect-policy.md`.

## Hand-offs

- Where content lives / templates / conditions → `wordpress-site-architecture`.
- Rendering structure → `design-to-elementor-plan`.
- Verification → `elementor-qa-gate`.

## Failure handling

- **Unknown ACF version** → assume Pro but label it; if the required types are Pro-only and Free is installed, state the constraint up front with options (upgrade, restructure, third-party).
- **User insists on repeaters** → provide the third-party or custom-tag route, state the maintenance cost and the exit condition, and record it as an exception.
- **Site is live with existing fields** → produce a delta plan; never rename existing field names without a migration path.
- **"Why does it show --?"** → diagnose in order: field has no value → location rules don't match the post type → preview context is wrong → field key vs name mismatch → cache.
