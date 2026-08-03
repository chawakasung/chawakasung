# On-site failure modes

The checkable version of the funnel table in `SKILL.md`. Each entry says what
to look for, how to check it, and why it costs engagement — the *why* matters
because it tells you whether the finding applies to Hall of Frame specifically
or only to the generic shop in your head.

Not a checklist to run top to bottom. Walk the funnel in order, stop at the
first stage that is clearly leaking, and fix that before looking further down:
a leak at Arrive makes every measurement below it noise.

A recurring theme worth noticing before you start — `products.csv` already
carries 19 columns of information about every SKU. Several of the failure
modes below are not missing *data*, they are data the site never shows. Those
are the cheapest wins available, because the content work is already done.

## Contents

- [Arrive](#arrive)
- [Browse](#browse)
- [Consider](#consider)
- [Act](#act)
- [Return and share](#return-and-share)
- [Cross-cutting: speed](#cross-cutting-speed)
- [Cross-cutting: measurement](#cross-cutting-measurement)

## Arrive

**Everyone lands on the homepage regardless of what they wanted.**
Check: does a specific painting have its own URL? Open one and read the
address bar; reload it and see whether it returns to the same painting.
Why: search and social send people to *one thing*. With no per-SKU URL, the
site cannot receive that traffic at all — the visitor is dropped at the front
door and asked to find it again. Confirm how products are addressed in
`web/app.js` before ranking anything else; this one constrains most of the
list below.

**The work is not visible above the fold.**
Check: load at 390×844 (phone) and note the scroll depth of the first painting.
Why: the only argument this shop has is how the pieces look. Anything between
the visitor and the first framed image is asking them to take it on faith.

**Layout shift as images load.**
Check: do image containers carry width/height or `aspect-ratio`? Watch the
grid reflow on a throttled connection.
Why: shifting content makes people lose their place and mis-tap. Cheapest fix
on this list and one of the most felt.

**Near-empty states rendered as if full.**
Check: a filtered view with few results, or a collection with two items.
Why: an empty grid reads as broken. An empty state that offers the next best
thing keeps the session alive.

## Browse

**The catalogue's own vocabulary is unused.**
Check: `collection`, `movement`, `room_fit`, `mood_tag`, `artist`, and price
are all columns in the CSV. Which of them can a visitor actually browse by?
Why: someone shopping for a wall thinks "something calm for the bedroom",
not "Impressionism, 1889". `room_fit` and `mood_tag` are that exact language
and are already filled in — leaving them unexposed throws away depth that
costs nothing to add.

**Dead-end product views.**
Check: at the bottom of an open painting, what is offered? Same artist, same
collection, same room fit, next/previous?
Why: the visitor has already proven interest by opening it. Offering nothing
at that moment discards the highest-intent second they will spend on the site.

**No sort, no price range.**
Check: can the grid be ordered by price, size, or newest?
Why: budget and wall size are the two real constraints people shop under.
Without them, browsing stops feeling like choosing and starts feeling like
scrolling.

**Grid renders only after JS fetches and parses the CSV.**
Check: fetch the page raw (`curl`) and look for product markup; throttle to
slow 3G and watch how long the grid takes to appear.
Why: a ~254 KB CSV parsed client-side before anything renders is a blank
screen at exactly the moment a first-time visitor decides whether to stay.
It is also why nothing is indexable — same root cause as the missing per-SKU
URLs.

## Consider

This is where a framed-print shop wins or loses, because the buyer cannot
touch the thing. Every item here is about making the product concrete.

**Scale is not shown.**
Check: is there a room shot with recognisable furniture, or any size
reference, on the product view? `<SKU>Room.webp` already exists for every SKU.
Why: "24×36 in" means nothing to most people. The room shot is the single
most persuasive asset the shop owns and it is already produced — check that it
is actually surfaced, and early.

**Sizes in inches only.**
Check: does the product view show `size_cm` as well as `size_in`?
Why: Thai buyers measure walls in centimetres. Both columns exist; showing one
makes half the audience do arithmetic before they can picture it.

**The frame is a word, not a picture.**
Check: is `frame` shown as text only? Is `<SKU>F.webp`, the dark-studio framed
shot, used anywhere on the site — or does it only ever reach Facebook
Marketplace through `rebuild.py`?
Why: the frame is what is actually being sold. If the best framed photograph
exists but never appears on the website, the site is selling the free part and
hiding the paid part.

**The story is missing.**
Check: are `story_th` / `story_en` rendered on the product view?
Why: two reasons at once. It is the difference between a poster and something
with meaning behind it, and it is the only body text a product page has to
rank on. Written already; costs nothing to show.

**Availability is stale or absent.**
Check: is the `status` column reflected in the UI? What happens when someone
opens something already sold?
Why: nothing damages trust faster than enquiring about something unavailable.
A visible "sold" is also honest scarcity — the kind that works.

**Delivery, materials, and returns are unanswered.**
Check: on the product view — not a separate policy page — can the visitor find
what the canvas and frame are, how long delivery takes, and what happens if it
arrives damaged?
Why: these are the questions that stop a purchase. Answering them where the
decision happens, rather than three clicks away, is a conversion fix disguised
as content.

**Bilingual fields, monolingual site.**
Check: `title_th`/`title_en` and `story_th`/`story_en` both exist. Does the
site expose both, and is there `hreflang` if it does?
Why: the data is already bilingual. Serving only one language halves the
addressable audience for content that is already written.

## Act

**The next step is not obvious from the product view.**
Check: with a painting open, how many taps to ask about it or buy it? Is the
action visible without scrolling on a phone?
Why: intent decays in seconds. An enquiry path that requires hunting converts
the interested visitor into a closed tab.

**Enquiries lose the SKU.**
Check: does the contact/DM path carry which painting was being viewed?
Why: a message that starts "which one?" adds a round trip at the most fragile
moment, and it makes attribution impossible — you lose both the sale and the
data about where it came from.

**No low-cost action short of buying.**
Check: is there anything between looking and committing — a save, a share, an
ask-a-question?
Why: engagement is a ladder — look, save, share, ask, buy, return. A site with
only the top rung gets almost no one onto it.

## Return and share

**Links paste as a grey box.**
Check: for a product URL, is there `og:title`, `og:description`, `og:image`
(absolute URL, ~1200×630), `twitter:card=summary_large_image`, and a
`canonical`? Are they per-SKU or copied from the site defaults?
Why: on a visual shop, a link with no preview is the loudest possible signal
that there is nothing to see. Every Marketplace and Instagram link goes
through this. Usually the highest return-per-hour fix available — but it
depends on per-SKU URLs existing first.

**Nothing changes between visits.**
Check: is there a "new this week", are additions dated, is there a current
collection?
Why: a return visit is a bet that something changed. Nothing signalling change
means the bet stops being placed.

**No owned channel.**
Check: email capture with a specific promise, or an opt-in of any kind.
Why: without one, every returning visitor has to remember the shop unprompted.
An owned channel is the only return path no algorithm controls.

## Cross-cutting: speed

Check the largest image actually shipped to a phone: responsive
(`srcset`/`sizes`), modern format, lazy below the fold, eager for the first
one. The gallery images are already `.webp`, which is most of the battle —
verify the *dimensions* served match the slot they are displayed in, since a
full-resolution artwork scan in a 400 px card is the usual culprit.

Why: on a shop whose payload is images, image delivery is approximately the
whole performance story. Slow first paint costs arrivals before anything else
on this list can matter.

## Cross-cutting: measurement

Check what exists: any analytics at all, custom events for the actions that
matter (product opened, filter used, size compared, enquiry started vs. sent),
and referrer data that can tell Marketplace from Instagram from search.

Why: without event data you can see sessions but not engagement, so every
ranking decision after that is taste rather than evidence. If the funnel
stages cannot be told apart in the data, adding that instrumentation is
usually the correct first shipped change of the whole effort.
