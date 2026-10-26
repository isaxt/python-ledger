CREATE TABLE IF NOT EXISTS expenses (
    id INTEGER PRIMARY KEY,
    entry_date TEXT NOT NULL,
    description TEXT NOT NULL,
    category TEXT NOT NULL,
    amount INTEGER NOT NULL CHECK(amount >= 0)
);

CREATE TABLE IF NOT EXISTS revenues (
    id INTEGER PRIMARY KEY,
    entry_date TEXT NOT NULL,
    description TEXT NOT NULL,
    category TEXT NOT NULL,
    amount INTEGER NOT NULL CHECK(amount >= 0)
);
