---
name: roche-illustrator
description: Create illustrations in the Roche brand style — flat, human-centered, faceless vector art for healthcare and science topics. Trigger when drawing, illustrating, or generating spot or hero illustrations, SVG figures, or decorative imagery for Roche / diagnostics / TB & IGRA content.
metadata:
  author: Roche brand illustration — derived from reference illustrations
  version: '0.1'
---

# Roche Illustrator

Produce illustrations that read unmistakably as **Roche**: flat, optimistic, human, and
built from bold blocks of a limited palette. The subject is almost always people and
healthcare/science — patients, clinicians, scientists, and the metaphors that connect them.

> ⚠️ **Provenance.** This guidance is **derived from a set of reference illustrations**, not
> from the authoritative Roche Brand Centre. The canonical rules, exact hex values, and
> asset library live at `branding.roche.com` — which is **not reachable from this
> environment** (network policy blocks `roche.com`). Treat colors and proportions here as
> close approximations to **verify against the Brand Centre** before final delivery.

---

## Two illustration modes

Roche illustration spans two related modes. Pick one per image — do not mix within a frame.

| Mode | Use for | Character |
| --- | --- | --- |
| **Flat spot** | icons-plus, editorial spots, concept metaphors, in-page figures | Bold flat color blocks, no outlines, faceless figures, one solid background, generous negative space |
| **Fluid hero** | page heroes, banners, section openers | Continuous organic silhouettes that merge and flow into one another; a "river" of negative space; more narrative, more depth |

Default to **flat spot** unless the brief calls for a wide hero/banner.

---

## Core principles

1. **Flat vector, never photoreal.** Shapes are defined by solid color fills — **no outlines
   or strokes** around figures, no drop shadows, no gradients as a rule (a single subtle
   tonal shift is the most you'd use). Fine internal linework is allowed only for detail
   (e.g. neurons, circuitry).

2. **Faces are minimal or absent.** Figures usually have **no eyes, nose, or mouth** — the
   silhouette, hair, posture, and props carry the meaning. When a feature does appear it is a
   single deliberate accent (round glasses, a mask), never a full face. This keeps figures
   universal.

3. **Diversity is the default, not the exception.** Vary skin tone across the **full range**
   (light peach → coral → deep brown → maroon), and vary age, hair, body, dress, and ability
   — hijab, white hair, a clinician with a stethoscope, a parent carrying a baby. A group
   illustration should visibly represent different people.

4. **Human + healthcare subject matter.** Patients and the people who care for them; science
   made approachable (a brain, a test tube, a puzzle). The tone is warm and forward-looking —
   in the spirit of *"Doing now what patients need next."*

5. **Limited palette per image.** Two to four hues from the palette below, **plus** skin
   tones, **plus** one solid background color. Restraint is the look — a whole illustration
   in purples + orange + cream reads as Roche; a rainbow does not.

6. **Solid single-color background.** Always one flat color drawn from the palette (lilac,
   orange, blue, blush, amber). No scenery unless the concept needs it.

7. **Confident, rounded, organic shapes.** Slightly imperfect, hand-considered curves — not
   rigid geometry, not thin fussy detail. Big readable forms; strong silhouette first.

---

## Palette

Approximate, **observed from references** — verify against the Brand Centre, and prefer RDS
color primitives where an exact match exists (see
[`rds-core-developer` → SKILL-colors.md](../rds-core-developer/SKILL-colors.md), hue groups
`blue`, `purple`, `red`, `orange`, `yellow`, `brand`).

| Role | Approx. hex | Notes |
| --- | --- | --- |
| Roche blue (bright) | `#1F6FE8` | hero backgrounds, science |
| Roche navy | `#12235E` | fluid-hero base, hair, depth |
| Violet / purple (bright) | `#A22BF0` | signature accent, frames, garments |
| Purple (deep) | `#6A1F9C` | shadows within purple areas |
| Orange | `#E4551E` | backgrounds, garments, energy |
| Amber / marigold | `#F6A623` | warm skin-adjacent, garments |
| Magenta / red-orange | `#D8352A` | small accents |
| Red (spark) | `#E4002B` | tiny accents only — glasses, a heart |
| Cream / blush | `#FBE7D2` | soft backgrounds, coats |
| Skin tones | peach `#F4C9A0` · coral `#E88A5A` · brown `#9C4A2A` · deep `#5E241A` | span the full range |

Rules of thumb: one background hue; one or two "garment/shape" hues; skin tones; sparse red
only as a spark. Keep foreground text/marks at **`high-contrast`** if the illustration sits
inside an RDS layout.

### Tonal & monochrome treatments

Two treatments are used within the palette rules:

- **Multi-hue** (most common) — background + two-to-four accent hues + skin.
- **Tonal monochrome** — the whole scene built from **tints and shades of one hue** (e.g. a
  full blue frame from pale sky-blue through to navy), with **skin tone as the only warm
  accent**. Use for quieter, reflective subjects (memory, aging, focus). Even here, shading is
  **stepped flat blocks**, not gradients.

A single subtle tonal step *within* a shape (a slightly darker fold of a garment, a lighter
plane of a drop) is allowed in both treatments; smooth gradients are not.

---

## Reference illustrations (observed)

The five references this skill is built from — described so the style is reproducible even
though the source files are not bundled here:

1. **Portrait wall.** Lilac background; a person points (with a child at their side) at a grid
   of framed portraits. Faceless figures, warm peach skin, purple frames with one orange
   frame; red round glasses and a red pointer as the only sharp accents. *Concept: selection /
   identifying the right match.*
2. **Five diverse women.** Amber background; five women stand together — one with a
   stethoscope, one in a hijab, one carrying a baby, one with white hair. Orange, magenta,
   deep maroon, cream. Faceless. *Concept: community, inclusive care.*
3. **Puzzle.** Orange background; two deep-brown hands assemble a purple jigsaw — a
   person-shaped gap and one piece bearing a small broken heart. *Concept: missing piece /
   solving a human problem.* Metaphor-driven, no faces at all.
4. **Fluid clinician hero.** Blue background; a small figure reaches up toward a large flowing
   scene of clinicians (masked, lab coat, test tube, stethoscope, a red medical cross) that
   melts into one continuous shape. Navy-led with purple + orange. *This is the fluid-hero
   mode.*
5. **Brain under magnifier.** Blush background; a scientist (navy bun, white coat, blue
   glasses) holds a purple magnifier over a stylized deep-blue brain drawn as a neuron
   network in fine light-blue lines. *Concept: research / discovery.* Flat blocks + fine
   internal linework.
6. **Blood drop in a hand.** Deep-purple background; a cupped hand (blue sleeve) holds a blue
   teardrop that contains a scene — a parent in orange walking with a child and a football
   under a bright sky. *Concept: a single drop of blood protects an ordinary life* —
   **directly on-topic for IGRA blood testing.** A scene-within-a-shape is a recurring device.
7. **DNA staircases.** Blush background; scientists in white coats and blue gloves climb DNA
   double-helices drawn as staircases (red, purple, red). Faceless. *Concept: genomics /
   research as a climb.*
8. **Scientist with a flashlight.** Amber/orange background; a scientist in a white coat over
   a violet outfit sweeps a large flashlight beam across cracked, faceted terrain, casting long
   shadows. *Concept: illuminating the unknown.* Faceted "landscape" background shapes.
9. **Elderly person + photo frames (monochrome).** Blue background rendered entirely in
   **tints and shades of blue**; a white-haired person looks up at framed photos of family and
   a pet — skin tone the only warm note. *Concept: memory / a life remembered.* The reference
   for the **tonal monochrome** treatment.

If you want these bundled as pinned examples, drop the PNGs into
`.agents/skills/roche-illustrator/references/` and reference them here.

---

## Producing an illustration (SVG for Artifacts)

When the output is an Artifact or inline figure, hand-author **inline SVG**:

- Flat `fill` only; **no `stroke`** on figure shapes (reserve thin strokes for detail like
  neurons). No filters, no gradients by default.
- One `<rect>` background in a palette color spanning the viewBox.
- Build each figure from a few `<path>`/`<ellipse>` shapes; omit facial features.
- Keep the palette to a handful of `fill` values; name them as CSS custom properties so a
  reviewer can retune to exact Brand Centre hex in one place.
- Make it theme-aware only where it sits in UI chrome; the illustration's own palette is
  intentional and usually **constant** (like an RDS primitive), so don't auto-swap its fills
  for dark mode — put it on a surface that suits it instead.
- Respect the same responsiveness rules as the rest of the page: `max-width: 100%`, scalable
  `viewBox`, wide art scrolls inside its own container.

> Loading the built-in `artifact-diagramming` skill is worthwhile for the inline-SVG
> mechanics; this skill governs the *look*, that one governs the *plumbing*.

---

## Do / Don't

✅ Flat blocks, faceless figures, 2–4 hues + skin + one background, diverse people, a clear
human/health concept.

❌ Photoreal or 3D renders · outlined/"sticker" figures · detailed faces · drop shadows and
glossy gradients · a full-rainbow palette · stocky generic clip-art poses · scenery clutter ·
homogeneous (single-skin-tone) groups.

---

## Decision rules

| Scenario | Do |
| --- | --- |
| In-page concept figure, icon-plus | **Flat spot** mode |
| Page hero / wide banner | **Fluid hero** mode |
| Need an exact brand color | Pull from RDS `blue`/`purple`/`orange`/`red` primitives; verify vs Brand Centre |
| Illustration inside an RDS layout | Solid palette background; text marks at `high-contrast`; spacing via `rds-spacing()` |
| Depicting people | Faceless, varied skin/age/ability; never a single-tone group |
| Output is an Artifact | Inline flat-fill SVG; palette as CSS variables; no strokes on figures |
| Tempted by gradients/shadows/3D | ❌ Don't — stay flat |
| Asked for exact Roche assets | Hand over `branding.roche.com` — assets can't be fetched here |
