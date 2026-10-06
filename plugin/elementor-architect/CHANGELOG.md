# Changelog

## 1.0.0 — 2026-10-06

Initial private build. Skills-only (no MCP server, no tools, no credentials).

**Skills**
- `elementor-native-architecture` — dialect policy, native definition, widget/element decision framework, exception register.
- `design-to-elementor-plan` — screenshot / Figma / URL / HTML → decision-complete blueprint.
- `elementor-structure-audit` — hostile audit of JSON, templates, exports, builder output, rendered HTML.
- `elementor-qa-gate` — pre-delivery QA verdict with responsive matrix and content-stress tests.
- `wordpress-site-architecture` — content model, Theme Builder conditions, template hierarchy, migrations.
- `acf-dynamic-content-plan` — field design, dynamic-tag mapping, unsupported-field strategies, fallbacks.
- `site-quality-review` — performance/CWV + SEO + accessibility with flag/recommend/defer decisions.

**Shared reference library (v1)**
- `verification-taxonomy.md` — CONFIRMED / LIKELY / ASSUMED / UNVERIFIED / VERSION-DEPENDENT and the emission rules that make uncertainty structural.
- `dialect-policy.md` — V3 vs V4 atomic vs hybrid decision rules and the probe checklist.
- `widget-map-v3.md`, `widget-map-v4.md` — widget/element selection and availability notes.
- `anti-pattern-catalogue.md` — AI-generated Elementor failure signatures, severity and native alternatives.
- `json-rules.md` — structure, typing, responsive keys, repeaters, output tiers T1/T2/T3.
- `structural-digest-protocol.md` — layered analysis of large artifacts.
- `house-standard.md` — agency conventions with TODO markers to fill in.

**Method note (deviation from the build brief):** the brief listed 14 small skill-specific reference files; this build consolidates them into one `references/playbook.md` per skill (same content, fewer files, easier to maintain). Assets/templates remain separate as specified.

**Known gaps (deliberate, see research report §12, §22)**
- No in-chat ZIP forensics: users extract exports locally and attach the files that matter.
- Atomic (V4) JSON is never presented as import-ready.
- No live site reads or writes; those are delegated to Elementor's own MCP in a later version.
