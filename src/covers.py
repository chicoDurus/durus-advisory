"""Generate the blog cover artworks (1600x1000 SVG). Each cover is a distinct
composition tied to its post; shared palette with the Durus site."""
import math, random, os, sys

W, H = 1600, 1000
INK, INK2, INK3 = "#0A0A0B", "#131316", "#191A1E"
LINE, LINE2 = "#25252A", "#33333A"
FG, FG2, MUT = "#EDEAE4", "#B8B4AB", "#8A8781"
OC, OCD, OCL = "#D96A2C", "#B85422", "#E8874F"

OUT = sys.argv[1] if len(sys.argv) > 1 else "covers"
os.makedirs(OUT, exist_ok=True)


def svg(body, bg):
    return (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" '
            f'preserveAspectRatio="xMidYMid slice">'
            f'<rect width="{W}" height="{H}" fill="{bg}"/>{body}</svg>')


def grid(step, color, op, w=1, dash=None):
    d = f' stroke-dasharray="{dash}"' if dash else ""
    s = "".join(f'<line x1="{x}" y1="0" x2="{x}" y2="{H}"/>' for x in range(step, W, step))
    s += "".join(f'<line x1="0" y1="{y}" x2="{W}" y2="{y}"/>' for y in range(step, H, step))
    return f'<g stroke="{color}" stroke-opacity="{op}" stroke-width="{w}"{d}>{s}</g>'


def f(v):
    return f"{v:.1f}"


# 1 — Gantt: project management
def gantt():
    r = random.Random(1)
    b = grid(100, FG, 0.05)
    rows, crit = 10, {0, 2, 3, 5, 7, 9}
    x, prev = 230, None
    for i in range(rows):
        y = 170 + i * 68
        w = r.randint(140, 330)
        start = x if i in crit else r.randint(200, 1200)
        if i in crit:
            if prev:
                px, py = prev
                b += (f'<path d="M{px} {py+15} H{px+20} V{y+15} H{start}" fill="none" stroke="{OC}" '
                      f'stroke-width="2" stroke-opacity=".7"/>')
            b += f'<rect x="{start}" y="{y}" width="{w}" height="30" fill="{OC}"/>'
            prev = (start + w, y)
            x = start + w + r.randint(20, 60)
        else:
            b += f'<rect x="{start}" y="{y}" width="{w}" height="30" fill="{LINE2}"/>'
            b += f'<rect x="{start}" y="{y}" width="{int(w*r.uniform(.2,.9))}" height="30" fill="{MUT}" fill-opacity=".35"/>'
    b += f'<line x1="980" y1="120" x2="980" y2="880" stroke="{FG}" stroke-width="2" stroke-dasharray="6 8" stroke-opacity=".6"/>'
    b += f'<circle cx="980" cy="120" r="7" fill="{FG}"/>'
    return svg(b, INK2)


# 2 — Frameworks: waterfall steps vs iterative loops
def frameworks():
    b = ""
    for i in range(5):
        x, y = 180 + i * 105, 210 + i * 125
        fill = OC if i == 4 else LINE2
        b += f'<rect x="{x}" y="{y}" width="230" height="70" fill="{fill}"/>'
        if i < 4:
            b += (f'<path d="M{x+190} {y+70} V{y+108} H{x+215}" fill="none" stroke="{FG2}" '
                  f'stroke-width="2" stroke-opacity=".6"/>')
    b += f'<line x1="830" y1="120" x2="830" y2="880" stroke="{FG}" stroke-opacity=".12" stroke-width="2" stroke-dasharray="4 10"/>'
    for i, (cx, op) in enumerate([(1010, .35), (1170, .6), (1330, 1)]):
        col = OC if i == 2 else FG
        b += (f'<circle cx="{cx}" cy="500" r="150" fill="none" stroke="{col}" stroke-opacity="{op}" '
              f'stroke-width="5" stroke-dasharray="860 82" transform="rotate(-70 {cx} 500)"/>')
        ax = cx + 150 * math.cos(math.radians(-70 + 360 * 860 / 942))
        ay = 500 + 150 * math.sin(math.radians(-70 + 360 * 860 / 942))
        b += f'<circle cx="{f(ax)}" cy="{f(ay)}" r="10" fill="{col}" fill-opacity="{op}"/>'
    return svg(b, INK)


# 3 — Do you need Scrum: sticky-note grid, mostly empty, on ochre
def question():
    r = random.Random(3)
    b = ""
    cols, rows, s, g = 9, 5, 120, 26
    x0 = (W - (cols * s + (cols - 1) * g)) / 2
    y0 = (H - (rows * s + (rows - 1) * g)) / 2
    for i in range(cols):
        for j in range(rows):
            x, y = x0 + i * (s + g), y0 + j * (s + g)
            k = r.random()
            if k < .22:
                b += f'<rect x="{f(x)}" y="{f(y)}" width="{s}" height="{s}" fill="{INK}" fill-opacity=".9"/>'
            elif k < .45:
                b += f'<rect x="{f(x)}" y="{f(y)}" width="{s}" height="{s}" fill="{INK}" fill-opacity=".14"/>'
            else:
                b += (f'<rect x="{f(x+1.5)}" y="{f(y+1.5)}" width="{s-3}" height="{s-3}" fill="none" '
                      f'stroke="{INK}" stroke-opacity=".28" stroke-width="3" stroke-dasharray="10 8"/>')
    b += (f'<text x="800" y="760" text-anchor="middle" font-family="Georgia, \'Times New Roman\', serif" '
          f'font-weight="700" font-size="680" fill="{FG}">?</text>')
    return svg(b, OC)


# 4 — Case study: scattered cards resolving into an ordered board
def chaos():
    r = random.Random(4)
    b = ""
    for _ in range(46):
        x, y = r.uniform(110, 720), r.uniform(120, 860)
        a = r.uniform(-50, 50)
        fill = OC if r.random() < .12 else (LINE2 if r.random() < .6 else MUT)
        op = r.uniform(.35, .9)
        b += (f'<rect x="{f(x)}" y="{f(y)}" width="110" height="64" fill="{fill}" fill-opacity="{f(op)}" '
              f'transform="rotate({f(a)} {f(x+55)} {f(y+32)})"/>')
    heights = [5, 3, 4, 6]
    for c in range(4):
        x = 900 + c * 150
        b += f'<line x1="{x}" y1="180" x2="{x+120}" y2="180" stroke="{FG}" stroke-opacity=".35" stroke-width="3"/>'
        for k in range(heights[c]):
            fill = OC if c == 3 else LINE2
            b += f'<rect x="{x}" y="{210 + k*82}" width="120" height="66" fill="{fill}"/>'
    b += f'<path d="M760 500 H850" stroke="{FG}" stroke-opacity=".5" stroke-width="3"/>'
    b += f'<path d="M836 486 L852 500 L836 514" fill="none" stroke="{FG}" stroke-opacity=".5" stroke-width="3"/>'
    return svg(b, INK)


# 5 — Meetings: a week view, meetings struck out, focus blocks in ochre
def calendar():
    r = random.Random(5)
    b = ""
    x0, cw, gap, top, rh = 220, 210, 30, 190, 66
    for d in range(5):
        x = x0 + d * (cw + gap)
        b += f'<rect x="{x}" y="130" width="{cw}" height="22" fill="{FG}" fill-opacity=".14"/>'
        b += f'<line x1="{x}" y1="{top}" x2="{x}" y2="{top+rh*10}" stroke="{FG}" stroke-opacity=".06" stroke-width="2"/>'
        h = 0
        while h < 10:
            span = r.choice([1, 1, 1, 2, 2, 3])
            span = min(span, 10 - h)
            y = top + h * rh
            k = r.random()
            if k < .2:
                b += f'<rect x="{x+6}" y="{y+5}" width="{cw-12}" height="{span*rh-10}" fill="{OC}"/>'
            elif k < .78:
                b += f'<rect x="{x+6}" y="{y+5}" width="{cw-12}" height="{span*rh-10}" fill="{LINE2}"/>'
                if r.random() < .35:
                    b += (f'<line x1="{x+18}" y1="{y+span*rh/2}" x2="{x+cw-18}" y2="{y+span*rh/2}" '
                          f'stroke="{FG2}" stroke-width="3" stroke-opacity=".7"/>')
            h += span
    return svg(b, INK2)


# 6 — Documentation: a stack of pages
def documents():
    r = random.Random(6)
    b = ""
    for i, a in enumerate([-11, -5, 3]):
        b += (f'<rect x="540" y="160" width="520" height="680" fill="{INK3}" stroke="{LINE2}" stroke-width="2" '
              f'transform="rotate({a} 800 500)" fill-opacity="{.6 + i*.15}"/>')
    g = f'<g transform="rotate(8 800 500)"><rect x="540" y="160" width="520" height="680" fill="#1E1F24" stroke="{LINE2}" stroke-width="2"/>'
    g += f'<rect x="590" y="215" width="290" height="26" fill="{OC}"/>'
    y = 280
    for blk in range(4):
        for _ in range(r.randint(2, 4)):
            g += f'<rect x="590" y="{y}" width="{r.randint(250, 420)}" height="9" fill="{FG}" fill-opacity=".22"/>'
            y += 26
        y += 18
        if blk < 3:
            g += f'<rect x="590" y="{y}" width="{r.randint(120, 200)}" height="14" fill="{FG}" fill-opacity=".55"/>'
            y += 34
    for k in range(3):
        g += f'<rect x="590" y="{y + k*30}" width="16" height="16" fill="none" stroke="{OC}" stroke-width="2.5"/>'
        g += f'<rect x="620" y="{y + k*30 + 4}" width="{r.randint(150, 300)}" height="9" fill="{FG}" fill-opacity=".22"/>'
    g += "</g>"
    return svg(b + g, INK)


# 7 — Launch: a dotted trajectory through stage markers to a burst
def launch():
    b = f'<line x1="0" y1="880" x2="{W}" y2="880" stroke="{FG}" stroke-opacity=".12" stroke-width="2"/>'
    p0, p1, p2 = (150, 880), (900, 860), (1380, 230)
    def bez(t):
        x = (1-t)**2*p0[0] + 2*(1-t)*t*p1[0] + t*t*p2[0]
        y = (1-t)**2*p0[1] + 2*(1-t)*t*p1[1] + t*t*p2[1]
        return x, y
    for i in range(70):
        t = i / 69
        x, y = bez(t)
        b += f'<circle cx="{f(x)}" cy="{f(y)}" r="{f(2 + 3*t)}" fill="{FG}" fill-opacity="{f(.25 + .5*t)}"/>'
    for t in (.18, .38, .58, .76):
        x, y = bez(t)
        b += f'<circle cx="{f(x)}" cy="{f(y)}" r="16" fill="{INK3}" stroke="{OC}" stroke-width="4"/>'
    cx, cy = p2
    for ring, n in ((60, 16), (100, 22), (145, 30)):
        for k in range(n):
            a = 2 * math.pi * k / n
            b += f'<circle cx="{f(cx + ring*math.cos(a))}" cy="{f(cy + ring*math.sin(a))}" r="{f(5 - ring/50)}" fill="{OC}" fill-opacity="{f(1.1 - ring/160)}"/>'
    b += f'<circle cx="{cx}" cy="{cy}" r="30" fill="{OC}"/>'
    return svg(b, INK3)


# 8 — Busy: frantic activity lines over one flat ochre metric
def busy():
    r = random.Random(8)
    b = ""
    for s in range(6):
        pts, y = [], 400 + r.uniform(-60, 60)
        for i in range(260):
            x = 120 + i * 1360 / 259
            y += r.uniform(-38, 38)
            y = max(200, min(600, y + (400 - y) * .08))
            pts.append(f"{f(x)},{f(y)}")
        col = FG if s == 0 else MUT
        b += (f'<polyline points="{" ".join(pts)}" fill="none" stroke="{col}" stroke-opacity="{.22 + .08*s}" '
              f'stroke-width="2" stroke-linejoin="round"/>')
    b += f'<line x1="120" y1="720" x2="1480" y2="720" stroke="{OC}" stroke-width="7" stroke-linecap="round"/>'
    b += f'<circle cx="1480" cy="720" r="14" fill="{OC}"/>'
    b += f'<line x1="120" y1="770" x2="1480" y2="770" stroke="{FG}" stroke-opacity=".1" stroke-width="2"/>'
    return svg(b, INK)


# 9 — Roadmap: confident start, dissolving into hollow, dashed milestones (light)
def roadmap():
    r = random.Random(9)
    b = grid(80, INK, .05)
    for lane, y in enumerate((300, 380, 620, 700)):
        x = 160
        while x < 1400:
            w = r.randint(120, 260)
            fade = max(.05, .55 - (x - 160) / 1400 * .7)
            b += f'<rect x="{x}" y="{y}" width="{w}" height="34" fill="{INK}" fill-opacity="{f(fade)}"/>'
            x += w + r.randint(30, 70)
    b += f'<line x1="140" y1="500" x2="560" y2="500" stroke="{INK}" stroke-width="6"/>'
    b += f'<line x1="560" y1="500" x2="1460" y2="500" stroke="{INK}" stroke-width="6" stroke-dasharray="18 16" stroke-opacity=".35"/>'
    for i, x in enumerate(range(200, 1461, 180)):
        if x < 560:
            b += f'<rect x="{x-17}" y="483" width="34" height="34" fill="{INK}" transform="rotate(45 {x} 500)"/>'
        else:
            op = max(.12, .8 - (x - 560) / 1100)
            b += (f'<rect x="{x-17}" y="483" width="34" height="34" fill="{FG}" stroke="{INK}" stroke-width="4" '
                  f'stroke-opacity="{f(op)}" transform="rotate(45 {x} 500)"/>')
    b += f'<line x1="560" y1="200" x2="560" y2="800" stroke="{OC}" stroke-width="5"/>'
    b += f'<circle cx="560" cy="500" r="16" fill="{OC}"/>'
    return svg(b, FG)


# 10 — Fracture: a solid block shattered into separating shards
def fracture():
    r = random.Random(17)
    C = (800, 500)
    def split(poly, p, d):
        a, bb = [], []
        n = (-d[1], d[0])
        side = lambda q: (q[0]-p[0])*n[0] + (q[1]-p[1])*n[1]
        for i in range(len(poly)):
            P, Q = poly[i], poly[(i+1) % len(poly)]
            sp, sq = side(P), side(Q)
            (a if sp >= 0 else bb).append(P)
            if (sp >= 0) != (sq >= 0):
                t = sp / (sp - sq)
                I = (P[0] + t*(Q[0]-P[0]), P[1] + t*(Q[1]-P[1]))
                a.append(I); bb.append(I)
        return [s for s in (a, bb) if len(s) >= 3]
    shards = [[(450, 150), (1150, 150), (1150, 850), (450, 850)]]
    for _ in range(7):
        ang = r.uniform(0, math.pi)
        p = (C[0] + r.uniform(-140, 140), C[1] + r.uniform(-140, 140))
        d = (math.cos(ang), math.sin(ang))
        new = []
        for s in shards:
            new += split(s, p, d)
        shards = new
    b = ""
    cols = [OC, OCD, OCL, OC, "#C85E26"]
    for i, s in enumerate(shards):
        cx = sum(q[0] for q in s) / len(s); cy = sum(q[1] for q in s) / len(s)
        vx, vy = cx - C[0], cy - C[1]
        dist = math.hypot(vx, vy) or 1
        k = .16 + dist / 2200
        tx, ty = vx * k + vx / dist * 14, vy * k + vy / dist * 14
        rot = r.uniform(-4, 4) * dist / 350
        pts = " ".join(f"{f(q[0])},{f(q[1])}" for q in s)
        b += (f'<polygon points="{pts}" fill="{cols[i % len(cols)]}" stroke="{FG}" stroke-opacity=".25" stroke-width="1.5" '
              f'transform="translate({f(tx)} {f(ty)}) rotate({f(rot)} {f(cx)} {f(cy)})"/>')
    return svg(b, INK)


# 11 — The gap: strategy and delivery as two monoliths, value falling between
def gap():
    r = random.Random(11)
    b = f'<rect x="150" y="230" width="560" height="770" fill="{FG}"/>'
    b += f'<rect x="890" y="300" width="560" height="700" fill="{OC}"/>'
    b += f'<line x1="710" y1="300" x2="790" y2="300" stroke="{FG2}" stroke-width="4" stroke-dasharray="14 10"/>'
    for i in range(40):
        y = 320 + i * 17 + r.uniform(-6, 6)
        x = 800 + r.uniform(-50, 50) * (1 + i / 40)
        b += f'<circle cx="{f(x)}" cy="{f(y)}" r="{f(max(1.2, 6 - i*0.12))}" fill="{FG}" fill-opacity="{f(max(.06, .9 - i*.022))}"/>'
    for k in range(6):
        b += f'<rect x="200" y="{290 + k*46}" width="{[380,300,420,260,340,200][k]}" height="12" fill="{INK}" fill-opacity=".18"/>'
    for k in range(4):
        b += f'<rect x="940" y="{360 + k*90}" width="460" height="60" fill="{INK}" fill-opacity=".14"/>'
    return svg(b, INK2)


# 12 - Fractional leadership: an org chart with one part-time seat in ochre
def orgchart():
    b = ""
    top = (800, 230)
    mids = [(420, 500), (800, 500), (1180, 500)]
    lows = [(300, 760), (540, 760), (680, 760), (920, 760), (1060, 760), (1300, 760)]
    def link(a, c):
        my = (a[1] + c[1]) / 2
        return f'<path d="M{a[0]} {a[1]+45} V{my} H{c[0]} V{c[1]-45}" fill="none" stroke="{FG}" stroke-opacity=".22" stroke-width="3"/>'
    for m in mids: b += link(top, m)
    for i, l in enumerate(lows): b += link(mids[i // 2], l)
    b += f'<rect x="{top[0]-110}" y="{top[1]-45}" width="220" height="90" fill="{FG}"/>'
    for i, (x, y) in enumerate(mids):
        if i == 1:
            b += f'<rect x="{x-110}" y="{y-45}" width="220" height="90" fill="{OC}" fill-opacity=".18" stroke="{OC}" stroke-width="5" stroke-dasharray="16 10"/>'
            b += f'<rect x="{x-110}" y="{y-45}" width="88" height="90" fill="{OC}"/>'
        else:
            b += f'<rect x="{x-110}" y="{y-45}" width="220" height="90" fill="{LINE2}"/>'
    for x, y in lows:
        b += f'<rect x="{x-60}" y="{y-45}" width="120" height="90" fill="{INK3}" stroke="{LINE2}" stroke-width="3"/>'
    return svg(b, INK)


# 13 - Multi-brand drift: identical brand panels slowly falling out of line
def brands():
    b = ""
    n = 5
    for i in range(n):
        x0 = 150 + i * 270
        dx, dy, rot = i * 6, i * i * 9, i * i * 1.1
        g = f'<g transform="translate({dx} {dy}) rotate({rot} {x0+110} 500)">'
        g += f'<rect x="{x0}" y="200" width="220" height="600" fill="{INK3}" stroke="{LINE2}" stroke-width="3"/>'
        g += f'<rect x="{x0}" y="200" width="220" height="56" fill="{OC if i == 0 else LINE2}" fill-opacity="{1 - i*0.15}"/>'
        for k in range(5):
            w = [160, 120, 170, 100, 140][(k + i) % 5] if i > 1 else [160, 120, 170, 100, 140][k]
            g += f'<rect x="{x0+30}" y="{300 + k*48}" width="{w}" height="14" fill="{FG}" fill-opacity=".25"/>'
        g += f'<rect x="{x0+30}" y="{580 + (i*14 if i>1 else 0)}" width="160" height="150" fill="{FG}" fill-opacity="{.12 + (0 if i>2 else .1)}"/>'
        g += f'<rect x="{x0+30}" y="750" width="{110 - i*12}" height="26" fill="{OC}" fill-opacity="{1 - i*0.18}"/>'
        g += '</g>'
        b += g
    b += f'<line x1="120" y1="200" x2="1480" y2="200" stroke="{OC}" stroke-width="2" stroke-dasharray="6 10" stroke-opacity=".6"/>'
    return svg(b, INK)


COVERS = dict(question=question, chaos=chaos,
              calendar=calendar, documents=documents, launch=launch, busy=busy,
              roadmap=roadmap, fracture=fracture, gap=gap,
              orgchart=orgchart, brands=brands)

for name, fn in COVERS.items():
    with open(os.path.join(OUT, f"{name}.svg"), "w") as fh:
        fh.write(fn())
print("wrote", len(COVERS), "covers to", OUT)
