# 💼 Expense Tracker

**Expense Tracker** is a simple, console-based Python application to help users manage personal finances. It allows you to record expenses, categorize them, filter by date or category, view summaries, and save data in multiple formats like TXT, CSV, and JSON. This project is perfect for anyone looking to track spending habits and gain insights into their financial behavior.

---

## Features

- Add new expenses with date, category, amount, and optional notes.
- View all recorded expenses in a tabular format.
- Filter expenses by **category** or **specific date**.
- View **total spent** across all expenses.
- Generate **summary by category**.
- Save expenses in multiple formats:
  - TXT
  - CSV
  - JSON
  - All formats at once
- Automatic backup before saving.
- Predefined categories: `food`, `travel`, `bills`, `shopping`, `others`.
- User-friendly console menu.

---

## How It Works

1. **Load Existing Data:** On startup, the program loads previously saved expenses from `expenses.txt`.
2. **Add Expenses:** Users can input date, category, amount, and notes.
3. **Save Expenses:** Choose to save in TXT, CSV, JSON, or all formats.
4. **View & Filter:** See all expenses, filter by category or date, and get a summary.
5. **Menu Navigation:** Use a simple numbered menu to navigate all features.

---

## Tech Stack

- Python 3.x
- Standard Libraries:
  - `os` for file operations
  - `csv` and `json` for data export
  - `datetime` for handling dates

---

## Usage

1. Clone the repository:
   ```bash
   git clone https://github.com/yugvac/Expense-Tracker.git
