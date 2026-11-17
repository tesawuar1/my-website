/* Komodo & Ko. — home page scroll story.
   One requestAnimationFrame loop maps scroll progress (0 to 1) through the pinned
   stage onto five beats: hero, camera push into Padar, landscape with hotspots,
   and the Komodo dragon / services station. */
(function () {
  "use strict";
  var story = document.getElementById("story");
  if (!story) return;
  function q(s) { return story.querySelector(s); }
  function qa(s) { return Array.prototype.slice.call(story.querySelectorAll(s)); }

  var cam = q(".cam"), plate = q(".plate"), shade = q(".shade"), fog = q(".fog"), night = q(".night");
  var camF = q(".camF"), plateF = q(".plateF"), veil = q(".veil"), veilB = q(".veil-b");
  var L0 = q(".L0"), L1 = q(".L1"), L2 = q(".L2"), L3 = q(".L3"), L4 = q(".L4");
  var heroCopy = q(".hero-copy"), hud = q(".hud"), cap = q(".caption"), hint = q(".hint");
  var vWords = qa(".vision h2 .w"), vChip = q(".vision .label"), vP = q(".vision p");
  var aWords = qa(".acct .w"), spots = qa(".spot");
  var dragon = q(".dragon"), dcard = q(".dcard"), stCopy = q(".st-copy"), feats = qa(".feats a"), num = q("[data-num]");
  var bar = q(".prog i");
  var reduce = matchMedia("(prefers-reduced-motion: reduce)").matches;

  function clamp(v, a, b) { a = a === undefined ? 0 : a; b = b === undefined ? 1 : b; return Math.min(b, Math.max(a, v)); }
  function seg(p, a, b) { return clamp((p - a) / (b - a)); }
  function ease(t) { return t < 0.5 ? 4 * t * t * t : 1 - Math.pow(-2 * t + 2, 3) / 2; }
  function vis(el, on) { var v = on ? "visible" : "hidden"; if (el.style.visibility !== v) el.style.visibility = v; }

  var sp = 0, sx = 0, sy = 0, mx = 0, my = 0, last = performance.now();
  addEventListener("pointermove", function (e) { mx = e.clientX / innerWidth - 0.5; my = e.clientY / innerHeight - 0.5; }, { passive: true });

  /* Geometry: where a point of the Padar photo sits inside the camera box */
  var G = null;
  function geo() {
    var pw = plate.offsetWidth, ph = plate.offsetHeight, pt = plate.offsetTop;
    var iw = plate.naturalWidth || 2400, ih = plate.naturalHeight || 1600;
    var k = Math.max(pw / iw, ph / ih), dw = iw * k, dh = ih * k, ox = (pw - dw) / 2;
    function map(fx, fy) { return [ox + fx * dw, pt + fy * dh]; }
    var v = map(0.5, 0.6);
    cam.style.transformOrigin = camF.style.transformOrigin = v[0] + "px " + v[1] + "px";
    /* line the skyline mask up with the photo exactly as object-fit:cover draws it */
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
  }
  /* Place the one-line headline so the main peak overlaps the lower half of its letters */
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
  geo();
  addEventListener("resize", geo);
  if (document.fonts && document.fonts.ready) document.fonts.ready.then(geo);
  if (!plate.complete) plate.addEventListener("load", geo);

  spots.forEach(function (s) {
    s.addEventListener("click", function () {
      var on = !s.classList.contains("on");
      spots.forEach(function (o) { o.classList.remove("on"); });
      s.classList.toggle("on", on);
    });
  });

  var featsDone = false;
  function frame(now) {
    var dt = Math.min(64, now - last); last = now;
    var r = story.getBoundingClientRect();
    var total = story.offsetHeight - innerHeight;
    var p = clamp(-r.top / total);
    if (reduce) sp = p;
    else { sp += (p - sp) * (1 - Math.pow(0.86, dt / 16.7)); if (Math.abs(p - sp) < 0.0002) sp = p; }
    sx += (mx - sx) * 0.06; sy += (my - sy) * 0.06;

    if (r.bottom < -50) { requestAnimationFrame(frame); return; }
    var W = G.W, H = G.H;

    /* Camera push into the island */
    var vp = ease(seg(sp, 0.04, 0.62));
    var s = 1 + vp * 0.85;
    var tx = -sx * 18 + (W * 0.5 - (G.cl + G.vx)) * vp * 0.6;
    var ty = -sy * 12 + (H * 0.55 - (G.ct + G.vy)) * vp * 0.8;
    cam.style.transform = camF.style.transform = "translate3d(" + tx.toFixed(1) + "px," + ty.toFixed(1) + "px,0) scale(" + s.toFixed(4) + ")";

    /* Hero */
    var h = seg(sp, 0.015, 0.09);
    heroCopy.style.transform = "translate3d(" + (-sx * 10).toFixed(1) + "px," + (-h * 80 - sy * 6).toFixed(1) + "px,0) scale(" + (1 + h * 0.12).toFixed(3) + ")";
    heroCopy.style.filter = h > 0 ? "blur(" + (h * 14).toFixed(1) + "px)" : "none";
    heroCopy.style.opacity = 1 - h;
    if (hud) {
      hud.style.transform = "translate3d(" + (sx * 26).toFixed(1) + "px," + (sy * 18 - h * 40).toFixed(1) + "px,0)";
      hud.style.opacity = 1 - seg(sp, 0.015, 0.07);
    }
    var c = 1 - seg(sp, 0.005, 0.04);
    cap.style.opacity = c; hint.style.opacity = c;
    vis(L0, h < 1); vis(L1, h < 1);
    /* the veil fades with the headline, so removing the cut-out afterwards is seamless */
    veil.style.opacity = 1 - h;
    veilB.style.opacity = c;
    vis(camF, h < 1);

    /* Vision statement */
    var vIn = seg(sp, 0.12, 0.22), vOut = seg(sp, 0.30, 0.38);
    vWords.forEach(function (w, i) {
      var k = clamp(vIn * 1.6 - i * 0.08);
      w.style.transform = "translate3d(0," + ((1 - k) * 30 - vOut * 60).toFixed(1) + "px,0)";
      w.style.filter = "blur(" + ((1 - k) * 12 + vOut * 14).toFixed(1) + "px)";
      w.style.opacity = k * (1 - vOut);
    });
    var cp = clamp(vIn * 2 - 0.6) * (1 - vOut);
    vChip.style.opacity = cp; vP.style.opacity = cp;
    vChip.style.transform = vP.style.transform = "translateY(" + (-vOut * 50).toFixed(1) + "px)";
    vis(L2, vIn > 0 && vOut < 1);
    shade.style.opacity = (clamp(vIn * 1.5) * (1 - vOut)).toFixed(3);

    /* Fog bank keeps the sky clean behind the paragraph */
    var fg = ease(seg(sp, 0.36, 0.45)) * (1 - seg(sp, 0.62, 0.68));
    vis(fog, fg > 0);
    fog.style.opacity = fg;
    fog.style.transform = "translate3d(" + ((fg - 1) * 18 - sx * 10).toFixed(2) + "vw," + (-sy * 6).toFixed(1) + "px,0)";

    /* Paragraph + hotspots */
    var aIn = seg(sp, 0.40, 0.50), aOut = seg(sp, 0.60, 0.66);
    var n = aWords.length;
    aWords.forEach(function (w, i) {
      var k = clamp(aIn * 2.2 - (i / n) * 1.2);
      w.style.opacity = ((0.15 + 0.85 * k) * (1 - aOut)).toFixed(3);
      w.style.filter = "blur(" + ((1 - k) * 6 + aOut * 10).toFixed(1) + "px)";
    });
    vis(L3, aIn > 0 && aOut < 1);
    spots.forEach(function (sEl, i) {
      var k = seg(sp, 0.45 + i * 0.02, 0.49 + i * 0.02) * (1 - aOut);
      var X = G.cl + G.vx + (sEl._x - G.vx) * s + tx;
      var Y = G.ct + G.vy + (sEl._y - G.vy) * s + ty;
      var onScreen = X > 8 && X < W - 40 && Y > 60 && Y < H - 40;
      vis(sEl, k > 0.01 && onScreen);
      sEl.style.transform = "translate3d(" + (X - 12).toFixed(1) + "px," + (Y - 12).toFixed(1) + "px,0) scale(" + k.toFixed(3) + ")";
    });

    /* Station: dragon + services */
    var nIn = ease(seg(sp, 0.64, 0.74));
    night.style.opacity = nIn; vis(night, nIn > 0); vis(L4, nIn > 0);
    var dIn = ease(seg(sp, 0.68, 0.80));
    dragon.style.opacity = dIn;
    dragon.style.transform = "translate3d(" + (sx * -14).toFixed(1) + "px," + ((1 - dIn) * 80 + sy * -10).toFixed(1) + "px,0) scale(" + (0.94 + 0.06 * dIn).toFixed(3) + ")";
    var cIn = ease(seg(sp, 0.74, 0.86));
    dcard.style.opacity = cIn;
    dcard.style.transform = "translate3d(" + (sx * -10).toFixed(1) + "px," + ((1 - cIn) * 50).toFixed(1) + "px,0) rotateY(" + (sx * 8).toFixed(2) + "deg) rotateX(" + (-sy * 8).toFixed(2) + "deg)";
    num.textContent = Math.round(3 * seg(sp, 0.76, 0.88));
    var sIn = seg(sp, 0.70, 0.80);
    stCopy.style.opacity = sIn;
    stCopy.style.transform = "translateY(" + ((1 - sIn) * 30).toFixed(1) + "px)";
    stCopy.style.filter = sIn < 1 ? "blur(" + ((1 - sIn) * 8).toFixed(1) + "px)" : "none";
    feats.forEach(function (a, i) {
      var k = ease(seg(sp, 0.74 + i * 0.025, 0.80 + i * 0.025));
      a.style.opacity = k;
      a.style.transform = k < 1 ? "translateX(" + ((1 - k) * 40).toFixed(1) + "px)" : "";
    });

    bar.style.transform = "scaleX(" + sp.toFixed(4) + ")";
    requestAnimationFrame(frame);
  }
  requestAnimationFrame(frame);
})();
