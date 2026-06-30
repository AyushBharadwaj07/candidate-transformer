import pandas as pd


def read_csv(file_path):
    df = pd.read_csv(file_path)

    if df.empty:
        return {}

    row = df.iloc[0]

    return {
        "name": row["name"],
        "email": row["email"],
        "phone": str(row["phone"]),
        "current_company": row["current_company"],
        "title": row["title"]
    }