from pathlib import Path
import sqlite3
import pandas as pd

# Create data directory if it doesn't exist
DATA_DIR = Path("data")
DATA_DIR.mkdir(exist_ok=True)

# Database file path
DB_PATH = DATA_DIR / "user_data.db"


def create_database_from_csv(csv_file):
    try:
        # Read uploaded CSV
        df = pd.read_csv(csv_file)

        if df.empty:
            return None, "Uploaded CSV is empty."

        # Create SQLite database
        conn = sqlite3.connect(DB_PATH)

        # Save dataframe as SQL table
        df.to_sql(
            "uploaded_data",
            conn,
            if_exists="replace",
            index=False
        )

        conn.close()

        return df.columns.tolist(), "Database created successfully!"

    except Exception as e:
        return None, str(e)


def execute_sql_query(sql_query):
    try:
        conn = sqlite3.connect(DB_PATH)

        result = pd.read_sql_query(sql_query, conn)

        conn.close()

        return result, None

    except Exception as e:
        return None, str(e)