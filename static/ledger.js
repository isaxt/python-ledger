(function () {
  var dialog = document.getElementById("record-dialog");
  var form = document.getElementById("record-form");
  var outcome = document.getElementById("outcome");
  var dateInput = document.getElementById("f-date");
  var opener = null;

  function today() {
    var d = new Date();
    var m = String(d.getMonth() + 1).padStart(2, "0");
    var day = String(d.getDate()).padStart(2, "0");
    return d.getFullYear() + "-" + m + "-" + day;
  }

  function selectedType() { return form.querySelector("input[name=record_type]:checked").value; }

  function updateOutcome() {
    outcome.textContent = selectedType() === "revenue"
      ? "Saving adds this to Money in and increases Total revenue and Net cash flow."
      : "Saving adds this to Money out and Spending by category, and increases Total expenses.";
  }

  function openRecord(type) {
    if (dialog.open) return;
    opener = document.activeElement;
    if (!opener || opener === document.body || opener.closest("#guide")) opener = document.querySelector(".site-header .js-add-record");
    if (type) form.querySelector("input[value=" + type + "]").checked = true;
    if (!dateInput.value) dateInput.value = today();
    updateOutcome();
    dialog.showModal();
    document.getElementById("f-desc").focus();
  }
  window.openRecordDialog = openRecord;

  function close() { dialog.close(); }
  dialog.addEventListener("close", function () {
    if (opener && document.contains(opener)) opener.focus();
  });
  dialog.addEventListener("click", function (e) { if (e.target === dialog) close(); });
  document.getElementById("close-record").addEventListener("click", close);
  document.getElementById("cancel-record").addEventListener("click", close);
  Array.prototype.forEach.call(form.querySelectorAll("input[name=record_type]"), function (r) {
    r.addEventListener("change", updateOutcome);
  });

  document.addEventListener("click", function (e) {
    var btn = e.target.closest(".js-add-record");
    if (!btn) return;
    e.preventDefault();
    openRecord(btn.getAttribute("data-type"));
  });

  var dismiss = document.getElementById("dismiss-notice");
  if (dismiss) dismiss.addEventListener("click", function () {
    var n = document.getElementById("saved-message");
    n.remove();
    document.getElementById("main").focus();
  });

  if (dialog.hasAttribute("data-open-on-load")) {
    updateOutcome();
    dialog.showModal();
  }
})();
