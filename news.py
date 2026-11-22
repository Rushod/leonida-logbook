"""News posts. Newest first. Each post: slug, date (YYYY-MM-DD), title, description, figure, body, sources.
build.py turns these into /news/<slug>/ pages, the /news/ listing, the home page block and /news/feed.xml."""
from html import escape as e
import art

AUTHOR = "Adrian R"
AUTHOR_BIO = "Adrian R writes the news for Leonida Logbook and has been playing Grand Theft Auto since the PlayStation 2 days."

POSTS = [
    dict(
        slug="gta-6-easter-eggs-fast-furious-dexter",
        date="2026-11-23",
        title="GTA 6 easter eggs found so far: a Fast & Furious car, Dexter's flat and a literal egg",
        desc="Players have spent launch week hunting Leonida for secrets. Here are the GTA VI easter eggs outlets have picked up, what's confirmed, and a first-person camera trick Rockstar didn't add on purpose.",
        fig=art.easter_eggs,
        body="""
  <p>It took players less than a day to start finding Rockstar's in-jokes in Leonida. Most of what's circulating comes from clips on X and Reddit, so we've only listed the finds that outlets have reported, and we say how solid each one is. Rockstar hasn't commented on any of them.</p>
  <h2>Brian O'Conner's 1995 Eclipse</h2>
  <p>The best-supported find so far. GamesRadar and BGR both report that a green 1995 Mitsubishi Eclipse in the style of Paul Walker's car from the first Fast and Furious film sits in a garage on <b>Vespucci Island</b>. BGR, citing Vice, places it in a garage attached to a white house near the middle of the island. GamesRadar says you have to break into the garage to take it, and that it's in every version of the game. The in-game badge isn't Mitsubishi, since GTA uses its own brand names, and we haven't seen a reliable report of what the game calls it.</p>
  <h2>A Dexter-style apartment</h2>
  <p>GamesRadar reports an apartment complex on <b>Washington Island</b> in Vice Beach that recreates Dexter Morgan's home from the TV series, down to a boat called "Slice of Life" and tools on the roof. This one comes from a GamesRadar video and player posts, so treat the exact details as reported rather than tested by us.</p>
  <h2>The egg on the tower</h2>
  <p>IBTimes UK picked up a player video from November 18 showing a bird's nest full of coloured eggs at the top of a communications tower, reached after a climb of about seven minutes. Throw an egg and the game cuts to a short scene of it hitting a car windscreen below. The tower's location hasn't been pinned down, and IBTimes is clear that this is still a player report, not a documented feature.</p>
  <h2>Comics and films</h2>
  <ul>
    <li><b>RX Men:</b> Reddit players spotted a comic called RX Men, with a Magneto-like villain called Dr. Placebo. GamesRadar reported it.</li>
    <li><b>Hulk:</b> GamesRadar says a side quest about strawberries ends with a character turning into something very Hulk-like.</li>
  </ul>
  <details class="spoiler">
    <summary><b>Film nods in later story missions</b> (tap to show)</summary>
    <p>GamesRadar's writer compares some later missions to the heist and siege set pieces of Heat and Die Hard. That's the writer's own comparison, not something Rockstar has said.</p>
  </details>
  <h2>A first-person camera, by accident</h2>
  <p>GTA VI has no first-person mode. GamesRadar reports a glitch that gives you one anyway: press the camera view button repeatedly while putting the phone away. It works better than you'd expect, with some visual glitches, but the only way back to the normal camera is to reload a save. Save first if you want to try it. GamesRadar also points out that GTA V only got its first-person mode in a later re-release, so a proper one could come later. Rockstar hasn't announced one.</p>
  <h2>Found one?</h2>
  <p>We'll add easter eggs to <a href="/map/">our map</a> once their locations are confirmed by more than one source. For now, the Eclipse garage is the only find with a location backed up by more than one outlet.</p>""",
        sources=[("GamesRadar+: GTA 6 is a movie and TV goldmine, from Fast and Furious cars to Dexter's apartment", "https://www.gamesradar.com/games/grand-theft-auto/gta-6-is-a-movie-and-tv-goldmine-as-players-discover-everything-from-fast-and-furious-cars-to-dexters-apartment/"),
                 ("BGR: GTA 6 has a hidden Fast and Furious easter egg", "https://www.bgr.com/2322463/gta-6-hidden-fast-and-furious-paul-walker-car/"),
                 ("IBTimes UK: GTA 6 easter egg is literally an egg", "https://www.ibtimes.co.uk/gta-6-player-discovers-literal-easter-egg-leonida-1833342"),
                 ("GamesRadar+: GTA 6 glitch adds the first-person mode that Rockstar skipped", "https://www.gamesradar.com/games/grand-theft-auto/gta-6-glitch-adds-the-first-person-mode-that-rockstar-skipped/")],
    ),
    dict(
        slug="gta-6-rockstar-developer-notes-play-without-guides",
        date="2026-11-23",
        title="Rockstar's GTA 6 developer notes: 1,000 NPC routines, months on one door, and a plea to skip the guides",
        desc="Rockstar gave press a packet of notes from more than 20 GTA VI developers. The highlights, including its design chief asking players to stop chasing completion percentages.",
        fig=art.dev_notes,
        body="""
  <p>Alongside review copies, Rockstar sent press a set of notes in which named developers explain how GTA VI was made. InvenGlobal published a long summary on November 18, and Kotaku wrote about one part of it on November 21. These are Rockstar's own words, so this is about as official as behind-the-scenes detail gets.</p>
  <h2>"Stop thinking in tasks"</h2>
  <p>According to Kotaku, Stephen Donkin, Rockstar's vice president of design, says the team hopes players drop the habit of working through tasks, completion percentages and online guides, and instead "let the game unfold in front of them". Senior design director Ghyan Koehne talks about wanting players to feel a sense of wonder.</p>
  <p>Yes, we see the irony of reporting that on a guide site. We agree with the spirit of it: on a first playthrough, wander off and don't worry about 100%. Our <a href="/walkthrough/">walkthrough</a> and <a href="/collectibles/">collectibles</a> pages will be here when you're stuck or want to clean up later.</p>
  <h2>Other highlights</h2>
  <ul>
    <li><b>Background life:</b> the team made about 1,000 sets of activity animations for the routines of people in the world.</li>
    <li><b>Small things take time:</b> gameplay animation director Mike Jones says the moment Lucia pushes a door open with her hip took months to get right.</li>
    <li><b>Location scouting:</b> John Macpherson, lead director of world and population design, describes the team scouting real Florida locations.</li>
    <li><b>The look of the UI:</b> the classic Pricedown font stays, and the phone is now held in the character's hand rather than floating on screen.</li>
    <li><b>Music:</b> Rockstar's music team describes 1980s Miami influences for the regions of Leonida and a collaboration with French electronic duo Justice.</li>
    <li><b>Cars:</b> physics technology director Ben Lyons says team members raced in the 24 Hours of Nürburgring after GTA V and took a class win.</li>
    <li><b>Sound:</b> the audio team recorded in an anechoic chamber to get speakers and other sounds right.</li>
  </ul>
  <p>The notes also include a foreword from Rockstar founder Sam Houser. Neither summary says anything about a PC version or an online mode, which Rockstar still hasn't announced.</p>""",
        sources=[("Kotaku: Rockstar dev tells GTA 6 players to stop thinking in tasks, completion percentages and online guides", "https://kotaku.com/rockstar-dev-tells-gta-6-players-to-stop-thinking-in-tasks-completion-percentages-online-guides-2000759151"),
                 ("InvenGlobal: GTA 6 developers share insights on the creation of Vice City", "https://www.invenglobal.com/articles/28826/gta-6-developers-share-insights-on-the-creation-of-vice-city")],
    ),
    dict(
        slug="gta-6-official-sales-3-79-billion-day-one",
        date="2026-11-22",
        title="GTA 6 made $3.79 billion on day one, Take-Two confirms",
        desc="Take-Two's first official GTA VI numbers: $3.79 billion in day-one retail sales and 32.5 million copies sold before release, both records. Here's what the figures do and don't include.",
        fig=art.sales_official,
        body="""
  <p>We now have official numbers. On November 20, Take-Two said GTA VI brought in <b>$3.79 billion in retail sales</b> on its first day and sold <b>32.5 million copies before release</b>. The company calls the first figure a record for any entertainment launch, films included.</p>
  <h2>What Take-Two announced</h2>
  <ul>
    <li><b>$3.79 billion</b> in day-one retail sales worldwide, based on company estimates up to the end of November 19.</li>
    <li><b>32.5 million copies</b> sold before launch, which Take-Two says is a record on any platform.</li>
    <li>The game is on sale through the PlayStation Store, the Microsoft Store, the Rockstar Games Store and shops. The announcement says nothing about a PC version or an online mode.</li>
  </ul>
  <h2>What the numbers mean</h2>
  <p>The $3.79 billion is money spent by players at retail. It isn't Take-Two's revenue, since stores and platform holders take their cut. It's also the company's own estimate, not an audited result. The Hollywood Reporter, as cited by Make Tech Easier, says the total includes pre-orders. Take-Two didn't say how much came from digital and how much from boxed copies.</p>
  <h2>How it compares</h2>
  <p>In 2013, Take-Two said GTA V sold more than $800 million on its first day. That makes the GTA VI figure about five times bigger. Earlier this week we reported <a href="/news/gta-6-sales-19-million-estimate/">Sensor Tower's estimate</a> of about 19 million copies by launch morning. Take-Two's 32.5 million is well above that. That estimate was made before launch day ended and was built from market data rather than Take-Two's own sales records, so the two numbers measure different things.</p>
  <h2>What's next</h2>
  <p>Take-Two hasn't said when it will share an updated total, and Rockstar still hasn't announced a PC version, an online mode or the first post-launch patch. We'll report those when they're official. For what's in the game right now, see our <a href="/walkthrough/">mission walkthrough</a>.</p>""",
        sources=[("Take-Two Interactive: Grand Theft Auto VI shatters entertainment box office records with $3.79 billion in day one retail sales", "https://www.take2games.com/ir/news/grand-theft-auto-vi-shatters-entertainment-box-office-records"),
                 ("ABC News: GTA 6 breaks entertainment box office records with $3.79B in 1st-day sales", "https://abcnews.com/GMA/Culture/grand-theft-auto-vi-breaks-1st-day-sales-record/story?id=138328412"),
                 ("Make Tech Easier: GTA 6 made $3.79 billion on its first day", "https://maketecheasier.com/gta-6-day-one-sales-record/")],
    ),
    dict(
        slug="gta-6-launch-bugs-psn-outages",
        date="2026-11-21",
        title="GTA 6 launch bugs: what players are hitting, and why there's no patch yet",
        desc="Clipping, falls through the map, cars flying off and a couple of PSN outages. Here's what's actually been reported in GTA VI's first days, what's confirmed and what to do if it happens to you.",
        fig=art.launch_bugs,
        body="""
  <p>A 99 Metascore doesn't mean a bug-free game. Since GTA VI unlocked on November 18 and 19, clips of it misbehaving have spread across X and Reddit. Some outlets have compared it to Cyberpunk 2077's launch, but the reports so far are mostly the odd, funny kind rather than anything that stops large numbers of people playing. Here's what we can stand behind.</p>
  <h2>What players are seeing</h2>
  <p>These come from player and streamer clips that several outlets picked up. None has been confirmed by Rockstar, and nobody knows how common each one is.</p>
  <ul>
    <li><b>Clipping:</b> Jason and police officers passing through walls and objects during arrests and shootouts.</li>
    <li><b>Falling through the world:</b> Lucia dropping through the ground during a mission, and a reported phone glitch that sends Jason through the map until you restart.</li>
    <li><b>Physics:</b> cars and even a truck launched into the air after crashes, and a boat behaving strangely near a bridge.</li>
    <li><b>Pop-in:</b> a ship appearing late on a bridge, a plane passing through buildings and textures loading slowly in the opening.</li>
    <li><b>NPCs:</b> pedestrians walking into walls, and people on a boat ignoring a speedboat ramming them.</li>
  </ul>
  <h2>The more serious reports</h2>
  <p>Latin Times rounded up player complaints of crashes during the prologue, screen freezes, audio static and a softlock that stops progress in an early Lucia mission. These are individual reports, not a confirmed widespread problem, and Rockstar hasn't acknowledged them.</p>
  <details class="spoiler">
    <summary><b>One bug report mentions a prologue moment</b> (tap to show)</summary>
    <p>Beebom's bug tracker lists clips of Lucia falling through the map right after the police taser her in the opening flashback.</p>
  </details>
  <h2>PlayStation Network went down twice</h2>
  <p>This part is confirmed. Sony's PSN status page acknowledged a sign-in outage on November 18, as the game unlocked around the world, and a shorter disruption of about 24 minutes to gaming and social services from around 9:34pm Pacific on November 19. Sony didn't give a cause, and it never said GTA VI was to blame. GTA VI is single-player, so the outage mostly mattered for downloads, store access and signing in.</p>
  <h2>Is there a patch?</h2>
  <p>Not yet. GTA VI got two updates before launch, version 01.002.000 on November 13 and 01.002.001 on November 16, and Rockstar published no patch notes for either. Up to November 19, outlets said Rockstar had not commented on any of the launch bugs, and we haven't found a fix announcement since. We'll report the first post-launch update and what it fixes as soon as it's out.</p>
  <h2>What to do if you hit one</h2>
  <ul>
    <li><b>Stuck in a mission:</b> retry from the last checkpoint first. If that doesn't clear it, close the game fully and reopen it.</li>
    <li><b>Fell through the map:</b> players say a restart puts you back on solid ground.</li>
    <li><b>Crashes:</b> check that you have the latest game version and console system software, and that your console has space around it so it doesn't overheat.</li>
    <li><b>Report it:</b> Rockstar Support takes bug reports, and a video helps.</li>
  </ul>
  <p>Performance is a separate question from bugs. For tested frame rates on every console, see <a href="/frame-rate/">our frame rate guide</a>.</p>""",
        sources=[("PC Guide: GTA 6 bugs draw comparisons to Cyberpunk 2077, but it's far from the same thing", "https://www.pcguide.com/news/gta-6-bugs-draw-comparisons-to-cyberpunk-2077s-messy-launch-but-its-far-from-the-same-thing/"),
                 ("Latin Times: GTA 6 Metacritic record, launch bugs and PSN outage", "https://www.latintimes.com/gta-6-metacritic-record-launch-bugs-psn-outage-601565"),
                 ("Gulf News: GTA 6 glitches go viral", "https://gulfnews.com/technology/gaming/gta-6-glitches-go-viral-flying-cars-disappearing-characters-and-police-encounter-issues-spark-cyberpunk-2077-comparisons-1.500752989"),
                 ("Beebom: GTA 6 bugs tracker", "https://beebom.com/gta-6-bugs-tracker/"),
                 ("Beebom: GTA 6 patch notes and updates tracker", "https://beebom.com/gta-6-patch-notes-updates-tracker/")],
    ),
    dict(
        slug="gta-6-sales-19-million-estimate",
        date="2026-11-19",
        title="GTA 6 sold an estimated 19 million copies by launch morning, but there's no official number yet",
        desc="Market data firm Sensor Tower puts GTA VI at about 19.1 million copies and $1.84 billion by the morning of November 19. Take-Two has not shared figures.",
        fig=art.sales_estimate,
        body="""
  <p class="note"><b>Update, November 22:</b> Take-Two has now released official figures: $3.79 billion in day-one retail sales and 32.5 million copies sold before release. <a href="/news/gta-6-official-sales-3-79-billion-day-one/">Read our report on the official numbers.</a></p>
  <p>The first sales number for GTA VI is out, and it is not from Rockstar. Market data firm Sensor Tower estimates the game had sold about <b>19.1 million copies</b>, worth about <b>$1.84 billion</b>, by the morning of launch day. Reuters reported the figure first.</p>
  <h2>What the estimate says</h2>
  <ul>
    <li><b>About 19.1 million copies</b> sold by the morning of November 19, counting pre-orders.</li>
    <li><b>About $1.84 billion</b> in revenue, more than $1.5 billion of it from pre-orders, according to 80 Level's summary.</li>
    <li><b>Roughly three in four copies were on PlayStation</b>, the rest on Xbox.</li>
  </ul>
  <h2>Is it official?</h2>
  <p>No. Sensor Tower estimates sales from store and market data, and Take-Two and Rockstar have not released a number. Take-Two has only said that pre-orders were tracking far above its expectations. Its CEO, Strauss Zelnick, said on an earnings call earlier in November, "we still aren't ready to declare victory." Some reports suggest official figures could come within days, but Take-Two has not given a date.</p>
  <h2>How it compares with GTA V</h2>
  <p>GTA V sold 11.21 million copies and made $815.7 million in its first 24 hours in September 2013, a Guinness world record at the time. The GTA VI estimate is already well above that, but the two numbers are not measured the same way: GTA V's covers a full day of sales, while GTA VI's is mostly pre-orders counted before most of the world could play.</p>
  <h2>Why it matters</h2>
  <p>If the estimate is close, GTA VI already had the biggest launch on record before most countries had even reached their unlock time. Take-Two has since shared its own numbers (<a href="/news/gta-6-official-sales-3-79-billion-day-one/">see the update above</a>). Still deciding on a console? See <a href="/platforms/">which consoles run GTA VI</a>.</p>""",
        sources=[("Men's Journal: GTA 6 sold an estimated 19 million copies by launch day", "https://www.mensjournal.com/news/gta-6-sales-19-million-copies-gta-v-record"),
                 ("80 Level: Report says GTA 6 generated nearly $2B in sales by launch day", "https://80.lv/articles/report-gta-6-generated-nearly-usd2b-in-sales-by-launch-day")],
    ),
    dict(
        slug="gta-6-trophy-list-platinum-100-percent",
        date="2026-11-19",
        title="GTA 6 trophy list: 55 trophies, and the platinum needs 100% completion",
        desc="GTA VI has 55 trophies and achievements, all single-player, worth 1,000 Gamerscore. The platinum needs 100% completion, which guides put at about 200 hours.",
        fig=art.trophies,
        body="""
  <p>Trophy hunters, clear your calendar. GTA VI's full list of trophies and achievements is now public on PS5 and Xbox, and the platinum asks for everything.</p>
  <h2>The list at a glance</h2>
  <ul>
    <li><b>55 in total:</b> 1 platinum, 2 gold, 6 silver and 46 bronze on PS5. On Xbox the same list is worth 1,000 Gamerscore.</li>
    <li><b>All single-player.</b> There are no online trophies, since GTA VI has no online mode at launch.</li>
    <li><b>About half are hidden.</b> GTABase counts 28 secret entries. GamesRadar+ warns that some of their names give away mild story spoilers, so we're not listing them here.</li>
    <li><b>The platinum needs 100% completion.</b> The trophy for reaching 100% is itself one of the two golds. Push Square's verdict: "Strap in for the long haul."</li>
  </ul>
  <h2>What counts toward 100%</h2>
  <p>GTABase's breakdown is the most detailed so far. Some things must be done in full, others only in part:</p>
  <ul>
    <li><b>All of them:</b> robberies (including the bank vaults), underwater discoveries, a gold medal at every shooting-range challenge, and every drone race.</li>
    <li><b>Most of them:</b> scanning 200 of the vehicles, studying 100 of the animals, a set number of optional missions, stunts and challenges.</li>
  </ul>
  <h2>Side trophies worth knowing about</h2>
  <ul>
    <li><b>Master of None:</b> try each of the 9 activity types once.</li>
    <li><b>Top Fun:</b> win a drone race at all 14 locations.</li>
    <li><b>Positive Mental Attitude:</b> meditate at all 18 spots. GTABase says one of them may be missable early in the story, but hasn't confirmed it.</li>
    <li><b>Whip It Good:</b> discover 100 vehicles.</li>
    <li><b>Cunning Stunts:</b> complete 250 stunts.</li>
    <li><b>Maximum Withdrawal:</b> rob five bank vaults and get away.</li>
    <li><b>Stick Fiddler:</b> beat an arcade game.</li>
  </ul>
  <h2>How long will it take?</h2>
  <p>GTABase estimates about 200 hours for the platinum, in line with Red Bull Gaming's early guess of more than 200 hours for 100%. One more warning: <a href="/news/gta-6-cheats-confirmed-how-to-unlock/">using a cheat</a> turns trophies off for that session. We've added the completion counts to our <a href="/collectibles/">collectibles page</a>, and the <a href="/story-length/">story length guide</a> has the main-story estimates.</p>""",
        sources=[("Push Square: GTA 6 PS5 trophies revealed, 100% completion needed for the platinum", "https://www.pushsquare.com/news/2026/11/gta-6-ps5-trophies-revealed-100percent-completion-needed-for-the-platinum"),
                 ("GamesRadar+: Complete GTA 6 trophy and achievement list", "https://www.gamesradar.com/games/grand-theft-auto/gta-6-trophy-achievement-list/"),
                 ("GTABase: GTA 6 trophy guide and achievements list", "https://www.gtabase.com/articles/gta-6/gta-6-achievements-trophies-list-ps5-xbox-series")],
    ),
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
  <p>Proper performance tests on Xbox, how bad any launch bugs are (<a href="/news/gta-6-launch-bugs-psn-outages/">update: here's what players are reporting</a>), and whether a day-one patch changes anything. Critic reviews and Digital Foundry's PS5 test are already out: <a href="/news/gta-6-reviews-metacritic-99/">here is what they say</a>.</p>
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
