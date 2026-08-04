#!/usr/bin/env python3.11
"""
Rebuild the Hall of Frame FB Marketplace batch. (portable)

Usage:
    python3.11 rebuild.py [--proj DIR] [--db DIR] <SKU> [<SKU> ...]

Path precedence:  --proj / --db flag  >  $HOF_PROJ / $HOF_DB env  >  built-in default.
  PROJ = project root containing  fb-marketplace/  and  web/img/Gallery/
  DB   = "Hall of Frame DB" folder containing  **/<SKU>/<SKU>F.webp

Needs: Python 3.11 + Pillow (`pip install Pillow`). Not standalone — it only
crops images that already exist under DB/ and web/img/Gallery/.
"""
import os, sys, shutil, subprocess, glob, argparse
from PIL import Image

DEFAULT_PROJ = os.environ.get("HOF_PROJ", "/Users/m1macbookpro/Desktop/peojects/CK/Only Frame/Ai")
DEFAULT_DB   = os.environ.get("HOF_DB",   "/Users/m1macbookpro/Desktop/Hall of Frame DB")
W, H = 1080, 1350
TAGS_HEX  = "62706C6973743030A101555265640A36080A0000000000000101000000000000000200000000000000000000000000000010"
FINFO_HEX = "0000000000000000000C00000000000000000000000000000000000000000000"


def db_framed(db, sku):
    pref = os.path.join(db, "Master frame/VG", sku, f"{sku}F.webp")
    if os.path.exists(pref):
        return pref
    hits = sorted(glob.glob(os.path.join(db, "*", sku, f"{sku}F.webp")))
    return hits[0] if hits else None


def save_1080x1350(src, dst):
    im = Image.open(src).convert("RGB")
    s = max(W / im.width, H / im.height)
    im = im.resize((round(im.width * s), round(im.height * s)), Image.LANCZOS)
    x, y = (im.width - W) // 2, (im.height - H) // 2
    im.crop((x, y, x + W, y + H)).save(dst, quality=92)


def red_tag(folder):
    # macOS Finder red tag only; no-op on other OSes or if `xattr` is unavailable.
    if sys.platform != "darwin" or shutil.which("xattr") is None:
        return
    try:
        subprocess.run(["xattr", "-wx", "com.apple.metadata:_kMDItemUserTags", TAGS_HEX, folder], check=True)
        subprocess.run(["xattr", "-wx", "com.apple.FinderInfo", FINFO_HEX, folder], check=True)
    except Exception as e:
        print(f"  (red-tag skipped for {os.path.basename(folder)}: {e})")


def main(proj, db, skus):
    mkt = os.path.join(proj, "fb-marketplace")
    gal = os.path.join(proj, "web/img/Gallery")
    if not os.path.isdir(gal):
        sys.exit(f"Gallery not found: {gal}\n  → set --proj or $HOF_PROJ to the project root.")
    if not os.path.isdir(db):
        sys.exit(f"DB not found: {db}\n  → set --db or $HOF_DB to the 'Hall of Frame DB' folder.")
    os.makedirs(mkt, exist_ok=True)

    keep = set(skus)
    bad = []
    for s in skus:
        missing = [t for t in ("Img", "Detail", "Room")
                   if not os.path.exists(os.path.join(gal, s, f"{s}{t}.webp"))]
        if db_framed(db, s) is None:
            missing.append("DB-F")
        if missing:
            bad.append((s, missing))
    if bad:
        for s, m in bad:
            print(f"  MISSING for {s}: {', '.join(m)}")
        sys.exit(f"Aborting — {len(bad)} SKU(s) missing sources (fix before rebuilding).")

    removed = 0
    for name in os.listdir(mkt):
        if name in keep:
            continue
        p = os.path.join(mkt, name)
        shutil.rmtree(p) if os.path.isdir(p) else os.remove(p)
        removed += 1
    print(f"removed {removed} entr{'y' if removed==1 else 'ies'} from fb-marketplace/")

    for s in skus:
        d = os.path.join(mkt, s)
        os.makedirs(d, exist_ok=True)
        f = db_framed(db, s)
        save_1080x1350(f, os.path.join(d, "01-framed.jpg"))
        save_1080x1350(os.path.join(gal, s, f"{s}Img.webp"),    os.path.join(d, "02-artwork.jpg"))
        save_1080x1350(os.path.join(gal, s, f"{s}Detail.webp"), os.path.join(d, "03-detail.jpg"))
        save_1080x1350(os.path.join(gal, s, f"{s}Room.webp"),   os.path.join(d, "04-room.jpg"))
        red_tag(d)
        listing = "ok" if os.path.exists(os.path.join(d, "LISTING.txt")) else "⚠️ MISSING — generate it"
        rel = f.split("Hall of Frame DB/")[-1]
        print(f"  {s}: 01-framed <- {rel}   LISTING: {listing}")

    print(f"\nfb-marketplace/ now = {sorted(os.listdir(mkt))}")
    print("All red-tagged where supported (= not yet posted). Show one 01-framed.jpg before declaring done.")


if __name__ == "__main__":
    ap = argparse.ArgumentParser(description="Rebuild the Hall of Frame FB Marketplace batch (portable).")
    ap.add_argument("--proj", default=DEFAULT_PROJ, help="project root (has fb-marketplace/ + web/img/Gallery/)")
    ap.add_argument("--db",   default=DEFAULT_DB,   help="Hall of Frame DB folder (has **/<SKU>/<SKU>F.webp)")
    ap.add_argument("skus", nargs="+", help="one or more SKUs")
    a = ap.parse_args()
    main(a.proj, a.db, a.skus)
