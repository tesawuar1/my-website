/* Komodo & Ko. — site behaviour */
(function () {
  "use strict";
  var nav = document.querySelector(".nav");
  var finePointer = matchMedia("(hover: hover) and (pointer: fine)").matches;

  /* Motion: sections and cards glide up into place as they reach the screen.
     Only movement, never hidden: text is always readable. Things already on screen
     when the page opens are left alone so nothing jumps. */
  (function () {
    if (!("IntersectionObserver" in window) || matchMedia("(prefers-reduced-motion: reduce)").matches) return;
    var phone = matchMedia("(max-width: 960px)").matches;
    var sel = [".sec-head", ".ed", ".svc-list a", ".why h2", ".why-grid > div", ".about > *", ".cta > div",
               ".item", ".prose section", ".days li", ".options > div", ".svc-intro > *", ".enq-side", ".facts", ".f-grid > div"];
    if (phone) sel.push("#story .L2 .vision", "#story .L3 .acct", "#story .L4 .dragon", "#story .L4 .st-copy");
    var els = Array.prototype.slice.call(document.querySelectorAll(sel.join(",")));
    var io = new IntersectionObserver(function (entries) {
      entries.forEach(function (en) {
        if (en.isIntersecting) { en.target.classList.add("in"); io.unobserve(en.target); }
      });
    }, { rootMargin: "0px 0px -6% 0px", threshold: 0.08 });
    els.forEach(function (el) {
      var r = el.getBoundingClientRect();
      if (r.top < innerHeight && r.bottom > 0) return;            // already visible: leave it
      var sibs = el.parentElement ? Array.prototype.indexOf.call(el.parentElement.children, el) : 0;
      el.style.setProperty("--rv", String(Math.min(sibs, 5)));
      el.classList.add(el.matches(".svc-list a, .days li") ? "rv-x" : "rv", "rv");
      io.observe(el);
    });
    /* switch the glide on only after the starting position is set, so nothing shifts on load */
    requestAnimationFrame(function () { requestAnimationFrame(function () {
      els.forEach(function (el) { if (el.classList.contains("rv")) el.classList.add("rv-on"); });
    }); });
  })();

  /* Komodo photo: tilts toward the mouse, and "reacts" when tapped or clicked */
  var dragon = document.querySelector(".dragon");
  if (dragon) {
    var dimg = dragon.querySelector(".dimg");
    var still = matchMedia("(prefers-reduced-motion: reduce)").matches;
    function poke() {
      if (still) return;
      dragon.classList.remove("poke");
      void dragon.offsetWidth;                       // restart the animation on every tap
      dragon.classList.add("poke");
    }
    dragon.addEventListener("click", poke);
    dragon.addEventListener("keydown", function (e) { if (e.key === "Enter" || e.key === " ") { e.preventDefault(); poke(); } });
    dragon.addEventListener("animationend", function () { dragon.classList.remove("poke"); });
    if (finePointer && !still) {
      dragon.addEventListener("pointermove", function (e) {
        if (dragon.classList.contains("poke")) return;
        var r = dragon.getBoundingClientRect();
        var x = (e.clientX - r.left) / r.width - 0.5, y = (e.clientY - r.top) / r.height - 0.5;
        dimg.style.transform = "perspective(900px) rotateY(" + (x * 7).toFixed(2) + "deg) rotateX(" + (-y * 7).toFixed(2) + "deg)";
      });
      dragon.addEventListener("pointerleave", function () { dimg.style.transform = ""; });
    }
  }

  /* Nav background once the page scrolls */
  var story = document.getElementById("story");
  function navState() {
    if (!nav) return;
    var limit = 60;
    if (story) limit = story.offsetHeight - innerHeight * 1.3 - nav.offsetHeight;
    nav.classList.toggle("solid", window.scrollY > limit);
  }
  navState();
  addEventListener("scroll", navState, { passive: true });
  addEventListener("resize", navState);
  addEventListener("load", navState);

  /* Dropdowns: hover on desktop, click/tap everywhere */
  var items = Array.prototype.slice.call(document.querySelectorAll(".menu > li.has-dd"));
  var closeTimer = null;
  function setOpen(li, open) {
    items.forEach(function (o) {
      var on = open && o === li;
      o.classList.toggle("open", on);
      var b = o.querySelector(".menu-btn");
      if (b) b.setAttribute("aria-expanded", on ? "true" : "false");
    });
    if (nav) nav.classList.toggle("open-dd", !!open);
  }
  items.forEach(function (li) {
    var btn = li.querySelector(".menu-btn");
    btn.addEventListener("click", function (e) {
      e.preventDefault();
      setOpen(li, !li.classList.contains("open"));
    });
    if (finePointer) {
      li.addEventListener("mouseenter", function () { clearTimeout(closeTimer); setOpen(li, true); });
      li.addEventListener("mouseleave", function () { closeTimer = setTimeout(function () { setOpen(null, false); }, 180); });
    }
  });
  document.addEventListener("click", function (e) {
    if (!e.target.closest(".menu")) setOpen(null, false);
  });
  document.addEventListener("keydown", function (e) {
    if (e.key === "Escape") { setOpen(null, false); document.body.classList.remove("menu-open"); }
  });

  /* Mobile drawer */
  var burger = document.querySelector(".burger");
  var drawer = document.querySelector(".drawer");
  if (burger && drawer) {
    burger.addEventListener("click", function () {
      document.body.classList.add("menu-open");
      burger.setAttribute("aria-expanded", "true");
      var c = drawer.querySelector(".drawer-close"); if (c) c.focus();
    });
    drawer.querySelector(".drawer-close").addEventListener("click", function () {
      document.body.classList.remove("menu-open");
      burger.setAttribute("aria-expanded", "false");
      burger.focus();
    });
  }

  /* Card tilt */
  if (finePointer && !matchMedia("(prefers-reduced-motion: reduce)").matches) {
    document.querySelectorAll("[data-tilt]").forEach(function (c) {
      c.addEventListener("pointermove", function (e) {
        var r = c.getBoundingClientRect();
        var x = (e.clientX - r.left) / r.width - 0.5, y = (e.clientY - r.top) / r.height - 0.5;
        c.style.transform = "perspective(1000px) rotateY(" + (x * 6).toFixed(2) + "deg) rotateX(" + (-y * 6).toFixed(2) + "deg)";
      });
      c.addEventListener("pointerleave", function () { c.style.transform = ""; });
    });
  }

  /* Services list: hovering a row changes the photo */
  var svcList = document.querySelector(".svc-list");
  if (svcList) {
    var rows = Array.prototype.slice.call(svcList.querySelectorAll("a"));
    var pics = Array.prototype.slice.call(document.querySelectorAll(".svc-media .bg"));
    function activate(i) {
      rows.forEach(function (r, k) { r.classList.toggle("on", k === i); });
      pics.forEach(function (p, k) { p.classList.toggle("on", k === i); });
    }
    rows.forEach(function (r, i) {
      r.addEventListener("mouseenter", function () { activate(i); });
      r.addEventListener("focus", function () { activate(i); });
    });
  }

  /* Destination slider buttons */
  var rail = document.querySelector(".rail");
  if (rail) {
    var btns = Array.prototype.slice.call(document.querySelectorAll("[data-rail]"));
    function step() { var c = rail.querySelector(".ed"); return c ? c.getBoundingClientRect().width + 28 : 300; }
    function update() {
      var max = rail.scrollWidth - rail.clientWidth - 4;
      btns.forEach(function (b) {
        var dir = +b.getAttribute("data-rail");
        b.disabled = dir < 0 ? rail.scrollLeft <= 4 : rail.scrollLeft >= max;
      });
    }
    btns.forEach(function (b) {
      b.addEventListener("click", function () { rail.scrollBy({ left: +b.getAttribute("data-rail") * step(), behavior: "smooth" }); });
    });
    rail.addEventListener("scroll", update, { passive: true });
    addEventListener("resize", update);
    update();
  }

  /* Table of contents highlight */
  var tocLinks = Array.prototype.slice.call(document.querySelectorAll(".toc a"));
  if (tocLinks.length && "IntersectionObserver" in window) {
    var io = new IntersectionObserver(function (entries) {
      entries.forEach(function (en) {
        if (en.isIntersecting) {
          tocLinks.forEach(function (a) { a.classList.toggle("on", a.getAttribute("href") === "#" + en.target.id); });
        }
      });
    }, { rootMargin: "-30% 0px -60% 0px" });
    document.querySelectorAll(".prose section[id]").forEach(function (s) { io.observe(s); });
  }

  /* Enquiry form */
  var form = document.getElementById("enquiry-form");
  if (form) {
    var cfg = JSON.parse(form.getAttribute("data-cfg"));
    var fields = Array.prototype.slice.call(form.querySelectorAll(".field input, .field textarea"));
    var trap = form.elements.website;   // hidden spam trap: people never see or fill it

    /* Save a copy of the enquiry to the Google Sheet (and email the team) before
       opening WhatsApp or the email app. Fire-and-forget: it never blocks the guest. */
    function saveEnquiry(channel) {
      if (!cfg.endpoint) return;
      var data = { channel: channel, lang: cfg.lang, page: location.href, website: trap ? trap.value : "" };
      fields.forEach(function (el) { data[el.name] = el.value.trim(); });
      try {
        fetch(cfg.endpoint, {
          method: "POST", mode: "no-cors", keepalive: true,
          headers: { "Content-Type": "text/plain;charset=utf-8" },
          body: JSON.stringify(data)
        }).catch(function () {});
      } catch (e) { /* never stop the guest from reaching us */ }
    }

    function check(el) {
      var v = el.value.trim(), msg = "";
      if (!v) msg = cfg.err.required;
      else if (el.name === "email" && !/^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(v)) msg = cfg.err.email;
      else if (el.name === "phone" && v.replace(/\D/g, "").length < 8) msg = cfg.err.phone;
      else if (el.name === "guests" && !(parseInt(v, 10) >= 1)) msg = cfg.err.guests;
      var f = el.closest(".field");
      f.classList.toggle("bad", !!msg);
      f.querySelector(".err").textContent = msg;
      el.setAttribute("aria-invalid", msg ? "true" : "false");
      return !msg;
    }
    fields.forEach(function (el) {
      el.addEventListener("blur", function () { if (el.value.trim()) check(el); });
      el.addEventListener("input", function () { if (el.closest(".field").classList.contains("bad")) check(el); });
    });

    function message() {
      var lines = [cfg.intro, ""];
      fields.forEach(function (el) { lines.push(cfg.labels[el.name] + ": " + el.value.trim()); });
      return lines.join("\n");
    }

    form.addEventListener("submit", function (e) { e.preventDefault(); });
    form.querySelectorAll("[data-send]").forEach(function (b) {
      b.addEventListener("click", function () {
        var ok = true, first = null;
        fields.forEach(function (el) { if (!check(el)) { ok = false; first = first || el; } });
        if (!ok) { first.focus(); return; }
        var text = message();
        saveEnquiry(b.getAttribute("data-send"));
        if (b.getAttribute("data-send") === "wa") {
          window.open("https://wa.me/" + cfg.wa + "?text=" + encodeURIComponent(text), "_blank", "noopener");
        } else {
          var name = form.elements.name.value.trim();
          window.location.href = "mailto:" + cfg.email + "?subject=" + encodeURIComponent(cfg.subject + " " + name) +
            "&body=" + encodeURIComponent(text);
        }
        var okBox = form.querySelector(".form-ok");
        okBox.classList.add("show");
      });
    });
  }
})();
