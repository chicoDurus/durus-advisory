"""Print-ready Durus Advisory business cards, recreated from the approved mockup.

Output (in this folder):
  durus-business-card-print.pdf   2 pages (front, back), 91 x 61 mm = 85 x 55 mm card + 3 mm bleed on every side
  durus-business-card-front.pdf / -back.pdf   the same, one side per file
  preview-front.png / preview-back.png        trimmed previews at 600 dpi
  preview-guides.png                          both sides with trim (orange) and safe-area (blue) lines

Run: python3 make_cards.py   (needs Playwright + Chromium)
Edit the CARD dictionary below to change contact details.
"""
import asyncio
import math
import os

from playwright.async_api import async_playwright

HERE = os.path.dirname(os.path.abspath(__file__))
FONTS = "file://" + os.path.join(HERE, "fonts")

CARD = {
    "name": "TVRTKO AŠČIĆ",
    "title": "FOUNDER & PRINCIPAL",
    "email": "tvrtko@durusadvisory.com",
    "phone": "+357 96 420 889",
    "web": "durusadvisory.com",
    "place": "Limassol, Cyprus",
}

W, H, BLEED = 85.0, 55.0, 3.0           # mm
PW, PH = W + 2 * BLEED, H + 2 * BLEED   # page incl. bleed
BLACK, ORANGE, INK, GREY = "#0B0B0C", "#D96A2C", "#EDEAE4", "#BDB9B2"

LATIN = ("U+0000-00FF,U+0131,U+0152-0153,U+02BB-02BC,U+02C6,U+02DA,U+02DC,U+0304,U+0308,U+0329,"
         "U+2000-206F,U+20AC,U+2122,U+2191,U+2193,U+2212,U+2215,U+FEFF,U+FFFD")
LATIN_EXT = ("U+0100-02BA,U+02BD-02C5,U+02C7-02CC,U+02CE-02D7,U+02DD-02FF,U+0304,U+0308,U+0329,U+1D00-1DBF,"
             "U+1E00-1E9F,U+1EF2-1EFF,U+2020,U+20A0-20AB,U+20AD-20C0,U+2113,U+2C60-2C7F,U+A720-A7FF")

CSS = f"""
@font-face{{font-family:'Jost';font-weight:300;src:url({FONTS}/jost-latin-300-normal.woff2)}}
@font-face{{font-family:'Jost';font-weight:400;src:url({FONTS}/jost-latin-400-normal.woff2)}}
@font-face{{font-family:'Plex Mono';font-weight:400;src:url({FONTS}/ibm-plex-mono-latin-400-normal.woff2);unicode-range:{LATIN}}}
@font-face{{font-family:'Plex Mono';font-weight:400;src:url({FONTS}/ibm-plex-mono-latin-ext-400-normal.woff2);unicode-range:{LATIN_EXT}}}
@font-face{{font-family:'Plex Mono';font-weight:500;src:url({FONTS}/ibm-plex-mono-latin-500-normal.woff2);unicode-range:{LATIN}}}
@font-face{{font-family:'Plex Mono';font-weight:500;src:url({FONTS}/ibm-plex-mono-latin-ext-500-normal.woff2);unicode-range:{LATIN_EXT}}}
@font-face{{font-family:'Domine';font-weight:700;src:url({FONTS}/domine-latin-700-normal.woff2)}}
@page{{size:{PW}mm {PH}mm;margin:0}}
html,body{{margin:0;padding:0}}
body>svg{{display:block;width:{PW}mm;height:{PH}mm}}
"""

# Lucide icons (ISC licence), drawn on a 24-unit grid
ICONS = {
    "mail": '<rect width="20" height="16" x="2" y="4" rx="2"/><path d="m22 7-8.97 5.7a1.94 1.94 0 0 1-2.06 0L2 7"/>',
    "phone": '<path d="M22 16.92v3a2 2 0 0 1-2.18 2 19.79 19.79 0 0 1-8.63-3.07 19.5 19.5 0 0 1-6-6 19.79 19.79 0 0 1-3.07-8.67A2 2 0 0 1 4.11 2h3a2 2 0 0 1 2 1.72 12.84 12.84 0 0 0 .7 2.81 2 2 0 0 1-.45 2.11L8.09 9.91a16 16 0 0 0 6 6l1.27-1.27a2 2 0 0 1 2.11-.45 12.84 12.84 0 0 0 2.81.7A2 2 0 0 1 22 16.92z"/>',
    "globe": '<circle cx="12" cy="12" r="10"/><path d="M12 2a14.5 14.5 0 0 0 0 20 14.5 14.5 0 0 0 0-20"/><path d="M2 12h20"/>',
    "pin": '<path d="M20 10c0 4.993-5.539 10.193-7.399 11.799a1 1 0 0 1-1.202 0C9.539 20.193 4 14.993 4 10a8 8 0 0 1 16 0"/><circle cx="12" cy="10" r="3"/>',
}


def esc(s):
    return s.replace("&", "&amp;").replace("<", "&lt;")


def dots(cx, cy, r, spacing, dot_r, gaps=()):
    """Dotted circle; gaps = (centre_deg, half_width_deg) ranges left empty (0 deg = right, 90 = down)."""
    n = max(12, round(2 * math.pi * r / spacing))
    out = []
    for i in range(n):
        a = 360 * i / n
        if any(abs(((a - g + 180) % 360) - 180) < hw for g, hw in gaps):
            continue
        x, y = cx + r * math.cos(math.radians(a)), cy + r * math.sin(math.radians(a))
        out.append(f'<circle cx="{x:.3f}" cy="{y:.3f}" r="{dot_r}" fill="{ORANGE}"/>')
    return "".join(out)


def front():
    cx, cy = PW / 2, PH / 2
    gaps = ((-4.5, 18), (184.5, 18))   # leave the left and right open where DURUS crosses the ring
    rings = dots(cx, cy, 17.2, 1.32, 0.27, gaps) + dots(cx, cy, 14.8, 1.12, 0.21, gaps)
    return f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {PW} {PH}">
<rect width="{PW}" height="{PH}" fill="{BLACK}"/>
{rings}
<text x="{cx + 1.7}" y="{cy + 2.4}" text-anchor="middle" font-family="Jost" font-weight="400" font-size="10.6" letter-spacing="3.4" fill="{ORANGE}">DURUS</text>
<text x="{cx + 0.65}" y="{cy + 7.6}" text-anchor="middle" font-family="Jost" font-weight="300" font-size="2.35" letter-spacing="1.3" fill="{GREY}">ADVISORY</text>
</svg>"""


def back():
    x0 = BLEED + 9.0                       # left text column
    top = BLEED
    rows = [("mail", CARD["email"]), ("phone", CARD["phone"]), ("globe", CARD["web"]), ("pin", CARD["place"])]
    rows_svg = ""
    for i, (icon, text) in enumerate(rows):
        base = top + 28.6 + i * 5.0
        rows_svg += (f'<svg x="{x0 - 0.2}" y="{base - 2.75}" width="3.3" height="3.3" viewBox="0 0 24 24" fill="none" '
                     f'stroke="{ORANGE}" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round">{ICONS[icon]}</svg>')
        rows_svg += (f'<text x="{x0 + 5.6}" y="{base}" font-family="Plex Mono" font-weight="400" font-size="2.45" '
                     f'letter-spacing="0.06" fill="{INK}">{esc(text)}</text>')
    divider_x = BLEED + 56.5
    icx, icy = (divider_x + BLEED + W) / 2, top + 31.0
    icon = dots(icx, icy, 8.3, 0.95, 0.2) + dots(icx, icy, 7.0, 0.82, 0.16)
    return f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {PW} {PH}">
<rect width="{PW}" height="{PH}" fill="{BLACK}"/>
<text x="{x0}" y="{top + 14.2}" font-family="Plex Mono" font-weight="500" font-size="3.45" letter-spacing="0.62" fill="{ORANGE}">{esc(CARD['name'])}</text>
<text x="{x0}" y="{top + 18.9}" font-family="Plex Mono" font-weight="400" font-size="2.3" letter-spacing="0.32" fill="{INK}">{esc(CARD['title'])}</text>
<line x1="{x0}" y1="{top + 22.6}" x2="{x0 + 5.2}" y2="{top + 22.6}" stroke="{ORANGE}" stroke-width="0.4"/>
{rows_svg}
<line x1="{divider_x}" y1="{top + 8.5}" x2="{divider_x}" y2="{top + 49.5}" stroke="{ORANGE}" stroke-width="0.28"/>
{icon}
<text x="{icx}" y="{icy + 3.35}" text-anchor="middle" font-family="Domine" font-weight="700" font-size="9.4" fill="{ORANGE}">D</text>
</svg>"""


def page(svg):
    return f"<!doctype html><html><head><meta charset='utf-8'><style>{CSS}</style></head><body>{svg}</body></html>"


def guides(svg):
    t, s = BLEED, BLEED + 3.0
    overlay = (f'<rect x="{t}" y="{t}" width="{W}" height="{H}" fill="none" stroke="#FF7A00" stroke-width="0.15"/>'
               f'<rect x="{s}" y="{s}" width="{W - 6}" height="{H - 6}" fill="none" stroke="#3DA5FF" stroke-width="0.12" stroke-dasharray="0.8 0.6"/>')
    return svg.replace("</svg>", overlay + "</svg>")


async def main():
    sides = {"front": front(), "back": back()}
    async with async_playwright() as p:
        browser = await p.chromium.launch()
        pg = await browser.new_page()
        tmp = os.path.join(HERE, "_render.html")
        both = "<!doctype html><html><head><meta charset='utf-8'><style>" + CSS + \
               "body>svg{page-break-after:always}</style></head><body>" + sides["front"] + sides["back"] + "</body></html>"
        for name, html in [("durus-business-card-front.pdf", page(sides["front"])),
                           ("durus-business-card-back.pdf", page(sides["back"])),
                           ("durus-business-card-print.pdf", both)]:
            open(tmp, "w", encoding="utf-8").write(html)
            await pg.goto("file://" + tmp)
            await pg.evaluate("document.fonts.ready")
            await pg.wait_for_timeout(300)
            await pg.pdf(path=os.path.join(HERE, name), width=f"{PW}mm", height=f"{PH}mm",
                         print_background=True, margin={"top": "0", "right": "0", "bottom": "0", "left": "0"},
                         prefer_css_page_size=True)
        # previews: 600 dpi = 23.622 px/mm
        scale = 600 / 25.4
        for side, svg in sides.items():
            for name, content, clip in [(f"preview-{side}.png", svg, True), (f"_guide-{side}.png", guides(svg), False)]:
                open(tmp, "w", encoding="utf-8").write(page(content).replace(f"body>svg{{display:block;width:{PW}mm;height:{PH}mm}}",
                                                                             f"body>svg{{display:block;width:{PW * scale}px;height:{PH * scale}px}}"))
                await pg.set_viewport_size({"width": round(PW * scale), "height": round(PH * scale)})
                await pg.goto("file://" + tmp)
                await pg.evaluate("document.fonts.ready")
                await pg.wait_for_timeout(300)
                kw = {"clip": {"x": BLEED * scale, "y": BLEED * scale, "width": W * scale, "height": H * scale}} if clip else {}
                await pg.screenshot(path=os.path.join(HERE, name), **kw)
        os.remove(tmp)
        await browser.close()

    from PIL import Image
    a = Image.open(os.path.join(HERE, "_guide-front.png")); b = Image.open(os.path.join(HERE, "_guide-back.png"))
    sheet = Image.new("RGB", (a.width + b.width + 60, a.height), "#777")
    sheet.paste(a, (0, 0)); sheet.paste(b, (a.width + 60, 0))
    sheet.save(os.path.join(HERE, "preview-guides.png"))
    os.remove(os.path.join(HERE, "_guide-front.png")); os.remove(os.path.join(HERE, "_guide-back.png"))
    print("done")


if __name__ == "__main__":
    asyncio.run(main())
