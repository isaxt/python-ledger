from datetime import date

from flask import Flask, redirect, render_template, request, url_for
import models

app = Flask(__name__)


@app.template_filter("money")
def money(value):
    return f"{int(value):,}"


def render_page(status=200, errors=None, form=None):
    saved = request.args.get("saved")
    categories = models.expense_totals_by_category()
    return render_template(
        "index.html",
        saved=saved if saved in ("expense", "revenue") else None,
        categories=models.category_suggestions(),
        expenses=models.get_expenses(),
        revenues=models.get_revenues(),
        summary=models.summary(),
        category_totals=categories,
        errors=errors or [],
        form=form or {"record_type": "expense"},
    ), status


def validate(form):
    errors = []
    if form.get("record_type") not in ("expense", "revenue"):
        errors.append("Choose whether this record is revenue or an expense.")
    try:
        date.fromisoformat(form.get("entry_date", ""))
    except ValueError:
        errors.append("Enter the date in year-month-day format, for example 2026-10-26.")
    if not form.get("description", "").strip():
        errors.append("Add a short description of what the money was for.")
    if not form.get("category", "").strip():
        errors.append("Add a category, such as Sales or Supplies.")
    try:
        amount = int(form.get("amount", ""))
        if amount < 0:
            errors.append("Amount cannot be negative. Choose Expense to record money going out.")
    except ValueError:
        errors.append("Enter the amount as a whole number of dollars, such as 35.")
    return errors


@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        form = request.form
        errors = validate(form)
        if errors:
            return render_page(400, errors, form.to_dict())
        add = {"expense": models.add_expense, "revenue": models.add_revenue}[form["record_type"]]
        add(
            form["entry_date"], form["description"].strip(),
            form["category"].strip(), int(form["amount"]),
        )
        return redirect(url_for("index", saved=form["record_type"], _anchor="saved-message"))
    return render_page()
