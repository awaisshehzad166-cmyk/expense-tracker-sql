# Expense Tracker (SQL)

A command-line Expense Tracker built with Python and SQLite. Allows adding, viewing, searching, updating, and deleting expense records, with data persisted in a SQL database. Also provides category-wise spending statistics.

## Features
- Add new expense records
- View all expenses
- Search expense by ID
- Update expense details
- Delete expense record
- View statistics (total expenses, sum, average, highest, lowest, category-wise totals)

## Tech Stack
- Python
- SQLite (via sqlite3 module)

## How to Run
python expense_tracker.py

## What I Learned
- Connecting Python with a SQL database using sqlite3
- Writing SQL queries (CREATE, INSERT, SELECT, UPDATE, DELETE) from Python
- Using parameterized queries (?) to prevent SQL injection
- Using row_factory to get dictionary-style access to query results
- Aggregate SQL functions (COUNT, SUM, AVG, GROUP BY)
