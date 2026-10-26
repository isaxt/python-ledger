# Student starter: Paperback & Pour

This is a working starting point for the class activity. Templates, CSS, app.py,
models.py, and the schema are supplied. You do not need to build the interface
from scratch.

## Run

Open a terminal in this starter folder:

```bash
python -m pip install -r requirements.txt
python init_db.py
python -m flask --app app run --debug
```

Open http://127.0.0.1:5000. Stop with Ctrl+C. Run init_db.py before the app's
first start. It creates missing tables without deleting existing records.

## Already working

- Expense form, saved database records, and expense list.
- Both expenses and revenues tables.
- Inherited base template and stylesheet.

## Your team builds

1. Revenue input, saving, and listing.
2. Separate expense and revenue totals and net cash flow.
3. If time permits, expense totals by category after the client change request.

Read 02_agile_ledger_group_activity.ipynb for the stories and sprint schedule.
All amounts are whole US dollars. Use fictional test records.

File map: app.py handles requests; models.py contains SQL; schema.sql defines
tables; templates/index.html holds the form and table; templates/base.html
holds shared structure; static/style.css contains the supplied styling.

The SQL notebook uses pandas to display query results. The Flask app itself
needs Flask and Python's built-in sqlite3, so pandas is not an app dependency.
