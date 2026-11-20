"""Second batch of guides, chosen from what players are searching for before launch.
Each body opens with an original graphic from art.py."""
import art
from articles import links, UPDATED

BRAND = " | Leonida Logbook"


def page(path, eyebrow, h1, lede, figure, body):
    return f"""
  <div class="prose"><span class="eyebrow">{eyebrow}</span><h1>{h1}</h1>
  <p class="note">{UPDATED}</p>
  <p class="lede">{lede}</p>
  {figure}
  {body}
  </div>
  {links(path)}"""


PC = page("/pc-release/", "Platforms", "Is GTA 6 coming to PC?",
          "Not at launch. GTA VI releases on November 19, 2026 for PS5 and Xbox Series X|S only, and no PC version or PC date has been announced.",
          art.pc_gap(), """
  <h2>What Take-Two has said</h2>
  <p>In a May 2026 interview with Bloomberg, Take-Two chief executive Strauss Zelnick explained the console-first plan by saying Rockstar is judged on serving its core audience first. He did not give a PC date.</p>
  <h2>What past Rockstar games did</h2>
  <ul>
    <li><b>GTA V</b> reached PC 19 months after its first console release.</li>
    <li><b>Red Dead Redemption 2</b> reached PC about 12 months after consoles.</li>
  </ul>
  <p>If GTA VI follows the same pattern, a PC version would arrive a year or more after November 2026. That is an estimate from history, not an announcement, and reports that name a specific month are unconfirmed.</p>
  <h2>Can you play it on a PC screen anyway?</h2>
  <p>If you own the game on a console, Remote Play can stream it from your PS5 or Xbox to a computer on a good connection. The game still runs on the console.</p>
  <h2>Should you wait for PC?</h2>
  <ul>
    <li><b>Wait</b> if you only game on PC and are happy to avoid spoilers for a year or more.</li>
    <li><b>Buy a console</b> if you want to play at launch. See <a href="/platforms/">which consoles run GTA VI</a>.</li>
  </ul>""")

ONLINE = page("/online/", "Multiplayer", "Does GTA 6 have online at launch?",
              "No online mode has been announced for launch day. Official listings describe GTA VI on November 19, 2026 as a single-player game.",
              art.online_status(), """
  <h2>What is confirmed</h2>
  <ul>
    <li>Take-Two's pre-order announcement and the PlayStation Store listing describe GTA VI as a single-player experience.</li>
    <li>Rockstar has not given a date, a name or any details for a GTA VI online mode.</li>
    <li>The launch download does not include the next GTA Online instalment.</li>
  </ul>
  <h2>What is only reported</h2>
  <p>In September 2026, Bloomberg reported comments from Twitch chief executive Dan Clancy suggesting Rockstar would launch multiplayer the following year. Rockstar has not confirmed that, so treat 2027 as a report and nothing more.</p>
  <h2>What happens to GTA Online?</h2>
  <p>Rockstar has not announced any shutdown of the current GTA Online, which runs on GTA V. For now it remains the way to play Grand Theft Auto with other people.</p>
  <h2>Can you play with a friend at all?</h2>
  <p>Not in the way previews describe it. The teamwork shown so far is between the two story leads, Jason and Lucia, who you switch between. See <a href="/characters/">the characters guide</a>.</p>""")

FPS = page("/frame-rate/", "Performance", "Is GTA 6 30 or 60 fps?",
           "GTA VI runs at 30 frames per second on PS5, PS5 Pro and Xbox Series X|S. There is no 60 fps or 40 fps mode, not even on PS5 Pro.",
           art.fps(), """
  <h2>By console</h2>
  <div class="scroll"><table>
    <tr><th>Console</th><th>What testing shows</th></tr>
    <tr><td><b>PS5 Pro</b></td><td>30 fps, held almost perfectly. Digital Foundry played for more than 50 hours without a noticeable dip. Renders at 1440p and upscales with PSSR for a sharper, near-4K look</td></tr>
    <tr><td><b>PS5</b></td><td>30 fps target with small dips throughout, and longer drops below 30 in heavy action such as big explosions. Renders at 1440p</td></tr>
    <tr><td><b>Xbox Series X</b></td><td>30 fps, generally held, with dips in busy chases and firefights. Renders at about 1440p. Close to the standard PS5, and slightly smoother on a 120Hz TV with VRR</td></tr>
    <tr><td><b>Xbox Series S</b></td><td>30 fps target, but often runs in the mid to upper 20s, and around 20 fps in heavy combat or when vehicles are destroyed. Renders at about 720p</td></tr>
  </table></div>
  <p class="note">All results from Digital Foundry's launch testing, published November 18, 2026, as reported by VGC, Pure Xbox and Kotaku. The PS5 1440p figure is as reported by TweakTown. Full Xbox details: <a href="/news/gta-6-xbox-series-x-s-performance-tested/">GTA 6 on Xbox, tested</a>.</p>
  <h2>How bad are the drops?</h2>
  <p>Xbox Series S has the biggest problem: Digital Foundry found it slips below 30 fps during much of normal play, not only in big fights. On Series X, drops are limited to the busiest moments, much like PS5.</p>
  <p>On PS5 Pro, the only drop Digital Foundry found was to 24 fps, and only when the tester deliberately set off huge numbers of explosions at once. On the standard PS5, the dips are minor in normal play but noticeable, and heavy fights can keep it below 30 until you leave the area. Some reviewers also mention frame rate dips in chases on PS5.</p>
  <h2>Why not 60?</h2>
  <p>A world this dense leans on the processor, and the PS5 Pro has the same CPU as the standard PS5, so its stronger graphics chip does not lift that limit. Digital Foundry's John Linneman doubts 60 fps is possible in a game of this scope on current consoles.</p>
  <h2>Could a 40 or 60 fps mode come later?</h2>
  <p>Nothing has been announced. Any site that promises a patch date is guessing.</p>
  <h2>Get the smoothest picture you can</h2>
  <ul>
    <li><b>Switch your TV to Game Mode.</b> It cuts the delay between pressing a button and seeing the result.</li>
    <li><b>Turn off motion smoothing.</b> It adds delay and visual glitches in games.</li>
    <li><b>Use an HDMI port that supports your TV's best features</b> if your set has only some ports marked for gaming.</li>
  </ul>
  <p>What critics made of the 30 fps cap: <a href="/news/gta-6-reviews-metacritic-99/">GTA 6 reviews round-up</a>.</p>""")

REVIEWS = page("/reviews/", "Before you buy", "GTA 6 reviews: what critics say",
               "Reviews went live on November 18, 2026, the day before launch. The PS5 version opened with a 99 Metascore from 98 reviews, an early figure that will move as more arrive.",
               art.reviews_cal(), """
  <h2>The scores so far</h2>
  <ul>
    <li><b>Metacritic, PS5:</b> 99 from 98 critic reviews (morning of November 18).</li>
    <li><b>Metacritic, Xbox Series X:</b> 99 from 9 reviews.</li>
    <li><b>Perfect scores:</b> IGN, VICE, Push Square and Cultured Vultures gave 10/10, and Creative Bloq gave 5/5.</li>
  </ul>
  <p>For comparison, GTA IV has a 98 and GTA V a 97.</p>
  <h2>In one line</h2>
  <p>Critics love the world, the driving and Jason and Lucia's story. The common complaints are fiddly controls, clunky small guns, slow later chapters and the 30 fps cap. Our <a href="/news/gta-6-reviews-metacritic-99/">full reviews round-up</a> has who said what.</p>
  <h2>Where to check the latest scores</h2>
  <ul>
    <li><b>Metacritic and OpenCritic</b> collect critic scores in one place. Look at how many reviews a score is based on.</li>
    <li><b>Performance:</b> see our <a href="/frame-rate/">frame rate guide</a> for tested results by console.</li>
  </ul>
  <h2>If you pre-ordered and changed your mind</h2>
  <p>Check the refund rules for the PlayStation Store or Microsoft Store now. Stores generally treat a pre-order differently once the game is released and downloaded.</p>""")

LENGTH = page("/story-length/", "The story", "How long is GTA 6?",
              "About 80 hours for the main story, going by one Rockstar developer's own playthrough. That is far longer than GTA V.",
              art.length_chart(), """
  <h2>Where the 80 hours comes from</h2>
  <p>Rockstar North's Rob Nelson told The New York Times that his playthrough in February 2026 took about 80 hours. It covered the main story and some optional goals that affect the narrative. It did not include all the side content, which would add more.</p>
  <h2>How the story is built</h2>
  <ul>
    <li>The story is split into chapters, and previews describe its length as comparable to Red Dead Redemption 2.</li>
    <li>It opens in the Leonida Keys, and the rest of the map opens up after the first missions.</li>
    <li>Previews say missions are less restrictive than in GTA V, with more than one way to approach them.</li>
  </ul>
  <h2>How many missions are there?</h2>
  <p>Rockstar has not published a mission count. The <a href="/tracker/">progress tracker</a> gets the full mission list once the game is out and it can be verified.</p>
  <h2>How long for 100%?</h2>
  <p>Unknown until players finish it. With a map about three times the size of Red Dead Redemption 2's, expect far more than 80 hours. See <a href="/map-size/">how big the map is</a>.</p>""")

RADIO = page("/radio-stations/", "Music", "GTA 6 radio stations and hosts",
             "Rockstar has revealed six GTA VI radio stations so far, with previews on its official music page. The full song list has not been published.",
             art.radio(), """
  <h2>The six stations</h2>
  <div class="scroll"><table>
    <tr><th>Station</th><th>Genre</th><th>Reported hosts</th></tr>
    <tr><td><b>Flash FM</b></td><td>Pop</td><td>Robyn and Alex Consani</td></tr>
    <tr><td><b>Cocoteo FM</b></td><td>Modern Latin: reggaeton, dembow, bachata, merengue</td><td>Bad Bunny and RaiNao</td></tr>
    <tr><td><b>Back Country Radio</b></td><td>Country</td><td>MW and Delta Dawne</td></tr>
    <tr><td><b>AfroBank FM</b></td><td>African music, from classics to amapiano</td><td>Burna Boy and Palms Trax</td></tr>
    <tr><td><b>The Chamber 106.6</b></td><td>Metal from the 1980s onward</td><td>Kerry King and Tom Araya</td></tr>
    <tr><td><b>Dirty South Classics</b></td><td>Southern rap and hip-hop classics</td><td>Trick Daddy and Trina</td></tr>
  </table></div>
  <p class="note">Station names and genres come from Rockstar's reveal in October 2026. Host names are as reported by games media at the time.</p>
  <h2>New ways to listen</h2>
  <ul>
    <li><b>On foot.</b> Jason and Lucia can listen through earbuds connected to their phones, not only in vehicles.</li>
    <li><b>Podcasts on demand.</b> The radio menu has a podcast section you can play whenever you like.</li>
    <li><b>Streamer-safe music.</b> Previews describe a toggle for copyright-free music, made for people who record or stream.</li>
  </ul>
  <h2>Is the full soundtrack out?</h2>
  <p>No. Rockstar has not published a track list, and more stations are expected. Song lists you see before launch are guesses or leaks.</p>""")

MAP = page("/map-size/", "The world", "How big is the GTA 6 map?",
           "The state of Leonida is reported to be about three times the size of Red Dead Redemption 2's map, which would make it Rockstar's largest world so far.",
           art.map_size(), """
  <h2>The numbers reported from previews</h2>
  <ul>
    <li><b>Whole map:</b> about 3 times the playable area of Red Dead Redemption 2.</li>
    <li><b>Vice City:</b> about 2 times the size of GTA V's Los Santos.</li>
    <li><b>Built-up land:</b> roughly 11 times the urban area of GTA V, counting the smaller towns.</li>
    <li><b>Roads:</b> about 15% narrower than in GTA V.</li>
  </ul>
  <p>These figures were relayed by people who attended Rockstar preview events. Rockstar has not published official measurements.</p>
  <h2>The six regions</h2>
  <div class="scroll"><table>
    <tr><th>Region</th><th>What it is</th></tr>
    <tr><td><b>Vice City</b></td><td>The main city: beaches, downtown and neon</td></tr>
    <tr><td><b>Leonida Keys</b></td><td>Island chain where the story begins</td></tr>
    <tr><td><b>Grassrivers</b></td><td>Wetlands and swamp</td></tr>
    <tr><td><b>Port Gellhorn</b></td><td>A worn coastal town</td></tr>
    <tr><td><b>Ambrosia</b></td><td>Industrial heartland</td></tr>
    <tr><td><b>Mount Kalaga</b></td><td>National park with forest and hills</td></tr>
  </table></div>
  <h2>How the map works in the game</h2>
  <ul>
    <li>Areas you have not visited are hidden until you explore them.</li>
    <li>The map screen uses satellite-style imagery.</li>
    <li>Fast travel uses the RydeMe taxi app, buses and a working train line.</li>
    <li>Previews report a very large number of buildings you can enter.</li>
  </ul>
  <p>Track which regions you have visited in the <a href="/tracker/">progress tracker</a>.</p>""")

CAST = page("/characters/", "The story", "GTA 6 characters: who's who",
            "GTA VI has two playable leads, Jason Duval and Lucia Caminos, and Rockstar has introduced six more characters around them.",
            art.cast(), """
  <h2>The leads</h2>
  <div class="scroll"><table>
    <tr><th>Character</th><th>Who they are</th></tr>
    <tr><td><b>Jason Duval</b></td><td>A former soldier who grew up around criminals and has been running drugs in the Keys</td></tr>
    <tr><td><b>Lucia Caminos</b></td><td>A fighter just out of prison who wants a better life for her family</td></tr>
  </table></div>
  <p>You can switch between them at any time. See <a href="/characters/">the characters guide</a>.</p>
  <h2>The people around them</h2>
  <div class="scroll"><table>
    <tr><th>Character</th><th>Who they are</th></tr>
    <tr><td><b>Cal Hampton</b></td><td>Jason's friend, a reclusive tech obsessive who listens in on restricted radio channels</td></tr>
    <tr><td><b>Brian Heder</b></td><td>A veteran drug runner with a boat yard, and Jason's landlord</td></tr>
    <tr><td><b>Raul Bautista</b></td><td>A charming, manipulative bank robber who is always recruiting</td></tr>
    <tr><td><b>Boobie Ike</b></td><td>A Vice City figure with real estate, a strip club and a recording studio</td></tr>
    <tr><td><b>Dre'Quan Priest</b></td><td>An aspiring music mogul connected to Boobie Ike</td></tr>
    <tr><td><b>Real Dimez</b></td><td>Rap duo Bae-Luxe and Roxy, chasing their next hit</td></tr>
  </table></div>
  <h2>Who are the voice actors?</h2>
  <p>Rockstar has not announced the actors behind Jason and Lucia. Names circulating online are fan theories and reports, so they are not listed here. This page will be updated when the cast is confirmed.</p>""")

PLATFORMS = page("/platforms/", "Platforms", "Can you play GTA 6 on PS4, Xbox One or PC?",
                 "GTA VI launches on November 19, 2026 for PS5 and Xbox Series X|S. Xbox One owners can stream it through Xbox Cloud Gaming. There is no PS4 or PC version.",
                 art.platforms(), """
  <h2>Console by console</h2>
  <div class="scroll"><table>
    <tr><th>System</th><th>GTA VI</th></tr>
    <tr><td><b>PS5 and PS5 Slim</b></td><td>Yes</td></tr>
    <tr><td><b>PS5 Pro</b></td><td>Yes, listed as PS5 Pro Enhanced</td></tr>
    <tr><td><b>Xbox Series X</b></td><td>Yes</td></tr>
    <tr><td><b>Xbox Series S</b></td><td>Yes, but check storage: the game needs up to 212 GB</td></tr>
    <tr><td><b>Xbox One</b></td><td>Streaming only, through Xbox Cloud Gaming from November 19 at 1am ET. You must buy the game. <a href="/news/gta-6-xbox-one-cloud-gaming/">Details</a></td></tr>
    <tr><td><b>PS4</b></td><td>No</td></tr>
    <tr><td><b>PC</b></td><td>Not announced. See <a href="/pc-release/">the PC page</a></td></tr>
    <tr><td><b>Nintendo Switch 2</b></td><td>Not announced</td></tr>
  </table></div>
  <h2>Things to know before buying a console for it</h2>
  <ul>
    <li><b>There is no disc.</b> Boxed copies contain a download code, so a console without a disc drive works fine.</li>
    <li><b>You need an internet connection</b> to download the game.</li>
    <li><b>Storage matters.</b> A 512 GB Xbox Series S has about 364 GB of usable space, and GTA VI can take 212 GB of it. See the <a href="/storage/">storage guide</a>.</li>
  </ul>
  <h2>Is it on Game Pass or PlayStation Plus?</h2>
  <p>We have found no announcement that GTA VI will be included with either subscription at launch. Plan on buying it. See <a href="/editions/">Standard vs Ultimate</a>.</p>""")

WANTED = page("/wanted-level/", "Gameplay", "GTA 6 wanted level: how it works and how to lose it",
              "Police in GTA VI only come after you when a crime is seen, reported or caught on camera, and they chase a description of you that you can change.",
              art.wanted(), """
  <p class="note">Based on hands-on previews. Every point gets re-tested in the finished game on launch day.</p>
  <h2>How you get stars</h2>
  <ul>
    <li>A witness sees the crime, the victim reports it, or a security system records it. No witness, no stars.</li>
    <li>The maximum is six stars. One star is fairly easy to escape.</li>
    <li>Hollow stars mean police know a crime happened but not who did it. They turn solid once you are identified.</li>
  </ul>
  <h2>What police know about you</h2>
  <p>Officers build a profile of your face, outfit, weapons and vehicle, and the screen shows which parts they have. Police do not normally appear as dots on the minimap during a chase, so you have to spot them yourself.</p>
  <h2>How to lose a wanted level</h2>
  <ul>
    <li><b>Break line of sight</b> and get out of the search area around the crime until it cools down.</li>
    <li><b>Change your look.</b> Swap outfits, or change your hair at a salon.</li>
    <li><b>Ditch what they identified.</b> Drop the weapon or leave the car they have on record.</li>
    <li><b>Switch to an ordinary vehicle</b> to pass roadblocks without being noticed.</li>
    <li><b>Use Pay &amp; Spray</b> to repaint a car mid-chase.</li>
    <li><b>Split up.</b> Separating Jason and Lucia drops the active player's level by one star.</li>
  </ul>
  <h2>Before the crime</h2>
  <p>Wearing a mask stops cameras and witnesses from identifying your face in the first place.</p>
  <h2>What happens if you are busted?</h2>
  <p>Getting arrested costs you the cash you are carrying. Money already deposited at an ATM is safe, which is a good reason to bank it before a risky job.</p>""")

ARTICLES2 = [
    ("/pc-release/", "Is GTA 6 Coming to PC? Release Date Status" + BRAND, "GTA VI launches on PS5 and Xbox Series X|S only. What Take-Two has said about PC, how long GTA V and Red Dead 2 took, and whether to wait.", PC),
    ("/online/", "Does GTA 6 Have Online at Launch? Multiplayer Explained" + BRAND, "GTA VI is listed as single-player for November 19, 2026. What is confirmed about an online mode, what is only reported, and what happens to GTA Online.", ONLINE),
    ("/frame-rate/", "Is GTA 6 30 or 60 FPS? PS5, PS5 Pro and Xbox Performance" + BRAND, "GTA VI runs at 30 fps on every console, with no 60 fps mode even on PS5 Pro. Tested results for PS5 and PS5 Pro, and what to expect on Xbox.", FPS),
    ("/reviews/", "GTA 6 Reviews: Metacritic Score and What Critics Say" + BRAND, "GTA VI reviews went live on November 18. The early Metacritic score, the perfect scores, and the most common complaints.", REVIEWS),
    ("/story-length/", "How Long Is GTA 6? Story Length in Hours" + BRAND, "GTA VI's story took a Rockstar developer about 80 hours. Where that number comes from and how it compares with GTA V and Red Dead Redemption 2.", LENGTH),
    ("/radio-stations/", "GTA 6 Radio Stations: All Six Stations and Hosts" + BRAND, "The six GTA VI radio stations revealed so far, their genres and reported hosts, plus podcasts and listening on foot.", RADIO),
    ("/map-size/", "How Big Is the GTA 6 Map? Leonida Size and Regions" + BRAND, "The GTA VI map is reported at about three times Red Dead Redemption 2's. Size comparisons, the six regions of Leonida and how the map works.", MAP),
    ("/characters/", "GTA 6 Characters: Jason, Lucia and the Full Cast" + BRAND, "Who's who in GTA VI: playable leads Jason Duval and Lucia Caminos and the six characters around them, plus what is known about the voice cast.", CAST),
    ("/platforms/", "Can You Play GTA 6 on PS4, Xbox One or PC?" + BRAND, "GTA VI launches on PS5 and Xbox Series X|S, and streams to Xbox One through Xbox Cloud Gaming. A console-by-console list.", PLATFORMS),
    ("/wanted-level/", "GTA 6 Wanted Level: How It Works and How to Lose It" + BRAND, "How GTA VI's six-star wanted level works, what hollow stars mean, and every reported way to lose the police.", WANTED),
]
