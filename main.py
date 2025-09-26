from finance_manager import add_transaction
from reports import plot_expense_pie
from colorama import init, Fore, Style

init(autoreset=True)  # Automatically reset colors after each print

def menu():
    while True:
        print(Fore.CYAN + "\n=== Personal Finance Tracker ===")
        print("1. Add Income")
        print("2. Add Expense")
        print("3. Show Expense Pie Chart")
        print("4. Exit")

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
            print(Fore.CYAN + "Exiting. Goodbye!")
            break
        else:
            print(Fore.MAGENTA + "Invalid option. Try again.")

if __name__ == "__main__":
    menu()
