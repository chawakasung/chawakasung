---
name: roche-ui
description: >-
  Roche.com front-end design system reference. Use whenever building, styling,
  or reviewing any web UI that must match the Roche brand — pages, sections,
  navs, footers, hero banners, teaser/card grids, buttons, typography. Provides
  exact color tokens, the Roche Sans/Serif type scale, button/pill styles,
  layout container + full-bleed rules, nav/footer structure, image framing,
  and hover/motion conventions distilled from the live roche.com site.
---

# Roche UI

Authoritative front-end spec for reproducing the look & feel of **roche.com**.
Apply these tokens verbatim — do not invent values.

## 1. Typography

**Families**
- `--font-sans: "Roche Sans","Helvetica Neue",Arial,sans-serif;` — default for everything.
- `--font-serif: "Roche Serif","Times New Roman",Georgia,serif;` — editorial accents only.
- Weights available: 200 (display headlines ONLY), 300 Light (body/subtitles), 400 Regular (nav, card titles, UI), 500 Medium, 700 Bold (rare).

**Rules**
- Body & subtitles: **weight 300**, never 200. 200 is reserved for large display H1/H2.
- All section body copy renders at **20px (desktop) / 18px (mobile ≤768px)**.
- Card/section titles ("sub heads"): **weight 400** Regular.
- Big display headline (page header H1): weight 200, `letter-spacing:-.02em`, `line-height:1.05–1.18`.

**Type scale** (clamp = responsive)
| Role | Size | Weight | LH |
|---|---|---|---|
| Display H1 (page header) | `clamp(36px,5cqw,62px)` | 200 (light, RocheSansLight) | 1.15 |
| Section H2 | `clamp(32px,3.4cqw,48px)` | 200 | 1.12 |
| Card/sub title | `clamp(20px,1.6cqw,24px)` | 400 | 1.2 |
| Intro / lead body | 20px (mobile 18px) | 300 | 1.6 |
| Body | **20px desktop / 18px mobile (≤768px)** | 300 | 1.6 |
| Small / meta / breadcrumb | 14–15px | 300 | 1.5 |
| Eyebrow / kicker | 15px | 300, grey-700 | — |

## 2. Color tokens

```
--roche-blue        #0B41CD   /* primary brand, links, accents, logo */
--roche-blue-900    #021A4F   /* deep blue */
--roche-dark-blue   #022366
--roche-black       #1D1D1D   /* default text */
--roche-grey-900    #1A1A1A
--roche-grey-700    #6B6B6B   /* secondary text, eyebrows, captions */
--roche-grey-300    #DBD6D1   /* warm hairlines */
warm border         #C2BAB5   /* pill & card image bottom border */
hairline / chevron  #DCD5CF   /* thin decorative lines */
divider             #C9CDD3
peach hover fill    #E5C5B0
```
Backgrounds are white `#fff`. Section/header gradients are **very pale warm**:
`linear-gradient(120deg,#FBEDE7 0%,#FDF4F0 42%,#FFFFFF 78%)`. Never use
saturated peach.

## 3. Layout & container

- **Content max-width: `1680px`**, centered (`margin:0 auto`).
- Side padding: `--pad-x: clamp(20px,6cqw,96px)`; vertical `--pad-y: clamp(48px,7cqw,96px)`.
- **Section backgrounds bleed full viewport** while content stays capped:
  on the section's first child use
  `--bleed: max(0px,(100vw - 100%)/2)` with negative margins + matching
  padding. (Use `100cqw` only inside a container-query canvas; for real
  deployed pages use `100vw`.)
- Footer inner rows also capped at 1680 centered; footer bg full-bleed.

## 4. Navigation

Two-tier, white bg, subtle bottom shadow `0 1px 0 rgba(0,0,0,.04)`,
padding `32px var(--pad-x) 24px`.
- Logo: left, the hexagon Roche mark in `--roche-blue`, rendered ~**100×52px**.
- Row gap between tiers: ~26px.
- Header box: full-bleed, **height 160px**, sticky top, z-index 300,
  `box-shadow:inset 0 -1px 0 #DBD6D1`, `-webkit-font-smoothing:antialiased`,
  transition `transform,background-color .25s cubic-bezier(.23,0,.56,.99)`.
- Nav links: **font-size 20px, font-weight 400 (RocheSans-Regular),
  line-height 32px** — applies to both rows.
- Top/utility row (right): (Stories, Careers, Contact),
  thin `1px×18px #cfcfcf` divider, then globe + search icons (~20px, stroke
  1.6–1.8, `#1d1d1d`, hover → blue).
- Primary row: `#1d1d1d` (About Roche, Solutions,
  Innovation | Investors, Media), `group-divider` 1px×20px.
- Logo rendered ~72×40px; left gutter `clamp(24px,5.4vw,96px)`.
- Link hover = blue underline that scales in from left
  (`transform:scaleX(0→1)`, `cubic-bezier(.65,.05,.36,1)`).
- ≤1023px: collapse to hamburger + slide-in drawer; hide text rows.

## 5. Buttons

- **Primary**: solid `--roche-blue` bg, white text, no/!slight radius,
  generous padding (~14px 28px), label is an action phrase
  ("Read our story", "Explore Careers").
- **Secondary/outline**: transparent bg, `1px` border, dark text, same padding;
  on dark imagery use white border + white text.
- **Tertiary/link**: inline text with a right-arrow icon; arrow translates
  `+4px` on hover, text → blue.
- **Pills/tags**: `border:1px solid #C2BAB5; border-radius:999px;
  padding:10px 22px; font 14px/300`. Hover = filled peach `#E5C5B0`,
  border same, lift `translateY(-1px)` + soft shadow
  `0 4px 14px rgba(149,99,70,.22)`.

## 6. Roche arrow icon

Right-pointing arrow used in link titles & teasers:
`<path d="M2.6 13h14.6l-5.3 5.3 1.4 1.4L21 12l-7.7-7.7-1.4 1.4 5.3 5.3H2.6v2z"/>`
(fill `currentColor`, color `--roche-blue`). Decorative page-header chevron =
thin `>` outline, stroke `#DCD5CF`, `vector-effect:non-scaling-stroke`,
anchored right edge, square aspect.

## 7. Image framing

- Hero: full-bleed background image, text overlay (light text on dark photo).
- Teaser/feature card image: `aspect-ratio:4/3` (or square ~1/1 for feature
  grid), `background-size:cover; background-position:center`.
- Card image carries a **3px bottom border `#C2BAB5`**; on card hover a
  **`--roche-blue` line sweeps left→right** over it
  (`::after{width:0→100%; transition:width .45s ease}`), and the card title
  + arrow turn blue simultaneously (hover scoped to whole card).
- Story page header: 4-image flush strip directly below the header block.

## 8. Section patterns (order seen on roche.com)

Page Header (eyebrow + display H1 + optional pills + right chevron, pale warm
gradient) → Spotlight/news + CEO quote w/ portrait → Investor stat cards (3) →
"We are Roche" mission split → 3-column mission cards (Prevent/Stop/Cure,
image+subhead+text+Read more) → "Read our stories" 3 story cards (landscape
thumb + tag + title + Read the story) → CTA band ("Shape the future…",
Explore Careers) → 4–5 column feature grid → Footer.

Footer: pale full-bleed bg, content capped 1680 centered, link columns
(Helpful links / Roche websites) + social icon row + legal row
(Privacy, Legal, Accessibility, Social Media guidelines, Cookies) +
"© F. Hoffmann-La Roche Ltd" + regional disclaimer.

## 9. Motion

Transitions ~`.2–.45s ease` / `cubic-bezier(.65,.05,.36,1)`. Effects: underline
scaleX from left, arrow translateX +4px, image blue-line sweep, pill lift.
Keep motion subtle and short.

## 10. Distribution note (Roche brand IP)

Roche fonts/logo/imagery are **internal-only**. Self-contain exported pages
(embed fonts as base64 inline — Safari blocks file:// font folders) and never
publish to public hosting.

---

When asked to build Roche UI: start from these tokens, pick the matching
section pattern from §8, keep content ≤1680 centered with full-bleed
backgrounds, and verify weight rules (§1) — the most common mistake is using
weight 200 for body text instead of 300.
