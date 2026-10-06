/* Shared behaviour for every page: header logo, mobile menu, scroll reveals. */
(function () {
  "use strict";

  // Header logo (static; replays on hover).
  var badge = document.getElementById("brandLogo");
  if (badge && window.DurusLogo) window.durusHeader = DurusLogo.header(badge, { autoplay: false });

  // Mobile menu.
  var btn = document.querySelector(".menu-btn");
  var menu = document.getElementById("mobileMenu");
  if (btn && menu) {
    var setOpen = function (open) {
      menu.hidden = !open;
      btn.setAttribute("aria-expanded", String(open));
      btn.setAttribute("aria-label", open ? "Close menu" : "Open menu");
    };
    btn.addEventListener("click", function () { setOpen(menu.hidden); });
    menu.addEventListener("click", function (e) { if (e.target.closest("a")) setOpen(false); });
    document.addEventListener("keydown", function (e) {
      if (e.key === "Escape" && !menu.hidden) { setOpen(false); btn.focus(); }
    });
    document.addEventListener("click", function (e) {
      if (!menu.hidden && !menu.contains(e.target) && !btn.contains(e.target)) setOpen(false);
    });
    window.addEventListener("resize", function () { if (window.innerWidth > 720) setOpen(false); });
  }

  // Fade sections in as they scroll into view.
  var els = document.querySelectorAll(".reveal");
  var reduce = window.matchMedia && window.matchMedia("(prefers-reduced-motion: reduce)").matches;
  if (reduce || !("IntersectionObserver" in window)) {
    els.forEach(function (el) { el.classList.add("in"); });
  } else {
    var io = new IntersectionObserver(function (entries) {
      entries.forEach(function (e) {
        if (e.isIntersecting) { e.target.classList.add("in"); io.unobserve(e.target); }
      });
    }, { threshold: 0.12, rootMargin: "0px 0px -8% 0px" });
    els.forEach(function (el, i) {
      if (i < 5) el.style.transitionDelay = (i * 70) + "ms";
      io.observe(el);
    });
  }
})();
