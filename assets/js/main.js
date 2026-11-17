/* Komodo & Ko. — site behaviour */
(function () {
  "use strict";
  var nav = document.querySelector(".nav");
  var finePointer = matchMedia("(hover: hover) and (pointer: fine)").matches;

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
    var fields = Array.prototype.slice.call(form.querySelectorAll("input, textarea"));

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
