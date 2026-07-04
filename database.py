import sqlite3
import pandas as pd


# Step 2: Create database from uploaded CSV
def create_database_from_csv(csv_file):
    try:
        df = pd.read_csv(csv_file)

        if df.empty:
            return None, "Uploaded CSV is empty."

        conn = sqlite3.connect("data/user_data.db")

        df.to_sql("uploaded_data", conn, if_exists="replace", index=False)

        conn.close()

        return df.columns.tolist(), "Database created successfully!"

    except Exception as e:
        return None, f"Error: {e}"


# Step 6: Execute SQL query
def execute_sql_query(sql_query):
    try:
        conn = sqlite3.connect("data/user_data.db")

        result = pd.read_sql_query(sql_query, conn)

        conn.close()

        return result, None

    except Exception as e:
        return None, str(e)