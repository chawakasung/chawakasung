#!/usr/bin/env python3
"""Build an Illustrator-ready SVG: real Roche logo vectors + Roche Sans text as outlines."""
import os
from fontTools.ttLib import TTFont
from fontTools.pens.svgPathPen import SVGPathPen

S = "/tmp/claude-0/-home-user-chawakasung/975967af-4225-58d8-a77e-049d1b9cc503/scratchpad"
FD = f"{S}/fonts/Roche Sans"

FONTS = {
    "light":   f"{FD}/RocheSansLight-Light.ttf",
    "regular": f"{FD}/RocheSans-Regular.ttf",
    "medium":  f"{FD}/RocheSansMedium-Medium.ttf",
    "bold":    f"{FD}/RocheSans-Bold.ttf",
}
_cache = {}


def _load(w):
    if w not in _cache:
        f = TTFont(FONTS[w])
        _cache[w] = (f, f.getGlyphSet(), f["cmap"].getBestCmap(), f["head"].unitsPerEm,
                     f["hmtx"])
    return _cache[w]


def text_width(s, size, weight="regular", tracking=0.0):
    font, gs, cmap, upm, hmtx = _load(weight)
    total = 0
    for ch in s:
        gn = cmap.get(ord(ch))
        if gn is None:
            gn = cmap.get(32)
        total += hmtx[gn][0]
    return total * size / upm + tracking * max(0, len(s) - 1)


def text_path(s, x, y, size, weight="regular", fill="#000", tracking=0.0, anchor="start"):
    """Return <path> data for a string rendered as outlines. y = baseline."""
    font, gs, cmap, upm, hmtx = _load(weight)
    scale = size / upm
    w = text_width(s, size, weight, tracking)
    if anchor == "middle":
        x -= w / 2
    elif anchor == "end":
        x -= w
    out = []
    cursor = x
    for ch in s:
        gn = cmap.get(ord(ch))
        if gn is None:
            gn = cmap.get(32)
        if ch != " ":
            pen = SVGPathPen(gs)
            gs[gn].draw(pen)
            d = pen.getCommands()
            if d:
                out.append(
                    f'<path d="{d}" fill="{fill}" '
                    f'transform="translate({cursor:.2f},{y:.2f}) scale({scale:.5f},{-scale:.5f})"/>'
                )
        cursor += hmtx[gn][0] * scale + tracking
    return "\n      ".join(out), w
