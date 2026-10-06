# Quality Report Template (Performance · SEO · Accessibility)

> Copy into the deliverable. Delete guidance lines. Every finding needs a decision.

## Scope

| | |
|---|---|
| Reviewed | URL / artifact / screenshots |
| Stage | pre-launch / live |
| Stack | Elementor __ · Pro __ · caching/CDN __ · SEO plugin __ |
| Must not change | *(sites mid-launch or mid-campaign)* |
| Client context | industry · compliance obligations · traffic priorities |

## Evidence base

| Item | Provided | Impact on conclusions |
|---|---|---|
| URL | | |
| Lighthouse/PSI export | | |
| HTML / artifacts | | |
| Elementor optimisations active | | |
| Field data available | | |

## Findings register

| ID | Area | Finding | Evidence | Impact hypothesis | Effort | Risk of change | **Decision** | Confidence |
|---|---|---|---|---|---|---|---|---|
| Q1 | Performance | | | | S/M/L | low/med/high | flag / recommend / prepare for approval / defer / do not touch | |

## Top actions (max ~5)

| # | Action | Why now | Expected effect | Risk | Owner |
|---|---|---|---|---|---|

## Deferral list

| Item | Why deferred | Trigger that reopens it |
|---|---|---|

## Do-not-touch list

| Item | Why |
|---|---|
| SEO plugin settings | Owned by the SEO stack; changes need a decision, not a default |
| Cache / CDN / minification | Fights the hosting layer |
| Security configuration | Outside this review's mandate |

## Areas reviewed

### Performance
- Optimisations already active: *(list)*
- Assets / DOM / JS / fonts / third-party: *(notes)*
- LCP element: *(identified? how?)*
- Hypotheses: *(clearly marked as hypotheses)*

### SEO (structure)
- Headings and semantics · slugs and URLs · indexability · redirects · schema ownership · internal linking · duplicate-content risk

### Accessibility
- Keyboard · focus · contrast · headings · landmarks · forms · alt text · targets · motion · carousel/dialog behaviour
- Escalation applied: yes/no *(compliance-bound clients → blockers)*

## Measurement plan

| Question | Method | Where | Owner |
|---|---|---|---|

## What this review cannot establish

- Measured field CWV (requires real-user data)
- Screen-reader experience (requires assistive-technology testing)
- Conformance to WCAG (requires a full audit against success criteria)
- Rendering on real devices

## Confidence ledger

| Claim | Label |
|---|---|
