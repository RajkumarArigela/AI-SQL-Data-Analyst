import streamlit as st
from database import create_database_from_csv, execute_sql_query
from llm_sql import generate_sql
from validator import validate_sql
from analyst_ai import analyze_result
from charts import generate_chart

st.title("AI SQL Data Analyst")
st.caption("Built by Rajkumar Arigela")

st.sidebar.title("About")
st.sidebar.info(
    "AI-powered SQL analytics app\nBuilt by Rajkumar Arigela"
)
# Session state
if "current_question" not in st.session_state:
    st.session_state.current_question = ""

if "followups" not in st.session_state:
    st.session_state.followups = []

uploaded_file = st.file_uploader("Upload CSV file", type=["csv"])

if uploaded_file:
    columns, message = create_database_from_csv(uploaded_file)

    if columns:
        st.success(message)
        st.write("Detected Columns:", columns)

        user_question = st.text_input(
            "Ask a question about your data",
            value=st.session_state.current_question
        )

        if user_question:
            st.session_state.current_question = user_question

            try:
                sql_query = generate_sql(user_question, columns)

                st.subheader("Generated SQL")
                st.code(sql_query, language="sql")

                is_valid, validation_message = validate_sql(sql_query)

                if is_valid:
                    st.success(validation_message)

                    result, error = execute_sql_query(sql_query)

                    if error:
                        st.error(error)

                    elif result.empty:
                        st.warning("No data found")

                    else:
                        # Step 7: Results
                        st.subheader("Query Results")
                        st.dataframe(result)

                        # Step 12: KPI Dashboard
                        st.subheader("KPI Dashboard")

                        col1, col2, col3 = st.columns(3)

                        col1.metric("Rows", len(result))
                        col2.metric("Columns", len(result.columns))

                        numeric_cols = result.select_dtypes(
                            include=["number"]
                        ).columns

                        col3.metric("Numeric Columns", len(numeric_cols))

                        # Optional total metric
                        if len(numeric_cols) > 0:
                            total_value = result[numeric_cols[0]].sum()
                            st.metric(
                                f"Total {numeric_cols[0]}",
                                f"{total_value:,.2f}"
                            )

                        # Step 11: Charts
                        st.subheader("Visualization")
                        generate_chart(result)

                        try:
                            # Step 8,9,10
                            analysis = analyze_result(
                                user_question,
                                sql_query,
                                result
                            )

                            st.subheader("AI Analysis")
                            st.write(analysis)

                            # Extract follow-up questions
                            if "Follow-up Questions:" in analysis:
                                followup_section = analysis.split(
                                    "Follow-up Questions:"
                                )[1]

                                followups = [
                                    line.strip("1234567890.- ").strip()
                                    for line in followup_section.split("\n")
                                    if line.strip()
                                ]

                                st.session_state.followups = followups

                        except Exception:
                            st.warning(
                                "AI analysis unavailable (quota exceeded)."
                            )

                else:
                    st.error(validation_message)

            except Exception:
                st.error(
                    "Gemini API quota exceeded. Please wait or use a new API key."
                )

        # Follow-up buttons
        if st.session_state.followups:
            st.subheader("Suggested Follow-up Questions")

            for question in st.session_state.followups:
                if st.button(question):
                    st.session_state.current_question = question
                    st.rerun()

    else:
        st.error(message)