---
name: roche-illustrator
description: Create and compose artwork in the Roche brand style — flat vector illustration, brand palette, Roche Sans typography, and the official illustration/character libraries. Trigger when drawing or generating illustrations, SVG figures, infographics, social/presentation layouts, or any Roche-branded visual for diagnostics / TB & IGRA content, and when working with Roche .ai asset files.
metadata:
  author: derived from official Roche assets supplied in-session
  version: '0.2'
---

# Roche Illustrator

Produce artwork that reads unmistakably as **Roche**: flat, optimistic, human, built from
bold blocks of a limited palette. Subjects are people and healthcare/science — patients,
clinicians, scientists, and the metaphors that connect them.

> **Provenance & limits.** Everything below is derived from **official Roche assets supplied
> by the user in-session** (the Brand Centre illustration library export, five `.ai` asset
> files, Roche Sans, and the logo) plus a set of reference illustrations. The canonical rules
> live at `branding.roche.com` and `diagnostics.roche.com`, both of which are **hard-blocked
> in this environment** — the proxy answers `403 to CONNECT`, for `curl` and headless Chrome
> alike. Do not claim to have read those sites. Ask the user to supply or export anything
> that must come from them.

---

## Do not commit brand assets

Roche Sans, the logo files, and the `.ai` libraries are **licensed brand assets**. Use them
to produce work; **never commit them to this repository** and never redistribute them. This
skill therefore stores *knowledge and scripts*, not the assets themselves. When a task needs
them, ask the user to re-supply them for that session.

---

## Working with `.ai` files (verified pipeline)

Modern `.ai` files are **PDF-compatible** (`%PDF-1.6` header), so they are fully readable
here even though Illustrator is not installed and this is a Linux container.

```bash
pip3 install pymupdf fonttools     # pypi is reachable; poppler/inkscape/gs are NOT installed
```

| Need | How |
| --- | --- |
| Open an `.ai` | `pymupdf.open("file.ai")` — each **artboard is a page** |
| See the artwork | `page.get_pixmap(matrix=Matrix(1.4,1.4)).save("out.png")`, then Read the PNG |
| Survey a big library | Count `len(page.get_drawings())` per page; pages with >25 shapes hold real art. Build a contact sheet with `new_page()` + `show_pdf_page()` |
| Extract a figure as vector | Tighten `page.set_cropbox()` to the drawings' bbox, then `page.get_svg_image()` |
| Real brand hex values | Walk `page.get_drawings()`, read each `fill`, weight by bbox area |
| Type as outlines | `fontTools` `SVGPathPen` over the glyph set — see `scripts/` |

**Two gotchas when embedding extracted SVG:**
1. `get_svg_image()` emits `clip_1`, `clip_2`… — **namespace the ids per figure** or multiple
   figures on one canvas will clip each other.
2. It also emits `inkscape:` attributes with no namespace declared — **strip them**, or the
   result is not well-formed XML.

**Always render and look at your own output before delivering.** Chromium is preinstalled
(`/opt/pw-browsers`, Playwright at `/opt/node22/lib/node_modules`) for HTML; for SVG use
`pymupdf.open(svg).convert_to_pdf()` → pixmap. Composing SVG blind produces broken
proportions — this was the single biggest source of error in practice.

---

## Palette — extracted from the official `.ai` vectors

Measured by painted area across the five asset libraries. These are **actual values from
Roche artwork**, not estimates.

| Role | Hex | Notes |
| --- | --- | --- |
| Roche blue | `#0B41CD` | the core brand blue; matches RDS primitive `600-roche-blue` |
| Navy | `#022366` / `#00246A` | depth, hair, ground, text |
| Bright blue | `#1482FA` / `#0084FC` | accents, secondary figures |
| Deep blue | `#0042D5` | garments |
| Sky | `#BDE3FF` | large calm fields, backgrounds |
| Violet | `#BC36F0` | signature accent |
| Deep purple | `#7D0096` | shadow within purple |
| Lilac | `#F0D2FB` | soft backgrounds |
| Orange | `#FF7D29` / `#FF7300` | energy, garments |
| Red-orange | `#ED4A0D` | accents |
| Rust / maroon | `#B22B0D` | deep warm shadow |
| Amber | `#FFBD69` | warm garments, backgrounds |
| Blush | `#FAD6C7` / `#FCD4C4` | the most-used background of all |
| Cream | `#FFF7F5` / `#FFE8DE` | coats, light surfaces |
| Skin tones | `#FFC7B1`, `#FAC9B5`, `#97533D` + browns | span the full range |

**Backgrounds are almost always a single flat field** — blush `#FAD6C7` and sky `#BDE3FF` by
a wide margin, then amber, orange, lilac, navy. Pick one and commit to it.

For UI work, prefer RDS semantic tokens over these literals — see
[`rds-core-developer`](../rds-core-developer/SKILL-colors.md). Use a raw hex only when the
color must not shift between themes.

---

## Typography — Roche Sans

Roche Sans ships in Light / Regular / Medium / Bold (+ Condensed and italics). Applied
hierarchy that matches Roche's own layouts:

| Role | Weight | Notes |
| --- | --- | --- |
| Headline | **Light** at large size | the signature look — big and light, never heavy |
| Emphasis inside a headline | **Bold**, same size | e.g. light "helps prevent " + bold "Office Syndrome!" |
| Eyebrow / kicker | **Medium**, small, uppercase, generous letter-spacing (~3–4 units), in Roche blue | sits directly under the headline |
| Card / section titles | **Bold**, small caps-ish scale | pair with a large bright-blue number |
| Body | **Light** | muted navy-grey, not pure black |

- Headline sits on a **strong left margin aligned with the logo block**, with the eyebrow
  hanging below it on the same axis.
- Never use system fonts as a substitute. If Roche Sans is unavailable, say so.
- **Convert type to outlines** when delivering SVG so the file renders anywhere without the
  licensed font — `fontTools` + `SVGPathPen` (see `scripts/`).
- In code/UI contexts use the RDS type scale instead
  ([`SKILL-typography.md`](../rds-core-developer/SKILL-typography.md)): `ui-*` for interfaces,
  `article-*` for editorial, never manual `font-size`.

---

## The official illustration library

The Brand Centre illustration library holds **~95 assets**, landscape format, each on one
flat background color. Observed coverage:

- **People scenes** — teams, consultations, clinicians with patients, community groups
- **Anatomical / scientific** — eye, brain, DNA helix, neurons, red blood cells, vasculature
- **Concept metaphors** — jigsaw with a missing person-shaped piece, a heart-shaped trail
  through mountains, a solar system of care, a blood drop containing a life
- **Abstract organic** — stacked balancing forms, flowing silhouettes

Character libraries (e.g. *Character Customisation*) hold **one character across ~25
artboards** in different poses and outfits — standing, pointing, arms raised, running,
seated at a desk, seated with a mug, on a bike, on a sofa — plus separate artboards of props
and scenery. **Prefer reusing these official characters over drawing new figures**: they are
on-brand by construction and far better drawn than anything hand-authored here.

---

## Core principles

1. **Flat vector, never photoreal.** Solid fills; no drop shadows, no gradients (one stepped
   tonal shift within a shape is the limit). Thin internal linework only for detail —
   neurons, garment folds, pocket seams.

2. **Faces vary by asset family — do not over-apply "faceless".** Editorial/metaphor
   illustrations are often **faceless**: silhouette, hair, posture and props carry the
   meaning. But the **character libraries and many people scenes do have features** — nose,
   beard, brows, sometimes a smile. Match whichever family the piece belongs to; do not mix
   faceless and featured figures in one composition.

3. **Diversity is the default.** Vary skin tone across the full range, plus age, hair, body,
   dress and ability — hijab, white hair, wheelchair users, a parent carrying a baby. Roche's
   own libraries include wheelchair users and elders as first-class poses. A homogeneous
   group is off-brand.

4. **Limited palette per image.** One background + two to four hues + skin tones. Restraint
   is the look.

5. **Confident rounded organic shapes.** Big readable forms; strong silhouette first.

### Two illustration modes

| Mode | Use for | Character |
| --- | --- | --- |
| **Flat spot** | editorial spots, concept metaphors, in-page figures | Bold flat blocks, one solid background, generous negative space |
| **Fluid hero** | heroes, banners, section openers | Continuous organic silhouettes merging into one another; a "river" of negative space |

### Two color treatments

- **Multi-hue** (most common) — background + two-to-four accents + skin.
- **Tonal monochrome** — the whole scene in tints/shades of one hue, skin the only warm
  accent. For quieter subjects: memory, aging, focus. Shading stays **stepped flat blocks**.

---

## Layout patterns

- **Logo top-left**, generous clear space; headline block starts on a strong left margin to
  its right and shares that axis with the eyebrow.
- **Card grids** (e.g. 3×2) with rounded corners (~20px radius), a pale panel fill
  (`#F4F9FF`-ish), a thin cool-grey-blue border, and a **figure at the left of each card**
  with the text block to its right.
- **Geometric hexagon outlines** in a pale tint are an accepted decorative motif in the
  corners — derived from the logo's hexagonal mark, but **never the logo itself**.
- Footer: a hairline rule, social marks in solid navy circles, brandline right-aligned.
- Keep the illustration's own palette constant rather than theme-swapping it; place it on a
  surface that suits it.

---

## Do / Don't

✅ Reuse official characters and library assets · flat blocks · one background color · 2–4
hues + skin · diverse people · Roche Sans Light headline with Bold emphasis · type outlined
on delivery · render and inspect before shipping.

❌ Photoreal/3D · outlined "sticker" figures · drop shadows and glossy gradients ·
rainbow palettes · system fonts standing in for Roche Sans · homogeneous groups · **recreating
the Roche logo by hand** (always place the supplied vector) · committing brand assets to git ·
claiming to have read a blocked Roche site.

---

## Decision rules

| Scenario | Do |
| --- | --- |
| Need a figure | Extract from the official character `.ai` library first |
| Need an exact brand color | Use the extracted table above, or an RDS primitive |
| Need a headline | Roche Sans **Light**, large; Bold only for the emphasised phrase |
| Delivering to a designer | One SVG, named layers, type as outlines — opens in Illustrator |
| Delivering to code/UI | RDS tokens and utility classes, not literal hex/px |
| Asked for exact Brand Centre rules | Say the site is blocked; ask for an export |
| Tempted to ship SVG unseen | Render it first — always |
