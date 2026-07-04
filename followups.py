import os
from pathlib import Path
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI

PROJECT_DIR = Path(__file__).resolve().parent
load_dotenv(PROJECT_DIR / ".env")


def generate_followups(user_question, result):
    api_key = os.getenv("GOOGLE_API_KEY")

    llm = ChatGoogleGenerativeAI(
        model="models/gemini-2.5-flash",
        temperature=0.4,
        api_key=api_key
    )

    prompt = f"""
You are a data analyst.

Original Question:
{user_question}

Query Result:
{result.to_string(index=False)}

Suggest 3 smart follow-up analytical questions the user can ask next.
Keep them short and useful.
"""

    response = llm.invoke(prompt)

    return response.content.strip()