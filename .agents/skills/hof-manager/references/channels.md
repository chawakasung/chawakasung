# Off-site channels

Read this when the work moves past the site itself to how people find it and
come back. On-site fixes raise the value of every visitor; channel work raises
the number of them. Both are needed, but they fail differently: on-site
problems are visible to anyone who looks, while channel problems are invisible
until you go looking for traffic that never arrived.

Order channels by what the gallery already has, not by what is fashionable. A
site with 500 featured creators and no email list should build the creator
channel before touching paid anything.

## Search

Search is the only channel that compounds without ongoing effort, and a
gallery is unusually well suited to it: many pages, each about one specific
thing, each with an image.

What to verify:

- **Item pages are server-rendered or prerendered.** Fetch an item URL raw and
  look for the title, description, and image in the HTML. A client-only render
  means an empty page in the index.
- **Titles and descriptions are per-item.** Grep for a hardcoded `<title>`
  shared across routes. Identical titles across thousands of pages is a
  self-inflicted ranking cap.
- **Item pages carry text.** A caption, medium, year, creator statement — a
  page with nothing but an image has almost nothing to rank on.
- **Structured data.** `ImageObject` for works, `Person` for creators,
  `BreadcrumbList` for navigation, `CreativeWork` where it fits. This is what
  earns rich results, and it is mostly restating data the page already has.
- **`sitemap.xml` includes item and creator URLs** and is referenced from
  `robots.txt`; `robots.txt` is not accidentally blocking the gallery routes.
- **Alt text is descriptive.** It feeds image search, which for a visual site
  can outproduce text search.

## Social

Treat social as *link surface*, not as a place to broadcast. The gallery's
content already is the post.

What to verify:

- Per-item OG/Twitter tags render a real preview (see the Share section in
  `failure-modes.md` — this is the same fix, and it is the prerequisite for
  every other social effort).
- Share targets match where the audience is, and are plain intent URLs rather
  than script widgets.
- A copy-link affordance exists, since a large share of sharing happens
  through chat apps that no button covers.

What to produce, if the user wants content rather than plumbing: post the work
itself with credit to the creator, on a rhythm tied to the site's own cadence
(new entries, round results). Announcements about the site perform worse than
the work the site exists to show — the work is the reason anyone follows.

## Creators as a channel

This is the channel a hall-of-fame site has that most sites do not, and it is
usually underbuilt.

- Notify people when they are featured, with the direct link.
- Hand them a ready-to-post image and suggested text, and a badge or embed
  they can put on their own site — every embed is a backlink and a permanent
  referral path.
- Make the profile worth pointing at: their links out, their other entries,
  something that makes being listed feel like an asset rather than an archive
  entry.

The test: after being featured, is sharing the *easiest* next action, or does
it require the creator to assemble anything?

## Email and owned channels

The only path back that no algorithm controls.

- Capture with a specific promise ("new entries every Friday") rather than a
  generic newsletter box — the promise is what determines whether it gets
  opened later.
- Send on the cadence promised, containing the work, linking deep into item
  pages rather than the homepage.
- Transactional moments — a submission accepted, an entry featured — are the
  highest-open messages the site will ever send. Make sure each carries the
  next step, not just an acknowledgement.
- An RSS/Atom feed is nearly free and serves the technically-inclined slice of
  the audience that will otherwise never come back.

## Attributing what worked

Channel work without attribution turns into an argument about vibes. Before
running a campaign of any size:

- Tag outbound links so the referrer survives (UTM or the project's own
  convention), consistently — inconsistent tags are worse than none, because
  they fragment the very report you need.
- Know the baseline for the metric before the push starts.
- Give it a window long enough for the channel's own rhythm. Search moves in
  weeks; a social post's effect is mostly spent in 48 hours. Judging one on the
  other's clock produces the wrong conclusion in both directions.
