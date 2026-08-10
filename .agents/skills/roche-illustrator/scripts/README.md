# Scripts

Helpers for producing Roche-branded vector artwork. Both were used to build a real
deliverable (a Live Well / Office Syndrome infographic) and are kept as working references.

| File | Purpose |
| --- | --- |
| `text_to_outlines.py` | Render a string in Roche Sans as SVG outline `<path>`s via `fontTools`. Returns path data + advance width, supports `start` / `middle` / `end` anchoring and letter-spacing. Use so delivered SVG needs no licensed font installed. |
| `example_draw_object.py` | A recliner massage chair drawn from scratch in flat brand shapes (shell / upholstery / navy frame). Use as the pattern for props the official libraries don't contain — check the libraries first, and always render and look before shipping. |
| `example_compose_infographic.py` | End-to-end example: flat background, embedded logo vector, outlined Roche Sans headline, a 3×2 card grid, and **real character figures extracted from a Roche `.ai` library**. Shows the id-namespacing and `inkscape:`-attribute stripping that embedded `get_svg_image()` output requires. |

## Before running

Both scripts carry **absolute paths to a scratchpad directory that no longer exists**, and
they depend on **licensed Roche assets that are deliberately not in this repository** —
Roche Sans (`fonts/Roche Sans/*.ttf`), the logo SVG, and the `.ai` character libraries.

To reuse them: have the user supply those assets for the session, then repoint `S`, `FD`,
and the `chars/` and `logo-inner.svg` paths at wherever they landed.

```bash
pip3 install pymupdf fonttools
```

See the parent `SKILL.md` for the full `.ai` extraction pipeline and the verified brand
palette.
