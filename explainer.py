import os
from pathlib import Path
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI

PROJECT_DIR = Path(__file__).resolve().parent
load_dotenv(PROJECT_DIR / ".env")


def explain_sql(sql_query):
    api_key = os.getenv("GOOGLE_API_KEY")

    llm = ChatGoogleGenerativeAI(
        model="models/gemini-2.5-flash",
        temperature=0.2,
        api_key=api_key
    )

    prompt = f"""
Explain this SQL query in simple business terms.

SQL Query:
{sql_query}
"""

    response = llm.invoke(prompt)

    return response.content.strip()