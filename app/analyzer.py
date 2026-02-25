
import pandas as pd
from .categorizer import categorize_transaction

def analyze_transactions(file_path):
    df = pd.read_csv(file_path)

    df["category"] = df["description"].apply(categorize_transaction)

    total_income = df[df["amount"] > 0]["amount"].sum()
    total_expense = df[df["amount"] < 0]["amount"].sum()

    category_summary = df.groupby("category")["amount"].sum().to_dict()

    advice = []

    if abs(total_expense) > total_income * 0.7:
        advice.append("Your expenses are too high compared to income.")
    else:
        advice.append("Your spending is under control.")

    if "food" in category_summary and abs(category_summary["food"]) > 300:
        advice.append("Consider reducing restaurant spending.")

    return {
        "total_income": float(total_income),
        "total_expense": float(total_expense),
        "net_balance": float(total_income + total_expense),
        "category_breakdown": category_summary,
        "advice": advice
    }
