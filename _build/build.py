# -*- coding: utf-8 -*-
"""Generate the Komodo & Ko. website (English at the root, Indonesian in /id/).

Usage:  python _build/build.py
Edit text in content_main.py / content_dest.py, then run this again.
"""
import html
import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import re  # noqa: E402
from content_dest import DESTINATIONS, DEST_HEADINGS  # noqa: E402
from content_offers import OFFERS, POINTS_TITLE, SEE_TITLE  # noqa: E402
from content_main import (  # noqa: E402
    ABOUT, CONTACT, ENQUIRY, HOME, PACKAGES, PRIVACY, SERVICES, TERMS, UI,
)

ROOT = Path(__file__).resolve().parent.parent
LANGS = ("en", "id")
FONTS = ("https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,wght@0,500;0,600;1,500"
         "&family=Jost:wght@400;500&display=swap")
WORDMARK = '<span class="brand-word">KOMODO &amp; KO.</span>'


def esc(s):
    return html.escape(s, quote=True)


class Page:
    """Knows the current language and where the page sits, so it can build relative links."""

    def __init__(self, lang, path):
        self.lang, self.path = lang, path
        depth = path.count("/")
        self.up_lang = "../" * depth
        self.up_site = "../" * (depth + (lang == "id"))

    def t(self, v):
        return v[self.lang] if isinstance(v, dict) else v

    def link(self, p):
        return self.up_lang + p

    def asset(self, p):
        return self.up_site + "assets/" + p

    def other_lang(self):
        return self.up_site + ("id/" if self.lang == "en" else "") + self.path


def pic_style(pg, kind, slug, pic):
    """Real photo if assets/img/<kind>/<slug>.jpg exists, otherwise a crop of a stand-in photo."""
    for ext in ("jpg", "jpeg", "webp", "png"):
        f = ROOT / "assets" / "img" / kind / f"{slug}.{ext}"
        if f.exists():
            rel = f"img/{kind}/{slug}.{ext}"
            return f"background-image:url('{pg.asset(rel)}?v={ver(rel)}');background-size:cover;background-position:center"
    src, pos, size = pic
    rel = f"img/{src}.jpg"
    return f"background-image:url('{pg.asset(rel)}?v={ver(rel)}');background-size:{size};background-position:{pos}"


WA_ICON = ('<svg viewBox="0 0 24 24" aria-hidden="true" fill="currentColor"><path d="M12 2a10 10 0 0 0-8.6 15.1L2 22l5-1.3A10 10 0 1 0 12 2zm0 18.2'
           'a8.2 8.2 0 0 1-4.2-1.2l-.3-.2-3 .8.8-2.9-.2-.3A8.2 8.2 0 1 1 12 20.2zm4.5-6.1c-.2-.1-1.5-.7-1.7-.8s-.4-.1-.6.1-.7.8-.8 1-.3.2-.5.1'
           'a6.7 6.7 0 0 1-3.3-2.9c-.3-.4.3-.4.8-1.4a.5.5 0 0 0 0-.5l-.8-1.8c-.2-.5-.4-.4-.6-.4h-.5a1 1 0 0 0-.7.3 3 3 0 0 0-.9 2.2 5.2 5.2 0 0 0 1.1 2.8'
           ' 11.9 11.9 0 0 0 4.6 4c1.7.7 2.4.8 3.2.7a2.8 2.8 0 0 0 1.8-1.3 2.3 2.3 0 0 0 .2-1.3c-.1-.1-.3-.2-.5-.3z"/></svg>')
MAIL_ICON = ('<svg viewBox="0 0 24 24" aria-hidden="true" fill="none" stroke="currentColor" stroke-width="1.5"><rect x="3" y="5" width="18" height="14"/>'
             '<path d="m3.5 6.5 8.5 6.5 8.5-6.5"/></svg>')
CHEV_L = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.3" aria-hidden="true"><path d="M15 5l-7 7 7 7"/></svg>'
CHEV_R = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.3" aria-hidden="true"><path d="M9 5l7 7-7 7"/></svg>'


# ---------------------------------------------------------------------------
# Shared layout
# ---------------------------------------------------------------------------
def lang_switch(pg):
    t = pg.t
    en = '<span>EN</span>' if pg.lang == "en" else f'<a href="{pg.other_lang()}" hreflang="en" lang="en">EN</a>'
    id_ = '<span>ID</span>' if pg.lang == "id" else f'<a href="{pg.other_lang()}" hreflang="id" lang="id">ID</a>'
    return f'<div class="lang" aria-label="{esc(t(UI["lang_label"]))}">{en}<i></i>{id_}</div>'


def sub_href(pg, s, a):
    """Link to an offer's own page when it has one, otherwise to its anchor on the service page."""
    if f"{s['slug']}/{a}" in OFFERS:
        return pg.link(f"services/{s['slug']}/{a}.html")
    return pg.link(f"services/{s['slug']}.html") + "#" + a


def nav(pg):
    t = pg.t
    svc_cols = []
    for s in SERVICES:
        subs = "" if s.get("steps") else "".join(
            f'<a class="sub" href="{sub_href(pg, s, a)}">{esc(t(n))}</a>' for a, n, _ in s["items"])
        svc_cols.append(f'<div><h4><a href="{pg.link("services/" + s["slug"] + ".html")}">{esc(t(s["name"]))}</a></h4>{subs}</div>')
    pkg_links = "".join(f'<a class="sub" href="{pg.link("packages/" + p["slug"] + ".html")}">{esc(t(p["name"]))}</a>' for p in PACKAGES)
    dest_links = "".join(f'<a class="sub" href="{pg.link("destinations/" + d["slug"] + ".html")}">{esc(t(d["name"]))}</a>' for d in DESTINATIONS)

    def cols_panel(intro, links, all_href, all_label):
        return (f'<div class="dd dd-cols"><div class="dd-in"><div class="dd-intro"><p>{esc(t(intro))}</p>'
                f'<a class="link" href="{all_href}">{esc(t(all_label))}</a></div><div class="dd-links">{links}</div></div></div>')

    def item(label, panel):
        return (f'<li class="has-dd"><button class="menu-btn" aria-expanded="false" aria-haspopup="true"><span>{esc(t(label))}</span>'
                f'<i class="chev" aria-hidden="true"></i></button>{panel}</li>')

    svc_panel = (f'<div class="dd dd-mega"><div class="dd-in">{"".join(svc_cols)}'
                 f'<div class="dd-foot"><a class="link" href="{pg.link("services/index.html")}">{esc(t(UI["all_services"]))}</a></div></div></div>')
    brand = (f'<a class="brand" href="{pg.link("index.html")}" aria-label="Komodo &amp; Ko. {esc(t(UI["home"]))}">'
             f'<span class="mark" aria-hidden="true"></span>{WORDMARK}</a>')

    desktop = f"""
<header class="nav"><div class="nav-in">
  <nav aria-label="Main"><ul class="menu">
    {item(UI["nav_services"], svc_panel)}
    {item(UI["nav_packages"], cols_panel(UI["dd_packages"], pkg_links, pg.link("packages/index.html"), UI["all_packages"]))}
    {item(UI["nav_destinations"], cols_panel(UI["dd_destinations"], dest_links, pg.link("destinations/index.html"), UI["all_destinations"]))}
  </ul></nav>
  {brand}
  <div class="nav-right">{lang_switch(pg)}<a class="btn btn-line" href="{pg.link("enquiry.html")}">{esc(t(UI["nav_enquiry"]))}</a>
    <button class="burger" aria-label="{esc(t(UI["menu"]))}" aria-expanded="false"><i></i></button></div>
</div></header>"""

    m_svc = "".join(
        f'<h5><a href="{pg.link("services/" + s["slug"] + ".html")}">{esc(t(s["name"]))}</a></h5>'
        + ("" if s.get("steps") else "".join(f'<a class="sub" href="{sub_href(pg, s, a)}">{esc(t(n))}</a>' for a, n, _ in s["items"]))
        for s in SERVICES)
    drawer = f"""
<div class="drawer" role="dialog" aria-modal="true" aria-label="{esc(t(UI["menu"]))}">
  <div class="drawer-top"><a class="brand" href="{pg.link("index.html")}"><span class="mark" aria-hidden="true"></span>{WORDMARK}</a>
    <button class="drawer-close" aria-label="{esc(t(UI["close"]))}">&times;</button></div>
  <div class="drawer-body">
    <details><summary>{esc(t(UI["nav_services"]))}<i class="chev" aria-hidden="true"></i></summary><div class="grp">{m_svc}</div></details>
    <details><summary>{esc(t(UI["nav_packages"]))}<i class="chev" aria-hidden="true"></i></summary><div class="grp">{pkg_links}</div></details>
    <details><summary>{esc(t(UI["nav_destinations"]))}<i class="chev" aria-hidden="true"></i></summary><div class="grp">{dest_links}</div></details>
    <a class="btn btn-ivory" href="{pg.link("enquiry.html")}">{esc(t(UI["nav_enquiry"]))}</a>
    {lang_switch(pg)}
  </div>
</div>"""
    return desktop + drawer


def footer(pg):
    t = pg.t
    socials = "".join(f'<li><a href="{u}" target="_blank" rel="noopener">{n}</a></li>' for n, u in CONTACT["social"])
    return f"""
<footer class="footer"><div class="wrap">
  <div class="f-crest"><span class="mark" aria-hidden="true"></span>{WORDMARK}<p>{esc(t(UI["footer_tagline"]))}</p></div>
  <div class="f-grid">
    <div><h3>{esc(t(UI["footer_enquiry"]))}</h3><ul class="f-list">
      <li><a href="mailto:{CONTACT["email_enquiry"]}">{CONTACT["email_enquiry"]}</a></li>
      <li><small>WhatsApp</small><a href="https://wa.me/{CONTACT["whatsapp_intl"]}" target="_blank" rel="noopener">{CONTACT["whatsapp_display"]}</a></li></ul></div>
    <div><h3>{esc(t(UI["footer_partner"]))}</h3><ul class="f-list">
      <li><a href="mailto:{CONTACT["email_partner"]}">{CONTACT["email_partner"]}</a></li></ul></div>
    <div><h3>{esc(t(UI["footer_follow"]))} @komodoandko</h3><ul class="f-list">{socials}</ul></div>
    <div><h3>{esc(t(UI["footer_explore"]))}</h3><ul class="f-list">
      <li><a href="{pg.link("services/index.html")}">{esc(t(UI["nav_services"]))}</a></li>
      <li><a href="{pg.link("packages/index.html")}">{esc(t(UI["nav_packages"]))}</a></li>
      <li><a href="{pg.link("destinations/index.html")}">{esc(t(UI["nav_destinations"]))}</a></li>
      <li><a href="{pg.link("about.html")}">{esc(t(UI["about"]))}</a></li></ul></div>
  </div>
  <div class="f-bottom"><span>&copy; 2026 Komodo &amp; Ko. {esc(t(UI["rights"]))}</span>
    <nav aria-label="Legal"><a href="{pg.link("privacy.html")}">{esc(t(UI["privacy"]))}</a><a href="{pg.link("terms.html")}">{esc(t(UI["terms"]))}</a></nav></div>
</div></footer>"""


def ver(rel):
    """Short content hash so browsers load the new file after every change."""
    import hashlib
    return hashlib.md5((ROOT / "assets" / rel).read_bytes()).hexdigest()[:8]


def layout(pg, title, desc, body, home_page=False, scripts=()):
    js = "".join(f'<script src="{pg.asset(s)}?v={ver(s)}" defer></script>' for s in ("js/main.js",) + tuple(scripts))
    return f"""<!doctype html>
<html lang="{pg.lang}">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>{esc(title)}</title>
<meta name="description" content="{esc(desc)}">
<meta name="theme-color" content="#283926">
<link rel="alternate" hreflang="en" href="{pg.up_site + pg.path}">
<link rel="alternate" hreflang="id" href="{pg.up_site + 'id/' + pg.path}">
<link rel="icon" href="{pg.asset("img/logo.jpg")}">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="{FONTS}">
<link rel="stylesheet" href="{pg.asset("css/style.css")}?v={ver("css/style.css")}">
</head>
<body class="{'home' if home_page else 'inner'}">
<a class="skip" href="#main">Skip to content</a>
{nav(pg)}
<main id="main">
{body}
</main>
{footer(pg)}
{js}
</body>
</html>
"""


def page_hero(pg, title, lead=None, crumbs=(), style=None):
    t = pg.t
    cr = [f'<a href="{pg.link("index.html")}">{esc(t(UI["home"]))}</a>']
    for label, href in crumbs:
        cr.append('<span aria-hidden="true">/</span>')
        cr.append(f'<a href="{href}">{esc(label)}</a>' if href else f'<span aria-current="page">{esc(label)}</span>')
    bg = f'<div class="bg" style="{style}"></div>' if style else ""
    cls = "page-hero" + ("" if style else " plain")
    ld = f'<p class="lead">{esc(lead)}</p>' if lead else ""
    return (f'<section class="{cls}">{bg}<div><h1>{esc(title)}</h1>{ld}</div>'
            f'<nav class="crumbs" aria-label="Breadcrumb">{"".join(cr)}</nav></section>')


def ed_card(href, title, style, desc=None, meta=None, link_label=None):
    m = f'<span class="meta">{esc(meta)}</span>' if meta else ""
    d = f"<p>{esc(desc)}</p>" if desc else ""
    lk = f'<span class="link">{esc(link_label)}</span>' if link_label else ""
    return (f'<a class="ed" href="{href}"><div class="pic"><div class="bg" style="{style}"></div></div>'
            f'<div class="txt">{m}<h3>{esc(title)}</h3>{d}{lk}</div></a>')


def cta_band(pg):
    t = pg.t
    return f"""<section class="cta"><div class="bg" style="{pic_style(pg, "pages", "cta", ("padar-island", "50% 60%", "cover"))}"></div>
  <div><h2>{esc(t(UI["cta_title"]))}</h2><p>{esc(t(UI["cta_text"]))}</p>
  <div class="btns"><a class="btn btn-ivory" href="{pg.link("enquiry.html")}">{esc(t(UI["plan_now"]))}</a>
  <a class="btn btn-line light" href="https://wa.me/{CONTACT["whatsapp_intl"]}" target="_blank" rel="noopener">{WA_ICON}{esc(t(UI["chat_wa"]))}</a></div></div>
</section>"""


# ---------------------------------------------------------------------------
# Reusable blocks
# ---------------------------------------------------------------------------
def services_grid(pg):
    t = pg.t
    return '<div class="grid g3">' + "".join(
        ed_card(pg.link(f"services/{s['slug']}.html"), t(s["name"]), pic_style(pg, "services", s["slug"], s["pic"]),
                t(s["short"]), link_label=t(UI["discover"]))
        for s in SERVICES) + "</div>"


def services_index_block(pg):
    t = pg.t
    media = "".join(f'<div class="bg{" on" if i == 0 else ""}" style="{pic_style(pg, "services", s["slug"], s["pic"])}"></div>'
                    for i, s in enumerate(SERVICES))
    rows = "".join(
        f'<a href="{pg.link("services/" + s["slug"] + ".html")}" data-i="{i}" class="{"on" if i == 0 else ""}">'
        f'<div class="thumb" style="{pic_style(pg, "services", s["slug"], s["pic"])}"></div>'
        f'<h3>{esc(t(s["name"]))}</h3><span class="go" aria-hidden="true"></span><p>{esc(t(s["short"]))}</p></a>'
        for i, s in enumerate(SERVICES))
    return f'<div class="svc"><div class="svc-media" aria-hidden="true">{media}</div><div class="svc-list">{rows}</div></div>'


def package_grid(pg, only_home=False, cls="pk", exclude=None):
    t = pg.t
    items = [p for p in PACKAGES if (p.get("home") or not only_home) and p["slug"] != exclude]
    return f'<div class="grid {cls}">' + "".join(
        ed_card(pg.link(f"packages/{p['slug']}.html"), t(p["name"]), pic_style(pg, "packages", p["slug"], p["pic"]),
                meta=t(p["duration"]), link_label=t(UI["view_package"]))
        for p in items) + "</div>"


def dest_card(pg, d, desc=True):
    t = pg.t
    return ed_card(pg.link(f"destinations/{d['slug']}.html"), t(d["name"]), pic_style(pg, "destinations", d["slug"], d["pic"]),
                   t(d["short"]) if desc else None)


# ---------------------------------------------------------------------------
# Home
# ---------------------------------------------------------------------------
def home(pg):
    t = pg.t
    H = HOME
    vision = "<br>".join(" ".join(f'<span class="w">{esc(w)}</span>' for w in t(line).split()) for line in H["vision_lines"])
    acct = " ".join(f'<span class="w">{esc(w)}</span>' for w in t(H["acct"]).split())
    spots = "".join(
        f'<div class="spot" data-x="{x}" data-y="{y}" role="button" tabindex="0"><span class="dot"></span>'
        f'<span class="lbl">{esc(t(lab))}<em>{esc(t(val))}</em></span></div>'
        for x, y, lab, val in H["hotspots"])
    feats = "".join(f'<a href="{pg.link("services/" + s["slug"] + ".html")}">{esc(t(s["name"]))}</a>' for s in SERVICES)
    why = "".join(f"<div><h3>{esc(t(a))}</h3><p>{esc(t(b))}</p></div>" for a, b in H["why"])
    rail = "".join(dest_card(pg, d) for d in DESTINATIONS)

    body = f"""
<section id="story" aria-label="Komodo &amp; Ko.">
 <div class="stage">
  <div class="cam"><img class="plate" src="{pg.asset("img/padar-island.jpg")}?v={ver("img/padar-island.jpg")}" alt="View over the bays of Padar Island in Komodo National Park, with boats at anchor"><div class="mist"></div></div>
  <div class="veil"></div>
  <div class="shade"></div>
  <div class="fog" aria-hidden="true"><i class="f0"></i><i class="f1"></i><i class="f2"></i></div>

  <div class="layer L0"><div class="hero-copy">
    <span class="label">{esc(t(UI["hero_label"]))}</span>
    <h1><span class="ln"><span>{esc(t(H["h1a"]))} {esc(t(H["h1b"]))}</span></span></h1>
  </div></div>

  <div class="cam camF" aria-hidden="true"><img class="plateF" src="{pg.asset("img/padar-island.jpg")}?v={ver("img/padar-island.jpg")}" alt=""></div>

  <div class="layer L1">
    <div class="veil-b"></div>
    <div class="hud"><span class="hud-name">{esc(t(DESTINATIONS[2]["name"]))}</span>
      <pre>LAT    8.6534&deg; S
LON  119.5714&deg; E
{esc(t(UI["hud_park"]))}</pre></div>
    <div class="caption"><p>{esc(t(H["tagline"]))}</p>
      <a class="btn btn-ivory" href="{pg.link("enquiry.html")}">{esc(t(UI["plan_now"]))}</a></div>
    <div class="hint" aria-hidden="true">{esc(t(UI["scroll"]))}<i></i></div>
  </div>

  <div class="layer L2" style="visibility:hidden"><div class="vision">
    <span class="label">{esc(t(UI["promise"]))}</span>
    <h2>{vision}</h2>
    <p>{esc(t(H["vision_p"]))}</p>
  </div></div>

  <div class="layer L3" style="visibility:hidden"><p class="acct">{acct}</p><div class="spots">{spots}</div></div>

  <div class="night"></div>
  <div class="layer L4" style="visibility:hidden"><div class="station">
    <div class="dragon"><img src="{pg.asset("img/komodo-dragon.jpg")}?v={ver("img/komodo-dragon.jpg")}" alt="A Komodo dragon resting with its tongue out">
      <div class="dcard"><h4>{esc(t(H["dragon_card_title"]))}</h4><div class="latin">{H["dragon_card_latin"]}</div>
        <div class="big"><span data-num>0</span><small>m</small></div><p>{esc(t(H["dragon_note"]))}</p></div></div>
    <div class="st-copy"><h2>{esc(t(H["station_title"]))}</h2><p>{esc(t(H["station_p"]))}</p>
      <a class="btn btn-line light" href="#services">{esc(t(H["services_title"]))}</a></div>
  </div></div>

  <div class="prog" aria-hidden="true"><i></i></div>
 </div>
</section>

<div class="panel">
 <section class="sec" id="services"><div class="wrap">
  <div class="sec-head"><h2>{esc(t(H["services_title"]))}</h2><p>{esc(t(H["services_p"]))}</p></div>
  {services_index_block(pg)}
 </div></section>

 <section class="sec tight" id="packages"><div class="wrap">
  <div class="sec-head"><h2>{esc(t(H["packages_title"]))}</h2><a class="link" href="{pg.link("packages/index.html")}">{esc(t(UI["all_packages"]))}</a></div>
  {package_grid(pg, only_home=True)}
 </div></section>

 <section class="sec paper" id="destinations">
  <div class="wrap"><div class="sec-head"><h2>{esc(t(H["destinations_title"]))}</h2>
   <div class="rail-ctl"><button type="button" data-rail="-1" aria-label="{esc(t(UI["prev"]))}">{CHEV_L}</button><button type="button" data-rail="1" aria-label="{esc(t(UI["next"]))}">{CHEV_R}</button></div></div></div>
  <div class="rail" tabindex="0" aria-label="{esc(t(H["destinations_title"]))}">{rail}</div>
 </section>

 <section class="why"><div class="wrap"><h2>{esc(t(H["why_title"]))}</h2><div class="why-grid">{why}</div></div></section>

 <section class="sec"><div class="wrap"><div class="about">
  <div class="crest" role="img" aria-label="Komodo &amp; Ko."><span class="mark"></span>{WORDMARK}</div>
  <div><h2>{esc(t(H["about_title"]))}</h2><p>{esc(t(H["about_p"]))}</p>
   <a class="btn btn-line" href="{pg.link("about.html")}">{esc(t(UI["learn_more"]))}</a></div>
 </div></div></section>

 {cta_band(pg)}
</div>"""
    return layout(pg, t(H["title"]), t(H["desc"]), body, home_page=True, scripts=("js/story.js",))


# ---------------------------------------------------------------------------
# Services
# ---------------------------------------------------------------------------
def services_index(pg):
    t = pg.t
    title = t(UI["nav_services"])
    body = page_hero(pg, title, t(HOME["services_p"]), [(title, None)], pic_style(pg, "services", "index", ("padar-island", "50% 70%", "cover"))) + \
        f'<section class="sec"><div class="wrap">{services_grid(pg)}</div></section>' + cta_band(pg)
    return layout(pg, f"{title} | Komodo & Ko.", t(HOME["services_p"]), body)


def service_page(pg, s):
    t = pg.t
    name = t(s["name"])
    hero = page_hero(pg, name, t(s["short"]), [(t(UI["nav_services"]), pg.link("services/index.html")), (name, None)],
                     pic_style(pg, "services", s["slug"], s["pic"]))
    has_offers = any(f"{s['slug']}/{a}" in OFFERS for a, _, _ in s["items"])
    if s.get("steps"):
        items = "".join(f'<article class="item" id="{a}"><div class="num">{i}</div><h3>{esc(t(n))}</h3><p>{esc(t(d))}</p></article>'
                        for i, (a, n, d) in enumerate(s["items"], 1))
        grid = f'<div class="items">{items}</div>'
    elif has_offers:
        # every offer has its own page: show them as picture cards
        cards = "".join(
            ed_card(sub_href(pg, s, a), t(n), offer_pic(pg, s, a), t(d), link_label=t(UI["discover"]))
            for a, n, d in s["items"])
        grid = f'<div class="grid {"g4" if len(s["items"]) == 4 else "g3"} offers">{cards}</div>'
    else:
        def one(a, n, d):
            img = ROOT / "assets" / "img" / "services" / s["slug"] / f"{a}.jpg"
            pic = (f'<div class="item-pic"><div class="bg" style="{pic_style(pg, "services/" + s["slug"], a, s["pic"])}"></div></div>'
                   if img.exists() else "")
            return f'<article class="item{" has-pic" if pic else ""}" id="{a}">{pic}<h3>{esc(t(n))}</h3><p>{esc(t(d))}</p></article>'
        items = "".join(one(a, n, d) for a, n, d in s["items"])
        cls = "items three" if len(s["items"]) in (3, 7) else "items"
        grid = f'<div class="{cls}">{items}</div>'
    body = (hero + f'<div class="wrap"><div class="svc-intro"><h2>{esc(name)}</h2><p>{esc(t(s["intro"]))}</p></div>'
            f'{grid}</div>' + cta_band(pg))
    return layout(pg, f"{name} | Komodo & Ko.", t(s["short"]), body)


def offer_pic(pg, s, a):
    o = OFFERS.get(f"{s['slug']}/{a}")
    kind, slug = o["img"] if o else ("services", s["slug"])
    return pic_style(pg, kind, slug, s["pic"])


def related_card(pg, path):
    """Card for a 'you may also like' link, given a page path such as packages/honeymoon.html."""
    t = pg.t
    parts = path[:-5].split("/")
    if parts[0] == "packages":
        p = next(x for x in PACKAGES if x["slug"] == parts[1])
        return ed_card(pg.link(path), t(p["name"]), pic_style(pg, "packages", p["slug"], p["pic"]), meta=t(p["duration"]))
    if parts[0] == "destinations":
        d = next(x for x in DESTINATIONS if x["slug"] == parts[1])
        return dest_card(pg, d)
    s = next(x for x in SERVICES if x["slug"] == parts[1])
    if len(parts) == 3:
        a, n, d = next(x for x in s["items"] if x[0] == parts[2])
        return ed_card(pg.link(path), t(n), offer_pic(pg, s, a), t(d))
    return ed_card(pg.link(path), t(s["name"]), pic_style(pg, "services", s["slug"], s["pic"]), t(s["short"]))


def offer_page(pg, s, item):
    t = pg.t
    a, n, d = item
    o = OFFERS[f"{s['slug']}/{a}"]
    name, sname = t(n), t(s["name"])
    hero = page_hero(pg, name, t(o["lead"]),
                     [(t(UI["nav_services"]), pg.link("services/index.html")), (sname, pg.link(f"services/{s['slug']}.html")), (name, None)],
                     offer_pic(pg, s, a))
    paras = "".join(f'<p class="{"lead" if i == 0 else ""}">{esc(t(x))}</p>' for i, x in enumerate(o["paras"]))
    points = "".join(f"<li>{esc(t(x))}</li>" for x in o["points"])
    side = f"""<aside class="facts"><p class="facts-name">{esc(sname)}</p><p class="facts-text">{esc(t(d))}</p>
      <a class="btn btn-solid" href="{pg.link("enquiry.html")}">{esc(t(UI["plan_now"]))}</a>
      <a class="btn btn-line" href="https://wa.me/{CONTACT["whatsapp_intl"]}" target="_blank" rel="noopener">{WA_ICON}WhatsApp</a></aside>"""
    see = "".join(related_card(pg, p) for p in o.get("see", []))
    others = [x for x in s["items"] if x[0] != a and f"{s['slug']}/{x[0]}" in OFFERS]
    more = "".join(ed_card(sub_href(pg, s, x[0]), t(x[1]), offer_pic(pg, s, x[0])) for x in others[:4])
    body = (hero + f'<div class="wrap"><div class="pkg"><div><div class="block offer-text">{paras}</div>'
            f'<div class="block"><h2>{esc(t(POINTS_TITLE))}</h2><ul class="ticks">{points}</ul></div></div>{side}</div></div>'
            + (f'<section class="sec paper"><div class="wrap"><div class="sec-head"><h2>{esc(t(SEE_TITLE))}</h2></div>'
               f'<div class="grid {"g4" if len(o["see"]) == 4 else "g3"}">{see}</div></div></section>' if see else "")
            + (f'<section class="sec"><div class="wrap"><div class="sec-head"><h2>{esc(sname)}</h2>'
               f'<a class="link" href="{pg.link("services/" + s["slug"] + ".html")}">{esc(t(UI["view_all"]))}</a></div>'
               f'<div class="grid g4">{more}</div></div></section>' if more else "")
            + cta_band(pg))
    return layout(pg, f"{name} | {sname} | Komodo & Ko.", t(o["lead"]), body)


# ---------------------------------------------------------------------------
# Packages
# ---------------------------------------------------------------------------
def packages_index(pg):
    t = pg.t
    title = t(UI["nav_packages"])
    body = page_hero(pg, title, t(UI["dd_packages"]), [(title, None)], pic_style(pg, "packages", "index", ("padar-island", "70% 60%", "cover"))) + \
        f'<section class="sec"><div class="wrap">{package_grid(pg, cls="g3")}</div></section>' + cta_band(pg)
    return layout(pg, f"{title} | Komodo & Ko.", t(UI["dd_packages"]), body)


def package_page(pg, p):
    t = pg.t
    name = t(p["name"])
    hero = page_hero(pg, name, t(p["duration"]), [(t(UI["nav_packages"]), pg.link("packages/index.html")), (name, None)],
                     pic_style(pg, "packages", p["slug"], p["pic"]))
    blocks = [f'<div class="block"><p class="lead">{esc(t(p["intro"]))}</p></div>']
    if p.get("options"):
        opts = "".join(f"<div><h3>{esc(t(a))}</h3><p>{esc(t(b))}</p></div>" for a, b in p["options"])
        blocks.append(f'<div class="block"><div class="options">{opts}</div></div>')
    if p.get("days"):
        days = "".join(f'<li><b>{esc(t(UI["day"]))} {i}</b><p>{esc(t(d))}</p></li>' for i, d in enumerate(p["days"], 1))
        blocks.append(f'<div class="block"><h2>{esc(t(UI["sample_route"]))}</h2><ol class="days">{days}</ol><p class="note">{esc(t(UI["sample_note"]))}</p></div>')
    if p.get("highlights"):
        hl = "".join(f"<li>{esc(t(x))}</li>" for x in p["highlights"])
        blocks.append(f'<div class="block"><ul class="ticks">{hl}</ul></div>')
    if p.get("includes"):
        inc = "".join(f"<li>{esc(t(x))}</li>" for x in p["includes"])
        blocks.append(f'<div class="block"><h2>{esc(t(UI["typically_includes"]))}</h2><ul class="ticks">{inc}</ul><p class="note">{esc(t(UI["includes_note"]))}</p></div>')
    price = t(p["price"]) if p.get("price") else t(UI["price_on_request"])
    facts = f"""<aside class="facts"><dl>
      <div><dt>{esc(t(UI["duration"]))}</dt><dd>{esc(t(p["duration"]))}</dd></div>
      <div><dt>{esc(t(UI["boat"]))}</dt><dd>{esc(t(p["boat"]))}</dd></div>
      <div><dt>{esc(t(UI["trip_type"]))}</dt><dd>{esc(t(p["type"]))}</dd></div>
      <div><dt>{esc(t(UI["price"]))}</dt><dd class="price">{esc(price)}</dd></div></dl>
      <a class="btn btn-solid" href="{pg.link("enquiry.html")}">{esc(t(UI["plan_now"]))}</a>
      <a class="btn btn-line" href="https://wa.me/{CONTACT["whatsapp_intl"]}" target="_blank" rel="noopener">{WA_ICON}WhatsApp</a></aside>"""
    others = (f'<section class="sec paper"><div class="wrap"><div class="sec-head"><h2>{esc(t(UI["other_packages"]))}</h2></div>'
              f'{package_grid(pg, cls="g4", exclude=p["slug"])}</div></section>')
    body = hero + f'<div class="wrap"><div class="pkg"><div>{"".join(blocks)}</div>{facts}</div></div>' + others + cta_band(pg)
    return layout(pg, f"{name} | Komodo & Ko.", t(p["intro"])[:155], body)


# ---------------------------------------------------------------------------
# Destinations
# ---------------------------------------------------------------------------
def destinations_index(pg):
    t = pg.t
    title = t(UI["nav_destinations"])
    body = page_hero(pg, title, t(UI["dd_destinations"]), [(title, None)], pic_style(pg, "destinations", "index", ("padar-island", "50% 50%", "cover"))) + \
        '<section class="sec"><div class="wrap"><div class="grid g3">' + "".join(dest_card(pg, d) for d in DESTINATIONS) + \
        '</div></div></section>' + cta_band(pg)
    return layout(pg, f"{title} | Komodo & Ko.", t(UI["dd_destinations"]), body)


def destination_page(pg, d):
    t = pg.t
    name = t(d["name"])
    hero = page_hero(pg, name, t(d["short"]), [(t(UI["nav_destinations"]), pg.link("destinations/index.html")), (name, None)],
                     pic_style(pg, "destinations", d["slug"], d["pic"]))
    toc, secs = [], []
    for key, head in DEST_HEADINGS:
        h = t(head).format(name=name)
        toc.append(f'<a href="#{key}">{esc(h)}</a>')
        if key == "todo":
            inner = '<ul class="ticks">' + "".join(f"<li>{esc(t(x))}</li>" for x in d["todo"]) + "</ul>"
        else:
            inner = f"<p>{esc(t(d[key]))}</p>"
        secs.append(f'<section id="{key}"><h2>{esc(h)}</h2>{inner}</section>')
    article = (f'<div class="wrap"><div class="article"><nav class="toc" aria-label="{esc(t(UI["on_this_page"]))}">'
               f'<span class="label">{esc(t(UI["on_this_page"]))}</span>{"".join(toc)}</nav>'
               f'<div class="prose">{"".join(secs)}</div></div></div>')
    related = [x for x in DESTINATIONS if x["slug"] != d["slug"]]
    idx = DESTINATIONS.index(d)
    pick = [related[(idx + i) % len(related)] for i in range(4)]
    more = (f'<section class="sec paper"><div class="wrap"><div class="sec-head"><h2>{esc(t(UI["more_destinations"]))}</h2>'
            f'<a class="link" href="{pg.link("destinations/index.html")}">{esc(t(UI["all_destinations"]))}</a></div>'
            '<div class="grid g4">' + "".join(dest_card(pg, x) for x in pick) + "</div></div></section>")
    body = hero + article + more + cta_band(pg)
    return layout(pg, f"{name} | Komodo & Ko.", t(d["what"])[:155], body)


# ---------------------------------------------------------------------------
# Enquiry, About, Legal
# ---------------------------------------------------------------------------
def enquiry_page(pg):
    t = pg.t
    E = ENQUIRY
    title = t(E["title"])
    F = E["fields"]

    def fld(name, typ="text", full=False, area=False, extra=""):
        lab, ph = F[name]
        cls = "field full" if full else "field"
        ctl = (f'<textarea id="f-{name}" name="{name}" placeholder="{esc(t(ph))}" required aria-describedby="e-{name}"></textarea>' if area
               else f'<input id="f-{name}" name="{name}" type="{typ}" placeholder="{esc(t(ph))}" required aria-describedby="e-{name}" {extra}>')
        return (f'<div class="{cls}"><label for="f-{name}">{esc(t(lab))}<span class="req" aria-hidden="true">*</span></label>{ctl}'
                f'<span class="err" id="e-{name}" role="alert"></span></div>')
    cfg = {
        "wa": CONTACT["whatsapp_intl"], "email": CONTACT["email_enquiry"],
        "intro": t(E["msg_intro"]), "subject": t(E["msg_subject"]),
        "labels": {k: t(v[0]) for k, v in F.items()},
        "err": {k: t(v) for k, v in E["errors"].items()},
    }
    steps = "".join(f"<li>{esc(t(x))}</li>" for x in E["next"])
    body = page_hero(pg, title, t(E["intro"]), [(title, None)], pic_style(pg, "pages", "enquiry", ("padar-island", "50% 80%", "cover"))) + f"""
<div class="wrap"><div class="enq">
  <aside class="enq-side"><h2>{esc(t(E["next_title"]))}</h2><ol>{steps}</ol>
    <div class="contact">
      <div><small>WhatsApp</small><a href="https://wa.me/{CONTACT["whatsapp_intl"]}" target="_blank" rel="noopener">{CONTACT["whatsapp_display"]}</a></div>
      <div><small>Email</small><a href="mailto:{CONTACT["email_enquiry"]}">{CONTACT["email_enquiry"]}</a></div>
    </div></aside>
  <form class="form" id="enquiry-form" novalidate data-cfg='{esc(json.dumps(cfg, ensure_ascii=False))}'>
    {fld("name", extra='autocomplete="name"')}
    {fld("phone", "tel", extra='autocomplete="tel" inputmode="tel"')}
    {fld("email", "email", extra='autocomplete="email"')}
    {fld("guests", "number", extra='min="1" inputmode="numeric"')}
    {fld("dates", full=True)}
    {fld("service", full=True, area=True)}
    {fld("budget", full=True)}
    <div class="form-actions">
      <button type="button" class="btn btn-solid" data-send="wa">{WA_ICON}{esc(t(E["send_wa"]))}</button>
      <button type="button" class="btn btn-line" data-send="email">{MAIL_ICON}{esc(t(E["send_email"]))}</button>
    </div>
    <p class="form-note">{esc(t(E["send_note"]))}</p>
    <div class="form-ok" role="status">{esc(t(E["sent"]))}</div>
  </form>
</div></div>"""
    return layout(pg, f"{title} | Komodo & Ko.", t(E["intro"]), body)


def about_page(pg):
    t = pg.t
    title = t(ABOUT["title"])
    paras = "".join(f"<p>{esc(t(x))}</p>" for x in ABOUT["body"])
    why = "".join(f"<div><h3>{esc(t(a))}</h3><p>{esc(t(b))}</p></div>" for a, b in HOME["why"])
    body = page_hero(pg, title, t(ABOUT["lead"]), [(title, None)], pic_style(pg, "pages", "about", ("komodo-dragon", "50% 40%", "cover"))) + f"""
<div class="wrap"><div class="about-body"><span class="label">Komodo &amp; Ko.</span><div class="txt">{paras}</div></div></div>
<section class="why"><div class="wrap"><h2>{esc(t(HOME["why_title"]))}</h2><div class="why-grid">{why}</div></div></section>
{cta_band(pg)}"""
    return layout(pg, f"{title} | Komodo & Ko.", t(ABOUT["lead"]), body)


TERMS_TABLE = [
    ("Booking conditions", "Private Trip", "Open / Share Trip", "Full-Day Speedboat"),
    ("Initial deposit", "50%", "50%", "50%"),
    ("Deposit refundable", "No", "No", "No"),
    ("Final payment deadline", "30 days before", "30 days before", "30 days before"),
    ("Booking within 30 days", "Full payment", "Full payment", "Full payment"),
    ("One-year advance booking", "30% + 20% + balance", "Same", "Same"),
    ("Guest cancellation", "Non-refundable", "Non-refundable", "Non-refundable"),
    ("Replacement guest", "Subject to approval", "Subject to approval", "Subject to approval"),
    ("Minimum participants", "Not stipulated", "10 guests", "10 guests for shared operation"),
    ("Child policy", "Full rate from age 3", "Full rate from age 3", "Full rate from age 3"),
]


def legal_blocks(fname):
    """Turn the plain text of a legal document (_build/legal/*.txt) into (kind, content) blocks."""
    raw = (ROOT / "_build" / "legal" / fname).read_text(encoding="utf-8").replace("​", "").replace("\f", "")
    lines = raw.splitlines()
    while lines and lines[0].strip():      # drop the document title; the page has its own
        lines.pop(0)
    out, para, state = [], [], {"items": None, "type": None}
    n = len(lines)

    def flush_para():
        if para:
            out.append(("p", " ".join(para)))
            para.clear()

    def flush_list():
        if state["items"]:
            out.append((state["type"], state["items"]))
        state["items"] = None

    def is_caps_heading(s):
        m = re.match(r"^\d+\.\s+(.+)$", s)
        return bool(m) and m.group(1) == m.group(1).upper() and any(c.isalpha() for c in m.group(1))

    i = 0
    while i < n:
        ln = lines[i]
        s = ln.strip()
        if not s:
            flush_para()
            j = i + 1
            while j < n and not lines[j].strip():
                j += 1
            if state["items"] is not None and j < n:
                nxt = lines[j]
                ind = len(nxt) - len(nxt.lstrip())
                body = nxt.strip()
                if ind >= 7 and not body.startswith("●") and not re.match(r"\d+\.\s", body):
                    state["items"][-1] += " " + body      # wrapped line of the previous list item
                    i = j + 1
                    continue
                if ind == 0:
                    flush_list()
            i += 1
            continue
        ind = len(ln) - len(ln.lstrip())
        if ind >= 3:
            flush_para()
            m = re.match(r"^(\d+)\.\s*(.+)$", s)
            if s.startswith("●") or m:
                kind = "ul" if s.startswith("●") else "ol"
                if state["items"] is None or state["type"] != kind:
                    flush_list()
                    state["items"], state["type"] = [], kind
                state["items"].append(s.lstrip("●").strip() if kind == "ul" else m.group(2))
            elif state["items"] is not None:
                state["items"][-1] += " " + s
            else:
                para.append(s)
            i += 1
            continue
        flush_list()
        m = re.match(r"^(\d+)\.\s+(.+)$", s)
        nxt_blank = i + 1 >= n or not lines[i + 1].strip()
        if re.match(r"^\d+\.\d+\.\s", s):
            flush_para()
            out.append(("h3", s))
        elif is_caps_heading(s):
            flush_para()
            title = s
            while i + 1 < n and lines[i + 1].strip() and lines[i + 1].strip() == lines[i + 1].strip().upper() \
                    and not re.match(r"^\d", lines[i + 1].strip()):
                i += 1
                title += " " + lines[i].strip()
            out.append(("h2", title.title().replace("'S", "'s").replace(" At A ", " at a ")))
            if "BOOKING CONDITIONS AT A GLANCE" in title:
                out.append(("table", TERMS_TABLE))
                while i + 1 < n and not is_caps_heading(lines[i + 1].strip()):
                    i += 1
        elif m and m.group(2).endswith("?"):
            flush_para()
            out.append(("h3", s))
        elif m and len(s) < 70 and nxt_blank:
            flush_para()
            out.append(("h2", s))
        elif len(s) <= 48 and s[-1] not in ".:,;?)]" and ":" not in s and nxt_blank and (not para or para[-1][-1] in ".:"):
            flush_para()
            out.append(("h4", s))
        else:
            para.append(s)
        i += 1
    flush_para()
    flush_list()
    return out


def legal_page(pg, data, fname):
    t = pg.t
    title = t(data["title"])
    toc, secs, cur, k = [], [], [], 0

    def close():
        if cur:
            secs.append(f'<section id="s{k}">{"".join(cur)}</section>')
            cur.clear()

    for kind, c in legal_blocks(fname):
        if kind == "h2":
            close()
            k += 1
            toc.append(f'<a href="#s{k}">{esc(c)}</a>')
            cur.append(f"<h2>{esc(c)}</h2>")
        elif kind in ("h3", "h4", "p"):
            cur.append(f"<{kind}>{esc(c)}</{kind}>")
        elif kind == "ul":
            cur.append('<ul class="ticks">' + "".join(f"<li>{esc(x)}</li>" for x in c) + "</ul>")
        elif kind == "ol":
            cur.append('<ol class="steps">' + "".join(f"<li>{esc(x)}</li>" for x in c) + "</ol>")
        elif kind == "table":
            head = "".join(f"<th>{esc(x)}</th>" for x in c[0])
            rows = "".join("<tr>" + f"<th>{esc(r[0])}</th>" + "".join(f"<td>{esc(x)}</td>" for x in r[1:]) + "</tr>" for r in c[1:])
            cur.append(f'<div class="table-wrap"><table><thead><tr>{head}</tr></thead><tbody>{rows}</tbody></table></div>')
    close()
    note = f'<p class="legal-note">{esc(t(UI["legal_note"]))}</p>' if pg.lang == "id" else ""
    body = (page_hero(pg, title, None, [(title, None)])
            + f'<div class="wrap"><div class="article legal-doc"><nav class="toc" aria-label="{esc(t(UI["on_this_page"]))}">'
              f'<span class="label">{esc(t(UI["on_this_page"]))}</span>{"".join(toc)}</nav>'
              f'<div class="prose">{note}{"".join(secs)}</div></div></div>')
    return layout(pg, f"{title} | Komodo & Ko.", title, body)


# ---------------------------------------------------------------------------
def build():
    count = 0
    for lang in LANGS:
        base = ROOT if lang == "en" else ROOT / "id"
        pages = {
            "index.html": home,
            "services/index.html": services_index,
            "packages/index.html": packages_index,
            "destinations/index.html": destinations_index,
            "enquiry.html": enquiry_page,
            "about.html": about_page,
            "privacy.html": lambda pg: legal_page(pg, PRIVACY, "privacy.txt"),
            "terms.html": lambda pg: legal_page(pg, TERMS, "terms.txt"),
        }
        for s in SERVICES:
            pages[f"services/{s['slug']}.html"] = (lambda s: lambda pg: service_page(pg, s))(s)
            for it in s["items"]:
                if f"{s['slug']}/{it[0]}" in OFFERS:
                    pages[f"services/{s['slug']}/{it[0]}.html"] = (lambda s, it: lambda pg: offer_page(pg, s, it))(s, it)
        for p in PACKAGES:
            pages[f"packages/{p['slug']}.html"] = (lambda p: lambda pg: package_page(pg, p))(p)
        for d in DESTINATIONS:
            pages[f"destinations/{d['slug']}.html"] = (lambda d: lambda pg: destination_page(pg, d))(d)
        for path, fn in pages.items():
            out = base / path
            out.parent.mkdir(parents=True, exist_ok=True)
            out.write_text(fn(Page(lang, path)), encoding="utf-8")
            count += 1
    write_credits()
    print(f"Built {count} pages.")


def write_credits():
    """Photo credits, generated from _build/photos.tsv (file, Unsplash id, photographer, width)."""
    tsv = ROOT / "_build" / "photos.tsv"
    if not tsv.exists():
        return
    lines = ["# Photo credits", "",
             "All photos are from Unsplash and used under the Unsplash License",
             "(free for commercial use, no permission or credit required): https://unsplash.com/license", "",
             "| File | Photographer | Source |", "|---|---|---|"]
    for row in tsv.read_text(encoding="utf-8").splitlines():
        if not row.strip():
            continue
        key, pid, by = row.split("\t")[:3]
        lines.append(f"| assets/img/{key}.jpg | {by} | https://images.unsplash.com/{pid} |")
    (ROOT / "assets" / "img" / "CREDITS.md").write_text("\n".join(lines) + "\n", encoding="utf-8")


if __name__ == "__main__":
    build()
