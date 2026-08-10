#!/usr/bin/env python3
import sys
sys.path.insert(0, "/tmp/claude-0/-home-user-chawakasung/975967af-4225-58d8-a77e-049d1b9cc503/scratchpad")
from build_ai import text_path, text_width

S = "/tmp/claude-0/-home-user-chawakasung/975967af-4225-58d8-a77e-049d1b9cc503/scratchpad"
W, H = 1600, 900

NAVY, BLUE, BRIGHT, SKY = "#022366", "#0B41CD", "#1482FA", "#BDE3FF"
STROKE, PANEL, MUTED, HEX = "#D6E7FA", "#F4F9FF", "#4A5D7E", "#E9F2FD"

logo_inner = open(f"{S}/logo-inner.svg").read()

CHAR_KEYS = ["standup","move","breathe","massage","water","stretch"]

CARDS = [
    ("1", "STAND UP",     ["Get up from your chair", "every 30 minutes."]),
    ("2", "MOVE",         ["Walk around or take", "the stairs."]),
    ("3", "BREATHE",      ["Practice deep,", "conscious breathing."]),
    ("4", "CHAIR MASSAGE",["Try simple neck and", "shoulder relief."]),
    ("5", "DRINK WATER",  ["Stay hydrated", "all day long."]),
    ("6", "STRETCH",      ["Stretch your arms,", "legs, and back."]),
]

# ---- line-art figure icons (64x64 local coords) --------------------------------
ST = f'fill="none" stroke="{BLUE}" stroke-width="3.6" stroke-linecap="round" stroke-linejoin="round"'
AC = f'fill="none" stroke="{BRIGHT}" stroke-width="2.6" stroke-linecap="round" stroke-linejoin="round"'
HD = f'fill="{BLUE}"'

ICONS = [
    # 1 stand up — arms raised, chair behind
    f'<circle cx="34" cy="13" r="6.2" {HD}/>'
    f'<path d="M34 19.5 V37" {ST}/>'
    f'<path d="M34 24 L25 13 M34 24 L43 13" {ST}/>'
    f'<path d="M34 37 L28 52 M34 37 L41 52" {ST}/>'
    f'<path d="M13 50 V36 h9 M13 50 h11" {AC}/>',
    # 2 move — climbing stairs
    f'<path d="M6 54 h12 v-11 h12 v-11 h12 v-11 h10" {AC}/>'
    f'<circle cx="35" cy="15" r="6" {HD}/>'
    f'<path d="M35 21 L31 34" {ST}/>'
    f'<path d="M31 34 L41 41 M31 34 L22 44" {ST}/>'
    f'<path d="M33 26 L43 23 M33 26 L24 28" {ST}/>',
    # 3 breathe — seated meditation + breath curls
    f'<circle cx="30" cy="15" r="6.2" {HD}/>'
    f'<path d="M30 21.5 V32" {ST}/>'
    f'<path d="M30 25 C23 25 19 31 19 37 M30 25 C37 25 41 31 41 37" {ST}/>'
    f'<path d="M17 43 Q30 34 43 43" {ST}/>'
    f'<path d="M48 18 q7 3 0 7 M48 30 q7 3 0 7" {AC}/>',
    # 4 chair massage — seated, hand to neck
    f'<circle cx="27" cy="15" r="6.2" {HD}/>'
    f'<path d="M27 21.5 V36 h12" {ST}/>'
    f'<path d="M27 26 C22 24 20 18 24 16" {ST}/>'
    f'<path d="M39 36 V52" {ST}/>'
    f'<path d="M45 18 V50 M40 43 h11" stroke="{SKY}" fill="none" stroke-width="3" stroke-linecap="round"/>'
    f'<path d="M15 12 q3 3 0 6 M19 10 q3 3 0 6" {AC}/>',
    # 5 drink water — figure holding glass + droplet
    f'<circle cx="27" cy="14" r="6.2" {HD}/>'
    f'<path d="M27 20.5 V39" {ST}/>'
    f'<path d="M27 39 L21 53 M27 39 L33 53" {ST}/>'
    f'<path d="M27 27 L38 31" {ST}/>'
    f'<path d="M37 29 h9 l-1.4 13 h-6.2 z" {AC}/>'
    f'<path d="M15 24 c4.2 5.5 4.2 9 0 9 c-4.2 0 -4.2 -3.5 0 -9 z" fill="{BRIGHT}"/>',
    # 6 stretch — side bend, arm overhead
    f'<circle cx="29" cy="13" r="6.2" {HD}/>'
    f'<path d="M29 19.5 C30 27 29 31 27 35" {ST}/>'
    f'<path d="M29 23 C36 21 42 23 44 14" {ST}/>'
    f'<path d="M29 23 L19 29" {ST}/>'
    f'<path d="M27 35 L20 52 M27 35 L37 50" {ST}/>'
    f'<path d="M48 19 a11 11 0 0 1 -4 11" {AC}/>',
]


import re as _re
def char_svg(name, box_w, box_h, ox, oy):
    """Load an extracted character SVG, namespace its ids, scale to fit box, centre it."""
    raw = open(f"{S}/chars/{name}.svg").read()
    vb = _re.search(r'viewBox="([\d.\- ]+)"', raw).group(1).split()
    vw, vh = float(vb[2]), float(vb[3])
    inner = raw.split('>', 1)[1].rsplit('</svg>', 1)[0]
    inner = inner[inner.index('<defs>'):] if '<defs>' in inner else inner
    inner = _re.sub(r'\s+inkscape:[A-Za-z]+="[^"]*"', '', inner)
    for i in _re.findall(r'id="([^"]+)"', inner):
        inner = inner.replace(f'id="{i}"', f'id="{name}_{i}"').replace(f'url(#{i})', f'url(#{name}_{i})')
    sc = min(box_w / vw, box_h / vh)
    tx = ox + (box_w - vw * sc) / 2
    ty = oy + (box_h - vh * sc) / 2
    return f'<g transform="translate({tx:.1f},{ty:.1f}) scale({sc:.4f})">{inner}</g>'

p = []
p.append(f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" width="{W}" height="{H}">')
p.append('<title>Live Well 2026 — Office Syndrome</title>')

# background
p.append('<g id="Background">')
p.append(f'<rect width="{W}" height="{H}" fill="#FFFFFF"/>')
p.append(f'<path d="M{W} 0 H{W-430} L{W} 470 Z" fill="{HEX}" opacity="0.75"/>')
p.append(f'<path d="M0 {H} H360 L0 {H-330} Z" fill="{HEX}" opacity="0.6"/>')
for cx, cy, r in [(1436, 96, 46), (1520, 150, 46), (1352, 150, 46), (150, 812, 40), (232, 858, 40)]:
    pts = []
    import math
    for i in range(6):
        a = math.radians(60 * i - 30)
        pts.append(f"{cx + r*math.cos(a):.1f},{cy + r*math.sin(a):.1f}")
    p.append(f'<polygon points="{" ".join(pts)}" fill="none" stroke="{SKY}" stroke-width="3.5" opacity="0.85"/>')
p.append('</g>')

# header: real logo + outlined type
p.append('<g id="Header">')
p.append(f'<g id="Roche-logo" transform="translate(56,44) scale(0.204)">{logo_inner}</g>')
t1, _ = text_path("Taking a break during long work hours", 350, 96, 46, "light", NAVY)
t2a, w2a = text_path("helps prevent ", 350, 152, 46, "light", NAVY)
t2b, _ = text_path("Office Syndrome!", 350 + w2a, 152, 46, "bold", NAVY)
t3, _ = text_path("LIVE WELL 2026 INITIATIVE", 352, 196, 19, "medium", BLUE, tracking=3.4)
p.append(f'<g id="Headline">{t1}{t2a}{t2b}</g>')
p.append(f'<g id="Eyebrow">{t3}</g>')
p.append('</g>')

# cards grid 3x2
GX, GY, GW, GH, GAP = 56, 250, 488, 232, 30
p.append('<g id="Cards">')
for i, (num, title, lines) in enumerate(CARDS):
    col, row = i % 3, i // 3
    x = GX + col * (GW + GAP)
    y = GY + row * (GH + GAP)
    p.append(f'<g id="Card-{num}">')
    p.append(f'<rect x="{x}" y="{y}" width="{GW}" height="{GH}" rx="20" fill="{PANEL}" stroke="{STROKE}" stroke-width="2"/>')
    # real Roche character (extracted vector)
    p.append(char_svg(CHAR_KEYS[i], 128, 196, x + 22, y + 18))
    tx = x + 176
    nd, nw = text_path(num, tx, y + 90, 34, "bold", BRIGHT)
    td, _ = text_path(title, tx + nw + 12, y + 90, 25, "bold", NAVY)
    p.append(f'<g id="Card-{num}-title">{nd}{td}</g>')
    for li, ln in enumerate(lines):
        ld, _ = text_path(ln, tx, y + 132 + li * 30, 20, "light", MUTED)
        p.append(ld)
    p.append('</g>')
p.append('</g>')

# footer
p.append('<g id="Footer">')
p.append(f'<line x1="56" y1="820" x2="{W-56}" y2="820" stroke="{STROKE}" stroke-width="2"/>')
ICON_BG = NAVY
socials = [
    "M13 22v-8h3l1-4h-4V7.5C13 6.6 13.3 6 14.7 6H17V2.3C16.6 2.2 15.3 2 13.8 2 10.7 2 9 3.9 9 7v3H6v4h3v8z",
    "M12 7.6A4.4 4.4 0 1 0 12 16.4 4.4 4.4 0 0 0 12 7.6zm0 7.2a2.8 2.8 0 1 1 0-5.6 2.8 2.8 0 0 1 0 5.6zM17.4 5.6a1.05 1.05 0 1 0 0 2.1 1.05 1.05 0 0 0 0-2.1zM12 4.2c2.6 0 2.9 0 3.9.06 1 .05 1.5.2 1.9.35.5.2.8.4 1.2.8.4.4.6.7.8 1.2.15.4.3.9.35 1.9.05 1 .06 1.3.06 3.9s0 2.9-.06 3.9c-.05 1-.2 1.5-.35 1.9-.2.5-.4.8-.8 1.2-.4.4-.7.6-1.2.8-.4.15-.9.3-1.9.35-1 .05-1.3.06-3.9.06s-2.9 0-3.9-.06c-1-.05-1.5-.2-1.9-.35-.5-.2-.8-.4-1.2-.8-.4-.4-.6-.7-.8-1.2-.15-.4-.3-.9-.35-1.9C4.2 14.9 4.2 14.6 4.2 12s0-2.9.06-3.9c.05-1 .2-1.5.35-1.9.2-.5.4-.8.8-1.2.4-.4.7-.6 1.2-.8.4-.15.9-.3 1.9-.35 1-.05 1.3-.06 3.9-.06z",
    "M21.5 8s-.2-1.4-.8-2c-.8-.8-1.6-.8-2-.9C15.9 4.8 12 4.8 12 4.8s-3.9 0-6.7.3c-.4.1-1.2.1-2 .9-.6.6-.8 2-.8 2S2.2 9.6 2.2 11.2v1.5C2.2 14.4 2.5 16 2.5 16s.2 1.4.8 2c.8.8 1.8.8 2.3.9 1.6.2 6.4.3 6.4.3s3.9 0 6.7-.3c.4-.1 1.2-.1 2-.9.6-.6.8-2 .8-2s.3-1.6.3-3.2v-1.5C21.8 9.6 21.5 8 21.5 8zM9.8 14.6V9.3l4.7 2.7z",
    "M15 3c.3 2.3 1.7 3.9 4 4.2v2.9c-1.4 0-2.7-.4-3.9-1.1v5.8c0 3.4-2.7 5.7-5.8 5.2C6.6 19.6 5 17.6 5 15.2c0-2.8 2.5-4.9 5.3-4.4v3c-1.1-.4-2.3.3-2.3 1.5 0 .9.7 1.6 1.6 1.6 1 0 1.7-.8 1.7-1.8V3z",
]
for i, d in enumerate(socials):
    cx = 70 + i * 46
    p.append(f'<circle cx="{cx}" cy="858" r="18" fill="{ICON_BG}"/>')
    p.append(f'<g transform="translate({cx-12},{846}) scale(1.0)"><path d="{d}" fill="#FFFFFF"/></g>')
jd, _ = text_path("JOIN US: LIVE WELL WEEK IN SEPTEMBER", 268, 866, 19, "medium", NAVY, tracking=0.5)
p.append(jd)
bd, _ = text_path("Live Well 2026", W - 56, 866, 22, "bold", BLUE, anchor="end")
p.append(bd)
p.append('</g>')

p.append('</svg>')

out = f"{S}/livewell-office-syndrome.svg"
open(out, "w").write("\n".join(p))
print("wrote", out, len("\n".join(p)), "bytes")
