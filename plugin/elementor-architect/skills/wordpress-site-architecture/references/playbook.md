# Playbook — WordPress Site Architecture

## 1. Content-model decision rules

| Situation | Decision | Why |
|---|---|---|
| Unique, hand-authored, few, individually designed | **Page** | No reuse or querying need |
| Many structurally identical items, individually URL-worthy, same editor | **Custom Post Type** | Archives, loops, single templates, scalable editing |
| Items exist to group/label other items | **Taxonomy** | Correct URLs, filters, archives; avoids fake CPTs |
| Global values reused site-wide (contact details, social, footer copy) | **Options page** | Single source of truth |
| Items authored by end users | **CPT + roles/capabilities review** | Permissions and moderation |
| Hierarchical editorial content (docs, chapters) | **Page hierarchy or CPT with hierarchy** | Depends on whether a template or a writer owns it |

Signs you have it wrong: a CPT with a handful of hand-designed entries; a page duplicating another page's structure 40 times; a taxonomy that should be a CPT; fields holding design decisions.

## 2. Template hierarchy mapping (fill per site)

| Surface | WordPress surface | Elementor template type | Conditions |
|---|---|---|---|
| Site header/footer | every page | header / footer | general, with exclusions (canvas, popups) |
| Blog single | `single` | single | `include/singular/post` |
| CPT single | `single-{cpt}` | single | `include/singular/{cpt}` |
| Category/tag/taxonomy archive | `taxonomy-*.php` | archive | `include/archive/taxonomy/...` |
| CPT archive | `archive-{cpt}` | archive | `include/archive/{cpt}` |
| Search | `search.php` | search results | `include/archive/search` |
| 404 | `404.php` | error 404 | `include/singular/not_found` |
| Shop / product (Woo) | Woo templates | single/archive (Woo widgets) | Woo-specific conditions |
| Popups | — | popup | conditions + triggers, with exclusions |

Condition IDs and labels are **VERSION-DEPENDENT** — verify against the site's Elementor Pro version.

## 3. Conditions matrix discipline

1. One template per surface unless there is a real reason; extra templates increase conflict risk.
2. Always write **exclusions**. Typical: header excludes popups and blank-canvas landing pages; single templates exclude the CPTs that have their own template.
3. Order by specificity: general → post type → taxonomy/term → specific post. The most specific matching template wins.
4. Never leave a template with no conditions "just in case" — it will fight another template.
5. Record priority values if adjusted, and why.
6. After changing conditions, verify the affected URLs on staging, not just the template preview.

## 4. Loop strategy

| Need | Approach | Notes |
|---|---|---|
| Blog/CPT listings on an archive | Archive template + loop with the main query | Best for SEO and simplicity |
| Curated listing on a page (selected posts) | Pro Loop Grid / Posts widget with a query | Keep the query explainable |
| Related content | Loop with taxonomy/relationship query | Beware query cost |
| Repeating content within one post (ACF repeater) | CPT + loop (preferred) or a documented third-party/custom tag | Repeaters cannot be natively rendered |
| Products | Woo widgets/loops | Watch performance and cache implications |
| Filtering | Taxonomy filters (4.3+ Pro for atomic loops) | Verify version; plan for SEO of filtered URLs |

Pagination, empty states and "no results" messaging are part of the plan, not an afterthought.

## 5. Design-token ownership

Decide one primary source and write it down:

| Option | Choose when | Watch out for |
|---|---|---|
| Elementor Kit globals + Theme Style | V3 sites, single-builder sites | `theme.json` palettes may also surface — decide who wins |
| Atomic Classes + Variables | V4 sites | 1000-class cap; classes are site-local; sync with legacy globals if hybrid |
| theme.json as source, Kit synced | Block-theme + Elementor mixes | Double-styling if both apply; regeneration needed after changes |

Rule: one source of truth, documented, and never two competing systems on the same surface.

## 6. Code placement

| Code type | Home |
|---|---|
| Presentation (templates, styles) | Child theme |
| CPTs, taxonomies, ACF field registration, custom widgets, dynamic tags | Small site plugin |
| Hardening, environment rules | mu-plugin |
| One-off visual tweaks | A named class in the child theme's stylesheet |
| Never | Parent theme; page-level Custom CSS for structural things; theme files edited in place |

## 7. Migration and redirect checklist

1. URL inventory of the current site (from sitemaps, analytics, server logs — not guesswork).
2. Redirect map for every changed URL (301), including paginated and taxonomy URLs.
3. Slug architecture decided *before* build, not after.
4. Staging → production sequence with a freeze window.
5. Cache, CDN and object-cache invalidation.
6. Regenerate Elementor CSS after the switch.
7. Post-launch checks: 404s, redirects, canonical tags, XML sitemap, analytics continuity, form submissions, search.
8. Rollback path documented and tested once.

## 8. Architecture anti-patterns

| Anti-pattern | Consequence | Fix |
|---|---|---|
| Everything is a Page | No reuse, no dynamic content, 200-page maintenance tax | CPT + archive + loop, or ACF modules |
| CPT used as a taxonomy | Broken semantics, confusing URLs | Terms |
| Site-wide Theme Builder conditions | Templates fight; unpredictable output | Explicit includes + exclusions |
| Two token systems | Visual drift | One source of truth |
| Dependency on an unmaintained add-on | Silent future breakage | Exit condition + fallback |
| Elementor used for article bodies | Writers blocked; rigid structure | Template frame + post content |
| No empty states | Broken-looking pages when data is missing | Fallbacks per field |
| Copy > paste as the reuse strategy | N× maintenance | Components / loops / template parts |
