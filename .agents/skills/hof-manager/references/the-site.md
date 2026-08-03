# Hall of Frame — what the site actually is

Facts confirmed by the site owner, 2026-08-03. Read this before proposing
anything, because most generic gallery advice does not survive contact with
these constraints. If a fact here turns out to be stale, correct this file in
the same change that acts on the correction — a stale fact here silently
poisons every future round.

## The business

`hallofframe.gallery` sells **framed canvas prints of public-domain classical
art** — Van Gogh, Monet, and the like. Every item is a product with a SKU, a
price, a size, and a frame. There are no user-submitted works and no creator
accounts: "artist" means the original painter, who is long dead and is not
going to promote anything.

Two consequences that shape all engagement work here:

1. **The image is not the differentiator.** Anyone can print the same
   public-domain scan. What is being sold is the framing, the sizing, how it
   looks on a wall, and the trust that it arrives as pictured. Engagement work
   that only surfaces the artwork competes with every free image of the same
   painting; work that surfaces *frame, scale, room, and trust* does not.
2. **Search demand is artist-name shaped.** People search "Van Gogh Starry
   Night canvas" far more than they search the shop's name. That demand
   already exists and is specific — which makes per-artist and per-artwork
   pages the highest-leverage indexable surface the site can have.

## The stack

- `web/` — static, vanilla. No framework, no build step, no server rendering.
- `web/app.js` — renders product cards **client-side, directly from the CSV**.
- `web/data/products.csv` — the source of truth for the whole site, ~254 KB,
  keyed by `sku`, 19 columns:

  ```
  sku, title_th, title_en, artist, year, movement, story_th, story_en,
  size_in, size_cm, frame, price, collection, room_fit, mood_tag,
  image_url, status, framed_image, gallery_folder
  ```

- `web/img/Gallery/<SKU>/` — `<SKU>Img.webp`, `<SKU>Detail.webp`,
  `<SKU>Room.webp`.
- `~/Desktop/Hall of Frame DB/**/<SKU>/<SKU>F.webp` — the dark-studio framed
  shot, kept outside the project.
- **There is no per-SKU HTML build.** Nothing renders a product to its own
  static page.

That last line is the structural fact to keep in mind. A client-rendered
catalogue with no per-SKU URL cannot be indexed, cannot be shared with a
preview, and cannot be linked from a Marketplace post — which means the site
is currently invisible to the exact artist-name demand described above. Treat
per-SKU pages as the default first candidate in any ranking, and check it
before assuming it: read `index.html` and `app.js` and confirm how a product
is addressed today.

## The local scripts

Content operations already exist and are already automated. Fit into them
rather than proposing a parallel system:

- `.claude/skills/hall-of-frame/rebuild.py <SKU>…` — treats `fb-marketplace/`
  as a **posting queue**: deletes everything not in the SKU list, then builds
  four 1080×1350 JPEGs per SKU (`01-framed`, `02-artwork`, `03-detail`,
  `04-room`), preserves any existing `LISTING.txt`, and red-tags each folder
  in Finder. It validates sources first and aborts before touching anything if
  a SKU is missing an image — keep that property in any change to it.
- `add-artwork.py`, `make-*.py` — the intake and asset-generation side.

The CSV is what everything reads from, so a column added there propagates to
the site, the listings, and the scripts at once. That makes the CSV schema the
cheapest place to add anything the site needs to say about a product, and the
most expensive place to be careless.

## Where the files live

The project is **local-only** on the owner's M1 Mac at
`/Users/m1macbookpro/Desktop/peojects/CK/Only Frame/Ai`, with an empty
`git remote -v`. An agent running anywhere else — a remote container, a web
session — cannot read any of it.

So when working from outside that machine: do not describe or edit these files
from memory of this document. Ask for the specific file, or for the project to
be pushed to a remote. This document records the shape of the project, not its
current contents; the difference matters the moment you write a patch.

## Channels in use

The website, Instagram and Facebook, and **Facebook Marketplace** — where
listings are posted by hand from the kits `rebuild.py` produces. Marketplace
is a real acquisition channel here, not an afterthought, and it is the one
place where the four-image sequence has already been standardised. Any
proposal that ignores it is ignoring the channel currently doing the work.
