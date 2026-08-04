---
name: hof-story-teller
description: Write Hall of Frame brand and product copy — FB Marketplace LISTING.txt, social captions, gallery blurbs, and the brand story. Use when working on Hall of Frame / Only Frame material, generating or fixing a LISTING.txt for a SKU, writing about a framed piece, or when the user invokes /hof-story-teller.
---

# Hall of Frame — Story Teller

Hall of Frame sells **framed reproductions of masterworks**. The name is the brand thesis:
a hall of fame of paintings, made ownable through the frame. The painting is famous already
— the thing being sold is the object on someone's wall.

That distinction drives every piece of copy here. Do not sell the painting's fame back to a
buyer who already knows it. Sell what it is like to own this one.

## Assumptions in force

Stated rather than hidden — correct any that are wrong and the skill adjusts cheaply.

- **Customer-facing copy is written in Thai.** English versions on request. Skill docs,
  filenames, and commit messages stay English per `CLAUDE.md`.
- The pieces are **reproductions / art prints**, not originals. See Fidelity rules.
- `Master frame/VG/` is a collection folder. Which artist or line each collection code maps
  to is **not** recorded anywhere in this repo — confirm before naming an artist from a code.

## The asset layout this copy attaches to

`scripts/rebuild.py` builds the Marketplace batch. It produces four 1080×1350 images per SKU
and reports `LISTING.txt: ⚠️ MISSING — generate it` when the copy does not exist yet. That
missing file is this skill's main output.

```
<DB>/Master frame/<COLLECTION>/<SKU>/<SKU>F.webp   framed shot   → 01-framed.jpg
<PROJ>/web/img/Gallery/<SKU>/<SKU>Img.webp         the artwork   → 02-artwork.jpg
<PROJ>/web/img/Gallery/<SKU>/<SKU>Detail.webp      close detail  → 03-detail.jpg
<PROJ>/web/img/Gallery/<SKU>/<SKU>Room.webp        in a room     → 04-room.jpg
<PROJ>/fb-marketplace/<SKU>/LISTING.txt            ← this skill
```

A red Finder tag on `fb-marketplace/<SKU>/` means **not yet posted**.

## The spine: copy follows the images

The four images are already a story in order. Copy that follows the same order gets read;
copy that wanders does not. Every format in this skill is a compression of this spine.

| # | Image | Beat | The reader's question |
|---|---|---|---|
| 1 | `01-framed` | **The object** | What am I actually buying? |
| 2 | `02-artwork` | **The work** | What is this painting, and why this one? |
| 3 | `03-detail` | **The making** | Is it any good up close? |
| 4 | `04-room` | **The living** | What does it do to my wall? |
| — | — | **The ask** | Size, price, how do I get it? |

Short formats drop beats from the middle, never from the ends. A caption with no object and
no ask is decoration.

## Workflow

1. **Gather what is real.** Collection, SKU, size, frame material and colour, mount, print
   substrate, price, stock. Read the four images if they are reachable — the detail shot in
   particular tells you what beat 3 can honestly claim.
2. **Fill the gaps or mark them.** Anything you do not have becomes `[CONFIRM: …]` in the
   draft. Never guess a dimension, a price, or a material.
3. **Pick the format.** See `references/formats.md` — `LISTING.txt`, social caption, gallery
   blurb, or brand story. Each has a template and a length budget.
4. **Write in the brand voice.** See `references/brand-voice.md` for register, the vocabulary
   to use and avoid, and how far the art-history content is allowed to go.
5. **Check.** Run the checklist at the end of `references/formats.md` before handing over.
   For a `LISTING.txt`, write it to `fb-marketplace/<SKU>/LISTING.txt` so the next
   `rebuild.py` run stops flagging it.

## Fidelity rules

Selling pressure is what makes copy lie. These are not style preferences.

1. **Never imply an original.** The piece is a reproduction. No wording that could be read as
   the artist's own hand, an authorised edition, a limited run, or a certificate — unless one
   genuinely exists and can be named.
2. **Never invent a specification.** Size, frame material, glass or acrylic, paper, ink,
   mount, weight, price, edition count. If you do not have it, write `[CONFIRM: …]`. A gap
   costs one message; a wrong dimension costs a return.
3. **Never invent provenance or art history.** No invented dates, museums, sale prices, or
   anecdotes about the painter. Ordinary well-known facts are fine; anything you would need
   to look up, you actually need to look up.
4. **No fake scarcity or fake urgency.** No "last one" or "price rising soon" unless true.
5. **Describe only what the images support.** If the detail shot does not show texture, the
   copy does not claim texture.
6. **Attribute the artwork plainly.** Name the painting and painter where known. Not naming
   them reads as concealment, and concealment is what rule 1 is guarding against.

## Related skills

- `frontend-design` — for the gallery page itself. This skill decides what is said; that one
  decides how it looks.
- `scrutinize` — a useful second pass on a batch of listings; it will ask whether the copy
  earns its length.
