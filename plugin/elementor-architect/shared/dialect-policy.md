# Dialect Policy (V3 vs V4 Atomic vs Hybrid)

**verified against:** Elementor 4.0–4.4 roadmap and release notes, 2026-10-06.

Elementor now has two native dialects. Advice that ignores this produces pages that are internally inconsistent or simply will not render. Every Elementor task starts with the probe below.

## The probe (ask as ONE consolidated question if unknown)

1. **Elementor core version** and **Elementor Pro version** (or Free only).
2. **Atomic Editor (V4) enabled?** WP Admin → Elementor → Editor → Settings → Atomic Editor. On by default for new sites from 4.0 (April 2026); existing sites are unaffected until someone enables it.
3. **New build or existing site?** Brownfield sites stay on their current dialect unless the user explicitly asks to migrate.
4. **Which layout system is live?** Flexbox containers (default since 3.16) or legacy sections/columns anywhere the work will touch.
5. **Design system in use:** global colours/fonts, Theme Style, atomic Classes/Variables, and whether `theme.json` palettes matter here.
6. **Pro or Free:** dynamic tags, Theme Builder, Forms, Loops are Pro. This is the biggest capability cliff.
7. **Add-ons installed**, and any known gaps that affect the plan (see below).

If the user cannot answer: proceed, but (a) label every dialect-dependent statement **ASSUMED**, and (b) default to **V3-safe** output, because V3 structures render on V4-enabled sites while atomic structures do not render on V3-only sites.

## Choosing a dialect

| Situation | Dialect | Why |
|---|---|---|
| New site on Elementor 4.x, atomic enabled | **V4 atomic** | Purpose-built for classes/variables/components; less markup |
| Existing site, atomic enabled, work is additive | **Hybrid, boundary recorded** | Match the neighbouring sections; do not convert half a page |
| Existing site, atomic disabled | **V3** | Atomic elements cannot render there |
| Elementor < 4.0 | **V3** | No atomic elements |
| Atomic available but the need is a gap (gallery, carousel, rich inline lists, complex repeater UI) | **Hybrid with a documented exception** | See gaps below |
| Deliverable must render on an unknown version | **V3 + containers** | Lowest-risk failure mode |

## Boundary rules for hybrids (non-negotiable)

1. **Never mix dialects inside one component boundary.** A card is either fully atomic or fully V3 — not a V3 Image Box inside an atomic Flexbox with atomic Heading siblings.
2. **Record every boundary** in the exception register: what, why, scope, exit condition.
3. **Prefer section-level boundaries** (a legacy pricing section inside an otherwise atomic page is normal and fine; a legacy widget in the middle of an atomic card is not).
4. **Check the global-styling bridge:** atomic Classes/Variables and legacy Global Colours/Fonts can be synced; a hybrid page must not end up with two competing token systems. Decide which one is the source of truth.

## Known V4 gaps to check before recommending atomic (re-check each minor release)

**VERSION-DEPENDENT — verify against the target version.**

| Gap | Status as of 4.3/4.4 | Consequence |
|---|---|---|
| Galleries, carousels, sliders as atomic elements | Not available | Use the classic widget as a documented exception, or a Loop with a classic carousel |
| Rich inline text formatting / lists inside atomic text elements | More limited than V3 | Long-form or list-heavy copy may justify a V3 Text Editor inside a documented boundary |
| Custom CSS support inside the atomic system | More limited | Prefer Classes/Variables; a scoped classic Custom CSS block may be the pragmatic exception |
| Default values / default units for atomic elements | Historically thin | Document units explicitly in the plan |
| Loop / Taxonomy filtering / alternating templates | Arrived 4.2–4.3 (Pro) | Verify Pro version before planning around them |
| Per-element style saving on atomic elements, Template-widget rendering of atomic local styles | Historically buggy | Prefer Classes over local styles so templates render predictably |
| Public API for creating atomic elements | **None, and Elementor discourages outside integration** | Never generate atomic JSON as import-ready; route writes through Elementor MCP |

## Migration guidance (brownfield)

- Do **not** re-dialect an existing site as a side effect of a redesign task. Migration is its own project with its own QA.
- If a migration is requested: inventory pages by dialect and structure first, migrate section by section, keep the old dialect working until the new one is verified on staging, and expect design-system reconciliation work (Classes/Variables vs Global Colours/Fonts).
- Converting "Sections/Columns → Containers" and "widgets → atomic elements" are two different migrations. Do them separately.

## Output requirement

Every plan states the chosen dialect up front, the reason, the boundary rule if hybrid, and the dialect of every section in the build specification. A plan without a dialect decision is incomplete and must not be presented as final.
