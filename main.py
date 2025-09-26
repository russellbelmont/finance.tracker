from finance_manager import add_transaction
from reports import plot_expense_pie

def menu():
    while True:
        print("\n=== Personal Finance Tracker ===")
        print("1. Add Income")
        print("2. Add Expense")
        print("3. Show Expense Pie Chart")
        print("4. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            category = input("Income Category: ")
            amount = float(input("Amount: "))
            description = input("Description (optional): ")
            add_transaction("Income", category, amount, description)
        elif choice == "2":
            category = input("Expense Category: ")
            amount = float(input("Amount: "))
            description = input("Description (optional): ")
            add_transaction("Expense", category, amount, description)
        elif choice == "3":
            try:
                plot_expense_pie()
            except Exception as e:
                print("Error showing pie chart:", e)
        elif choice == "4":
            print("Exiting. Goodbye!")
            break
        else:
            print("Invalid option. Try again.")

if __name__ == "__main__":
    menu()
