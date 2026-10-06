"""Generate a 1200x630 share image for each blog post (site/assets/og/<slug>.png).

Run after adding or renaming a post, then run build.py:
    python3 src/og.py && python3 src/build.py
Needs Playwright with Chromium (pip install playwright && playwright install chromium).
"""
import asyncio
import html
import importlib.util
import os

from playwright.async_api import async_playwright

HERE = os.path.dirname(os.path.abspath(__file__))
spec = importlib.util.spec_from_file_location("build", os.path.join(HERE, "build.py"))
build = importlib.util.module_from_spec(spec)
spec.loader.exec_module(build)

SITE = build.SITE
OUT = os.path.join(SITE, "assets", "og")
FONTS = "file://" + os.path.join(SITE, "assets", "fonts")

BADGE = build.BADGE.replace(' id="brandLogo"', "").replace('class="brand-badge"', 'class="badge"')

TEMPLATE = """<!doctype html><html><head><meta charset="utf-8"><style>
@font-face{{font-family:'Archivo';font-weight:800;src:url({fonts}/archivo-latin-800-normal.woff2)}}
@font-face{{font-family:'Domine';font-weight:700;src:url({fonts}/domine-latin-700-normal.woff2)}}
@font-face{{font-family:'IBM Plex Mono';font-weight:500;src:url({fonts}/ibm-plex-mono-latin-500-normal.woff2)}}
html,body{{margin:0;width:1200px;height:630px;overflow:hidden;background:#0A0A0B}}
.cover{{position:absolute;right:0;top:0;width:780px;height:630px;object-fit:cover}}
.shade{{position:absolute;inset:0;background:linear-gradient(90deg,#0A0A0B 0%,#0A0A0B 40%,rgba(10,10,11,.88) 56%,rgba(10,10,11,.25) 100%)}}
.content{{position:absolute;left:64px;top:52px;bottom:58px;width:640px;display:flex;flex-direction:column}}
.badge{{width:150px;height:auto;margin-left:-22px}}
h1{{margin:auto 0;font-family:'Archivo';font-weight:800;color:#EDEAE4;font-size:58px;line-height:1.06;letter-spacing:-1px}}
.foot{{font-family:'IBM Plex Mono';font-weight:500;font-size:19px;letter-spacing:2px;text-transform:uppercase;color:#D96A2C}}
.bar{{position:absolute;left:0;right:0;bottom:0;height:8px;background:#D96A2C}}
</style></head><body>
<img class="cover" src="{cover}">
<div class="shade"></div>
<div class="content">{badge}<h1 id="t">{title}</h1><div class="foot">Blog · durusadvisory.com</div></div>
<div class="bar"></div>
<script>
  // Shrink the title until it fits the space between logo and footer.
  const t = document.getElementById('t'); let s = 58;
  while ((t.scrollHeight > 330 || t.scrollWidth > 640) && s > 34) {{ s -= 2; t.style.fontSize = s + 'px'; }}
</script>
</body></html>"""


async def main():
    os.makedirs(OUT, exist_ok=True)
    posts = build.load_posts()
    async with async_playwright() as p:
        browser = await p.chromium.launch()
        page = await browser.new_page(viewport={"width": 1200, "height": 630})
        for post in posts:
            cover = "file://" + os.path.join(SITE, "assets", "covers", post["cover"] + ".svg")
            tmp = os.path.join(OUT, "_render.html")
            with open(tmp, "w", encoding="utf-8") as fh:
                fh.write(TEMPLATE.format(fonts=FONTS, cover=cover, badge=BADGE, title=html.escape(post["title"])))
            await page.goto("file://" + tmp)
            await page.evaluate("document.fonts.ready")
            await page.wait_for_timeout(200)
            await page.screenshot(path=os.path.join(OUT, post["slug"] + ".png"))
            os.remove(tmp)
            print("og:", post["slug"])
        await browser.close()


if __name__ == "__main__":
    asyncio.run(main())
