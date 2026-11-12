/* Leonida Logbook: countdown, saved checklists and progress bars. Page content is static HTML built by build.py. */
(function () {
  var RELEASE = new Date(2026, 10, 19, 0, 0, 0); // local midnight, Nov 19 2026
  var KEY = "leonida-logbook-v1";
  var $ = function (id) { return document.getElementById(id); };
  var saved = {};
  try { saved = JSON.parse(localStorage.getItem(KEY) || "{}") || {}; } catch (e) { saved = {}; }
  function persist() { try { localStorage.setItem(KEY, JSON.stringify(saved)); } catch (e) {} }

  var boxes = [].slice.call(document.querySelectorAll("input[data-key]"));
  boxes.forEach(function (b) { b.checked = !!saved[b.dataset.key]; });

  function updateProgress() {
    var done = 0, total = 0;
    [].forEach.call(document.querySelectorAll("[data-group]"), function (g) {
      var items = g.querySelectorAll("input[data-key]"), d = 0;
      [].forEach.call(items, function (i) { if (i.checked) d++; });
      var n = g.querySelector(".count"), bar = g.querySelector(".bar i");
      if (n) n.textContent = d + " / " + items.length;
      if (bar) bar.style.width = (items.length ? 100 * d / items.length : 0) + "%";
      if (g.dataset.group !== "prep") { done += d; total += items.length; }
    });
    if ($("totalPct")) {
      var pct = total ? Math.round(100 * done / total) : 0;
      $("totalPct").textContent = pct + "%";
      $("totalBar").style.width = pct + "%";
      $("totalNote").textContent = done + " of " + total + " items ticked. More lists unlock at launch.";
    }
  }
  document.addEventListener("change", function (e) {
    var k = e.target.dataset && e.target.dataset.key; if (!k) return;
    if (e.target.checked) saved[k] = 1; else delete saved[k];
    persist(); updateProgress();
  });
  updateProgress();

  if ($("resetBtn")) {
    var show = function (confirming) { $("resetWrap").hidden = confirming; $("resetConfirm").hidden = !confirming; };
    $("resetBtn").onclick = function () { show(true); };
    $("resetNo").onclick = function () { show(false); };
    $("resetYes").onclick = function () {
      Object.keys(saved).forEach(function (k) { if (k.indexOf("prep-") !== 0) delete saved[k]; });
      persist();
      boxes.forEach(function (b) { if (b.dataset.key.indexOf("prep-") !== 0) b.checked = false; });
      updateProgress(); show(false);
    };
  }

  [].forEach.call(document.querySelectorAll("[data-db]"), function (db) {
    var q = db.querySelector("input[type=search]"), chips = db.querySelectorAll(".chip"), rows = db.querySelectorAll("tr[data-type], .wcard[data-type]"), type = "";
    function run() {
      var t = q ? (q.value || "").toLowerCase() : "", n = 0;
      [].forEach.call(rows, function (r) {
        var ok = (!type || r.getAttribute("data-type") === type) && r.textContent.toLowerCase().indexOf(t) !== -1;
        r.hidden = !ok; if (ok) n++;
      });
      var em = db.querySelector("[data-empty]"); if (em) em.hidden = n > 0;
    }
    if (q) q.addEventListener("input", run);
    [].forEach.call(chips, function (c) { c.addEventListener("click", function () {
      type = c.getAttribute("data-type"); [].forEach.call(chips, function (x) { x.classList.toggle("on", x === c); }); run();
    }); });
  });

  var cheats = document.querySelector(".cheats");
  if (cheats) {
    var segs = document.querySelectorAll(".seg button");
    var setShow = function (v) {
      cheats.setAttribute("data-show", v);
      [].forEach.call(segs, function (b) { b.setAttribute("aria-pressed", String(b.getAttribute("data-show") === v)); });
      try { localStorage.setItem("leonida-cheat-platform", v); } catch (e) {}
    };
    [].forEach.call(segs, function (b) { b.addEventListener("click", function () { setShow(b.getAttribute("data-show")); }); });
    try { var pv = localStorage.getItem("leonida-cheat-platform"); if (pv) setShow(pv); } catch (e) {}
    document.addEventListener("click", function (ev) {
      var b = ev.target.closest && ev.target.closest("[data-copy]"); if (!b) return;
      var code = b.getAttribute("data-copy");
      var done = function () { b.textContent = "Copied"; setTimeout(function () { b.textContent = "Copy"; }, 1500); };
      if (navigator.clipboard && navigator.clipboard.writeText) navigator.clipboard.writeText(code).then(done, function () { selectCode(b); });
      else selectCode(b);
    });
    var selectCode = function (b) { var c = b.previousElementSibling; var r = document.createRange(); r.selectNodeContents(c); var s = getSelection(); s.removeAllRanges(); s.addRange(r); };
  }

  if ($("clock")) {
    var pad = function (n) { return String(n).padStart(2, "0"); };
    var tick = function () {
      var ms = RELEASE - Date.now();
      if (ms <= 0) {
        $("heroEyebrow").textContent = "Released November 19, 2026";
        $("heroTitle").textContent = "GTA VI is out now";
        $("clock").hidden = true; $("clockNote").hidden = true; return;
      }
      var s = Math.floor(ms / 1000);
      $("cd").textContent = Math.floor(s / 86400); $("ch").textContent = pad(Math.floor(s % 86400 / 3600));
      $("cm").textContent = pad(Math.floor(s % 3600 / 60)); $("cs").textContent = pad(s % 60);
    };
    tick(); setInterval(tick, 1000);
  }
})();
