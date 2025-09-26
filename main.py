from finance_manager import add_transaction, set_savings_goal, get_savings_progress, get_total_income, get_total_expenses
from reports import plot_expense_pie
from colorama import init, Fore, Style

init(autoreset=True)

def menu():
    while True:
        print(Fore.CYAN + "\n=== Personal Finance Tracker ===")
        print("1. Add Income")
        print("2. Add Expense")
        print("3. Show Expense Pie Chart")
        print("4. Set Savings Goal")
        print("5. Show Summary Report")
        print("6. Exit")

        choice = input(Fore.YELLOW + "Choose an option: " + Style.RESET_ALL)

        if choice == "1":
            category = input("Income Category: ")
            amount = float(input("Amount: "))
            description = input("Description (optional): ")
            add_transaction("Income", category, amount, description)
            print(Fore.GREEN + f"✅ Income added: {category} - {amount}")

        elif choice == "2":
            category = input("Expense Category: ")
            amount = float(input("Amount: "))
            description = input("Description (optional): ")
            add_transaction("Expense", category, amount, description)
            print(Fore.RED + f"❌ Expense added: {category} - {amount}")

        elif choice == "3":
            try:
                plot_expense_pie()
            except Exception as e:
                print(Fore.RED + "Error showing pie chart:", e)

        elif choice == "4":
            amount = float(input("Enter your savings goal amount: "))
            set_savings_goal(amount)

        elif choice == "5":
    total_income = get_total_income()
    total_expenses = get_total_expenses()
    savings = get_savings_progress()
    
    print(Fore.CYAN + "\n--- Summary Report ---")
    print(Fore.GREEN + f"Total Income: {total_income}")
    print(Fore.RED + f"Total Expenses: {total_expenses}")
    
    if savings:
        saved, percent = savings
        # Create a simple progress bar
        bar_length = 30
        filled_length = int(bar_length * percent / 100)
        bar = "█" * filled_length + "-" * (bar_length - filled_length)
        print(Fore.MAGENTA + f"Savings Progress: {saved} ({percent:.1f}% of goal)")
        print(Fore.YELLOW + f"[{bar}]")
    else:
        print(Fore.MAGENTA + "No savings goal set yet.")

        elif choice == "6":
            print(Fore.CYAN + "Exiting. Goodbye!")
            break
        else:
            print(Fore.MAGENTA + "Invalid option. Try again.")

if __name__ == "__main__":
    menu()
