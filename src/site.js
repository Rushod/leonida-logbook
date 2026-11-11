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
