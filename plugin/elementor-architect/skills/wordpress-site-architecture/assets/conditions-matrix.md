# Theme Builder Conditions Matrix

> Copy into deliverables. Condition IDs and labels are **VERSION-DEPENDENT** — verify against the site's Elementor Pro version. Specificity rule: the most specific matching template wins.

## Template inventory

| Template | Type | Purpose | Priority |
|---|---|---|---|
| Global header | header | site-wide navigation | 10 |
| Global footer | footer | site-wide footer | 10 |
| Blog single | single | standard posts | 20 |
| *(add rows)* | | | |

## Conditions matrix

| Template | Include conditions | Exclude conditions | Priority | Notes |
|---|---|---|---|---|
| Global header | `include/general` | popups; blank-canvas landing pages | 10 | sticky desktop only |
| Blog single | `include/singular/post` | CPTs with their own single template | 20 | ACF hero group + post content |
| CPT single | `include/singular/{cpt}` | — | 20 | overrides blog single by specificity |
| Taxonomy archive | `include/archive/taxonomy/{tax}` | terms with dedicated templates | 30 | filters per 4.3+ Pro |
| *(add rows)* | | | | |

## Conflict resolution rules (write these down and keep them)

1. Specific beats general: post type > taxonomy/term > singular > general.
2. Every general template must carry exclusions for the surfaces handled by more specific templates.
3. No template ships without conditions.
4. Priority values only change for a stated reason.
5. After any condition change, verify the affected URLs on staging (not just the template preview).

## Popup conditions (if used)

| Popup | Include | Exclude | Triggers | Notes |
|---|---|---|---|---|
| Newsletter | posts + pages | checkout, thank-you pages | exit intent / scroll % | respects consent tooling |

## Loop / query plan

| Loop | Source | Query | Pagination | Empty state | Version notes |
|---|---|---|---|---|---|
| Blog listing | posts | main query | numeric | message + CTA | — |
| Related posts | posts | taxonomy match | none | hide section | — |

## Verification checklist after condition changes

- [ ] Each URL renders exactly one template per surface
- [ ] Exclusions verified (canvas templates, popups, Woo pages)
- [ ] Search, 404 and pagination surfaces checked
- [ ] Mobile header/footer rendering checked
- [ ] CSS regenerated; caches cleared
- [ ] Accessibility of the header/footer nav re-checked (focus, target sizes)
