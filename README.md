# 🤖 AI SQL Data Analyst 2.0

An AI-powered SQL Data Analyst that allows users to upload any CSV dataset, ask questions in natural language, automatically generates SQL queries, executes them on a SQLite database, visualizes results, and provides AI-generated business insights.

**🚀 Live Demo:** https://ai-sql-data-analyst-2pz9k4b6xdg6vfmi4qyx3i.streamlit.app/

**💻 GitHub Repository:** https://github.com/RajkumarArigela/AI-SQL-Data-Analyst

---

# 📌 Features

✅ Upload any CSV dataset

✅ Automatically convert CSV into SQLite database

✅ Ask questions in plain English

✅ AI converts natural language into SQL

✅ SQL validation for safer execution

✅ Execute SQL automatically

✅ Display query results

✅ Interactive visualizations

✅ KPI Dashboard

✅ AI-generated SQL explanation

✅ AI-generated business insights

✅ Smart follow-up analytical questions

✅ Robust error handling

✅ Streamlit web application

---

# 🏗️ System Architecture

```
                User Uploads CSV
                        │
                        ▼
                Pandas DataFrame
                        │
                        ▼
              SQLite Database Creation
                        │
                        ▼
            User Asks Question (English)
                        │
                        ▼
         Gemini AI → SQL Query Generation
                        │
                        ▼
                SQL Validation Layer
                        │
                        ▼
             Execute Query on SQLite
                        │
                        ▼
                  Query Results
                        │
         ┌──────────────┼──────────────┐
         ▼              ▼              ▼
     KPI Cards      Charts       AI Analysis
                                      │
             ┌────────────────────────┼────────────────────┐
             ▼                        ▼                    ▼
      SQL Explanation        Business Insights     Follow-up Questions
```

---

# 📂 Project Structure

```
AI-SQL-Data-Analyst/
│
├── app.py
├── database.py
├── llm_sql.py
├── validator.py
├── analyst_ai.py
├── charts.py
├── requirements.txt
├── .gitignore
├── README.md
├── .env
├── data/
└── venv/
```

---

# ⚙️ Tech Stack

- Python
- Streamlit
- SQLite
- Pandas
- LangChain
- Google Gemini API
- Matplotlib

---

# 🚀 Installation

Clone the repository

```bash
git clone https://github.com/RajkumarArigela/AI-SQL-Data-Analyst.git
```

Go to the project folder

```bash
cd AI-SQL-Data-Analyst
```

Create virtual environment

```bash
python -m venv venv
```

Activate virtual environment

### Windows

```bash
venv\Scripts\activate
```

### Linux / macOS

```bash
source venv/bin/activate
```

Install dependencies

```bash
pip install -r requirements.txt
```

---

# 🔑 Configure API Key

Create a file named

```
.env
```

Add

```env
GOOGLE_API_KEY=YOUR_GEMINI_API_KEY
```

---

# ▶️ Run Application

```bash
streamlit run app.py
```

---

# 📊 Example Questions

Try asking:

- Which state has the highest total investment?
- Show total investment by city.
- What is the average investment by gender?
- Which payment mode is used the most?
- Which age group invests the most?
- Show KYC completed investors by state.
- Which city tier contributes the highest revenue?
- What is the average annual income by state?
- Which transaction type is most common?
- Show top 10 investors based on investment amount.

---

# 📈 Workflow

```
Upload CSV

↓

Create SQLite Database

↓

Ask Question

↓

Generate SQL

↓

Validate SQL

↓

Execute SQL

↓

Display Results

↓

Generate Charts

↓

Show KPI Dashboard

↓

AI Analysis

↓

Business Insights

↓

Follow-up Questions
```

---

# 📸 Application Screenshots

## Upload Dataset

(Add Screenshot Here)

---

## SQL Generation

(Add Screenshot Here)

---

## Query Results

(Add Screenshot Here)

---

## Dashboard

(Add Screenshot Here)

---

## AI Analysis

(Add Screenshot Here)

---

# 🎯 Skills Demonstrated

- Python Programming
- SQL
- SQLite
- Data Analysis
- Streamlit
- Prompt Engineering
- Google Gemini API
- LangChain
- Data Visualization
- AI Application Development
- LLM Integration
- Error Handling
- Git & GitHub

---

# 🔮 Future Improvements

- Multiple CSV uploads
- Automatic table relationship detection
- SQL query history
- Download query results as Excel/PDF
- Authentication and user accounts
- Dark mode
- Advanced interactive charts
- Conversation memory
- Database schema visualization
- Support for PostgreSQL and MySQL
- Voice-based analytical queries
- Agentic AI workflow with LangGraph
- Automatic report generation
- Predictive analytics and forecasting

---

# 👨‍💻 Author

**Rajkumar Arigela**

📧 Email: therajkumararigela@gmail.com

💼 LinkedIn: https://www.linkedin.com/in/rajkumar-arigela

🐙 GitHub: https://github.com/RajkumarArigela

---

# ⭐ Support

If you found this project useful, consider giving it a ⭐ on GitHub.

It helps others discover the project and motivates future improvements.

---

# 📜 License

This project is licensed under the MIT License.

---

## 🚀 Built with ❤️ by Rajkumar Arigela
