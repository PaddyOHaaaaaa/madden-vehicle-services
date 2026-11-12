// Simple cookie consent banner. Only essential storage is used to remember the choice.
(function () {
  var KEY = "mvs-cookie-consent";
  var banner = document.getElementById("cookie-banner");
  if (!banner) return;

  var saved = null;
  try { saved = localStorage.getItem(KEY); } catch (e) {}
  if (!saved) banner.classList.add("show");

  function choose(value) {
    try { localStorage.setItem(KEY, value); } catch (e) {}
    banner.classList.remove("show");
  }

  var accept = document.getElementById("cookie-accept");
  var reject = document.getElementById("cookie-reject");
  if (accept) accept.addEventListener("click", function () { choose("accepted"); });
  if (reject) reject.addEventListener("click", function () { choose("rejected"); });

  // Footer year
  var year = document.getElementById("year");
  if (year) year.textContent = new Date().getFullYear();
})();
