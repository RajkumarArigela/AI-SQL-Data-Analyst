import os
import re
from pathlib import Path
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI

PROJECT_DIR = Path(__file__).resolve().parent
load_dotenv(PROJECT_DIR / ".env")


def generate_sql(user_question, columns):
    api_key = os.getenv("GOOGLE_API_KEY")

    if not api_key:
        raise ValueError("Missing GOOGLE_API_KEY in .env file")

    llm = ChatGoogleGenerativeAI(
        model="models/gemini-2.5-flash",
        temperature=0.2,
        api_key=api_key
    )

    prompt = f"""
You are an expert SQL analyst.

Table name: uploaded_data

Columns:
{columns}

Convert the user's question into a valid SQLite SQL query.

Rules:
- Only return SQL
- Start directly with SELECT
- No markdown
- No explanations
- No 'sqlite' word
- Use only given columns

User Question:
{user_question}
"""

    response = llm.invoke(prompt)
    sql_query = response.content.strip()

    # Extract SQL starting from SELECT
    match = re.search(r"(SELECT .*?;)", sql_query, re.IGNORECASE | re.DOTALL)

    if match:
        sql_query = match.group(1)

    return sql_query.strip()