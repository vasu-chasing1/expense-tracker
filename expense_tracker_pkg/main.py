import logging
from .expense_adder import add_expense
from .expense_viewer import view_all_expenses, view_expenses_by_category
from .expense_deleter import delete_expense
from .expense_summary import (
    get_total_spent,
    get_average_expense,
    get_expense_count,
    get_summary_by_category
)

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(message)s')

def display_menu():
    """Display the main menu"""
    print("\n" + "="*40)
    print("     EXPENSE TRACKER")
    print("="*40)
    print("1. Add Expense")
    print("2. View All Expenses")
    print("3. View Expenses by Category")
    print("4. Delete Expense")
    print("5. View Summary")
    print("6. Exit")
    print("="*40)

def add_expense_menu(db_path):
    """Menu for adding an expense"""
    print("\n--- Add Expense ---")
    description = input("Enter description: ").strip()
    amount = float(input("Enter amount: "))
    date = input("Enter date (YYYY-MM-DD): ").strip()
    category = input("Enter category (optional): ").strip() or None
    
    if add_expense(db_path, description, amount, date, category):
        print("✅ Expense added successfully!")
    else:
        print("❌ Failed to add expense")

def view_all_menu(db_path):
    """Menu for viewing all expenses"""
    print("\n--- All Expenses ---")
    expenses = view_all_expenses(db_path)
    if expenses:
        print(f"\n{'ID':<5} {'Description':<20} {'Amount':<10} {'Date':<12} {'Category':<15}")
        print("-" * 65)
        for expense in expenses:
            print(f"{expense[0]:<5} {expense[1]:<20} ${expense[2]:<9.2f} {expense[3]:<12} {expense[4] or 'N/A':<15}")
    else:
        print("No expenses found.")

def view_by_category_menu(db_path):
    """Menu for viewing expenses by category"""
    print("\n--- View by Category ---")
    category = input("Enter category: ").strip()
    expenses = view_expenses_by_category(db_path, category)
    if expenses:
        print(f"\n{'ID':<5} {'Description':<20} {'Amount':<10} {'Date':<12} {'Category':<15}")
        print("-" * 65)
        for expense in expenses:
            print(f"{expense[0]:<5} {expense[1]:<20} ${expense[2]:<9.2f} {expense[3]:<12} {expense[4] or 'N/A':<15}")
    else:
        print(f"No expenses found for category: {category}")

def delete_expense_menu(db_path):
    """Menu for deleting an expense"""
    print("\n--- Delete Expense ---")
    expense_id = int(input("Enter expense ID to delete: "))
    if delete_expense(db_path, expense_id):
        print("✅ Expense deleted successfully!")
    else:
        print("❌ Failed to delete expense")

def summary_menu(db_path):
    """Menu for viewing summary"""
    print("\n--- Expense Summary ---")
    total = get_total_spent(db_path)
    average = get_average_expense(db_path)
    count = get_expense_count(db_path)
    
    print(f"\nTotal Spent: ${total:.2f}")
    print(f"Average Expense: ${average:.2f}")
    print(f"Total Expenses: {count}")
    
    print("\n--- Summary by Category ---")
    category_summary = get_summary_by_category(db_path)
    if category_summary:
        print(f"\n{'Category':<20} {'Total':<15}")
        print("-" * 35)
        for category, total_amount in category_summary:
            print(f"{category or 'N/A':<20} ${total_amount:<14.2f}")
    else:
        print("No expenses to summarize.")

def run(db_path):
    """Main application loop"""
    while True:
        display_menu()
        choice = input("Select an option (1-6): ").strip()
        
        if choice == '1':
            add_expense_menu(db_path)
        elif choice == '2':
            view_all_menu(db_path)
        elif choice == '3':
            view_by_category_menu(db_path)
        elif choice == '4':
            delete_expense_menu(db_path)
        elif choice == '5':
            summary_menu(db_path)
        elif choice == '6':
            print("\nThank you for using Expense Tracker! 👋")
            break
        else:
            print("❌ Invalid option. Please try again.")