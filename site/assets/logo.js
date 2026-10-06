/* Durus Advisory logo animation.
   A lone D inside two full rings of dots; the rings unwind into the top and
   bottom arcs while DURUS / ADVISORY settle into place. Geometry matches the
   static header badge exactly (viewBox 0 0 950 500), so the last frame is the logo. */
(function () {
  "use strict";
  var NS = "http://www.w3.org/2000/svg";
  var OCHRE = "#D96A2C", FG = "#EDEAE4";
  var CX = 475, CY = 250;
  var WORD = { text: "DURUS", x: 475, y: 270, size: 150, ls: 30,
               family: "Domine, Georgia, serif", weight: 700, fill: OCHRE };
  var SUB = { text: "ADVISORY", x: 483, y: 330, size: 42, ls: 26,
              family: "'IBM Plex Mono', ui-monospace, Menlo, monospace", weight: 500, fill: FG };
  var CAP = 0.70; // cap height of Domine, as a share of font size
  var END = 4.6;

  var RINGS = [
    { n: 25, R0: 158, R1: 210, from: -145, to: -35, r: 3.0, spin: 720, delay: 0.12 },
    { n: 23, R0: 132, R1: 178, from: -140, to: -40, r: 2.5, spin: -360, delay: 0 }
  ];

  function clamp(v) { return v < 0 ? 0 : v > 1 ? 1 : v; }
  function lerp(a, b, p) { return a + (b - a) * p; }
  function inOut(p) { return p < 0.5 ? 4 * p * p * p : 1 - Math.pow(-2 * p + 2, 3) / 2; }
  function out(p) { return 1 - Math.pow(1 - p, 3); }
  function el(name, attrs, parent) {
    var e = document.createElementNS(NS, name);
    for (var k in attrs) e.setAttribute(k, attrs[k]);
    if (parent) parent.appendChild(e);
    return e;
  }

  function DurusLogo(svg, opts) {
    opts = opts || {};
    this.svg = svg;
    this.introScale = opts.introScale || 1.5;
    this.raf = 0;
    this.playing = false;
    this.build();
  }

  DurusLogo.prototype.build = function () {
    var svg = this.svg;
    while (svg.firstChild) svg.removeChild(svg.firstChild);
    svg.setAttribute("viewBox", "0 0 950 500");
    this.dotsG = el("g", {}, svg);
    this.textG = el("g", {}, svg);

    this.rings = RINGS.map(function (ring) {
      var N = ring.n * 2, step = 360 / N, dots = [];
      for (var k = 0; k < N; k++) {
        var j = k % ring.n, top = k < ring.n;
        var span = ring.to - ring.from;
        var a1 = top ? ring.from + j * span / (ring.n - 1)
                     : -ring.to + j * span / (ring.n - 1);
        dots.push({
          el: el("circle", { fill: OCHRE }, this.dotsG),
          a0: -90 - (ring.n - 1) / 2 * step + k * step,
          a1: a1,
          appear: k / N
        });
      }
      return { cfg: ring, dots: dots };
    }, this);

    this.letters = this.makeLetters(WORD);
    this.subs = this.makeLetters(SUB);
    var D = this.letters[0];
    this.dx = parseFloat(D.getAttribute("x"));
    this.dw = WORD.size * 0.72;
    try { this.dw = D.getComputedTextLength() || this.dw; } catch (e) {}
  };

  // Lay out each string exactly as the static badge does (letter-spacing,
  // centred), then split it into one <text> per letter at the measured spots.
  DurusLogo.prototype.makeLetters = function (spec) {
    var probe = el("text", {
      x: spec.x, y: spec.y, "text-anchor": "middle",
      "font-family": spec.family, "font-weight": spec.weight,
      "font-size": spec.size, "letter-spacing": spec.ls, fill: "none"
    }, this.textG);
    probe.textContent = spec.text;
    var xs = [];
    for (var i = 0; i < spec.text.length; i++) {
      var x;
      try { x = probe.getStartPositionOfChar(i).x; } catch (e) { x = NaN; }
      if (!isFinite(x)) x = spec.x - (spec.text.length * spec.size * 0.62) / 2 + i * spec.size * 0.82;
      xs.push(x);
    }
    this.textG.removeChild(probe);
    return spec.text.split("").map(function (ch, i) {
      var t = el("text", {
        x: xs[i].toFixed(2), y: spec.y,
        "font-family": spec.family, "font-weight": spec.weight,
        "font-size": spec.size, fill: spec.fill
      }, this.textG);
      t.textContent = ch;
      return t;
    }, this);
  };

  DurusLogo.prototype.render = function (t) {
    for (var r = 0; r < this.rings.length; r++) {
      var ring = this.rings[r], c = ring.cfg;
      var spin = c.spin * inOut(clamp((t - 0.15) / 3.7));
      var p = inOut(clamp((t - 1.4 - c.delay) / 2.2));
      var R = lerp(c.R0, c.R1, p);
      var size = lerp(c.r * 0.95, c.r, p);
      for (var i = 0; i < ring.dots.length; i++) {
        var d = ring.dots[i];
        var a = (lerp(d.a0, d.a1, p) + spin) * Math.PI / 180;
        d.el.setAttribute("cx", (CX + R * Math.cos(a)).toFixed(2));
        d.el.setAttribute("cy", (CY + R * Math.sin(a)).toFixed(2));
        d.el.setAttribute("r", size.toFixed(2));
        d.el.setAttribute("opacity", clamp((t - 0.15 - d.appear * 0.8) / 0.25).toFixed(3));
      }
    }

    // The D: large in the centre, then shrinks into its slot.
    var D = this.letters[0];
    var dcx = this.dx + this.dw / 2, dcy = WORD.y - WORD.size * CAP / 2;
    var intro = out(clamp(t / 0.8));
    var pd = inOut(clamp((t - 2.0) / 1.5));
    var s = lerp(lerp(this.introScale * 1.15, this.introScale, intro), 1, pd);
    var tx = lerp(CX, dcx, pd), ty = lerp(CY, dcy, pd);
    D.setAttribute("transform", "translate(" + tx.toFixed(2) + " " + ty.toFixed(2) + ") scale(" +
      s.toFixed(4) + ") translate(" + (-dcx).toFixed(2) + " " + (-dcy).toFixed(2) + ")");
    D.setAttribute("opacity", clamp(t / 0.6).toFixed(3));

    for (var l = 1; l < this.letters.length; l++) {
      var q = out(clamp((t - (2.9 + 0.11 * (l - 1))) / 0.7));
      this.letters[l].setAttribute("opacity", q.toFixed(3));
      this.letters[l].setAttribute("transform", "translate(" + ((1 - q) * -28).toFixed(2) + " 0)");
    }
    for (var m = 0; m < this.subs.length; m++) {
      var q2 = out(clamp((t - (3.6 + 0.06 * m)) / 0.5));
      this.subs[m].setAttribute("opacity", q2.toFixed(3));
      this.subs[m].setAttribute("transform", "translate(0 " + ((1 - q2) * 8).toFixed(2) + ")");
    }
  };

  DurusLogo.prototype.seek = function (t) {
    cancelAnimationFrame(this.raf);
    this.playing = false;
    this.render(t);
  };
  DurusLogo.prototype.finish = function () { this.seek(END); };

  DurusLogo.prototype.play = function (opts) {
    opts = opts || {};
    var self = this, speed = opts.speed || 1, start = performance.now();
    cancelAnimationFrame(this.raf);
    this.playing = true;
    this.render(0);
    function tick(now) {
      var t = (now - start) / 1000 * speed;
      self.render(Math.min(t, END));
      if (t < END) { self.raf = requestAnimationFrame(tick); }
      else { self.playing = false; if (opts.onDone) opts.onDone(); }
    }
    this.raf = requestAnimationFrame(tick);
  };

  DurusLogo.END = END;
  DurusLogo.reduceMotion = function () {
    return window.matchMedia && window.matchMedia("(prefers-reduced-motion: reduce)").matches;
  };
  // Resolve once the logo fonts are in (or after a short timeout).
  DurusLogo.fontsReady = function (timeout) {
    if (!document.fonts || !document.fonts.load) return Promise.resolve();
    return Promise.race([
      Promise.all([
        document.fonts.load("700 150px Domine"),
        document.fonts.load("500 42px 'IBM Plex Mono'")
      ]),
      new Promise(function (r) { setTimeout(r, timeout || 1500); })
    ]);
  };

  // Header badge: plays once on load (unless told not to) and replays on hover.
  DurusLogo.header = function (svg, opts) {
    opts = opts || {};
    var logo = new DurusLogo(svg);
    logo.finish();
    var brand = svg.closest("a") || svg;
    var reduce = DurusLogo.reduceMotion();
    brand.addEventListener("mouseenter", function () {
      if (!reduce && !logo.playing && !document.documentElement.classList.contains("intro-on")) {
        logo.play({ speed: 1.5 });
      }
    });
    DurusLogo.fontsReady().then(function () {
      logo.build();
      if (opts.autoplay && !reduce) logo.play({ speed: 1.2 });
      else logo.finish();
    });
    return logo;
  };

  window.DurusLogo = DurusLogo;
})();
