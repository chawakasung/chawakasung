# On-site failure modes

The checkable version of the funnel table in `SKILL.md`. Each entry says what
to look for, how to check it, and why it costs engagement — the *why* matters
because it tells you whether the finding applies to this particular site or
only to the generic gallery in your head.

Not a checklist to run top to bottom. Walk the funnel in order, stop at the
first stage that is clearly leaking, and fix that before looking further down
— a leak at Arrive makes every measurement below it noise.

## Contents

- [Arrive](#arrive)
- [Browse](#browse)
- [Participate](#participate)
- [Share](#share)
- [Return](#return)
- [Cross-cutting: speed](#cross-cutting-speed)
- [Cross-cutting: measurement](#cross-cutting-measurement)

## Arrive

**The work is not visible above the fold.**
Check: load the landing page at 390×844 (phone) and note the scroll depth of
the first artwork. Grep the landing template for a full-viewport hero, splash
screen, cookie/age gate, or "Enter" button.
Why: a gallery's only argument is the work. Anything between the visitor and
the first image is asking them to take the site on faith, which most will not.

**No sense of scale or freshness.**
Check: is there any visible count ("2,481 entries by 630 creators") or recency
signal ("added this week")?
Why: scale is the social proof that makes browsing feel worthwhile, and
freshness is the implicit promise that returning is worthwhile. A gallery that
looks abandoned gets treated as abandoned.

**Near-empty states rendered as if full.**
Check: visit a sparse category, a new creator's profile, a filtered view with
few results.
Why: an empty grid reads as broken. An empty state that offers the next best
thing ("nothing here yet — see the most recent 12") keeps the session alive.

**Layout shift as images load.**
Check: do image containers carry width/height or `aspect-ratio`? Watch the
grid reflow on a throttled connection.
Why: shifting content makes people lose their place and mis-tap. It is the
cheapest fix on this list and one of the most felt.

## Browse

**Item pages exist only as modals.**
Check: open an item, copy the URL. Does it identify the item? Reload it — does
it deep-link back to the same item?
Why: no URL means no share, no search result, no bookmark, no link from a
creator's own post. This is usually the single most expensive architectural
choice a gallery makes.

**Dead-end item pages.**
Check: at the bottom of an item page, what is offered? Next/previous within
the same collection? More by this creator? Similar tags?
Why: the visitor has already proven interest by opening one item. Offering
nothing at that exact moment discards the highest-intent second they will
spend on the site.

**Infinite scroll with no crawlable pagination.**
Check: disable JS, or fetch the grid URL raw. Are item links present in the
HTML? Is there a `?page=` fallback?
Why: search engines and link-previewers see the empty shell, and visitors lose
their scroll position when they navigate back. Keep infinite scroll if it
suits the site, but back it with real paginated URLs.

**No filtering or sorting once the collection outgrows one screen.**
Check: count items, then look for tags, categories, year, medium, sort by
recent/popular.
Why: browsing without structure stops feeling like exploring and starts
feeling like scrolling. Depth per session is the metric that moves here.

**Keyboard and screen-reader navigation absent.**
Check: tab through the grid; arrow keys in the lightbox; `alt` text on
`<img>`; focus visible.
Why: it excludes real visitors, and the same markup is what image search and
share previews read. One fix, three payoffs.

## Participate

**Signup demanded before value is shown.**
Check: what is the first gate in the submit flow? Can a visitor see what a
featured entry looks like before creating an account?
Why: the visitor is being asked to pay before seeing the price list. Show the
outcome first, ask for the account at the last possible step.

**No low-cost action for anonymous visitors.**
Check: is there anything between "look" and "create an account and submit"?
Why: engagement is a ladder — view, react, share, follow, submit, return. A
site with only the top rung gets almost no one onto it. A one-tap reaction
that needs no account converts far more people into people-who-did-something,
and those are the ones who come back.

**Submission friction that is not doing any work.**
Check: field count, required vs. optional, file-size limits, does it accept
what creators actually have?
Why: every optional-but-required field is a chance to abandon. Ask for what
you truly need to publish, and collect the rest later from people who already
said yes.

**Creator profiles that go nowhere.**
Check: can a creator link out to their own site or accounts? Can a visitor
follow them?
Why: creators promote pages that serve them. A profile that is a dead end
gives them no reason to send their own audience to it.

## Share

**Missing or broken per-item share previews.**
Check: for an item URL, is there `og:title`, `og:description`, `og:image`
(absolute URL, ~1200×630), `twitter:card=summary_large_image`, and a
`canonical`? Are they per-item or copied from the site defaults?
Why: on a visual site, a link that pastes as a grey box is the loudest
possible signal that there is nothing to see. This is usually the highest
return-per-hour fix available.

**Share paths that depend on third-party widgets.**
Check: are share buttons plain links, or a script bundle from a social
network?
Why: widgets are slow, get blocked, and leak visitor data. Plain intent URLs
and a copy-link button do the same job.

**Nothing prepared for the people most likely to share.**
Check: when someone is featured, are they given the link, a preview image, and
suggested text?
Why: featured creators are the site's distribution channel and they *want* to
post. Handing them a ready asset converts that goodwill into traffic; making
them assemble it themselves usually converts it into nothing.

## Return

**No visible change between visits.**
Check: is there a "new this week", dated entries, a current round or theme?
Why: a return visit is a bet that something changed. Nothing signalling change
means the bet stops being placed.

**No owned channel.**
Check: email capture, RSS/Atom feed, or opt-in notifications — and whether
anything is actually sent.
Why: without one, every returning visitor has to remember the site
unprompted. An owned channel is the only return path that does not depend on
an algorithm.

**Cadence hidden.**
Check: for a site with rounds, awards, or seasons — is the next date visible?
Why: a published date creates a reason to come back on a specific day, which
is far stronger than a general intention to return sometime.

## Cross-cutting: speed

Check the largest image actually shipped to a phone: is it responsive
(`srcset`/`sizes`), modern format (AVIF/WebP), lazy below the fold, eager for
the first one, and served through an image CDN or a build-time pipeline?

Why: on a gallery, images *are* the payload, so image delivery is
approximately the whole performance story. Slow first paint costs arrivals
before any other work on this list can matter — which is why a genuinely slow
site outranks almost everything else in the ranking step.

## Cross-cutting: measurement

Check what exists: any analytics at all, custom events for the actions that
matter (item opened, filter used, share clicked, submission started vs.
completed), and referrer data.

Why: without event data you can see sessions but not engagement, so every
ranking decision after that is taste rather than evidence. If the funnel
stages cannot be told apart in the data, adding that instrumentation is
usually the correct first shipped change of the whole engagement effort.
