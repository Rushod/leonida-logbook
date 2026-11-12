"""News posts. Newest first. Each post: slug, date (YYYY-MM-DD), title, description, figure, body, sources.
build.py turns these into /news/<slug>/ pages, the /news/ listing, the home page block and /news/feed.xml."""
from html import escape as e
import art

AUTHOR = "Adrian R"
AUTHOR_BIO = "Adrian R writes the news for Leonida Logbook and has been playing Grand Theft Auto since the PlayStation 2 days."

POSTS = [
    dict(
        slug="gta-6-xbox-one-cloud-gaming",
        date="2026-11-11",
        title="GTA 6 is coming to Xbox One after all, through cloud streaming",
        desc="Microsoft says Xbox One owners can stream GTA VI through Xbox Cloud Gaming from November 19 at 1am ET. You still have to buy the game.",
        fig=art.cloud,
        body="""
  <p>Xbox One owners are not locked out of GTA VI after all. Microsoft announced on November 10 that the game will stream through Xbox Cloud Gaming from launch day, so it plays on the 2013 console even though it was never built for it.</p>
  <h2>The key facts</h2>
  <ul>
    <li><b>When:</b> streaming starts on November 19 at 1am ET.</li>
    <li><b>Where:</b> Xbox One, plus Xbox Series X|S. On Series X|S, Microsoft recommends playing the installed version for the best picture.</li>
    <li><b>You must buy the game.</b> Microsoft says GTA VI is purchased separately, so streaming does not make it free.</li>
    <li><b>Picture quality:</b> the stream uses Xbox Series S graphics settings. Microsoft has not given a resolution or frame rate.</li>
  </ul>
  <h2>Do you need Game Pass?</h2>
  <p>Microsoft's post does not say which subscription GTA VI streaming needs. It does say that from November 11, players in supported markets can buy cloud playtime to stream supported games without Game Pass, but it does not confirm GTA VI is one of them. Check the game's page on your console before launch day.</p>
  <h2>Who this helps</h2>
  <ul>
    <li><b>Xbox One owners</b> who are not ready to buy a new console.</li>
    <li><b>Series S owners short on space.</b> Streaming needs no download, while the installed game needs up to 212 GB. See the <a href="/storage/">storage guide</a>.</li>
  </ul>
  <h2>The catch</h2>
  <p>Streaming depends on your internet connection. A slow or busy connection means a blurrier picture and input lag, which matters in a shooter. On launch night, demand for the servers will also be at its peak.</p>
  <h2>A bonus most people missed</h2>
  <p>Microsoft's post also lists what comes with a pre-order made before November 19 at 23:59:59: the Vintage Vice City Pack and one month of GTA+, which has to be redeemed within 180 days. See <a href="/editions/">Standard vs Ultimate</a> for the full contents.</p>
  <p>We have updated our <a href="/platforms/">platforms guide</a> to include Xbox One streaming.</p>""",
        sources=[("Xbox Wire: Grand Theft Auto VI comes to Xbox Cloud Gaming", "https://news.xbox.com/en-us/2026/11/10/grand-theft-auto-6-comes-to-xbox-cloud-gaming-november-19/")],
    ),
    dict(
        slug="gta-6-preload-live",
        date="2026-11-11",
        title="GTA 6 preload is live: start times, 212 GB and how to make room",
        desc="Digital GTA VI pre-orders can download now on PS5 and Xbox Series X|S, and boxed copies follow on November 12. What to do before launch.",
        fig=art.preload_bar,
        body="""
  <p>You can now download GTA VI ahead of launch. Digital preloading opened on November 10, two days earlier than an early pre-order listing suggested.</p>
  <h2>When preload opened</h2>
  <div class="scroll"><table>
    <tr><th>Version</th><th>Preload starts</th></tr>
    <tr><td><b>PS5, digital</b></td><td>November 10, midnight in your local time zone</td></tr>
    <tr><td><b>Xbox Series X|S, digital</b></td><td>November 10, midnight GMT everywhere (7pm ET on November 9)</td></tr>
    <tr><td><b>Boxed copies</b></td><td>November 12, once you redeem the download code inside</td></tr>
  </table></div>
  <p>Preloading does not let you play early. The game stays locked until it unlocks in your region. See <a href="/release-time/">what time GTA 6 unlocks</a>.</p>
  <h2>212 GB, and that is before the patch</h2>
  <p>Rockstar says the download needs up to 212 GB depending on your console. A day-one update will add more. On a 512 GB Xbox Series S, that is well over half of the usable space.</p>
  <h2>Do these three things tonight</h2>
  <ul>
    <li><b>Check your free space</b> and clear room. The <a href="/storage/">storage guide</a> shows how much each console really has.</li>
    <li><b>Start the download early.</b> At these sizes, a slow connection can take a full day. Step-by-step instructions are in the <a href="/preload/">preload guide</a>.</li>
    <li><b>Leave the console in rest mode</b> with internet access on, so it keeps downloading and grabs the patch.</li>
  </ul>
  <h2>No space at all?</h2>
  <p>Xbox One and Xbox Series owners can also stream GTA VI through Xbox Cloud Gaming from launch day, with no download. <a href="/news/gta-6-xbox-one-cloud-gaming/">Here is how that works</a>.</p>""",
        sources=[("GamesRadar+: Rockstar confirms GTA 6 is 212GB", "https://gamesradar.com/games/grand-theft-auto/rockstar-confirms-gta-6-is-212gb-pre-loading-opens-earlier-than-previously-announced-for-digital-orders"),
                 ("Xbox Wire: Grand Theft Auto VI comes to Xbox Cloud Gaming", "https://news.xbox.com/en-us/2026/11/10/grand-theft-auto-6-comes-to-xbox-cloud-gaming-november-19/")],
    ),
    dict(
        slug="gta-6-leaked-cheats-explained",
        date="2026-11-11",
        title="Those \"leaked\" GTA 6 cheat codes are GTA V's. Here's what we know",
        desc="Viral posts claim GTA 6 cheat codes have leaked. The lists are GTA V's codes, and Rockstar has not confirmed any cheats for GTA VI.",
        fig=art.cheats_check,
        body="""
  <p>If your feed is full of "GTA 6 cheat codes may have just leaked" posts this week, here is the short answer: the codes in them are from GTA V, and none has been confirmed for GTA VI.</p>
  <h2>What the viral lists actually show</h2>
  <p>The posts going around show familiar names: PAINKILLER for invincibility, BUZZOFF for an attack helicopter, phone numbers starting 1-999. Those are GTA V's cheats, released in 2013. Even the posts themselves usually admit in the caption that nothing is confirmed.</p>
  <h2>What Rockstar has said</h2>
  <p>Nothing. Rockstar has not said whether GTA VI has cheat codes at all, or how you would enter them.</p>
  <h2>Will GTA V's cheats work in GTA VI?</h2>
  <p>Probably not as they are. Rockstar usually changes cheats between games, and GTA VI changes things the old codes relied on. There is no weapon wheel, for example, which makes a "give all weapons" cheat work differently. What could return is the idea: an in-game phone exists, and Rockstar used phone numbers for cheats in GTA V.</p>
  <h2>How we will handle it on launch day</h2>
  <ul>
    <li>From November 19, we test GTA V's codes in GTA VI and mark each one as working or not.</li>
    <li>Any real GTA VI cheat gets added with the button inputs for PS5 and Xbox.</li>
    <li>Nothing goes on the list until we have seen it work.</li>
  </ul>
  <p>Until then, every GTA V code with PS5, Xbox and PC inputs is on our <a href="/cheats/">cheats page</a>, ready to try.</p>""",
        sources=[],
    ),
]


def nice_date(iso):
    y, m, d = iso.split("-")
    months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
    return f"{months[int(m) - 1]} {int(d)}, {y}"


def post_page(p):
    srcs = ""
    if p["sources"]:
        srcs = "<h2>Sources</h2><ul>" + "".join(f'<li><a href="{e(u)}" rel="noopener">{e(t)}</a></li>' for t, u in p["sources"]) + "</ul>"
    more = "".join(f'<a class="tile" href="/news/{q["slug"]}/"><em>{nice_date(q["date"])}</em><h3>{e(q["title"])}</h3></a>' for q in POSTS if q is not p)[:4000]
    return f"""
  <article class="prose news">
  <span class="eyebrow">News</span><h1>{e(p["title"])}</h1>
  <p class="byline">By <a href="/about/#adrian">{AUTHOR}</a> · <time datetime="{p["date"]}">{nice_date(p["date"])}</time></p>
  <p class="lede">{e(p["desc"])}</p>
  {p["fig"]()}
  {p["body"]}
  {srcs}
  </article>
  <div class="stack"><h2>More news</h2><div class="tiles">{more}</div><p><a class="btn ghost" href="/news/">All news</a></p></div>"""


def tile(p):
    return f'<a class="tile" href="/news/{p["slug"]}/"><em>{nice_date(p["date"])}</em><h3>{e(p["title"])}</h3><span>{e(p["desc"])}</span></a>'


def listing():
    return f"""
  <div class="stack"><span class="eyebrow">News</span><h1>GTA 6 news</h1>
  <p class="lede">The GTA VI stories that matter to players, and what each one means for you.</p></div>
  <div class="tiles">{"".join(tile(p) for p in POSTS)}</div>
  <p class="note"><a href="/news/feed.xml">Subscribe to the news feed</a></p>"""


def home_block():
    return f'<div class="stack"><h2>Latest news</h2><div class="tiles">{"".join(tile(p) for p in POSTS[:3])}</div><p><a class="btn ghost" href="/news/">All news</a></p></div>'


def pages(brand):
    out = [("/news/", "GTA 6 News: Latest Updates for Players" + brand, "The latest GTA VI news and what it means for players: launch, preload, platforms, cheats and more.", listing())]
    for p in POSTS:
        out.append((f"/news/{p['slug']}/", p["title"] + brand, p["desc"], post_page(p)))
    return out


def meta(path):
    """Extra structured-data fields for news posts."""
    for p in POSTS:
        if path == f"/news/{p['slug']}/":
            return {"@type": "NewsArticle", "headline": p["title"], "datePublished": p["date"] + "T09:00:00-05:00",
                    "dateModified": p["date"] + "T09:00:00-05:00",
                    "author": {"@type": "Person", "name": AUTHOR, "url": "https://leonidalogbook.com/about/#adrian"}}
    return None


def feed(site):
    items = "".join(
        f"<item><title>{e(p['title'])}</title><link>{site}/news/{p['slug']}/</link><guid>{site}/news/{p['slug']}/</guid>"
        f"<pubDate>{rfc822(p['date'])}</pubDate><description>{e(p['desc'])}</description></item>" for p in POSTS)
    return (f'<?xml version="1.0" encoding="UTF-8"?>\n<rss version="2.0"><channel><title>Leonida Logbook news</title><link>{site}/news/</link>'
            f"<description>GTA VI news for players</description><language>en</language>{items}</channel></rss>\n")


def rfc822(iso):
    import datetime
    d = datetime.datetime.strptime(iso, "%Y-%m-%d").replace(hour=14)
    return d.strftime("%a, %d %b %Y %H:%M:%S +0000")
