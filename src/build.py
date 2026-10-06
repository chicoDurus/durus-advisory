"""Build the Durus Advisory site.

Every page goes through one layout (head, header, footer, scripts):
  src/pages/*.html      hand-written pages (front matter + HTML body)
  src/services/*.md     service pages
  src/posts/*.md        blog posts
  src/css/*.css         concatenated into site/assets/site.css
Output goes to site/, served by Vercel with clean URLs (/about -> about.html).

Run: python3 src/build.py   (needs: pip install markdown)
"""
import datetime as dt
import html
import json
import os
import re

import markdown

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SRC = os.path.join(ROOT, "src")
SITE = os.path.join(ROOT, "site")
BASE_URL = "https://www.durusadvisory.com"
TODAY = dt.date.today().isoformat()
CALENDLY = "https://calendly.com/durusadvisory"
EMAIL = "durus@durusadvisory.com"
LINKEDIN = "https://linkedin.com/company/durus-advisory"


BADGE = """<svg class="brand-badge" id="brandLogo" viewBox="0 0 950 500" xmlns="http://www.w3.org/2000/svg" aria-hidden="true">
        <path d="M 647.02 129.55 A 210 210 0 0 0 302.98 129.55" fill="none" stroke="#D96A2C" stroke-width="6" stroke-linecap="round" stroke-dasharray="0.1 16.699"/>
        <path d="M 611.36 135.58 A 178 178 0 0 0 338.64 135.58" fill="none" stroke="#D96A2C" stroke-width="5" stroke-linecap="round" stroke-dasharray="0.1 14.021"/>
        <path d="M 647.02 370.45 A 210 210 0 0 1 302.98 370.45" fill="none" stroke="#D96A2C" stroke-width="6" stroke-linecap="round" stroke-dasharray="0.1 16.699"/>
        <path d="M 611.36 364.42 A 178 178 0 0 1 338.64 364.42" fill="none" stroke="#D96A2C" stroke-width="5" stroke-linecap="round" stroke-dasharray="0.1 14.021"/>
        <text x="475" y="270" text-anchor="middle" font-family="Domine,Georgia,serif" font-weight="700" font-size="150" letter-spacing="30" fill="#D96A2C">DURUS</text>
        <text x="483" y="330" text-anchor="middle" font-family="'IBM Plex Mono',ui-monospace,Menlo,monospace" font-weight="500" font-size="42" letter-spacing="26" fill="#EDEAE4">ADVISORY</text>
      </svg>"""

NAV = [("services", "/services", "Services"), ("method", "/how-we-work", "How we work"),
       ("about", "/about", "About"), ("blog", "/blog", "Blog")]

ORG_LD = {"@context": "https://schema.org", "@type": "Organization", "name": "Durus Advisory",
          "url": BASE_URL + "/", "logo": BASE_URL + "/favicon-512.png", "email": EMAIL,
          "sameAs": [LINKEDIN], "description": "Product and strategy advisory for complex digital platforms."}


def esc(s):
    return html.escape(s, quote=True)


def front_matter(raw):
    m = re.match(r"---\n(.*?)\n---\n(.*)", raw, re.S)
    meta = {}
    for line in m.group(1).splitlines():
        k, v = line.split(":", 1)
        v = v.strip()
        if len(v) > 1 and v[0] == v[-1] == '"':
            v = v[1:-1]
        meta[k.strip()] = v
    return meta, m.group(2)


def md(text):
    out = markdown.markdown(text, extensions=["tables", "smarty"])
    return out.replace("<table>", '<div class="table-scroll"><table>').replace("</table>", "</table></div>")


# ---------- content loading ----------

def load_posts():
    posts = []
    folder = os.path.join(SRC, "posts")
    for name in sorted(os.listdir(folder)):
        if not name.endswith(".md"):
            continue
        meta, body = front_matter(open(os.path.join(folder, name), encoding="utf-8").read())
        meta["minutes"] = max(1, round(len(re.findall(r"\w+", body)) / 220))
        meta["date_obj"] = dt.date.fromisoformat(meta["date"])
        meta["date_h"] = meta["date_obj"].strftime("%-d %b %Y")
        meta["url"] = f"/blog/{meta['slug']}"
        meta["html"] = md(body)
        posts.append(meta)
    posts.sort(key=lambda p: p["date_obj"], reverse=True)
    return posts


def load_services():
    services = []
    folder = os.path.join(SRC, "services")
    for name in sorted(os.listdir(folder)):
        if name.endswith(".md"):
            meta, body = front_matter(open(os.path.join(folder, name), encoding="utf-8").read())
            meta["url"] = f"/services/{meta['slug']}"
            meta["html"] = md(body)
            meta["related"] = [s.strip() for s in meta.get("related", "").split(",") if s.strip()]
            services.append(meta)
    return services


# ---------- shared pieces ----------

def header(active):
    cur = ' aria-current="page"'
    links = "\n".join(
        f'      <a class="lnk" href="{href}"{cur if key == active else ""}>{label}</a>'
        for key, href, label in NAV)
    mobile = "\n".join(
        f'    <a href="{href}"{cur if key == active else ""}>{label}</a>'
        for key, href, label in NAV + [("contact", "/contact", "Contact")])
    return f"""<header class="nav">
  <div class="wrap nav-in">
    <a href="/" class="brand" aria-label="Durus Advisory home">
      {BADGE}
      <span class="visually-hidden">Durus Advisory</span>
    </a>
    <nav class="nav-links" aria-label="Primary">
{links}
      <a class="btn" href="{CALENDLY}" target="_blank" rel="noopener">Book a call <span class="arw" aria-hidden="true">↗</span></a>
      <button class="menu-btn" type="button" aria-expanded="false" aria-controls="mobileMenu" aria-label="Open menu"><span></span><span></span></button>
    </nav>
  </div>
  <div class="mobile-menu" id="mobileMenu" hidden>
{mobile}
  </div>
</header>"""


def footer():
    return f"""<footer>
  <div class="wrap foot-in">
    <span>© {dt.date.today().year} Durus Advisory</span>
    <div class="foot-links">
      <a href="/services">Services</a>
      <a href="/how-we-work">How we work</a>
      <a href="/about">About</a>
      <a href="/blog">Blog</a>
      <a href="/contact">Contact</a>
      <a href="{LINKEDIN}" target="_blank" rel="noopener">LinkedIn</a>
    </div>
  </div>
</footer>"""


CTA = f"""  <section class="cta-band" id="contact">
    <div class="wrap cta-in reveal">
      <span class="eyebrow" style="display:block;margin-bottom:22px">Get in touch</span>
      <h2>Got a product that's drifting, or a roadmap stalled between strategy and delivery?</h2>
      <p>Send us a note. We'll tell you straight whether we can help.</p>
      <div class="row">
        <a class="btn" href="{CALENDLY}" target="_blank" rel="noopener">Book a call <span class="arw" aria-hidden="true">↗</span></a>
        <a class="btn ghost email" href="mailto:{EMAIL}">{EMAIL}</a>
      </div>
    </div>
  </section>"""

INTRO_HEAD = """<script>
  /* Play the logo intro once per browser session, unless motion is reduced. */
  (function(){
    try{
      var reduce = window.matchMedia && window.matchMedia('(prefers-reduced-motion: reduce)').matches;
      if(!reduce && !sessionStorage.getItem('durusIntroSeen')) document.documentElement.classList.add('intro-on');
    }catch(e){}
  })();
</script>"""

INTRO_JS = '\n<script src="/assets/intro.js"></script>'

INTRO_BODY = """<div class="intro" id="intro" aria-hidden="true">
  <svg class="intro-logo" id="introLogo" viewBox="0 0 950 500"></svg>
  <button class="intro-skip" id="introSkip" type="button">Skip intro</button>
</div>"""


def layout(*, path, title, description, body, active="", intro=False, cta=True,
           og_type="website", ld=None, extra_head="", og_image="/og-image.png"):
    url = BASE_URL + path
    lds = "".join(f'\n<script type="application/ld+json">{json.dumps(x, ensure_ascii=False)}</script>' for x in (ld or []))
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8" />
<meta name="viewport" content="width=device-width, initial-scale=1.0" />
<title>{esc(title)}</title>
<meta name="description" content="{esc(description)}" />
<link rel="canonical" href="{url}" />
<meta property="og:title" content="{esc(title)}" />
<meta property="og:description" content="{esc(description)}" />
<meta property="og:type" content="{og_type}" />
<meta property="og:url" content="{url}" />
<meta property="og:image" content="{BASE_URL}{og_image}" />
<meta property="og:image:width" content="1200" />
<meta property="og:image:height" content="630" />
<meta name="twitter:card" content="summary_large_image" />{extra_head}
<link rel="icon" href="/favicon.ico" sizes="48x48">
<link rel="icon" href="/favicon.svg" type="image/svg+xml">
<link rel="icon" href="/favicon-96.png" type="image/png" sizes="96x96">
<link rel="apple-touch-icon" href="/apple-touch-icon.png">
<link rel="manifest" href="/site.webmanifest">
<meta name="theme-color" content="#0A0A0B">
<link rel="preload" href="/assets/fonts/ibm-plex-sans-latin-400-normal.woff2" as="font" type="font/woff2" crossorigin>
<link rel="preload" href="/assets/fonts/archivo-latin-800-normal.woff2" as="font" type="font/woff2" crossorigin>
<link rel="preload" href="/assets/fonts/domine-latin-700-normal.woff2" as="font" type="font/woff2" crossorigin>
<link rel="stylesheet" href="/assets/site.css">{lds}
{INTRO_HEAD if intro else ""}
</head>
<body>
{INTRO_BODY if intro else ""}
{header(active)}

<main id="top">
{body}
{CTA if cta else ""}
</main>

{footer()}

<script src="/assets/logo.js"></script>
<script src="/assets/site.js"></script>{INTRO_JS if intro else ""}
</body>
</html>
"""


# ---------- snippets ----------

def service_cards(services):
    cards = "\n".join(f"""        <a class="offer" href="{s['url']}">
          <h3>{esc(s['title'])}</h3>
          <p>{esc(s['card'])}</p>
          <span class="offer-who">{esc(s['who'])}</span>
          <span class="offer-more">Learn more →</span>
        </a>""" for s in services)
    return f'      <div class="offer-grid reveal">\n{cards}\n      </div>'


ENGAGEMENTS = """      <div class="engage-grid reveal">
        <div class="engage">
          <span class="fmt">Fixed scope</span>
          <h3>Product &amp; platform audit</h3>
          <p>A close look at the product, the data and the delivery, ending in a ranked plan of what to fix first and what each problem costs.</p>
          <div class="meta">2 to 4 weeks · fixed fee</div>
        </div>
        <div class="engage">
          <span class="fmt">Ongoing</span>
          <h3>Fractional product leadership</h3>
          <p>An experienced product lead embedded in your team, owning the roadmap and accountable for business results.</p>
          <div class="meta">2 to 3 days a week · rolling monthly</div>
        </div>
        <div class="engage">
          <span class="fmt">Light touch</span>
          <h3>Leadership advisory</h3>
          <p>A senior sounding board for founders and product leaders: roadmap reviews, big decisions, and hiring the right product people.</p>
          <div class="meta">A few sessions a month</div>
        </div>
      </div>"""


def post_card(p, featured=False, eager=False):
    cls = "post-card featured" if featured else "post-card"
    loading = "" if eager else ' loading="lazy"'
    return f"""        <a class="{cls}" href="{p['url']}">
          <div class="pc-media">
            <img src="/assets/covers/{p['cover']}.svg" alt=""{loading}>
            <div class="pc-title">
              <span class="pc-meta">{p['date_h']} · {p['minutes']} min</span>
              <h3>{esc(p['title'])}</h3>
            </div>
            <div class="pc-desc" aria-hidden="true">
              <p>{esc(p['excerpt'])}</p>
              <span class="pc-read">Read the post →</span>
            </div>
          </div>
          <p class="pc-touch">{esc(p['excerpt'])}</p>
        </a>"""


def link_card(kicker, title, text, href):
    t = f"<p>{esc(text)}</p>" if text else ""
    return f"""        <a class="link-card" href="{href}"><span class="k">{esc(kicker)}</span><h3>{esc(title)}</h3>{t}</a>"""


# ---------- page builders ----------

def post_page(p, newer, older):
    og = f"/assets/og/{p['slug']}.png" if os.path.exists(os.path.join(SITE, "assets", "og", p["slug"] + ".png")) else "/og-image.png"
    ld = [{"@context": "https://schema.org", "@type": "BlogPosting", "headline": p["title"],
           "description": p["excerpt"], "datePublished": p["date"], "dateModified": p["date"],
           "author": {"@type": "Organization", "name": "Durus Advisory", "url": BASE_URL},
           "publisher": {"@type": "Organization", "name": "Durus Advisory", "url": BASE_URL},
           "mainEntityOfPage": BASE_URL + p["url"], "image": BASE_URL + og}]
    related = [x for x in (older, newer) if x]
    more = ""
    if related:
        cards = "".join(f"""<a class="more-card" href="{x['url']}">
        <img src="/assets/covers/{x['cover']}.svg" alt="" loading="lazy">
        <div><span class="k">{x['date_h']}</span><h3>{esc(x['title'])}</h3></div>
      </a>""" for x in related)
        more = f"""  <section class="more">
    <div class="wrap">
      <h2>Keep reading</h2>
      <div class="more-grid">{cards}</div>
    </div>
  </section>"""
    body = f"""  <article>
    <header class="post-head wrap">
      <a class="back" href="/blog"><span aria-hidden="true">←</span> All posts</a>
      <h1>{esc(p['title'])}</h1>
      <div class="post-meta">
        <time datetime="{p['date']}"><b>{p['date_h']}</b></time>
        <span>{p['minutes']} min read</span>
      </div>
      <p class="post-lede">{esc(p['excerpt'])}</p>
    </header>
    <figure class="post-cover wrap">
      <img src="/assets/covers/{p['cover']}.svg" alt="" width="1600" height="1000">
    </figure>
    <div class="post-body">
{p['html']}
    </div>
  </article>

{more}"""
    return layout(path=p["url"], title=f"{p['title']} | Durus Advisory", description=p["excerpt"],
                  body=body, active="blog", og_type="article", ld=ld, og_image=og,
                  extra_head=f'\n<meta property="article:published_time" content="{p["date"]}" />')


def service_page(s, services, posts_by_slug):
    reading = [posts_by_slug[x] for x in s["related"] if x in posts_by_slug]
    reading_html = ""
    if reading:
        cards = "\n".join(link_card(p["date_h"], p["title"], "", p["url"]) for p in reading)
        reading_html = f"""  <section class="tight">
    <div class="wrap">
      <div class="sec-head"><h2>Further reading.</h2></div>
      <div class="link-grid">
{cards}
      </div>
    </div>
  </section>"""
    others = "\n".join(link_card("Service", o["title"], o["who"], o["url"]) for o in services if o is not s)
    body = f"""  <header class="page-head wrap">
    <a class="back" href="/services"><span aria-hidden="true">←</span> All services</a>
    <span class="eyebrow">{esc(s['title'])}</span>
    <h1>{esc(s['h1'])}</h1>
    <p class="page-lede">{esc(s['lede'])}</p>
    <div class="page-cta">
      <a class="btn" href="{CALENDLY}" target="_blank" rel="noopener">Book a call <span class="arw" aria-hidden="true">↗</span></a>
      <a class="btn ghost" href="/how-we-work">How we work</a>
    </div>
  </header>

  <hr class="divider"/>

  <section class="tight">
    <div class="post-body page-body">
{s['html']}
    </div>
  </section>

{reading_html}

  <section class="tight">
    <div class="wrap">
      <div class="sec-head"><h2>Other services.</h2></div>
      <div class="link-grid">
{others}
      </div>
    </div>
  </section>
"""
    ld = [{"@context": "https://schema.org", "@type": "Service", "name": s["title"], "description": s["description"],
           "provider": {"@type": "Organization", "name": "Durus Advisory", "url": BASE_URL}, "areaServed": "Europe",
           "url": BASE_URL + s["url"]}]
    return layout(path=s["url"], title=f"{s['title']} | Durus Advisory", description=s["description"],
                  body=body, active="services", ld=ld)


def write(rel, content):
    out = os.path.join(SITE, rel)
    os.makedirs(os.path.dirname(out), exist_ok=True)
    with open(out, "w", encoding="utf-8") as fh:
        fh.write(content)


def main():
    posts = load_posts()
    services = load_services()
    posts_by_slug = {p["slug"]: p for p in posts}
    sitemap = []

    # stylesheet
    css = "".join(open(os.path.join(SRC, "css", f), encoding="utf-8").read() for f in ("fonts.css", "base.css", "article.css", "pages.css"))
    write("assets/site.css", "/* Generated by src/build.py from src/css/. Edit those files, not this one. */\n" + css)

    snippets = {
        "{{SERVICE_CARDS}}": service_cards(services),
        "{{ENGAGEMENTS}}": ENGAGEMENTS,
        "{{LATEST_POSTS}}": '      <div class="posts latest reveal">\n' + "\n".join(post_card(p) for p in posts[:3]) + "\n      </div>",
        "{{ALL_POSTS}}": '      <div class="posts">\n' + "\n".join(post_card(p, i == 0, i < 4) for i, p in enumerate(posts)) + "\n      </div>",
    }

    # hand-written pages
    for name in sorted(os.listdir(os.path.join(SRC, "pages"))):
        meta, body = front_matter(open(os.path.join(SRC, "pages", name), encoding="utf-8").read())
        for k, v in snippets.items():
            body = body.replace(k, v)
        path = meta["path"]
        ld = [ORG_LD] if path == "/" else None
        page = layout(path=path, title=meta["title"], description=meta["description"], body=body,
                      active=meta.get("nav", ""), intro=meta.get("intro") == "yes", cta=meta.get("cta") != "no", ld=ld)
        write("index.html" if path == "/" else path.strip("/") + ".html", page)
        if meta.get("sitemap") != "no":
            sitemap.append((BASE_URL + (path if path != "/" else "/"), TODAY))

    # services
    for s in services:
        write(f"services/{s['slug']}.html", service_page(s, services, posts_by_slug))
        sitemap.append((BASE_URL + s["url"], TODAY))

    # posts
    for i, p in enumerate(posts):
        newer = posts[i - 1] if i > 0 else None
        older = posts[i + 1] if i + 1 < len(posts) else None
        write(f"blog/{p['slug']}.html", post_page(p, newer, older))
        sitemap.append((BASE_URL + p["url"], p["date"]))

    urls = "".join(f"<url><loc>{u}</loc><lastmod>{d}</lastmod></url>" for u, d in sitemap)
    write("sitemap.xml", f'<?xml version="1.0" encoding="UTF-8"?><urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">{urls}</urlset>\n')
    print(f"built {len(sitemap)} pages ({len(services)} services, {len(posts)} posts)")


if __name__ == "__main__":
    main()
