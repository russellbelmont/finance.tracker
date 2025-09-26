import json

GOAL_FILE = "data/savings_goal.json"

def set_savings_goal(amount):
    """Set a savings goal."""
    goal_data = {"goal": amount}
    with open(GOAL_FILE, "w") as f:
        json.dump(goal_data, f)
    print(f"💰 Savings goal set to {amount}")

def get_savings_goal():
    """Retrieve the savings goal, if set."""
    if not os.path.exists(GOAL_FILE):
        return None
    with open(GOAL_FILE, "r") as f:
        goal_data = json.load(f)
    return goal_data.get("goal", None)

def get_total_income():
    df = load_data()
    return df[df["Type"] == "Income"]["Amount"].sum()

def get_total_expenses():
    df = load_data()
    return df[df["Type"] == "Expense"]["Amount"].sum()

def get_savings_progress():
    goal = get_savings_goal()
    if goal is None:
        return None
    total_income = get_total_income()
    total_expenses = get_total_expenses()
    saved = total_income - total_expenses
    percent = (saved / goal) * 100 if goal > 0 else 0
    return saved, percent
