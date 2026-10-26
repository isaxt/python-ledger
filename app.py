from flask import Flask, redirect, render_template, request, url_for
import models

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        models.add_expense(
            request.form["entry_date"], request.form["description"],
            request.form["category"], int(request.form["amount"]),
        )
        return redirect(url_for("index"))
    return render_template("index.html", expenses=models.get_expenses())
