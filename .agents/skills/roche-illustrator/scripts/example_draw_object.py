NAVY, SKY, ORANGE, CREAM, SKIN = "#022366", "#BDE3FF", "#FF7D29", "#FFF7F5", "#F4C9A0"
MIDBLUE, VIOLET, HAIR = "#1482FA", "#BC36F0", "#7A3620"

def massage_chair(ox, oy, h):
    """Woman relaxing in a massage chair — flat side view facing left.
    Shell in sky, cushions in midblue, navy headrest/base, violet leggings."""
    s = h / 175.0
    def P(v): return " ".join(f"{ox+a*s:.1f},{oy+b*s:.1f}" for a, b in v)
    def D(c): return " ".join(t if isinstance(t, str) else f"{ox+t[0]*s:.1f} {oy+t[1]*s:.1f}" for t in c)
    def poly(v, f): return f'<polygon points="{P(v)}" fill="{f}"/>'
    def path(c, f): return f'<path d="{D(c)}" fill="{f}"/>'
    def band(p1, p2, w):
        (x1,y1),(x2,y2) = p1,p2
        dx,dy = x2-x1, y2-y1
        L = (dx*dx+dy*dy)**0.5 or 1
        nx,ny = -dy/L*w/2, dx/L*w/2
        return [(x1+nx,y1+ny),(x1-nx,y1-ny),(x2-nx,y2-ny),(x2+nx,y2+ny)]
    def circle(c, r, f):
        return f'<circle cx="{ox+c[0]*s:.1f}" cy="{oy+c[1]*s:.1f}" r="{r*s:.1f}" fill="{f}"/>'

    p = ['<g id="massage-chair">']

    # shell: tall rounded backrest, slight recline
    p.append(path(["M",(114,122),"L",(128,30),"Q",(130,14),(146,14),
                   "Q",(164,14),(165,32),"L",(163,122),"Z"], SKY))
    # headrest pillow
    p.append(poly([(130,30),(158,32),(156,58),(128,56)], NAVY))
    # accent stripe on the shell edge
    p.append(poly([(156,62),(163,62),(161,118),(154,118)], ORANGE))
    # seat cushion
    p.append(poly([(64,104),(130,104),(132,124),(62,124)], MIDBLUE))
    # attached leg rest + pad
    p.append(poly(band((62,110),(34,142), 30), SKY))
    p.append(poly(band((60,110),(37,138), 16), MIDBLUE))
    # rear support + base skid
    p.append(poly([(146,122),(163,122),(168,150),(151,150)], NAVY))
    p.append(path(["M",(64,150),"Q",(56,150),(56,155),"Q",(56,160),(64,160),
                   "L",(168,160),"Q",(176,160),(176,155),"Q",(176,150),(168,150),"Z"], NAVY))

    # ---- woman ----
    HIP=(104,100); KNEE=(72,90); ANKLE=(52,124); SHOULDER=(124,54); HAND=(98,80); HEAD=(130,36)
    p.append(poly(band(KNEE, ANKLE, 15), VIOLET))                 # calf
    p.append(poly([(46,122),(58,130),(50,142),(38,134)], NAVY))   # shoe
    p.append(poly(band(HIP, KNEE, 20), VIOLET))                   # thigh
    p.append(poly(band(SHOULDER, HIP, 26), ORANGE))               # torso
    p.append(poly(band((127,46),(122,56), 8), SKIN))              # neck
    p.append(circle(HEAD, 12, SKIN))                              # head
    p.append(path(["M",(142,34),"Q",(143,22),(130,22),"Q",(118,23),(117,34),
                   "L",(123,36),"Q",(124,28),(131,28),"Q",(138,29),(137,36),"Z"], HAIR))
    p.append(circle((143,28), 5.5, HAIR))                         # bun
    # armrest pod over the hip, rounded nose
    p.append(path(["M",(96,84),"Q",(86,84),(86,94),"L",(86,116),"L",(134,116),
                   "L",(134,84),"Z"], SKY))
    p.append(poly(band(SHOULDER, HAND, 11), ORANGE))              # arm onto the armrest
    p.append(circle(HAND, 5, SKIN))                               # hand

    # electric control: cord + remote pendant on the armrest side
    p.append(f'<path d="{D(["M",(130,96),"Q",(140,104),(139,116)])}" fill="none" '
             f'stroke="{NAVY}" stroke-width="{2.6*s:.1f}"/>')
    p.append(path(["M",(134,116),"Q",(132,114),(132,120),"L",(132,136),"Q",(132,140),(136,140),
                   "L",(144,140),"Q",(148,140),(148,136),"L",(148,120),"Q",(148,114),(144,116),"Z"], NAVY))
    for k in range(3):
        p.append(circle((137+k*3.4,124), 1.5, ORANGE))
    p.append(circle((140,132), 2.2, MIDBLUE))
    p.append('</g>')
    return "".join(p)
