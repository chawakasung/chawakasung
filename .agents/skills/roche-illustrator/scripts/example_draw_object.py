def massage_chair(ox, oy, h):
    """Flat brand-style recliner massage chair, side view, seat facing left."""
    s = h / 150.0
    def pts(v):
        return " ".join(f"{ox+a*s:.1f},{oy+b*s:.1f}" for a, b in v)
    def d(cmds):
        out = []
        for c in cmds:
            out.append(c if isinstance(c, str) else f"{ox+c[0]*s:.1f} {oy+c[1]*s:.1f}")
        return " ".join(out)

    SHELL, PAD, DEEP, NAVY = "#BDE3FF", "#FF7D29", "#B22B0D", "#022366"
    p = ['<g id="massage-chair">']

    # base + pedestal
    p.append(f'<polygon points="{pts([(56,134),(142,134),(134,148),(48,148)])}" fill="{NAVY}"/>')
    p.append(f'<polygon points="{pts([(84,112),(118,112),(124,134),(78,134)])}" fill="{NAVY}"/>')

    # outer shell: reclined back column + seat ledge
    # seat shell (stays level)
    seat_shell = ["M",(58,88),"L",(120,88),"Q",(146,88),(146,110),"Q",(146,116),(126,116),
                  "L",(58,116),"Z"]
    p.append(f'<path d="{d(seat_shell)}" fill="{SHELL}"/>')
    # reclined back assembly
    px, py = ox + 108*s, oy + 104*s
    p.append(f'<g transform="rotate(-14 {px:.1f} {py:.1f})">')
    back_shell = ["M",(96,104),"L",(96,34),"Q",(96,10),(121,10),"Q",(146,10),(146,34),
                  "L",(146,104),"Z"]
    p.append(f'<path d="{d(back_shell)}" fill="{SHELL}"/>')

    # leg / calf rest angled down-left
    p.append(f'<polygon points="{pts([(60,90),(60,116),(14,132),(6,112)])}" fill="{SHELL}"/>')
    p.append(f'<polygon points="{pts([(58,94),(58,111),(18,125),(13,113)])}" fill="{PAD}"/>')

    # backrest cushion, then headrest band on top of it
    back = ["M",(104,40),"Q",(104,22),(120,22),"L",(126,22),"Q",(140,22),(140,40),
            "L",(140,96),"L",(104,96),"Z"]
    head = ["M",(104,40),"Q",(104,22),(120,22),"L",(126,22),"Q",(140,22),(140,40),
            "L",(140,50),"L",(104,50),"Z"]
    p.append(f'<path d="{d(back)}" fill="{PAD}"/>')
    p.append(f'<path d="{d(head)}" fill="{DEEP}"/>')
    p.append('</g>')

    # seat cushion + armrest
    p.append(f'<polygon points="{pts([(60,94),(104,94),(104,112),(60,112)])}" fill="{PAD}"/>')
    arm = ["M",(56,78),"Q",(52,78),(52,86),"L",(52,96),"L",(104,96),"L",(104,78),"Z"]
    p.append(f'<path d="{d(arm)}" fill="{SHELL}"/>')

    p.append('</g>')
    return "".join(p)
