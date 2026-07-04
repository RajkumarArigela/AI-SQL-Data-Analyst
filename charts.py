import streamlit as st
import matplotlib.pyplot as plt


def generate_chart(result):
    if len(result.columns) < 2:
        return

    x_col = result.columns[0]
    y_col = result.columns[1]

    fig, ax = plt.subplots()

    # Bar chart
    ax.bar(result[x_col], result[y_col])

    ax.set_xlabel(x_col)
    ax.set_ylabel(y_col)
    ax.set_title(f"{y_col} by {x_col}")

    st.pyplot(fig)