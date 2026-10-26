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

# Sprint 1: add get_revenues() and add_revenue().
# Sprint 2: add summary() with separate SUM queries for each table.
