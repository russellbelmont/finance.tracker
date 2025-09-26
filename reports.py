import matplotlib.pyplot as plt
import pandas as pd
import os
from finance_manager import load_data

CHART_FOLDER = "charts"

def plot_expense_pie():
    df = load_data()
    expenses = df[df["Type"] == "Expense"]

    if expenses.empty:
        print("No expenses to display.")
        return

    summary = expenses.groupby("Category")["Amount"].sum()
    fig, ax = plt.subplots(figsize=(6,6))
    summary.plot.pie(autopct="%1.1f%%", ax=ax, title="Expenses by Category")
    ax.set_ylabel("")
    
    # Ensure folder exists
    os.makedirs(CHART_FOLDER, exist_ok=True)
    chart_path = os.path.join(CHART_FOLDER, "expense_pie_chart.png")
    plt.savefig(chart_path)
    plt.show()
    print(f"📊 Pie chart saved to {chart_path}")
