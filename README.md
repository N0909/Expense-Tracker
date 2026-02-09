# Expense Tracker CLI

A simple command-line tool to track daily expenses.
You can add, delete, list, and summarize your expenses directly from the terminal.

This project stores data in a JSON file and provides a clean table view for better readability.

---

## Features

* Add a new expense with description and amount
* Delete an expense by ID
* List all expenses
* Filter expenses by month
* Get total expense summary
* Monthly summary support

---

## Tech Stack

* Python
* `dataclasses` for structured data
* `argparse` for CLI handling
* `tabulate` for formatted terminal tables
* JSON file for data persistence

---

## Installation

Clone the repository:

```bash
git clone https://github.com/N0909/Expense-Tracker.git
cd expense-tracker
```

Install dependencies:

```bash
pip install tabulate
```

Make sure an `expense.json` file exists in the root directory.
If not, create one with the following initial content:

```json
[0, []]
```

---

## Usage

### Add an Expense

```bash
python main.py add "Groceries" 250.50
```

### Delete an Expense

```bash
python main.py delete 1
```

### List All Expenses

```bash
python main.py list
```

### List Expenses by Month

```bash
python main.py list --month 2
```

### Get Total Summary

```bash
python main.py summary
```

### Get Monthly Summary

```bash
python main.py summary --month 2
```

---

## Project Structure

```
expense-tracker/
│
├── expense-tracker.py          # CLI entry point
├── working.py       # Core expense logic
├── expense.json     # Data storage
└── README.md
```

---

## Credits

This project idea is based on the Expense Tracker project from roadmap.sh:

[https://roadmap.sh/projects/expense-tracker](https://roadmap.sh/projects/expense-tracker)
