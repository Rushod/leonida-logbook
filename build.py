#!/usr/bin/env python3
"""Builds the static site into ./public from content/data.json and src/.
Run:  python3 build.py   (then commit and push; Cloudflare deploys ./public)"""
import json, shutil, urllib.parse
from html import escape as e
from pathlib import Path
from articles import ARTICLES, GUIDE_LINKS, ALL_GUIDES, GUIDES_PAGE
from articles2 import ARTICLES2
from extra import EXTRA

ROOT = Path(__file__).parent
OUT = ROOT / "public"
D = json.loads((ROOT / "content/data.json").read_text())
SITE = "https://leonidalogbook.com"
CONTACT = "contact@leonidalogbook.com"
TODAY = "2026-11-11"
ADSENSE = "ca-pub-6848827685182284"


BG = "#120824"
_sky = [(150,46,38),(200,34,70),(238,52,52),(294,30,96),(328,58,60),(390,40,84),(434,36,44),(474,54,112),(532,30,66),(566,44,88),(614,50,54),(668,34,104),(706,56,72),(766,38,48),(808,46,92),(858,32,62),(894,60,80),(958,40,50),(1002,48,68)]
_palms = [(18,1.25),(96,0.95),(168,1.1),(292,0.78),(868,0.8),(960,1.12),(1040,0.95),(1104,1.3)]
SCENE = (
    '<svg class="scene" viewBox="0 0 1200 240" preserveAspectRatio="xMidYMax slice" aria-hidden="true"><defs>'
    '<linearGradient id="sun" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#fff3b0"/><stop offset=".55" stop-color="#ffb14a"/><stop offset="1" stop-color="#ff5fa2"/></linearGradient>'
    '<radialGradient id="glow"><stop offset="0" stop-color="#ffd98a" stop-opacity=".6"/><stop offset="1" stop-color="#ffd98a" stop-opacity="0"/></radialGradient>'
    '<g id="palm"><path d="M50 172C47 126 55 86 50 42" fill="none" stroke-width="5" stroke-linecap="round"/>'
    '<path d="M50 42Q24 14 0 38Q28 28 50 42ZM50 42Q30 4 8 8Q34 14 50 42ZM50 42Q48 6 30-8Q56 6 50 42ZM50 42Q66 2 90 0Q66 14 50 42ZM50 42Q80 16 102 34Q74 28 50 42ZM50 42Q78 36 96 62Q70 44 50 42ZM50 42Q24 38 6 64Q30 46 50 42Z"/></g></defs>'
    '<circle cx="600" cy="205" r="240" fill="url(#glow)"/><circle cx="600" cy="208" r="88" fill="url(#sun)"/>'
    '<g fill="#3a1166">' + "".join(f'<rect x="{x}" y="{222-h}" width="{w}" height="{h}"/>' for x, w, h in _sky) + '</g>'
    f'<g fill="{BG}" stroke="{BG}"><rect x="0" y="218" width="1200" height="24" stroke="none"/>'
    + "".join(f'<use href="#palm" transform="translate({x} {226-172*s:.0f}) scale({s})"/>' for x, s in _palms) + '</g></svg>'
)

NAV = [("/", "Home"), ("/map/", "Map"), ("/guides/", "Guides"), ("/guide/", "What's new"), ("/tracker/", "Tracker"), ("/cheats/", "Cheats"), ("/gear/", "Gear")]


def layout(path, title, desc, body, index=True):
    nav = "".join(f'<a href="{h}"{" aria-current=\"page\"" if h == path else ""}>{t}</a>' for h, t in NAV)
    url = SITE + path
    robots = "" if index else '<meta name="robots" content="noindex">\n'
    head_extra = ""
    if "<!--map-->" in body:
        top, body = body.split("<!--map-->", 1)
        sky = top
        head_extra = '<link rel="stylesheet" href="/assets/map-app.css">\n'
    elif "<!--hero-end-->" in body:
        hero, body = body.split("<!--hero-end-->", 1)
        sky = f'<div class="sky sky-hero"><div class="wrap">{hero}</div>{SCENE}</div>'
    else:
        sky = f'<div class="sky" aria-hidden="true">{SCENE}</div>'
    return f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<title>{e(title)}</title>
<meta name="description" content="{e(desc)}">
{robots}<link rel="canonical" href="{url}">
<meta property="og:type" content="website">
<meta property="og:site_name" content="Leonida Logbook">
<meta property="og:title" content="{e(title)}">
<meta property="og:description" content="{e(desc)}">
<meta property="og:url" content="{url}">
<meta property="og:image" content="{SITE}/og.png">
<meta name="twitter:card" content="summary_large_image">
<meta name="theme-color" content="#120824">
<link rel="icon" href="/favicon.svg" type="image/svg+xml">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Anton&family=Barlow+Condensed:wght@600;700&family=Barlow:wght@400;500;600&family=Yellowtail&display=swap">
<link rel="stylesheet" href="/assets/site.css">
{head_extra}<script async src="https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js?client={ADSENSE}" crossorigin="anonymous"></script>
</head>
<body>
<header><div class="wrap">
  <a class="brand" href="/">Leonida <i>Logbook</i><small>UNOFFICIAL GTA VI COMPANION</small></a>
  <nav aria-label="Sections">{nav}</nav>
</div></header>
{sky}
<main class="wrap"><div class="view">
{body}
</div></main>
<footer><div class="wrap stack">
  <nav aria-label="Site"><a href="/launch/">Launch details</a><a href="/about/">About</a><a href="/privacy/">Privacy</a><a href="/gear/">Gear</a></nav>
  <p>Leonida Logbook is an unofficial fan site. It is not affiliated with, endorsed by or connected to Rockstar Games or Take-Two Interactive. Grand Theft Auto and all related names are trademarks of their owners.</p>
  <p>As an Amazon Associate I earn from qualifying purchases. Launch details last checked {D['last_checked']}.</p>
</div></footer>
<script src="/assets/site.js" defer></script>
</body>
</html>
"""


def check(key, title, sub=None):
    small = f"<small>{e(sub)}</small>" if sub else ""
    return f'<li><label><input type="checkbox" id="c-{key}" data-key="{key}"><span>{e(title)}{small}</span></label></li>'


def pairs(rows):
    return "".join(f"<div><b>{e(a)}</b><span>{e(b)}</span></div>" for a, b in rows)


def star(fill):
    f = "currentColor" if fill else "none"
    return f'<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M12 2.5l2.9 6.2 6.6.8-4.9 4.6 1.3 6.6L12 17.4l-5.9 3.3 1.3-6.6L2.5 9.5l6.6-.8z" fill="{f}" stroke="currentColor" stroke-width="1.8" stroke-linejoin="round"/></svg>'


# ---------- pages ----------
prep = "".join(check(f"prep-{i}", t, s) for i, (t, s) in enumerate(D["prep"]))
HOME = f"""
  <div class="stack">
    <span class="eyebrow" id="heroEyebrow">Thursday, November 19, 2026</span>
    <h1 id="heroTitle">GTA VI unlocks in</h1>
    <div class="clock" id="clock">
      <div><b id="cd">--</b><span>Days</span></div><div><b id="ch">--</b><span>Hours</span></div>
      <div><b id="cm">--</b><span>Minutes</span></div><div><b id="cs">--</b><span>Seconds</span></div>
    </div>
    <p class="note" id="clockNote">Counting down to midnight on November 19 on your device's clock. Unlock times can differ by region, so check your console store for yours.</p>
  </div>
<!--hero-end-->
  <div class="facts">
    <div><span>Platforms</span><b>PS5 · Xbox Series X|S</b></div>
    <div><span>Standard</span><b>$79.99</b></div>
    <div><span>Ultimate</span><b>$99.99</b></div>
    <div><span>Storage</span><b>Up to 212 GB</b></div>
    <div><span>Preload</span><b>Open now</b></div>
  </div>
  <div class="cols">
    <div class="panel stack" data-group="prep">
      <div class="grouphead"><h2>Launch-day checklist</h2><span class="count"></span></div>
      <div class="bar"><i></i></div>
      <ul class="check">{prep}</ul>
      <p class="note">Your ticks are saved in this browser.</p>
    </div>
    <div class="tiles" style="grid-template-columns:minmax(0,1fr)">
      <a class="tile" href="/map/"><em>Explore</em><h3>Interactive map</h3><span>The six regions of Leonida, with markers you can tick off.</span></a>
      <a class="tile" href="/launch/"><em>Before you buy</em><h3>Release date, price and preload</h3><span>Key dates, both editions and how much space you need.</span></a>
      <a class="tile" href="/guide/"><em>Read before you play</em><h3>GTA 6 vs GTA 5: what's new</h3><span>The ten biggest changes in one table, plus tips for your first hours.</span></a>
      <a class="tile" href="/tracker/"><em>Track</em><h3>Progress tracker</h3><span>Regions and activities now. Missions and collectibles from launch day.</span></a>
      <a class="tile" href="/cheats/"><em>Launch day</em><h3>Cheat codes</h3><span>Verified codes only, added as they are tested.</span></a>
    </div>
  </div>"""

LAUNCH = """
  <div class="stack"><span class="eyebrow">Launch details</span><h1>GTA VI release date, price and preload</h1>
  <p class="lede">The facts you need before November 19, checked against launch coverage on November 10, 2026.</p></div>
  <div class="cols">
    <div class="stack">
      <h2>Key dates</h2>
      <div class="scroll"><table>
        <tr><th>When</th><th>What happens</th></tr>
        <tr><td class="n">Nov 10</td><td>Preload opens for digital pre-orders</td></tr>
        <tr><td class="n">Nov 12</td><td>Preload opens for boxed copies, which contain a download code and no disc</td></tr>
        <tr><td class="n">Nov 19</td><td>Release day on PS5 and Xbox Series X|S</td></tr>
        <tr><td class="n">Nov 20</td><td>Buy before this date to get the Vintage Vice City Pack</td></tr>
      </table></div>
      <h2>Editions</h2>
      <div class="scroll"><table>
        <tr><th>Edition</th><th>Price</th><th>What you get</th></tr>
        <tr><td><b>Standard</b></td><td class="n">$79.99</td><td>The full game</td></tr>
        <tr><td><b>Ultimate</b></td><td class="n">$99.99</td><td>The game plus extra vehicles, weapons, clothing, shops and a safehouse garage, including the '67 Vapid Dominator Buggy, '95 Grotti Cheetah and Shitzu Squalo</td></tr>
        <tr><td><b>Pre-order bonus</b></td><td class="n">Free</td><td>Vintage Vice City Pack: a two-tone '55 Vapid Stanier, Shore Court Garage, and two outfits and hairstyles each for Jason and Lucia</td></tr>
      </table></div>
      <p class="note">There is no PC version at launch. Rockstar has not announced one.</p>
    </div>
    <div class="panel stack">
      <h3>Do you have the space?</h3>
      <p class="big">212 GB</p>
      <p>That is the most the game needs, depending on your console. It does not include the day-one update.</p>
      <div class="scroll"><table>
        <tr><th>Console</th><th>Usable storage</th></tr>
        <tr><td>PS5 (original)</td><td class="n">667 GB</td></tr>
        <tr><td>PS5 Slim</td><td class="n">842 GB</td></tr>
        <tr><td>PS5 Pro</td><td class="n">1.89 TB</td></tr>
        <tr><td>Xbox Series X</td><td class="n">802 GB</td></tr>
        <tr><td>Xbox Series S (512 GB)</td><td class="n">364 GB</td></tr>
      </table></div>
      <a class="btn" href="/gear/">Storage upgrades</a>
    </div>
  </div>"""

CHANGES = [  # (area, GTA V, GTA VI, link, link text)
    ("Main characters", "Three leads: Michael, Franklin and Trevor, each with their own money.", "Two leads, Jason and Lucia, who work as a pair and share one bank account.", "/characters/", "Characters"),
    ("Wanted level", "Five stars. Police know who you are as soon as you commit a crime.", "Six stars, and only if someone sees or reports the crime. Hollow stars mean police do not know it was you yet.", "/wanted-level/", "Wanted level guide"),
    ("Weapons", "Carry every gun you own through the weapon wheel.", "Carry two handguns and two long guns. The rest stay in your car's trunk or an Ammu-Nation locker.", "/weapons/", "Weapons guide"),
    ("Stealing cars", "Press a button and you are in.", "Older cars need a slim jim or a smashed window. Modern ones need a key cloner or phone hacking tool.", "/vehicles/", "Vehicles guide"),
    ("Keeping a car", "Any car you park in your garage is yours.", "A stolen car disappears unless you register it at Pay & Spray. Cars also need fuel or charging.", "/vehicles/", "Vehicles guide"),
    ("Making money", "Big story heists that pay out at set points.", "Rob any store whenever you like, and sell stolen goods and cars to fences.", "/robberies/", "Robbery guide"),
    ("Getting around", "Taxis, and driving everywhere.", "The RydeMe app, buses and a working train line.", "/map/", "Interactive map"),
    ("Getting stronger", "Stats rise slowly as you do activities.", "Gym sessions, and strength only rises if you train three days in a row.", "/gym/", "Gym guide"),
    ("Online", "GTA Online arrived about two weeks after launch.", "No online mode at launch and no date announced.", "/online/", "Online at launch"),
    ("Story length", "About 30 to 35 hours for the main story.", "About 80 hours, going by one Rockstar developer's playthrough.", "/story-length/", "Story length"),
]
TIPS = [
    ("Bank your cash", "Getting arrested costs you the money you are carrying. Deposit it at an ATM before anything risky."),
    ("Mask up before a robbery", "Cameras and witnesses cannot identify a masked face, so you may get hollow stars instead of solid ones."),
    ("Register cars you want to keep", "Stolen cars vanish unless you register them at Pay & Spray. High-end cars need their tracker removed at a fence first."),
    ("Watch your fuel", "Cars and bikes can run dry, which is the worst thing that can happen in a chase."),
    ("Keep long guns out of sight", "Walking around with a rifle on show makes people nervous and draws police."),
    ("Use your trunk as an armory", "You carry only four guns. Store spares and outfits in your car."),
    ("Change clothes to lose the police", "Police chase a description. A new outfit, haircut or car can break it."),
    ("Train three days in a row", "One gym session does nothing for strength. Plan for three consecutive in-game days."),
]
rows = "".join(f'<tr><td><b>{e(a)}</b></td><td>{e(v)}</td><td>{e(vi)}</td><td><a href="{l}">{e(lt)}</a></td></tr>' for a, v, vi, l, lt in CHANGES)
tips = "".join(f'<li><b>{e(t)}.</b> {e(d)}</li>' for t, d in TIPS)
GUIDE = f"""
  <div class="stack"><span class="eyebrow">What's new</span><h1>GTA 6 vs GTA 5: what's new</h1>
  <p class="lede">If you played GTA V, a lot works differently in GTA VI. This page sums up the ten biggest changes in one table, with a link to the full guide for each, plus tips for your first hours.</p>
  <p class="note">Based on hands-on previews. Every row is re-checked in the finished game on November 19.</p></div>
  <div class="stack"><h2>The 10 biggest changes</h2>
  <div class="scroll"><table class="vs"><tr><th>Area</th><th>GTA V</th><th>GTA VI</th><th>Full guide</th></tr>{rows}</table></div></div>
  <div class="panel stack"><h2>Tips for your first hours</h2><ol class="tips">{tips}</ol></div>
  <div class="stack"><h2>Know the world</h2>
  <div class="tiles">
    <a class="tile" href="/map/"><em>Explore</em><h3>Interactive map</h3><span>900+ places across Leonida you can search and tick off.</span></a>
    <a class="tile" href="/characters/"><em>The story</em><h3>Who's who</h3><span>Jason, Lucia and the people around them.</span></a>
    <a class="tile" href="/activities/"><em>Things to do</em><h3>Activities</h3><span>All twelve reported side activities.</span></a>
    <a class="tile" href="/cheats/"><em>Launch day</em><h3>Cheat codes</h3><span>GTA V's codes to try on November 19.</span></a>
  </div></div>
"""

groups = ""
for g in D["track"]:
    if "locked" in g:
        groups += f'<div class="panel"><div class="grouphead"><h3>{e(g["title"])}</h3><span class="tag">At launch</span></div><div class="locked" style="border-top:0">{e(g["locked"])}</div></div>'
    else:
        items = "".join(check(f'{g["id"]}-{i}', t) for i, t in enumerate(g["items"]))
        groups += f'<div class="panel" data-group="{g["id"]}"><div class="grouphead"><h3>{e(g["title"])}</h3><span class="count"></span></div><div class="bar"><i></i></div><ul class="check">{items}</ul></div>'
TRACKER = f"""
  <div class="stack"><span class="eyebrow">Your save file, on paper</span><h1>GTA VI progress tracker</h1>
  <p class="lede">Tick things off as you play. Missions, collectibles and wildlife lists go live once the game is out and the lists can be verified.</p></div>
  <div class="cols">
    <div class="stack">{groups}</div>
    <div class="stack">
      <div class="panel stack">
        <h3>Overall</h3>
        <p class="big" id="totalPct">0%</p>
        <div class="bar"><i id="totalBar"></i></div>
        <p class="note" id="totalNote">Your ticks are saved in this browser.</p>
        <div id="resetWrap"><button class="btn ghost" id="resetBtn" type="button">Reset progress</button></div>
        <div id="resetConfirm" hidden class="stack"><p class="note">Clear every tick on this device?</p><div style="display:flex;gap:8px;flex-wrap:wrap"><button class="btn" id="resetYes" type="button">Yes, clear</button><button class="btn ghost" id="resetNo" type="button">Keep</button></div></div>
      </div>
      <div class="panel stack">
        <h3>Logbook Pro <span class="tag">Coming soon</span></h3>
        <p>No ads, progress synced across your phone and console browser, and extra map filters.</p>
      </div>
    </div>
  </div>"""

from cheats import render as gta5_cheats
if D["cheats"]:
    rows = "".join(f"<tr><td><b>{e(c['name'])}</b></td><td class=\"n\">{e(c['ps5'])}</td><td class=\"n\">{e(c['xbox'])}</td><td>{e(c['effect'])}</td></tr>" for c in D["cheats"])
    verified = f'<h2>Tested in GTA VI</h2><div class="scroll"><table><tr><th>Cheat</th><th>PS5</th><th>Xbox</th><th>Effect</th></tr>{rows}</table></div>'
else:
    verified = ''
CHEATS = f"""
  <div class="stack"><span class="eyebrow">PS5 · Xbox · PC</span><h1>GTA 6 cheat codes</h1>
  <p class="lede">No GTA VI cheats are confirmed yet. Below are all of GTA V's cheat codes, the most likely to return, with buttons for PS5 and Xbox, PC codes and phone numbers.</p></div>
  {verified}
  {gta5_cheats()}"""

tiles = ""
for name, blurb, q in D["gear"]:
    url = "https://www.amazon.com/s?k=" + urllib.parse.quote(q) + "&tag=" + D["affiliate_tag"]
    tiles += f'<a class="tile" href="{e(url)}" target="_blank" rel="noopener sponsored"><h3>{e(name)}</h3><span>{e(blurb)}</span><em>Search on Amazon</em></a>'
GEAR = f"""
  <div class="stack"><span class="eyebrow">Launch gear</span><h1>Make room for 212 GB</h1>
  <p class="lede">Storage is the one upgrade many players need for this game. Links open an Amazon search in a new tab.</p></div>
  <div class="tiles">{tiles}</div>
  <p class="note">As an Amazon Associate I earn from qualifying purchases.</p>"""

ABOUT = f"""
  <div class="prose"><span class="eyebrow">About</span><h1>About Leonida Logbook</h1>
  <p class="lede">An independent fan-made companion for Grand Theft Auto VI.</p>
  <p>Leonida Logbook is built for players who want quick, checked answers: when the game unlocks, how its systems work, what is left to find, and which cheat codes are real.</p>
  <h2>How information is checked</h2>
  <p>Before launch, pages are based on official announcements and press previews, and each page says so. From launch day, guides, cheat codes and checklists are tested against the game before they are listed. Unconfirmed reports are labelled as unconfirmed and never presented as fact.</p>
  <h2>Who runs it</h2>
  <p>The site is run by an independent fan. It is not affiliated with, endorsed by or connected to Rockstar Games or Take-Two Interactive.</p>
  <h2>How the site is funded</h2>
  <p>The site earns money from advertising and from affiliate links. As an Amazon Associate I earn from qualifying purchases. This does not change what you pay.</p>
  <h2>Contact</h2>
  <p>Corrections and questions: {CONTACT}</p></div>"""

PRIVACY = f"""
  <div class="prose"><span class="eyebrow">Privacy</span><h1>Privacy policy</h1>
  <p class="note">Last updated November 11, 2026</p>
  <p>This policy explains what information Leonida Logbook (leonidalogbook.com) handles when you visit.</p>
  <h2>What the site stores</h2>
  <ul>
    <li><b>Checklist progress.</b> Your ticks are saved in your own browser's local storage. They are not sent to us, and you can clear them with the Reset button or by clearing your browser's site data.</li>
    <li><b>No accounts.</b> The site has no sign-up, and we do not ask for your name, email address or payment details.</li>
  </ul>
  <h2>Services that receive data when you visit</h2>
  <ul>
    <li><b>Cloudflare</b> hosts the site and processes technical data such as your IP address and browser type to deliver pages and protect against abuse.</li>
    <li><b>Google Fonts</b> supplies the typefaces. Your browser requests them from Google, which receives your IP address.</li>
  </ul>
  <h2>Advertising</h2>
  <p>The site may show ads served by Google AdSense. When ads are shown, third-party vendors, including Google, use cookies to serve ads based on your prior visits to this and other websites. Google's use of advertising cookies enables it and its partners to serve ads based on your visits to this site and other sites on the internet.</p>
  <p>You can opt out of personalized advertising at <a href="https://www.google.com/settings/ads" rel="noopener">Google Ads Settings</a>, or opt out of some third-party vendors' cookies at <a href="https://www.aboutads.info/choices/" rel="noopener">aboutads.info</a>.</p>
  <h2>Affiliate links</h2>
  <p>Some links go to Amazon. As an Amazon Associate I earn from qualifying purchases. When you follow one of these links, Amazon may set cookies and handles your data under its own privacy notice.</p>
  <h2>Children</h2>
  <p>The site covers a game rated for mature audiences and is not directed at children under 13. We do not knowingly collect personal information from children.</p>
  <h2>Changes</h2>
  <p>If this policy changes, the new version is posted on this page with a new date.</p>
  <h2>Contact</h2>
  <p>Questions about this policy: {CONTACT}</p></div>"""

NOTFOUND = """
  <div class="stack"><span class="eyebrow">404</span><h1>Wrong turn</h1>
  <p class="lede">That page does not exist. It may have moved when the site was reorganized.</p>
  <div><a class="btn" href="/">Back to home</a></div></div>"""

HOME += ALL_GUIDES
LAUNCH += GUIDE_LINKS

PAGES = [
    ("/", "GTA 6 Countdown, Guide and Progress Tracker | Leonida Logbook", "Live GTA VI launch countdown, release date and preload details, a guide to the new systems, a progress tracker and verified cheat codes.", HOME),
    ("/launch/", "GTA 6 Release Date, Price, Preload and File Size | Leonida Logbook", "GTA VI releases November 19, 2026 on PS5 and Xbox Series X|S. Preload dates, edition prices, pre-order bonus and the 212 GB storage requirement.", LAUNCH),
    ("/guide/", "GTA 6 vs GTA 5: Every Big Gameplay Change | Leonida Logbook", "The ten biggest differences between GTA 6 and GTA 5, from the six-star wanted level to the four-gun limit, plus tips for your first hours.", GUIDE),
    ("/tracker/", "GTA 6 Progress Tracker and Checklist | Leonida Logbook", "Free GTA VI progress tracker. Tick off regions and activities now; missions, wildlife and collectibles are added at launch.", TRACKER),
    ("/cheats/", "GTA 6 Cheat Codes for PS5, Xbox and PC (GTA V Codes to Try) | Leonida Logbook", "No GTA VI cheats are confirmed yet. All 34 GTA V cheat codes for PS5, Xbox and PC, with phone numbers, ready to test in GTA VI on November 19, 2026.", CHEATS),
    ("/gear/", "Storage Upgrades and Accessories for GTA 6 | Leonida Logbook", "GTA VI needs up to 212 GB. Storage upgrades for PS5 and Xbox Series X|S, plus controller docks and headsets.", GEAR),
    ("/about/", "About | Leonida Logbook", "Leonida Logbook is an independent, unofficial fan companion for Grand Theft Auto VI.", ABOUT),
    ("/privacy/", "Privacy Policy | Leonida Logbook", "What information Leonida Logbook handles when you visit, and the advertising and affiliate services it uses.", PRIVACY),
]

PAGES += ARTICLES + ARTICLES2 + EXTRA
PAGES.append(("/guides/", "GTA 6 Guides: Launch, Gameplay and Platform Answers | Leonida Logbook", "Every Leonida Logbook guide in one place: release time, preload, storage, editions, PC, online, frame rate, map, characters and more.", GUIDES_PAGE))

# ---------- write ----------
keep = {"og.png", "tiles"}
for p in OUT.iterdir():
    if p.name in keep:
        continue
    shutil.rmtree(p) if p.is_dir() else p.unlink()
(OUT / "assets").mkdir(parents=True)
shutil.copy(ROOT / "src/site.css", OUT / "assets/site.css")
shutil.copy(ROOT / "src/site.js", OUT / "assets/site.js")
shutil.copy(ROOT / "map-app/dist/map-app.js", OUT / "assets/map-app.js")
shutil.copy(ROOT / "map-app/dist/map-app.css", OUT / "assets/map-app.css")
(OUT / "data").mkdir(exist_ok=True)
shutil.copy(ROOT / "content/locations.json", OUT / "data/locations.json")
for path, title, desc, body in PAGES:
    d = OUT / path.strip("/")
    d.mkdir(parents=True, exist_ok=True)
    (d / "index.html").write_text(layout(path, title, desc, body))
(OUT / "404.html").write_text(layout("/404.html", "Page not found | Leonida Logbook", "Page not found.", NOTFOUND, index=False))
(OUT / "robots.txt").write_text(f"User-agent: *\nAllow: /\n\nSitemap: {SITE}/sitemap.xml\n")
urls = "".join(f"  <url><loc>{SITE}{p}</loc><lastmod>{TODAY}</lastmod></url>\n" for p, *_ in PAGES)
(OUT / "sitemap.xml").write_text(f'<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n{urls}</urlset>\n')
(OUT / "ads.txt").write_text(f"google.com, {ADSENSE[3:]}, DIRECT, f08c47fec0942fa0\n")
(OUT / "favicon.svg").write_text('<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 32 32"><defs><linearGradient id="g" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#3a1268"/><stop offset=".6" stop-color="#e2437f"/><stop offset="1" stop-color="#ffb14a"/></linearGradient></defs><rect width="32" height="32" rx="6" fill="url(#g)"/><path d="M16 5l3.2 6.9 7.3.9-5.4 5.1 1.4 7.3L16 21.5l-6.5 3.7 1.4-7.3-5.4-5.1 7.3-.9z" fill="#fff"/></svg>\n')
print("built", len(PAGES), "pages")
