import os
from pathlib import Path
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI

PROJECT_DIR = Path(__file__).resolve().parent
load_dotenv(PROJECT_DIR / ".env")


def analyze_result(user_question, sql_query, result):
    api_key = os.getenv("GOOGLE_API_KEY")

    llm = ChatGoogleGenerativeAI(
        model="models/gemini-2.5-flash",
        temperature=0.3,
        api_key=api_key
    )

    prompt = f"""
You are an expert data analyst.

User Question:
{user_question}

SQL Query:
{sql_query}

Query Result:
{result.to_string(index=False)}

Provide:

1. SQL Explanation (simple)
2. Business Insights (important observations)
3. 3 Suggested Follow-up Questions

Format exactly:

SQL Explanation:
...

Business Insights:
...

Follow-up Questions:
1. ...
2. ...
3. ...
"""

    response = llm.invoke(prompt)

    return response.content.strip()