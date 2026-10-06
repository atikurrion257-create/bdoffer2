---
name: wordpress-site-architecture
description: >
  Plan the WordPress layer of an Elementor build: content model decisions (pages versus
  custom post types versus taxonomies), theme and child-theme strategy, Theme Builder parts
  with an explicit display-conditions matrix (include, exclude, priority), template hierarchy
  mapping, loop strategy, design-token ownership, code placement, plugin-stack risk,
  performance/SEO/accessibility by design, and migration plus redirect planning for redesigns.
  Use for site-level architecture questions, redesign planning, Theme Builder structure,
  "where should this content live?", template planning, or multi-page migration questions.
  Do NOT use for field-level ACF or dynamic-content design (use acf-dynamic-content-plan),
  for auditing an existing artifact (use elementor-structure-audit), or for page-level layout
  planning (use design-to-elementor-plan).
---

# WordPress Site Architecture

Site-level decisions outlive pages. Get these wrong and every page pays for it.

## When to use

- "Plan the WordPress architecture."
- "Redesign plan for an existing site."
- "Where should this content live — page, CPT, or taxonomy?"
- "How many templates do I need / what conditions?"
- Migration, redirect, or template-hierarchy questions.

## When NOT to use

Field design and dynamic content (→ `acf-dynamic-content-plan`); artifact auditing; page-level blueprinting.

## Inputs

- A content inventory or description (page list, content types, rough volumes).
- Existing site facts where relevant: theme, plugins, Elementor/Pro versions, dialect, SEO plugin, hosting/caching.
- Constraints: WooCommerce, memberships, multi-language, multi-author, regulated content, legacy data.
- Editorial roles: who edits what, and how technical they are.

## Workflow

1. **Content inventory and classification.** For each content type decide: unique hand-authored page / repeatable collection (CPT) / classification (taxonomy) / global content (options) / user-generated. Write the rationale — never "just because".
2. **URL and template-hierarchy mapping.** For every type: single, archive, taxonomy, search, 404, pagination. Where does it live, what is its slug structure, what owns its title/meta?
3. **Theme Builder plan.** Parts inventory (header, footer, single, archive, search results, 404, popup, loop items) with an explicit matrix: include conditions, **exclude conditions**, priority, and conflict-resolution rule.
4. **Loop strategy.** Atomic Loop vs Pro Loop Grid/Carousel vs archive templates: query source, pagination, empty state, filters, alternating templates. Mark version-dependent features.
5. **Reuse strategy.** V4 Components vs global widgets vs template parts: what is reused, and what stays editable per instance (Component properties).
6. **Design-token ownership.** One primary source of truth (Kit globals / atomic Classes+Variables / theme.json synced). State who edits what and how drift is prevented.
7. **Code placement.** Child theme vs small site plugin vs mu-plugin. No structural customisation in a parent theme or page-level Custom CSS.
8. **Plugin stack.** Required / optional / forbidden; each dependency with a purpose, a risk note and an exit condition.
9. **Performance, SEO and accessibility by design.** DOM and widget budgets; image/font conventions; slug and redirect architecture; schema ownership; heading/landmark strategy; contrast and focus requirements.
10. **Migration and rollback.** Staging → production sequence, redirect map, cache/CDN invalidation, rollback path, and what must be frozen during the switch.
11. **Output** the architecture map, conditions matrix and risk register.

## Output contract

1. Content-model decisions with rationale (and the rejected alternatives).
2. Template hierarchy table.
3. Theme Builder conditions matrix (include / exclude / priority).
4. Loop plan.
5. Token ownership decision.
6. Code placement.
7. Plugin stack with risks and exit conditions.
8. Budgets (DOM, assets, fonts).
9. Migration/redirect/rollback plan.
10. Risks and decisions requiring client approval.
11. Confidence ledger.

## Hard rules

- **Avoid CPT proliferation.** If a "CPT" only groups items, it is a taxonomy. If a page is unique and hand-authored, it is a page.
- **Conditions must include exclusions.** "Site-wide" is a bug waiting to happen. State the specificity rule and the priority.
- **Never propose architecture that depends on a plugin the client will not maintain** — or, if you must, say so loudly with an exit condition.
- **Never change SEO configuration.** Recommend, and defer to whoever owns the SEO stack.
- **Mark version-specific features** (Loops, taxonomy filtering, alternating templates, condition UIs) as VERSION-DEPENDENT.
- **Do not design pages here.** This skill decides structure; page layout belongs to `design-to-elementor-plan`.
- **Long-form content is not a builder problem.** Templates frame pages; post content owns article bodies.

## References

- `references/playbook.md` — content-model rules, conditions matrix guidance, token ownership, migration/redirect checklist, anti-patterns.
- `references/verification-taxonomy.md`, `references/dialect-policy.md`, `references/house-standard.md`.
- `assets/conditions-matrix.md` — the matrix format (copy into deliverables).

## Hand-offs

- Field-level design → `acf-dynamic-content-plan`.
- Page structure → `design-to-elementor-plan`.
- Verification → `elementor-qa-gate`.
- Quality review of the plan's implications → `site-quality-review`.

## Failure handling

- **No content inventory** → ask for a page list plus a sample item of each type; otherwise deliver a *provisional* model clearly labelled provisional.
- **Unknown existing stack** → state assumptions; list what must be confirmed before build.
- **Client wants to "keep everything as pages"** → quantify the maintenance cost and offer the smallest viable model change.
- **Migration with unknown URLs** → produce the redirect framework and require the URL inventory before launch.
