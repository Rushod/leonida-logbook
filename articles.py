"""Pre-launch guide articles. Each entry: (path, title, description, body_html).
build.py imports ARTICLES and GUIDE_LINKS from here."""

UPDATED = "Updated November 11, 2026"

GUIDES = [
    ("/release-time/", "What time does GTA 6 unlock?", "What is confirmed about the unlock time, and how to check yours."),
    ("/preload/", "GTA 6 preload guide", "Preload dates and the steps for PS5 and Xbox."),
    ("/storage/", "How much storage does GTA 6 need?", "The 212 GB requirement against every console."),
    ("/editions/", "GTA 6 Standard vs Ultimate", "What each edition includes and what the extra $20 buys."),
    ("/pc-release/", "Is GTA 6 coming to PC?", "What Take-Two has said, and how long past games took."),
    ("/online/", "Does GTA 6 have online at launch?", "What is confirmed about multiplayer and GTA Online."),
    ("/frame-rate/", "Is GTA 6 30 or 60 fps?", "Reported performance on PS5, PS5 Pro and Xbox."),
    ("/reviews/", "When do GTA 6 reviews come out?", "The reported review date and where to find scores."),
    ("/story-length/", "How long is GTA 6?", "The 80-hour figure and how it compares."),
    ("/radio-stations/", "GTA 6 radio stations", "All six revealed stations, genres and hosts."),
    ("/map-size/", "How big is the GTA 6 map?", "Leonida's size against GTA V and Red Dead 2."),
    ("/characters/", "GTA 6 characters", "Jason, Lucia and the six characters around them."),
    ("/platforms/", "GTA 6 on PS4, Xbox One or PC?", "Which systems run the game at launch."),
    ("/wanted-level/", "GTA 6 wanted level", "How stars work and every way to lose the police."),
    ("/activities/", "GTA 6 activities", "All twelve reported side activities and more to do."),
    ("/robberies/", "GTA 6 robberies", "How store robberies, safes and fences pay out."),
    ("/gym/", "GTA 6 gym guide", "How workouts work and how to gain strength."),
    ("/wildlife/", "GTA 6 animals and zoo", "The wildlife checklist, the zoo and dogs."),
    ("/vehicles/", "GTA 6 vehicles list", "Confirmed vehicles, garages, fuel and mod shops."),
    ("/weapons/", "GTA 6 weapons list", "Carry limits, Ammu-Nation lockers and Focus."),
    ("/missions/", "GTA 6 missions list", "Story structure now, every mission at launch."),
    ("/collectibles/", "GTA 6 collectibles", "What there is to find, with locations at launch."),
]
LAUNCH_PATHS = ["/release-time/", "/preload/", "/storage/", "/editions/"]


def tiles(paths):
    by = {p: (t, d) for p, t, d in GUIDES}
    return "".join(f'<a class="tile" href="{p}"><h3>{by[p][0]}</h3><span>{by[p][1]}</span></a>' for p in paths)


def links(exclude=None):
    """Four related guides: the next four after this one, wrapping round."""
    paths = [p for p, _, _ in GUIDES]
    i = paths.index(exclude) if exclude in paths else -1
    pick = [paths[(i + k) % len(paths)] for k in range(1, 5)]
    return f'<div class="stack"><h2>More guides</h2><div class="tiles">{tiles(pick)}</div><p><a class="btn ghost" href="/guides/">All guides</a></p></div>'


GUIDE_LINKS = f'<div class="stack"><h2>Launch guides</h2><div class="tiles">{tiles(LAUNCH_PATHS)}</div></div>'
ALL_GUIDES = f'<div class="stack"><h2>All guides</h2><div class="tiles">{tiles([p for p, _, _ in GUIDES])}</div></div>'
GUIDES_PAGE = f"""
  <div class="stack"><span class="eyebrow">Guides</span><h1>GTA VI guides</h1>
  <p class="lede">Short, checked answers to the questions players are asking before launch.</p></div>
  <div class="tiles">{tiles([p for p, _, _ in GUIDES])}</div>"""

RELEASE_TIME = f"""
  <div class="prose"><span class="eyebrow">Launch guide</span><h1>What time does GTA 6 unlock?</h1>
  <p class="note">{UPDATED}</p>
  <p class="lede">GTA VI unlocks at <b>midnight local time on Thursday, November 19, 2026</b>, on both PS5 and Xbox Series X|S. Rockstar confirmed this on its support site. New Zealand plays first and Hawaii plays last.</p>
  </div>
  <div class="unlock panel" data-unlock>
    <span class="eyebrow">Your unlock time</span>
    <label class="uzone">Time zone <select data-uzone></select></label>
    <p class="ubig" data-uwhen>Midnight, Thursday November 19</p>
    <div class="clock ucount" data-ucount>
      <div><b data-ud>--</b><span>Days</span></div><div><b data-uh>--</b><span>Hours</span></div>
      <div><b data-um>--</b><span>Minutes</span></div><div><b data-us>--</b><span>Seconds</span></div>
    </div>
    <p class="note" data-unote>We picked your time zone from your device. Change it above to check a friend's.</p>
  </div>
  <div class="prose">
  <h2>When it unlocks around the world</h2>
  <p>Every region unlocks at its own midnight. The right-hand column shows each one in <b data-uyour>your time</b>, so you can see who plays before you.</p>
  <div class="scroll"><table class="utable"><thead><tr><th>Region</th><th>Local time</th><th>In your time</th></tr></thead><tbody data-utable></tbody></table></div>
  <p class="note">Times follow Rockstar's rule of local midnight. If your console is set to a different region or time zone from where you are, check the countdown on the game's store page.</p>
  <h2>Exceptions</h2>
  <ul>
    <li><b>Xbox Cloud Gaming</b> (including Xbox One): Microsoft says streaming starts on November 19 at <b>1am ET</b>. See <a href="/news/gta-6-xbox-one-cloud-gaming/">our cloud streaming story</a>.</li>
    <li><b>Boxed copies</b> contain a download code, so they unlock at the same time as digital once the download is done. See the <a href="/preload/">preload guide</a>.</li>
  </ul>
  <h2>How to check on your console</h2>
  <ul>
    <li><b>PS5:</b> open GTA VI from your Game Library. Pre-ordered games show a countdown on the game's page.</li>
    <li><b>Xbox Series X|S:</b> open GTA VI in the Microsoft Store on your console and check the release date and time.</li>
  </ul>
  <h2>Does preloading let you play early?</h2>
  <p>No. Preloading only downloads the game. It stays locked until midnight on November 19 where you are.</p>
  <h2>Sources</h2>
  <ul>
    <li><a href="https://support.rockstargames.com/articles/29jV3Cv2cCgvwM1XgtMO5o/grand-theft-auto-vi-regional-pre-load-and-release-times-on-playstation-5-and-xbox-series-x-or-s" rel="noopener">Rockstar Games Support: regional pre-load and release times</a></li>
    <li><a href="https://news.xbox.com/en-us/2026/11/10/grand-theft-auto-6-comes-to-xbox-cloud-gaming-november-19/" rel="noopener">Xbox Wire: GTA VI comes to Xbox Cloud Gaming</a></li>
  </ul>
  </div>
  {links("/release-time/")}"""

PRELOAD = f"""
  <div class="prose"><span class="eyebrow">Launch guide</span><h1>GTA 6 preload guide for PS5 and Xbox</h1>
  <p class="note">{UPDATED}</p>
  <p class="lede">Preloading downloads GTA VI before release day, so you can play the moment it unlocks. The game needs up to 212 GB, so start early.</p>
  <h2>Preload dates</h2>
  <div class="scroll"><table>
    <tr><th>How you bought it</th><th>Preload opens</th></tr>
    <tr><td>Digital pre-order on PS5</td><td class="n">November 10, 2026</td></tr>
    <tr><td>Boxed copy (download code)</td><td class="n">November 12, 2026</td></tr>
    <tr><td>Game unlocks</td><td class="n">November 19, 2026</td></tr>
  </table></div>
  <p>Boxed copies of GTA VI contain a download code and no disc, so they need the same download as a digital copy. On Xbox, check the game's page in the store: the Install button appears once pre-install is available for your pre-order.</p>
  <h2>Before you start</h2>
  <ul>
    <li><b>Free up 212 GB.</b> See the <a href="/storage/">storage guide</a> for how much room each console has.</li>
    <li><b>Use a wired connection if you can.</b> A download this size can take many hours on slow Wi-Fi.</li>
    <li><b>Leave room for the day-one update.</b> It is not included in the 212 GB figure.</li>
  </ul>
  <h2>How to preload on PS5</h2>
  <ul>
    <li>Go to your <b>Game Library</b> and open the <b>Your Collection</b> tab.</li>
    <li>Select <b>Grand Theft Auto VI</b>.</li>
    <li>Choose <b>Download</b>. Progress shows under Downloads/Uploads in the control center.</li>
  </ul>
  <p>If automatic downloads are switched on and the console is in rest mode with internet access, a pre-ordered game can download by itself once preload opens.</p>
  <h2>How to preload on Xbox Series X|S</h2>
  <ul>
    <li>Open <b>My games &amp; apps</b>, then <b>Full library</b>, then <b>All owned games</b>.</li>
    <li>Select <b>Grand Theft Auto VI</b>.</li>
    <li>Choose <b>Install</b>. Progress shows under Manage, then Queue.</li>
  </ul>
  <h2>If you have a boxed copy</h2>
  <ul>
    <li><b>PS5:</b> open the PlayStation Store, choose the <b>More</b> (three dots) menu, then <b>Redeem Code</b>, and enter the code from the box.</li>
    <li><b>Xbox:</b> open the Store, choose <b>Redeem</b>, and enter the code.</li>
  </ul>
  <p>After the code is redeemed, the game appears in your library and downloads like a digital copy.</p>
  <h2>Does preloading let you play early?</h2>
  <p>No. The game stays locked until it unlocks in your region. See <a href="/release-time/">what time GTA 6 unlocks</a>.</p>
  </div>
  {links("/preload/")}"""

STORAGE = f"""
  <div class="prose"><span class="eyebrow">Launch guide</span><h1>How much storage does GTA 6 need?</h1>
  <p class="note">{UPDATED}</p>
  <p class="lede">GTA VI needs up to 212 GB of free space, depending on your console. That makes it one of the largest console games so far.</p>
  <h2>212 GB against each console</h2>
  <div class="scroll"><table>
    <tr><th>Console</th><th>Usable storage</th><th>GTA VI takes about</th></tr>
    <tr><td>PS5 (original, 825 GB)</td><td class="n">667 GB</td><td class="n">32%</td></tr>
    <tr><td>PS5 Slim (1 TB)</td><td class="n">842 GB</td><td class="n">25%</td></tr>
    <tr><td>PS5 Pro (2 TB)</td><td class="n">1.89 TB</td><td class="n">11%</td></tr>
    <tr><td>Xbox Series X (1 TB)</td><td class="n">802 GB</td><td class="n">26%</td></tr>
    <tr><td>Xbox Series S (512 GB)</td><td class="n">364 GB</td><td class="n">58%</td></tr>
  </table></div>
  <p>Percentages use the 212 GB maximum. The exact size per console has not been published, and the day-one update is extra.</p>
  <h2>How to check your free space</h2>
  <ul>
    <li><b>PS5:</b> Settings, then Storage, then Console Storage.</li>
    <li><b>Xbox Series X|S:</b> Settings, then System, then Storage devices.</li>
  </ul>
  <h2>Ways to make room</h2>
  <ul>
    <li><b>Delete games you have finished.</b> Your saves stay on the console or in the cloud, and you can download the game again later.</li>
    <li><b>Move older games to a USB drive.</b> PS4 and Xbox One games can run from an external USB drive, which frees the fast internal storage.</li>
    <li><b>Clear captures.</b> Saved video clips can take tens of gigabytes.</li>
  </ul>
  <h2>If you need more storage</h2>
  <p>GTA VI has to run from fast storage. A normal USB drive can hold the game but cannot run it.</p>
  <ul>
    <li><b>PS5:</b> add an M.2 NVMe SSD to the expansion slot inside the console. Sony recommends one with a heatsink.</li>
    <li><b>Xbox Series X|S:</b> plug a Storage Expansion Card into the port on the back.</li>
  </ul>
  <p><a class="btn" href="/gear/">See storage upgrades</a></p>
  </div>
  {links("/storage/")}"""

EDITIONS = f"""
  <div class="prose"><span class="eyebrow">Launch guide</span><h1>GTA 6 Standard vs Ultimate edition</h1>
  <p class="note">{UPDATED}</p>
  <p class="lede">GTA VI comes in two editions. Both include the full game. The Ultimate Edition costs $20 more and adds in-game vehicles, weapons, clothing and properties.</p>
  <h2>Prices</h2>
  <div class="scroll"><table>
    <tr><th>Edition</th><th>US price</th><th>UK price</th></tr>
    <tr><td><b>Standard</b></td><td class="n">$79.99</td><td class="n">£69.99</td></tr>
    <tr><td><b>Ultimate</b></td><td class="n">$99.99</td><td class="n">£89.99</td></tr>
  </table></div>
  <h2>What the Ultimate Edition adds</h2>
  <div class="scroll"><table>
    <tr><th>Type</th><th>Reported contents</th></tr>
    <tr><td><b>Vehicles</b></td><td>'67 Vapid Dominator Buggy with Paradise Garage, '95 Grotti Cheetah, Shitzu Squalo, a Vapid Ganado Retro Build at Jason's safehouse, and a Classic Car Collection</td></tr>
    <tr><td><b>Weapons</b></td><td>Hawk &amp; Little Morgan Revolver and personalized weapon variants</td></tr>
    <tr><td><b>Style</b></td><td>Vice City Styles for Jason and Lucia, Goodtime Gear, Stock 305 Clothing Store, Sara's Unisex Salon and Electric Fang Tattoo</td></tr>
    <tr><td><b>Other</b></td><td>Vehicle Mod Shops, and the PTT Youngin$ Compound and Scores</td></tr>
  </table></div>
  <p class="note">This list comes from press coverage of the store listings. Check the edition's page in your console store for the final wording.</p>
  <h2>The pre-order bonus comes with both</h2>
  <p>The Vintage Vice City Pack is included with either edition if you buy by launch day, November 19. It contains a two-tone '55 Vapid Stanier, the Shore Court Garage, and two outfits and hairstyles each for Jason and Lucia.</p>
  <h2>Which one fits you</h2>
  <ul>
    <li><b>Standard</b> is the whole story and open world. Nothing in the Ultimate list is described as required to finish the game.</li>
    <li><b>Ultimate</b> suits players who want extra cars, clothing and properties from the first hour instead of earning or buying them in the game.</li>
  </ul>
  <p>We have not found an announced way to upgrade from Standard to Ultimate later, so check the store page before assuming you can.</p>
  <h2>Boxed copies</h2>
  <p>Boxed copies contain a download code and no disc. They need the same 212 GB download as the digital version. See the <a href="/preload/">preload guide</a>.</p>
  </div>
  {links("/editions/")}"""

ARTICLES = [
    ("/release-time/", "What Time Does GTA 6 Unlock? Countdown for Your Time Zone | Leonida Logbook", "GTA 6 unlocks at midnight local time on November 19 on PS5 and Xbox. See the exact time and a live countdown for your time zone, plus every region worldwide.", RELEASE_TIME),
    ("/preload/", "GTA 6 Preload Guide: Dates and Steps for PS5 and Xbox | Leonida Logbook", "When GTA VI preload opens, how to start the download on PS5 and Xbox Series X|S, and how to redeem a boxed copy's code.", PRELOAD),
    ("/storage/", "How Much Storage Does GTA 6 Need? PS5 and Xbox Space Guide | Leonida Logbook", "GTA VI needs up to 212 GB. How that compares with each PS5 and Xbox model, how to check free space, and how to make room.", STORAGE),
    ("/editions/", "GTA 6 Standard vs Ultimate Edition: Price and Contents | Leonida Logbook", "GTA VI Standard is $79.99 and Ultimate is $99.99. What the Ultimate Edition adds, the pre-order bonus, and which edition fits you.", EDITIONS),
]
