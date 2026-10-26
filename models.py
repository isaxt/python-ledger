import sqlite3
from pathlib import Path

ROOT = Path(__file__).parent
DB_PATH = ROOT / "ledger.db"


def initialize():
    connection = sqlite3.connect(DB_PATH)
    connection.executescript((ROOT / "schema.sql").read_text())
    connection.commit()
    connection.close()


def query(sql, values=()):
    connection = sqlite3.connect(DB_PATH)
    connection.row_factory = sqlite3.Row
    rows = connection.execute(sql, values).fetchall()
    connection.commit()
    connection.close()
    return rows


def get_expenses():
    return query("SELECT * FROM expenses ORDER BY entry_date DESC, id DESC")


def add_expense(entry_date, description, category, amount):
    query(
        "INSERT INTO expenses (entry_date, description, category, amount) VALUES (?, ?, ?, ?)",
        (entry_date, description, category, amount),
    )

def get_revenues():
    return query("SELECT * FROM revenues ORDER BY entry_date DESC, id DESC")


def add_revenue(entry_date, description, category, amount):
    query(
        "INSERT INTO revenues (entry_date, description, category, amount) VALUES (?, ?, ?, ?)",
        (entry_date, description, category, amount),
    )


def summary():
    """Separate SUMs (no join, so rows are never multiplied); empty tables give 0."""
    revenue = query("SELECT COALESCE(SUM(amount), 0) AS total FROM revenues")[0]["total"]
    expenses = query("SELECT COALESCE(SUM(amount), 0) AS total FROM expenses")[0]["total"]
    return {"revenue": revenue, "expenses": expenses, "net": revenue - expenses}


def expense_totals_by_category():
    return query(
        "SELECT category, SUM(amount) AS total FROM expenses "
        "GROUP BY category ORDER BY total DESC, category"
    )
