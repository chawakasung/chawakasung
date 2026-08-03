# Channels

Read this when the work moves past the site itself to how people find it and
come back. On-site fixes raise the value of every visitor; channel work raises
the number of them. Both are needed, but they fail differently: on-site
problems are visible to anyone who looks, while channel problems are invisible
until you go looking for traffic that never arrived.

Order channels by what the shop already has. Facebook Marketplace is already
running with a standardised four-image kit; search is wide open and currently
unreachable. Those two, in that order of certainty, before anything new.

## Facebook Marketplace

The channel already doing work. `rebuild.py` turns `fb-marketplace/` into a
posting queue and builds `01-framed`, `02-artwork`, `03-detail`, `04-room` at
1080×1350 per SKU, then red-tags each folder in Finder so the remaining manual
step is visible.

Where engagement leaks here:

- **Image order is the pitch.** Framed first (what you get), then the artwork
  (what it is), then detail (quality), then room (scale). If that sequence is
  ever reordered, it stops answering the buyer's questions in the order they
  ask them.
- **`LISTING.txt` is the copy surface.** `rebuild.py` preserves it and warns
  when it is missing, which means a missing one is a SKU posted with improvised
  text. The CSV already holds `title_th`, `story_th`, `size_cm`, `frame`, and
  `price` — generating a first draft of `LISTING.txt` from those columns is a
  content fix that removes the most common manual step.
- **Nothing links back.** A Marketplace listing that carries no URL to the
  product on the site converts one buyer and ends. A per-SKU link in the
  listing turns every post into a permanent path back to the catalogue — which
  is another reason per-SKU pages rank so high.

## Search

The only channel that compounds without ongoing effort, and the one this shop
is structurally best suited to: the demand is artist-name shaped and already
exists — "Van Gogh canvas print", "โมเนต์ ภาพติดผนัง" — while the catalogue
has a page-worth of specific data for every SKU.

It is also entirely blocked today if the site renders client-side from the CSV
with no per-SKU URL. Fix that first; everything below depends on it.

Then verify:

- **Per-SKU pages are in the HTML**, not assembled after a fetch. A static
  generator that reads `products.csv` and writes one file per SKU fits the
  project as it is — no framework, no server.
- **Titles and descriptions are per-product**, built from `title_*`, `artist`,
  `size_in`/`size_cm`, and `frame` rather than a single site-wide `<title>`.
- **Body text exists** — `story_th`/`story_en` is what a product page ranks on.
- **Structured data**: `Product` with `Offer` (price, `availability` from
  `status`), plus `ImageObject`. This mostly restates data the page already
  shows, and it is what earns rich results.
- **Artist and collection pages.** One page per painter, listing everything
  available by them, is the page that matches how people actually search.
- **`sitemap.xml` lists every SKU and artist URL**, referenced from
  `robots.txt`; nothing accidentally blocks the catalogue.
- **Alt text names the painting and the painter.** Image search is a real
  channel for this inventory, and this is how it reads the page.

## Instagram and Facebook

Treat social as *link surface*, not as a broadcast channel — the inventory is
the post.

- Per-SKU OG tags must render a real preview first; without them every share
  is a grey box, and no posting cadence can compensate.
- The room shot is the one that performs on a feed, because it answers "how
  big is it" without words.
- Post on the rhythm the catalogue already has — new arrivals, a collection
  filling out. Announcements about the shop perform worse than the inventory
  the shop exists to sell.

## Email and owned channels

The only return path no algorithm controls.

- Capture with a specific promise ("new pieces every Friday") rather than a
  generic newsletter box — the promise is what determines whether it gets
  opened later.
- Send the work, linking deep into product pages rather than the homepage.
- Transactional moments — an enquiry answered, an order shipped — are the
  highest-open messages the shop will ever send. Make each carry the next step,
  not just an acknowledgement.

## Attributing what worked

Channel work without attribution turns into an argument about vibes. Before
any push:

- Tag outbound links so the source survives — Marketplace, Instagram bio,
  email — consistently. Inconsistent tags are worse than none, because they
  fragment the report you need.
- Know the baseline before the push starts.
- Give it a window matched to the channel's own rhythm. Search moves in weeks;
  a social post is mostly spent in 48 hours. Judging one on the other's clock
  produces the wrong conclusion in both directions.
