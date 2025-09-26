import pandas as pd
import os

DATA_FILE = "data/finances.csv"

# Load CSV data
def load_data():
    if os.path.exists(DATA_FILE):
        return pd.read_csv(DATA_FILE)
    else:
        # Create empty CSV with headers if it doesn't exist
        df = pd.DataFrame(columns=["Date", "Type", "Category", "Amount", "Description"])
        df.to_csv(DATA_FILE, index=False)
        return df

# Add income or expense
def add_transaction(tx_type, category, amount, description=""):
    df = load_data()
    df = pd.concat([df, pd.DataFrame([{
        "Date": pd.Timestamp.now(),
        "Type": tx_type,
        "Category": category,
        "Amount": amount,
        "Description": description
    }])], ignore_index=True)
    df.to_csv(DATA_FILE, index=False)
    print(f"{tx_type} added: {category} - {amount}")
