/* Komodo & Ko. — home page scroll story.
   Four scenes, each shown whole and sharp: 0 hero, 1 promise, 2 island paragraph,
   3 Komodo dragon. Scrolling or swiping snaps to the next scene (CSS scroll-snap on
   the .snap markers); the scene's text appears with one quick fade set in CSS.
   Only the camera push into Padar follows the scroll continuously.
   Performance: layout is measured on resize only, styles are written only when they
   change, and the loop sleeps when nothing is moving. */
(function () {
  "use strict";
  var story = document.getElementById("story");
  if (!story) return;
  function q(s) { return story.querySelector(s); }
  function qa(s) { return Array.prototype.slice.call(story.querySelectorAll(s)); }

  var cam = q(".cam"), plate = q(".plate"), camF = q(".camF"), plateF = q(".plateF");
  var heroCopy = q(".hero-copy"), hud = q(".hud");
  var spots = qa(".spot"), snaps = qa(".snap");
  var bar = q(".prog i");
  var reduce = matchMedia("(prefers-reduced-motion: reduce)").matches;
  /* On phones the story is four normal sections (see style.css), so this script stays idle */
  var phone = matchMedia("(max-width: 960px)");
  var finePointer = matchMedia("(hover: hover) and (pointer: fine)").matches;

  /* Scene boundaries (scroll progress 0-1). Snap stops sit inside each scene. */
  var BOUNDS = [0.13, 0.39, 0.69];

  function clamp(v, a, b) { a = a === undefined ? 0 : a; b = b === undefined ? 1 : b; return Math.min(b, Math.max(a, v)); }
  function seg(p, a, b) { return clamp((p - a) / (b - a)); }
  function ease(t) { return t < 0.5 ? 4 * t * t * t : 1 - Math.pow(-2 * t + 2, 3) / 2; }
  function set(el, prop, val) {
    var key = "_" + prop;
    if (el[key] !== val) { el[key] = val; el.style[prop] = val; }
  }
  function tr(x, y, s) {
    return "translate3d(" + x.toFixed(1) + "px," + y.toFixed(1) + "px,0)" + (s === undefined ? "" : " scale(" + s.toFixed(4) + ")");
  }

  /* Geometry, measured on load and resize only */
  var G = null, storyTop = 0, total = 1;
  function geo() {
    if (phone.matches) return;
    var pw = plate.offsetWidth, ph = plate.offsetHeight, pt = plate.offsetTop;
    var iw = plate.naturalWidth || 2400, ih = plate.naturalHeight || 1600;
    var k = Math.max(pw / iw, ph / ih), dw = iw * k, dh = ih * k, ox = (pw - dw) / 2;
    function map(fx, fy) { return [ox + fx * dw, pt + fy * dh]; }
    var v = map(0.5, 0.6);
    cam.style.transformOrigin = camF.style.transformOrigin = v[0] + "px " + v[1] + "px";
    plateF.style.setProperty("--mw", dw + "px");
    plateF.style.setProperty("--mh", dh + "px");
    plateF.style.setProperty("--mx", ox + "px");
    G = { W: innerWidth, H: innerHeight, cl: cam.offsetLeft, ct: cam.offsetTop, map: map, vx: v[0], vy: v[1] };
    if (hud) {
      var hp = map(0.52, 0.60);
      hud.style.left = (G.cl + hp[0]).toFixed(0) + "px";
      hud.style.top = (G.ct + hp[1]).toFixed(0) + "px";
    }
    layoutHero();
    spots.forEach(function (s) {
      var m = map(parseFloat(s.getAttribute("data-x")), parseFloat(s.getAttribute("data-y")));
      s._x = m[0]; s._y = m[1];
    });
    storyTop = story.getBoundingClientRect().top + window.pageYOffset;
    total = Math.max(1, story.offsetHeight - innerHeight);
    snaps.forEach(function (el) { el.style.top = Math.round(parseFloat(el.getAttribute("data-stop")) * total) + "px"; });
    wake();
  }
  /* Place the one-line headline so the main peak overlaps the lower part of its letters */
  function layoutHero() {
    var h1 = heroCopy.querySelector("h1"), line = h1.querySelector(".ln span");
    if (innerWidth < 961) { heroCopy.style.top = ""; h1.style.fontSize = ""; return; }
    var fs = Math.min(104, innerWidth * 0.064);
    h1.style.fontSize = fs + "px";
    var w = line.offsetWidth, max = innerWidth * 0.88;
    if (w > max) { fs = fs * max / w; h1.style.fontSize = fs + "px"; }
    var peakY = G.ct + G.map(0.82, 0.305)[1];
    var navH = document.querySelector(".nav").offsetHeight;
    var top = peakY + fs * 0.36 - heroCopy.offsetHeight;
    heroCopy.style.top = Math.max(navH + 12, top).toFixed(0) + "px";
  }

  spots.forEach(function (s) {
    s.addEventListener("click", function () {
      var on = !s.classList.contains("on");
      spots.forEach(function (o) { o.classList.remove("on"); });
      s.classList.toggle("on", on);
    });
  });

  var sp = 0, sx = 0, sy = 0, mx = 0, my = 0, last = 0, running = false, scene = -1;
  function progress() { return clamp((window.pageYOffset - storyTop) / total); }
  function wake() {
    if (running || phone.matches) return;
    running = true;
    last = performance.now();
    requestAnimationFrame(frame);
  }
  addEventListener("scroll", wake, { passive: true });
  if (finePointer && !reduce) {
    addEventListener("pointermove", function (e) { mx = e.clientX / innerWidth - 0.5; my = e.clientY / innerHeight - 0.5; wake(); }, { passive: true });
  }

  function frame(now) {
    var dt = Math.min(48, now - last); last = now;
    var p = progress();
    if (reduce) sp = p;
    else { sp += (p - sp) * (1 - Math.pow(0.7, dt / 16.7)); if (Math.abs(p - sp) < 0.0003) sp = p; }
    sx += (mx - sx) * 0.08; sy += (my - sy) * 0.08;
    var settled = sp === p && Math.abs(mx - sx) < 0.002 && Math.abs(my - sy) < 0.002;

    /* the scene follows the real scroll position, so text switches straight away */
    var n = p < BOUNDS[0] ? 0 : p < BOUNDS[1] ? 1 : p < BOUNDS[2] ? 2 : 3;
    if (n !== scene) { scene = n; story.setAttribute("data-scene", String(n)); }

    var inView = window.pageYOffset < storyTop + total + G.H;
    if (inView) render();
    if (settled || !inView) { running = false; return; }
    requestAnimationFrame(frame);
  }

  function render() {
    var W = G.W, H = G.H;
    /* Camera push into the island follows the scroll */
    var vp = ease(seg(sp, 0.02, 0.5));
    var s = 1 + vp * 0.85;
    var tx = -sx * 14 + (W * 0.5 - (G.cl + G.vx)) * vp * 0.6;
    var ty = -sy * 10 + (H * 0.55 - (G.ct + G.vy)) * vp * 0.8;
    var camT = tr(tx, ty, s);
    set(cam, "transform", camT);
    if (scene === 0) set(camF, "transform", camT);
    if (hud) set(hud, "transform", tr(sx * 20, sy * 14));

    /* Hotspots ride on the photo */
    spots.forEach(function (sEl) {
      var X = G.cl + G.vx + (sEl._x - G.vx) * s + tx;
      var Y = G.ct + G.vy + (sEl._y - G.vy) * s + ty;
      var on = scene === 2 && X > 8 && X < W - 40 && Y > 60 && Y < H - 40;
      set(sEl, "visibility", on ? "visible" : "hidden");
      if (on) set(sEl, "transform", tr(X - 12, Y - 12));
    });

    set(bar, "transform", "scaleX(" + sp.toFixed(3) + ")");
  }

  /* Snap to scenes: when scrolling stops inside the story, glide to the next scene in
     the direction of travel, so one swipe or wheel turn lands straight on the next text. */
  var STOPS = snaps.map(function (el) { return parseFloat(el.getAttribute("data-stop")); });
  var lastY = window.pageYOffset, dir = 0, autoScrolling = false, endTimer = 0, settleTimer = 0;
  function stopY(i) { return Math.round(storyTop + STOPS[i] * total); }
  function onScrollEnd() {
    if (autoScrolling) { autoScrolling = false; return; }
    if (reduce || phone.matches || document.body.classList.contains("menu-open")) return;
    var y = window.pageYOffset;
    var last = stopY(STOPS.length - 1);
    if (y < storyTop - 2 || y > last + 4) return;           // outside the story: scroll freely
    var target = null, i;
    for (i = 0; i < STOPS.length; i++) if (Math.abs(stopY(i) - y) <= 3) return;   // already on a scene
    if (dir > 0) { for (i = 0; i < STOPS.length; i++) if (stopY(i) > y) { target = stopY(i); break; } }
    else { for (i = STOPS.length - 1; i >= 0; i--) if (stopY(i) < y) { target = stopY(i); break; } }
    if (target === null) return;
    autoScrolling = true;
    window.scrollTo({ top: target, behavior: "smooth" });
    clearTimeout(settleTimer);
    settleTimer = setTimeout(function () { autoScrolling = false; }, 1200);   // safety if scrollend never fires
  }
  addEventListener("scroll", function () {
    var y = window.pageYOffset;
    if (y !== lastY) dir = y > lastY ? 1 : -1;
    lastY = y;
    if (!("onscrollend" in window)) { clearTimeout(endTimer); endTimer = setTimeout(onScrollEnd, 160); }
  }, { passive: true });
  if ("onscrollend" in window) addEventListener("scrollend", onScrollEnd);

  /* switching between phone and desktop layouts (e.g. rotating a tablet) */
  function onLayoutChange() {
    if (phone.matches) {
      [cam, camF, hud, heroCopy].forEach(function (el) { if (el) { el.style.transform = ""; el._transform = undefined; } });
      if (hud) { hud.style.left = hud.style.top = ""; }
      heroCopy.style.top = ""; heroCopy.querySelector("h1").style.fontSize = "";
      spots.forEach(function (el) { el.style.transform = el.style.visibility = ""; el._transform = el._visibility = undefined; });
      story.setAttribute("data-scene", "0"); scene = -1;
    } else {
      geo();
    }
  }
  if (phone.addEventListener) phone.addEventListener("change", onLayoutChange);
  else if (phone.addListener) phone.addListener(onLayoutChange);

  geo();
  addEventListener("resize", geo);
  addEventListener("load", geo);
  if (document.fonts && document.fonts.ready) document.fonts.ready.then(geo);
  if (!plate.complete) plate.addEventListener("load", geo);
})();
