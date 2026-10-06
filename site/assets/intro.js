/* Homepage logo intro (about 4 seconds): plays once per session, then the
   finished logo slides into the header badge. Needs logo.js and site.js first. */
(function () {
  "use strict";
  var root = document.documentElement;
  if (!root.classList.contains("intro-on") || !window.DurusLogo) return;

  var intro = document.getElementById("intro");
  var svg = document.getElementById("introLogo");
  var brand = document.getElementById("brandLogo");
  var logo = new DurusLogo(svg);
  logo.seek(0);
  var done = false;

  function markSeen() { try { sessionStorage.setItem("durusIntroSeen", "1"); } catch (e) {} }
  function finishHeader() { if (window.durusHeader) window.durusHeader.finish(); }
  function remove() { if (intro.parentNode) intro.parentNode.removeChild(intro); }

  function handOff() {
    if (done) return; done = true;
    logo.finish();
    var from = svg.getBoundingClientRect();
    var to = brand.getBoundingClientRect();
    intro.classList.add("leaving");
    svg.style.transition = "transform .7s cubic-bezier(.65,0,.25,1)";
    svg.style.transform = "translate(" + (to.left - from.left) + "px," + (to.top - from.top) + "px) scale(" + (to.width / from.width) + ")";
    setTimeout(function () { root.classList.remove("intro-on"); remove(); finishHeader(); markSeen(); }, 720);
  }

  function skip() {
    if (done) return; done = true;
    markSeen();
    intro.classList.add("leaving");
    intro.style.transition = "opacity .35s ease";
    intro.style.opacity = "0";
    setTimeout(function () { root.classList.remove("intro-on"); remove(); finishHeader(); }, 360);
  }

  document.getElementById("introSkip").addEventListener("click", skip);
  document.addEventListener("keydown", function (e) { if (e.key === "Escape") skip(); });

  DurusLogo.fontsReady(1500).then(function () {
    if (done) return;
    logo.build();
    logo.play({ speed: 1.5, onDone: function () { setTimeout(handOff, 250); } });
  });
})();
