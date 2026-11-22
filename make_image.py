#!/usr/bin/env python3
"""Draw the news-image entry for 21 November 2026 (1024x1024, deterministic).

Run: python3 make_image.py  -> writes entry.png (1024x1024, PNG, <= 1 MiB).
No network, no randomness, no timestamps. Re-running produces identical bytes.
"""
from PIL import Image, ImageDraw, ImageFont

W, H = 1024, 1024
OUT = "entry.png"

BOLD = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"
REG = "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"
SERIF_BOLD = "/usr/share/fonts/truetype/dejavu/DejaVuSerif-Bold.ttf"

PAPER = (247, 243, 236)      # warm off-white
INK = (18, 24, 33)           # near-black
NAVY = (15, 42, 68)          # masthead
RED = (178, 34, 34)          # accent red
GOLD = (212, 160, 60)
GREEN = (34, 120, 70)
STEEL = (52, 90, 130)
TEAL = (14, 120, 118)
ORANGE = (214, 96, 20)
GREY = (90, 96, 104)
CARD = (255, 255, 255)


def font(path, size):
    return ImageFont.truetype(path, size)


def wrap(draw, text, fnt, max_w):
    """Wrap text to fit max_w pixels; returns list of lines."""
    words = text.split()
    lines, cur = [], ""
    for w in words:
        t = (cur + " " + w).strip()
        if draw.textlength(t, font=fnt) <= max_w:
            cur = t
        else:
            if cur:
                lines.append(cur)
            cur = w
    if cur:
        lines.append(cur)
    return lines


def draw_centered(draw, cx, y, text, fnt, fill):
    w = draw.textlength(text, font=fnt)
    draw.text((cx - w / 2, y), text, font=fnt, fill=fill)
    return y + fnt.size


def flame(draw, cx, cy, s):
    """Stylised flame (orange/red polygons) centred at (cx, cy), size s."""
    # outer flame
    outer = [
        (cx, cy - s),
        (cx + s * 0.55, cy - s * 0.25),
        (cx + s * 0.45, cy + s * 0.35),
        (cx + s * 0.75, cy + s * 0.10),
        (cx + s * 0.35, cy + s * 0.75),
        (cx, cy + s * 0.95),
        (cx - s * 0.35, cy + s * 0.75),
        (cx - s * 0.75, cy + s * 0.10),
        (cx - s * 0.45, cy + s * 0.35),
        (cx - s * 0.55, cy - s * 0.25),
    ]
    draw.polygon(outer, fill=ORANGE)
    # inner flame (gold)
    inner = [
        (cx, cy - s * 0.45),
        (cx + s * 0.30, cy - s * 0.05),
        (cx + s * 0.25, cy + s * 0.35),
        (cx, cy + s * 0.55),
        (cx - s * 0.25, cy + s * 0.35),
        (cx - s * 0.30, cy - s * 0.05),
    ]
    draw.polygon(inner, fill=GOLD)
    # core (pale yellow)
    draw.ellipse([cx - s * 0.14, cy + s * 0.10, cx + s * 0.14, cy + s * 0.45],
                 fill=(255, 226, 120))


def badge_star(draw, cx, cy, r, fill):
    """Five-pointed star (police badge) centred at (cx, cy), radius r."""
    import math
    pts = []
    for i in range(10):
        ang = -math.pi / 2 + i * math.pi / 5
        rr = r if i % 2 == 0 else r * 0.45
        pts.append((cx + rr * math.cos(ang), cy + rr * math.sin(ang)))
    draw.polygon(pts, fill=fill)
    draw.ellipse([cx - r * 0.22, cy - r * 0.22, cx + r * 0.22, cy + r * 0.22],
                 fill=(255, 255, 255))


def globe(draw, cx, cy, r, fill):
    """Simple globe: circle + meridian/parallel lines."""
    draw.ellipse([cx - r, cy - r, cx + r, cy + r], fill=fill)
    draw.ellipse([cx - r, cy - r, cx + r, cy + r], outline=(255, 255, 255), width=3)
    # meridians
    for k in (-0.55, 0.0, 0.55):
        x0 = cx + k * r
        draw.arc([x0 - r * 0.45, cy - r, x0 + r * 0.45, cy + r], 270, 90,
                 fill=(255, 255, 255), width=2)
        draw.arc([x0 - r * 0.45, cy - r, x0 + r * 0.45, cy + r], 90, 270,
                 fill=(255, 255, 255), width=2)
    draw.line([cx - r, cy, cx + r, cy], fill=(255, 255, 255), width=2)
    draw.line([cx, cy - r, cx, cy + r], fill=(255, 255, 255), width=2)


def ship(draw, cx, cy, s, fill):
    """Simple cargo ship silhouette (hull + containers + smoke)."""
    # hull
    hull = [(cx - s, cy), (cx + s, cy), (cx + s * 0.75, cy + s * 0.45),
            (cx - s * 0.75, cy + s * 0.45)]
    draw.polygon(hull, fill=fill)
    # containers
    for i, dx in enumerate((-0.55, -0.15, 0.25)):
        x0 = cx + dx * s
        draw.rectangle([x0, cy - s * 0.55, x0 + s * 0.32, cy - s * 0.05],
                       fill=(255, 255, 255) if i % 2 == 0 else GOLD)
    # funnel
    draw.rectangle([cx + s * 0.55, cy - s * 0.75, cx + s * 0.78, cy - s * 0.05],
                   fill=fill)
    # smoke puffs
    for j, (dx, dy, r) in enumerate(((0.62, -0.95, 0.16), (0.78, -1.15, 0.20),
                                     (0.95, -1.35, 0.24))):
        draw.ellipse([cx + dx * s - r * s, cy + dy * s - r * s,
                      cx + dx * s + r * s, cy + dy * s + r * s],
                     fill=(120, 126, 134))


def med_cross(draw, cx, cy, r, fill):
    """Medical cross in a circle."""
    draw.ellipse([cx - r, cy - r, cx + r, cy + r], fill=fill)
    w = r * 0.28
    draw.rectangle([cx - w, cy - r * 0.62, cx + w, cy + r * 0.62],
                   fill=(255, 255, 255))
    draw.rectangle([cx - r * 0.62, cy - w, cx + r * 0.62, cy + w],
                   fill=(255, 255, 255))


def main():
    img = Image.new("RGB", (W, H), PAPER)
    d = ImageDraw.Draw(img)

    # ---------- masthead ----------
    d.rectangle([0, 0, W, 148], fill=NAVY)
    d.rectangle([0, 148, W, 156], fill=RED)
    f_title = font(SERIF_BOLD, 58)
    f_sub = font(BOLD, 26)
    draw_centered(d, W // 2, 22, "THE WORLD IN ONE DAY", f_title, (255, 255, 255))
    draw_centered(d, W // 2, 96, "SATURDAY  ·  21  NOVEMBER  2026", f_sub, (255, 214, 120))

    # ---------- lead story: Iran strikes Bahrain ----------
    # panel
    d.rounded_rectangle([28, 178, 996, 428], radius=18, fill=(255, 255, 255),
                        outline=(200, 196, 188), width=2)
    # left: flame graphic on dark panel
    d.rounded_rectangle([48, 198, 268, 408], radius=14, fill=(24, 28, 38))
    flame(d, 158, 300, 62)
    d.text((158, 372), "", font=font(REG, 10), fill=(255, 255, 255))
    # kicker + headline + deck
    f_kick = font(BOLD, 22)
    f_head = font(BOLD, 46)
    f_deck = font(REG, 24)
    x = 292
    d.text((x, 200), "MIDDLE EAST  •  LEAD STORY", font=f_kick, fill=RED)
    head_lines = wrap(d, "IRAN STRIKES BAHRAIN", f_head, 996 - x - 24)
    y = 232
    for ln in head_lines:
        d.text((x, y), ln, font=f_head, fill=INK)
        y += 52
    deck = ("Iran's Guards say they hit two US bases; Bahrain reports an "
            "industrial fire, no injuries, and air defences intercepting "
            "other attacks — as Gulf tensions flare.")
    y += 6
    for ln in wrap(d, deck, f_deck, 996 - x - 24):
        d.text((x, y), ln, font=f_deck, fill=(52, 58, 66))
        y += 30

    # ---------- four story cards (2 x 2) ----------
    cards = [
        ("MEXICO", RED, "EL CHAPO ISIDRO CAPTURED",
         "Mexican forces seize the FBI most-wanted cartel boss in Sinaloa; "
         "at least 11 dead in the violence that followed.", "star"),
        ("CLIMATE  •  ANTALYA", GREEN, "COP31 NEARS A DEAL",
         "Talks run past their deadline and close in on a final pact as "
         "nations wrestle over fossil fuels.", "globe"),
        ("WAR  •  EUROPE", STEEL, "RUSSIAN SHIP BURNS",
         "A drone strike sets the cargo ship Sparta II ablaze in the Gulf "
         "of Finland; missiles also land in Poland.", "ship"),
        ("HEALTH  •  BRAZIL", TEAL, "DENGUE BREAKTHROUGH",
         "Specially bred mosquitoes cut dengue in children by about 69% in "
         "a major Brazil study.", "cross"),
    ]
    cw, ch, gap = 472, 236, 24
    x0, y0 = 28, 452
    f_tag = font(BOLD, 19)
    f_card = font(BOLD, 30)
    f_body = font(REG, 21)
    for i, (tag, colour, head, body, icon) in enumerate(cards):
        cx = x0 + (i % 2) * (cw + gap)
        cy = y0 + (i // 2) * (ch + gap)
        d.rounded_rectangle([cx, cy, cx + cw, cy + ch], radius=16,
                            fill=CARD, outline=(200, 196, 188), width=2)
        # colour bar on top
        d.rounded_rectangle([cx, cy, cx + cw, cy + 10], radius=5, fill=colour)
        # icon
        ix, iy = cx + 52, cy + 78
        if icon == "star":
            badge_star(d, ix, iy, 34, colour)
        elif icon == "globe":
            globe(d, ix, iy, 34, colour)
        elif icon == "ship":
            ship(d, ix, iy, 30, colour)
        else:
            med_cross(d, ix, iy, 34, colour)
        # tag + headline + body
        tx = cx + 108
        d.text((tx, cy + 26), tag, font=f_tag, fill=colour)
        hy = cy + 52
        for ln in wrap(d, head, f_card, cw - 108 - 20):
            d.text((tx, hy), ln, font=f_card, fill=INK)
            hy += 36
        by = hy + 6
        for ln in wrap(d, body, f_body, cw - 108 - 20):
            d.text((tx, by), ln, font=f_body, fill=(52, 58, 66))
            by += 27

    # ---------- footer ----------
    f_foot = font(REG, 20)
    draw_centered(d, W // 2, 962,
                  "Sources: Reuters  ·  AP  ·  CNN  ·  AFP  —  21 November 2026",
                  f_foot, GREY)
    draw_centered(d, W // 2, 990,
                  "The day's world news, in one image.",
                  font(BOLD, 20), GREY)

    img.save(OUT, format="PNG")
    print(f"wrote {OUT}: {img.size[0]}x{img.size[1]}")


if __name__ == "__main__":
    main()
