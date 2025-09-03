import os
import csv
import json
from datetime import datetime

expenses = []

TXT_FILE = 'expenses.txt'
CSV_FILE = 'expenses.csv'
JSON_FILE = 'expenses.json'
BACKUP_FILE = 'expenses_backup.txt'

CATEGORIES = ['food', 'travel', 'bills', 'shopping', 'others']


def load_expenses():
    if os.path.exists(TXT_FILE):
        with open(TXT_FILE, 'r') as f:
            for line in f:
                parts = line.strip().split('|')
                if len(parts) == 4:
                    date, category, amount, note = parts
                    expenses.append({
                        'date': date,
                        'category': category,
                        'amount': float(amount),
                        'note': note
                    })


def backup():
    if os.path.exists(TXT_FILE):
        with open(TXT_FILE, 'r') as original, open(BACKUP_FILE, 'w') as backup:
            backup.write(original.read())


def save_txt():
    with open(TXT_FILE, 'w') as f:
        for e in expenses:
            f.write(f"{e['date']}|{e['category']}|{e['amount']}|{e['note']}\n")


def save_csv():
    with open(CSV_FILE, 'w', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=['date', 'category', 'amount', 'note'])
        writer.writeheader()
        for e in expenses:
            writer.writerow(e)


def save_json():
    with open(JSON_FILE, 'w') as f:
        json.dump(expenses, f, indent=4)


def save_custom():
    backup()
    print("\n💾 Save Options:")
    print("1. Save as TXT")
    print("2. Save as CSV")
    print("3. Save as JSON")
    print("4. Save to All formats")
    choice = input("Choose format (1-4): ")

    if choice == '1':
        save_txt()
        print(" Saved to TXT")
    elif choice == '2':
        save_csv()
        print(" Saved to CSV")
    elif choice == '3':
        save_json()
        print(" Saved to JSON")
    elif choice == '4':
        save_txt()
        save_csv()
        save_json()
        print(" Saved to TXT, CSV, and JSON")
    else:
        print(" Invalid choice. Not saved.")


def add_expense():
    print("\n Add New Expense")
    date = input("Date (YYYY-MM-DD) [Press Enter for today]: ")
    if not date:
        date = datetime.now().strftime('%Y-%m-%d')

    print(f"Available categories: {', '.join(CATEGORIES)}")
    category = input("Category: ").lower()
    if category not in CATEGORIES:
        print(" Invalid category. Use one from the list.")
        return

    try:
        amount = float(input("Amount (₹): "))
    except ValueError:
        print(" Invalid amount.")
        return

    note = input("Note (optional): ")

    expense = {
        'date': date,
        'category': category,
        'amount': amount,
        'note': note
    }

    expenses.append(expense)

    save = input("💬 Do you want to save this? (yes/no): ").strip().lower()
    if save == 'yes':
        save_custom()
    else:
        print("⚠ Not saved.")


def show_expenses():
    if not expenses:
        print("\n No expenses yet.")
        return
    print("\n------------------ All Expenses ------------------")
    print(" No |     Date     | Category | Amount  | Note")
    print("--------------------------------------------------")
    for i, e in enumerate(expenses, start=1):
        print(f" {i:<2} | {e['date']} | {e['category']:<8} | ₹{e['amount']:<7.2f} | {e['note']}")
    print("--------------------------------------------------")


def total_spent():
    total = sum(e['amount'] for e in expenses)
    print(f"\n💰 Total Spent: ₹{total:.2f}")


def filter_by_category():
    cat = input("Enter category to filter: ").lower()
    found = [e for e in expenses if e['category'].lower() == cat]
    if not found:
        print(" No expenses in this category.")
        return
    for e in found:
        print(f"{e['date']} | {e['category']} | ₹{e['amount']} | {e['note']}")


def filter_by_date():
    dt = input("Enter date to filter (YYYY-MM-DD): ")
    found = [e for e in expenses if e['date'] == dt]
    if not found:
        print(" No expenses on this date.")
        return
    for e in found:
        print(f"{e['date']} | {e['category']} | ₹{e['amount']} | {e['note']}")


def summary_by_category():
    print("\n Expense Summary by Category")
    summary = {}
    for e in expenses:
        summary[e['category']] = summary.get(e['category'], 0) + e['amount']
    for cat, amt in summary.items():
        print(f"{cat.capitalize():<10}: ₹{amt:.2f}")


def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')


def menu():
    while True:
        clear_screen()
        print("========== 💼 Expense Tracker ==========")
        print("1. Add Expense")
        print("2. Show All Expenses")
        print("3. Show Total Spent")
        print("4. Filter by Category")
        print("5. Filter by Date")
        print("6. Show Category Summary")
        print("7. Exit")
        print("========================================")

        choice = input("Choose an option (1-7): ")

        if choice == '1':
            add_expense()
        elif choice == '2':
            show_expenses()
            input("\nPress Enter to return...")
        elif choice == '3':
            total_spent()
            input("\nPress Enter to return...")
        elif choice == '4':
            filter_by_category()
            input("\nPress Enter to return...")
        elif choice == '5':
            filter_by_date()
            input("\nPress Enter to return...")
        elif choice == '6':
            summary_by_category()
            input("\nPress Enter to return...")
        elif choice == '7':
            print("Goodbye have a nice day")
            break
        else:
            print(" Invalid choice. Try again.")


load_expenses()
menu()