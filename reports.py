import matplotlib.pyplot as plt
import pandas as pd
from finance_manager import load_data

def plot_expense_pie():
    df = load_data()
    expenses = df[df["Type"] == "Expense"]

    if expenses.empty:
        print("No expenses to display.")
        return

    summary = expenses.groupby("Category")["Amount"].sum()
    summary.plot.pie(autopct="%1.1f%%", title="Expenses by Category", figsize=(6,6))
    plt.ylabel("")  # Remove default y-label
    plt.show()
