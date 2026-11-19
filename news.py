"""News posts. Newest first. Each post: slug, date (YYYY-MM-DD), title, description, figure, body, sources.
build.py turns these into /news/<slug>/ pages, the /news/ listing, the home page block and /news/feed.xml."""
from html import escape as e
import art

AUTHOR = "Adrian R"
AUTHOR_BIO = "Adrian R writes the news for Leonida Logbook and has been playing Grand Theft Auto since the PlayStation 2 days."

POSTS = [
    dict(
        slug="gta-6-cheats-confirmed-how-to-unlock",
        date="2026-11-19",
        title="GTA 6 does have cheats: 61 of them, and you have to beat the story first",
        desc="GTA VI's cheats are entered on the phone with a D-pad code, unlock after the main story, and turn off trophies and saving. The 11 codes two guides agree on so far.",
        fig=art.cheats_real,
        body="""
  <p>Good news for anyone who spent launch week typing GTA V codes into the wrong game: GTA VI does have cheats. Bad news for anyone hoping to spawn a tank on day one: you have to finish the main story before any of them work.</p>
  <p>Guides from GamesRadar+ and Red Bull Gaming, both updated since the game unlocked, agree on how the system works. Rockstar itself has not published a list.</p>
  <h2>How cheats work in GTA VI</h2>
  <ul>
    <li><b>61 cheats in five groups:</b> player, combat, vehicle spawns, environment and screen filters.</li>
    <li><b>No phone numbers and no PC-style typing.</b> Press Up on the D-pad to take out the phone, hold L1 and R1 (LB and RB on Xbox), then enter a D-pad sequence. The codes are the same on PS5 and Xbox.</li>
    <li><b>They are earned.</b> Every cheat stays locked until the Jason and Lucia story is complete. Most then need a challenge or stat as well, such as shooting-range medals, workouts or shopping challenges. GamesRadar+ says the Cheats list sits in the pause menu's Progress tab.</li>
    <li><b>There's a price.</b> Activating a cheat turns off trophies and achievements, and saving, for the rest of that session.</li>
  </ul>
  <h2>Codes found so far</h2>
  <p>Most codes are still unknown: GamesRadar+ lists 19 of 61, and its list is still growing. We have added the <b>11 codes that both guides give identically</b> to our <a href="/cheats/">cheats page</a>, including the $250,000 money cheat, Infinite Ammo and Body Armor. We have not tested them ourselves yet, so we mark them as reported rather than verified.</p>
  <h2>Do the GTA V codes work?</h2>
  <p>No. GTA VI uses its own sequences, and the old phone numbers do nothing. That matches what <a href="/news/gta-6-leaked-cheats-explained/">we said about the "leaked" lists</a> last week.</p>
  <h2>Why it matters</h2>
  <p>Locking cheats behind the ending makes them a post-game toy rather than a shortcut. With the main story at 91 missions (see our <a href="/missions/">missions page</a>), most players will not see a single cheat for weeks.</p>""",
        sources=[("GamesRadar+: All GTA 6 cheats and how to unlock them for PS5 and Xbox", "https://www.gamesradar.com/games/grand-theft-auto/gta-6-cheats/"),
                 ("Red Bull Gaming: GTA 6 cheats, all the codes and how to unlock them", "https://www.redbull.com/int-en/gta-6-cheat-codes"),
                 ("IBTimes Australia: GTA 6 cheat codes and how to unlock them", "https://www.ibtimes.com.au/gta-6-cheat-codes-how-unlock-use-cheats-1878899")],
    ),
    dict(
        slug="gta-6-xbox-series-x-s-digital-foundry",
        date="2026-11-19",
        title="GTA 6 on Xbox tested: Series X matches PS5, Series S runs at 720p and drops to 20 fps",
        desc="Digital Foundry's Xbox results are in. Series X looks and runs much like a base PS5. Series S renders at 720p and often sits below 30 fps.",
        fig=art.xbox_fps,
        body="""
  <p>The last gap in the launch performance picture is filled. Digital Foundry has now tested GTA VI on Xbox Series X and Series S, and the two consoles have very different stories.</p>
  <h2>Xbox Series X: about the same as a PS5</h2>
  <ul>
    <li><b>Resolution:</b> about 1440p internally, the same as PS5.</li>
    <li><b>Frame rate:</b> a 30 fps target it mostly holds, with dropped frames in especially busy chases and firefights.</li>
    <li><b>Verdict:</b> VGC sums up DF's view as performing similarly to the standard PS5. PS5 Pro is still the best place to play.</li>
  </ul>
  <h2>Xbox Series S: the weakest version</h2>
  <ul>
    <li><b>Resolution:</b> 720p internally by DF's counts, output at 1080p. Pure Xbox reports Rockstar told Wccftech it uses AMD's FSR 4 upscaling, and DF says the final image looks a lot better than 720p suggests.</li>
    <li><b>Frame rate:</b> cutscenes and walking are usually fine, but slow driving sits in the mid-to-upper 20s for long stretches, typical combat holds in the mid-20s, and the hardest fights fall to about 20 fps.</li>
    <li><b>What's cut:</b> it keeps ray-traced reflections and detailed hair, but lighting is less precise, reflections are softer, shadows messier, and clouds, water and draw distance are lower quality.</li>
    <li><b>Verdict:</b> DF's Oliver Mackenzie said he'd "advise players to play the game on other console platforms for now."</li>
  </ul>
  <h2>What if Series S is all you have?</h2>
  <ul>
    <li><b>It's still playable.</b> DF admires how much of the game survives, and it is the same GTA VI, just rougher.</li>
    <li><b>Turn on VRR if your TV has it.</b> Variable refresh rate can make small dips feel less jarring. That's general advice: DF's results don't cover it.</li>
    <li><b>A fix is not promised.</b> Rockstar has not announced a performance patch, and VGC says it's unclear how much Series S can improve after launch.</li>
  </ul>
  <p>All four consoles side by side are in our <a href="/frame-rate/">frame rate guide</a>. Planning to play on Series S? Check <a href="/storage/">how much space you need</a> too.</p>""",
        sources=[("VGC: GTA 6 Xbox Series S performance analysis says significant frame drops are a problem", "https://www.videogameschronicle.com/news/gta-6-xbox-series-s-performance-analysis-admires-the-effort-but-says-significant-frame-drops-are-a-problem/"),
                 ("Pure Xbox: Three big takeaways from Digital Foundry's GTA 6 analysis for Xbox Series X|S", "https://www.purexbox.com/news/2026/11/three-big-takeaways-from-digital-foundrys-gta-6-analysis-for-xbox-series-xs"),
                 ("Pure Xbox: GTA 6 comparison shows difference between Xbox Series X and Series S", "https://www.purexbox.com/news/2026/11/gta-6-comparison-shows-difference-between-xbox-series-x-and-series-s"),
                 ("TweakTown: GTA 6 drops to 720p and below 30 fps on one console", "https://www.tweaktown.com/news/114779/gta-6-drops-to-720p-and-below-30-fps-on-one-console-gamers-advised-to-play-elsewhere/index.html")],
    ),
    dict(
        slug="gta-6-out-in-new-zealand",
        date="2026-11-18",
        title="GTA 6 is out in New Zealand: what players are finding inside the game",
        desc="Kiwi players got GTA VI first, at 11:00 UTC on November 18. Here's what the first hours show, from the prologue to Snapmatic, with spoilers kept behind a warning.",
        fig=art.nz_first,
        body="""
  <p>The 13-year wait is over in at least one country. GTA VI unlocked at midnight on November 19 in New Zealand, which was 11:00 UTC on November 18 (6am Eastern), and streams from the first players filled X and Twitch within minutes. Everyone else unlocks at their own local midnight. See <a href="/release-time/">your exact unlock time</a>.</p>
  <h2>The basics, now confirmed in the released game</h2>
  <ul>
    <li><b>Platforms:</b> PS5 and Xbox Series X|S. No PC version at launch.</li>
    <li><b>Single-player only.</b> There is no online mode on day one. See <a href="/online/">what we know about online</a>.</li>
    <li><b>Download:</b> up to 212 GB. New Zealand's main broadband network operator, Chorus, called the size unprecedented, and said one download is more than a quarter of what an average home uses in a month.</li>
  </ul>
  <h2>What the opening hours look like (no story spoilers)</h2>
  <ul>
    <li><b>It starts with a prologue.</b> A flashback doubles as the tutorial, teaching you to move, handle a weapon and survive an on-foot police chase.</li>
    <li><b>Jason's first mission covers a lot of ground.</b> It mixes in stealth and puts you at the controls of a boat and then a plane before you ever reach a road and a car.</li>
    <li><b>The game shows how Jason and Lucia met</b> early on, and yes, it involves a stolen car.</li>
  </ul>
  <h2>Snapmatic is huge, and it is laughing at us</h2>
  <p>The phone's Instagram-style app, Snapmatic, holds hundreds of posts, videos and comments, and new ones appear as the story moves on and Leonida reacts to what you have done. One early post has already gone viral: a character complains that a game based on a kids' cartoon came out before "Race and Chase 7". Race'n'Chase was GTA's original working title, so it's Rockstar's joke about everyone who spent years saying they got something before GTA 6.</p>
  <details class="spoiler">
    <summary><b>Story spoilers from the prologue</b> (tap to show)</summary>
    <ul>
      <li>The game opens with Lucia in prison. You can talk to other inmates before she is called to see her counsellor, which leads into the flashback.</li>
      <li>The flashback is the armed convenience-store robbery that put her there. She runs, and the police tackle and taser her.</li>
      <li>The big surprise: Jason and Lucia have a child, who was waiting in a nearby coffee shop during the robbery and has been taken by child protective services. None of the trailers showed this.</li>
    </ul>
  </details>
  <h2>The "New Zealand trick": does it work?</h2>
  <ul>
    <li><b>Xbox:</b> players on Reddit say the game unlocked after they set their console's location to New Zealand. Microsoft and Rockstar have not said whether that will keep working.</li>
    <li><b>PS5:</b> changing settings does not work. You would need a separate New Zealand PlayStation account and a second copy bought from that store.</li>
    <li><b>Bans:</b> posts claim some accounts were suspended, but none has been confirmed. Separately, Twitch reportedly warned a German streamer that using the trick on stream could lead to a ban.</li>
  </ul>
  <h2>What we still don't know</h2>
  <p>Proper performance tests on Xbox, how bad any launch bugs are, and whether a day-one patch changes anything. Critic reviews and Digital Foundry's PS5 test are already out: <a href="/news/gta-6-reviews-metacritic-99/">here is what they say</a>.</p>
  <h2>What we are updating</h2>
  <p>As GTA VI unlocks around the world, we are checking our <a href="/map/">map</a>, <a href="/cheats/">cheats</a>, <a href="/missions/">missions</a> and <a href="/collectibles/">collectibles</a> against the finished game. Anything we confirm gets marked as verified.</p>""",
        sources=[("PC Guide: GTA 6 launches in NZ, including an early plot surprise", "https://www.pcguide.com/news/gta-6-launches-in-nz-with-millions-of-viewers-tuning-in-to-discover-the-game-including-an-early-plot-surprise/"),
                 ("AP via WRBL: Grand Theft Auto VI finally arrives", "https://www.wrbl.com/news/national/grand-theft-auto-vi-finally-arrives-heres-what-one-early-player-thinks/"),
                 ("Gulf News: GTA 6 early reactions and the New Zealand trick", "https://gulfnews.com/technology/gaming/gta-6-early-reviews-set-internet-alight-first-driving-clips-99-metacritic-claim-fuel-unprecedented-hype-1.500752451"),
                 ("Kotaku: Grand Theft Auto 6 includes a joke about GTA 7", "https://kotaku.com/grand-theft-auto-6-includes-a-joke-about-gta-7-2000755921"),
                 ("Notebookcheck: Streamer faces ban for using GTA 6 early unlock trick", "https://www.notebookcheck.net/Streamer-faces-ban-for-using-GTA-6-early-unlock-time-trick-on-release-date.1451653.0.html")],
    ),
    dict(
        slug="gta-6-reviews-metacritic-99",
        date="2026-11-18",
        title="GTA 6 reviews are in: a 99 on Metacritic, and the complaints worth knowing",
        desc="GTA VI's PS5 Metascore stood at 99 from 98 early reviews. What critics loved, what they didn't, and what Digital Foundry found about 30 fps.",
        fig=art.metascore,
        body="""
  <p>Reviews for GTA VI went live on November 18, the day before launch, and the early numbers are about as high as they go. On the morning of November 18, the PS5 version held a <b>99 Metascore from 98 critic reviews</b>. The Xbox Series X score was also 99, but from only nine reviews. Both will move as more reviews come in.</p>
  <p>For comparison, GTA IV sits at 98 and GTA V at 97, so GTA VI is on course to be the best-reviewed game in the series.</p>
  <h2>Perfect scores so far</h2>
  <p>IGN, VICE, Push Square and Cultured Vultures all gave 10 out of 10, and Creative Bloq gave 5 stars.</p>
  <h2>What critics loved</h2>
  <ul>
    <li><b>Leonida itself.</b> Reviewers describe a dense, handcrafted world full of detail and places to go.</li>
    <li><b>Driving.</b> IGN calls the handling the best in the series, with more weight and more convincing damage.</li>
    <li><b>Jason and Lucia.</b> The writing, the performances and their relationship get wide praise, as does a more grown-up story than past GTAs.</li>
    <li><b>Robberies you plan yourself</b> rather than follow a script, and smarter police. See our <a href="/robberies/">robberies guide</a> and <a href="/wanted-level/">wanted level guide</a>.</li>
  </ul>
  <h2>What they didn't</h2>
  <ul>
    <li><b>Controls.</b> The Guardian says complicated button inputs can start fights you didn't mean to, and Kotaku calls some controls cumbersome.</li>
    <li><b>Guns.</b> GamingBolt finds the smaller firearms clunky, and The Verge found switching weapons in a fight frustrating.</li>
    <li><b>Driving early on.</b> GamingBible found the heavier handling hard at first, especially when crashes cost money to repair.</li>
    <li><b>Pacing.</b> Kotaku says the later chapters of the story drag.</li>
    <li><b>No mission replays.</b> IGN notes you can't replay finished story missions one at a time, which you could in GTA V.</li>
  </ul>
  <h2>Performance: 30 fps everywhere</h2>
  <p>There is no 60 fps mode on any console, including PS5 Pro. Push Square gave the game a 10 but still flagged that. Digital Foundry's tests found:</p>
  <ul>
    <li><b>PS5 Pro:</b> a "near flawless" 30 fps with perfect frame pacing over more than 50 hours. It only fell to 24 fps when the tester set off huge numbers of explosions on purpose.</li>
    <li><b>PS5:</b> small dips throughout, and longer drops below 30 in heavy action.</li>
    <li><b>Xbox Series X|S:</b> not tested yet.</li>
  </ul>
  <p>Full details by console are in our <a href="/frame-rate/">frame rate guide</a>.</p>
  <h2>Should the complaints change your mind?</h2>
  <p>Probably not, if you were already excited. Most of the criticism is about controls and feel, which you get used to. If smooth frame rates matter a lot to you, the 30 fps cap is the one thing that won't change with practice.</p>""",
        sources=[("The PC Enthusiast: GTA 6 reviews hit 99 on Metacritic", "https://thepcenthusiast.com/gta-6-reviews-metascore-critic-reactions/"),
                 ("PlayStationInfo: GTA 6 achieves 99 points (citing Insider Gaming and Push Square)", "https://www.playstationinfo.de/en/2026/11/18/gta-6-achieves-an-incredible-99-points-and-even-the-ps5-pro-has-a-catch/"),
                 ("TweakTown: Digital Foundry on GTA 6 at 30 fps on PS5 and PS5 Pro", "https://www.tweaktown.com/news/114764/gta-6-struggles-to-hold-30-fps-on-base-ps5-more-often-than-expected/index.html"),
                 ("Dexerto: GTA 6's PS5 Pro upgrade", "https://www.dexerto.com/gta/gta-6s-ps5-pro-upgrade-is-bigger-than-you-might-expect-3429387/")],
    ),
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
