(function () {
  var KEY = "ledgerGuideCompleted";
  var dialog = document.getElementById("guide");
  var steps = Array.prototype.slice.call(dialog.querySelectorAll(".step"));
  var back = document.getElementById("back-step");
  var next = document.getElementById("next-step");
  var count = document.getElementById("step-count");
  var bar = document.getElementById("progress-bar");
  var opener = document.getElementById("open-guide");
  var current = 0;
  var returnFocus = null;

  function read() { try { return localStorage.getItem(KEY); } catch (e) { return null; } }
  function write() { try { localStorage.setItem(KEY, "1"); } catch (e) {} }

  function show(index, moveFocus) {
    current = Math.max(0, Math.min(steps.length - 1, index));
    steps.forEach(function (s, i) { s.hidden = i !== current; });
    count.textContent = "Step " + (current + 1) + " of " + steps.length;
    bar.style.width = ((current + 1) / steps.length * 100) + "%";
    back.hidden = current === 0;
    next.hidden = current === steps.length - 1;
    if (moveFocus) steps[current].focus();
  }

  function open() {
    if (dialog.open) return;
    returnFocus = document.activeElement;
    show(0, false);
    if (typeof dialog.showModal === "function") dialog.showModal(); else dialog.setAttribute("open", "");
    steps[0].focus();
  }

  // Closing by any route (Skip, Esc, Finish) counts as done, so it never reappears uninvited.
  dialog.addEventListener("close", function () {
    write();
    if (returnFocus && document.contains(returnFocus) && !dialog.dataset.goForm) returnFocus.focus();
    delete dialog.dataset.goForm;
  });
  // Clicking the dimmed backdrop closes too.
  dialog.addEventListener("click", function (e) { if (e.target === dialog) dialog.close(); });

  next.addEventListener("click", function () { show(current + 1, true); });
  back.addEventListener("click", function () { show(current - 1, true); });
  opener.addEventListener("click", open);
  document.getElementById("finish-guide").addEventListener("click", function () { dialog.close(); });
  document.getElementById("go-to-form").addEventListener("click", function () {
    dialog.dataset.goForm = "1";
    dialog.close();
    window.openRecordDialog();
  });

  // After saving, move focus to the confirmation so screen readers announce it.
  var saved = document.getElementById("saved-message");
  if (saved) saved.focus();

  var recordOpen = document.getElementById("record-dialog").open;
  if (!read() && !saved && !recordOpen) open();
})();
