"""LinkedIn company page assets: cover 1128x191 (exported at 2x) and logo 400x400."""
import pathlib, asyncio
from playwright.async_api import async_playwright
ROOT = pathlib.Path(__file__).resolve().parents[2]
OUT = pathlib.Path(__file__).parent
logo = (ROOT/'brand/durus-logo-light-text.svg').read_text()
fonts = (ROOT/'site/assets/fonts').as_uri()
W, H = 1128*2, 191*2
html = f"""<!doctype html><html><head><style>
@font-face{{font-family:Mono;src:url({fonts}/ibm-plex-mono-latin-400-normal.woff2)}}
html,body{{margin:0;width:{W}px;height:{H}px;background:#0A0A0B;overflow:hidden}}
.logo{{position:absolute;left:50%;top:50%;transform:translate(-50%,-50%);height:{H-24}px}}
.logo svg{{height:100%;width:auto;display:block}}
.tag{{position:absolute;right:120px;top:50%;transform:translateY(-50%);font-family:Mono;
 color:#EDEAE4;opacity:.72;font-size:25px;letter-spacing:.14em;text-transform:uppercase;line-height:1.75;text-align:right}}
.tag b{{color:#D96A2C;font-weight:400}}
.rule{{position:absolute;right:120px;top:calc(50% + 66px);width:60px;height:3px;background:#D96A2C}}
</style></head><body>
<div class="logo">{logo}</div>
<div class="tag">Product leadership for<br>complex digital platforms</div>
<div class="rule"></div>
</body></html>"""
async def main():
    async with async_playwright() as p:
        b = await p.chromium.launch()
        pg = await b.new_page(viewport={'width':W,'height':H})
        f = OUT/'_cover.html'; f.write_text(html)
        await pg.goto(f.as_uri()); await pg.wait_for_timeout(400)
        await pg.screenshot(path=str(OUT/'durus-linkedin-cover-2256x382.png'))
        f.unlink(); await b.close()
asyncio.run(main())
from PIL import Image
im = Image.open(ROOT/'brand/durus-icon-square-1024.png').convert('RGB')
im.resize((400,400), Image.LANCZOS).save(OUT/'durus-linkedin-logo-400.png')
# preview simulating the company page header, with the logo overlapping bottom-left
c = Image.open(OUT/'durus-linkedin-cover-2256x382.png').convert('RGB').resize((1128,191), Image.LANCZOS)
pv = Image.new('RGB',(1128,330),(243,242,239)); pv.paste(c,(0,0))
lg = im.resize((176,176), Image.LANCZOS); pv.paste(Image.new('RGB',(184,184),'white'),(32,108)); pv.paste(lg,(36,112))
pv.save(OUT/'_preview.png')
