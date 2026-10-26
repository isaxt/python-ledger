from flask import Flask, redirect, render_template, request, url_for
import models

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        record_type = request.form.get("record_type")
        try:
            amount = int(request.form["amount"])
        except ValueError:
            return "Amount must be a whole number of dollars.", 400
        if amount < 0:
            return "Amount cannot be negative.", 400
        add = {"expense": models.add_expense, "revenue": models.add_revenue}.get(record_type)
        if add is None:
            return "Choose expense or revenue.", 400
        add(
            request.form["entry_date"], request.form["description"].strip(),
            request.form["category"].strip(), amount,
        )
        return redirect(url_for("index"))
    return render_template(
        "index.html",
        expenses=models.get_expenses(),
        revenues=models.get_revenues(),
        summary=models.summary(),
        category_totals=models.expense_totals_by_category(),
    )
