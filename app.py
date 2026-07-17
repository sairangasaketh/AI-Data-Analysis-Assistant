import streamlit as st
import pandas as pd

from utils.loader import load_data
from utils.analysis import (
    get_dataset_summary,
    get_missing_values,
    get_dataset_health,
    get_data_types,
)

from utils.ui import (
    inject_css,
    hero,
    feature_cards,
    sidebar,
    dataset_metrics,
)

from utils.charts import *

from utils.query_engine import QueryEngine

from utils.gemini import (
    ask_gemini,
    generate_dataset_summary,
    generate_report,
)

from utils.report_generator import generate_pdf_report


# ---------------------------------------------------
# Page Configuration
# ---------------------------------------------------

st.set_page_config(
    page_title="AI Data Analysis Assistant",
    page_icon="📊",
    layout="wide",
)

inject_css()

hero()

feature_cards()


# ---------------------------------------------------
# Sidebar
# ---------------------------------------------------

page = sidebar()


# ---------------------------------------------------
# File Upload
# ---------------------------------------------------

uploaded_file = st.sidebar.file_uploader(
    "Upload CSV or Excel File",
    type=["csv", "xlsx"],
)

if uploaded_file is None:

    st.info("👈 Upload a dataset to begin.")

    st.stop()


# ---------------------------------------------------
# Load Dataset
# ---------------------------------------------------

try:

    df = load_data(uploaded_file)

except Exception as e:

    st.error(f"Unable to load dataset.\n\n{e}")

    st.stop()


summary = get_dataset_summary(df)

health = get_dataset_health(df)

query_engine = QueryEngine(df)


# ===================================================
# DASHBOARD
# ===================================================

if page == "🏠 Dashboard":

    st.title("📊 Dashboard")

    dataset_metrics(summary)

    st.divider()

    col1, col2 = st.columns([2, 1])

    with col1:

        st.subheader("Dataset Preview")

        st.dataframe(df.head(15), use_container_width=True)

    with col2:

        st.subheader("Dataset Health")

        health_df = pd.DataFrame(
            {
                "Metric": [
                    "Rows",
                    "Columns",
                    "Missing Values",
                    "Duplicate Rows",
                    "Memory Usage",
                ],
                "Value": [
                    summary["Rows"],
                    summary["Columns"],
                    summary["Missing Values"],
                    summary["Duplicate Rows"],
                    summary["Memory Usage"],
                ],
            }
        )

        st.dataframe(
            health_df,
            use_container_width=True,
            hide_index=True,
        )

    st.divider()

    col1, col2 = st.columns(2)

    with col1:

        st.subheader("Missing Values")

        st.dataframe(
            get_missing_values(df),
            use_container_width=True,
        )

    with col2:

        st.subheader("Data Types")

        st.dataframe(
            get_data_types(df),
            use_container_width=True,
        )

    st.divider()

    st.subheader("Dataset Health Score")

    st.progress(health["Health Score"] / 100)

    st.write(f"**Health Score:** {health['Health Score']} / 100")

    st.write(health["Status"])

    st.divider()

    st.subheader("🤖 AI Dataset Summary")

    if st.button("Generate AI Summary"):

        with st.spinner("Analyzing dataset..."):

            ai_summary = generate_dataset_summary(summary)

        st.success("Analysis Completed")

        st.write(ai_summary)
# ===================================================
# CHARTS
# ===================================================

elif page == "📈 Charts":

    st.title("📈 Data Visualization")

    numeric_cols = df.select_dtypes(include="number").columns.tolist()
    categorical_cols = df.select_dtypes(exclude="number").columns.tolist()

    if len(numeric_cols) == 0:
        st.warning("No numeric columns available.")
    else:

        # Histogram
        st.subheader("Histogram")

        col = st.selectbox(
            "Select Column",
            numeric_cols,
            key="hist_col",
        )

        st.plotly_chart(
            histogram(df, col),
            use_container_width=True,
        )

        st.divider()

        # Box Plot
        st.subheader("Box Plot")

        col = st.selectbox(
            "Select Column ",
            numeric_cols,
            key="box_col",
        )

        st.plotly_chart(
            box_plot(df, col),
            use_container_width=True,
        )

        st.divider()

        # Scatter Plot

        if len(numeric_cols) >= 2:

            st.subheader("Scatter Plot")

            c1, c2 = st.columns(2)

            with c1:

                x = st.selectbox(
                    "X-axis",
                    numeric_cols,
                    key="scatter_x",
                )

            with c2:

                y = st.selectbox(
                    "Y-axis",
                    numeric_cols,
                    index=min(1, len(numeric_cols)-1),
                    key="scatter_y",
                )

            st.plotly_chart(
                scatter_plot(df, x, y),
                use_container_width=True,
            )

        st.divider()

        # Line Chart

        st.subheader("Line Chart")

        y = st.selectbox(
            "Select Numeric Column",
            numeric_cols,
            key="line_y",
        )

        fig = px.line(
            df,
            y=y,
            markers=True,
            title=f"{y} Trend",
        )

        fig.update_layout(
            template="plotly_dark",
            height=500,
            title_x=0.5,
        )

        st.plotly_chart(fig, use_container_width=True)

        st.divider()

        # Correlation Heatmap

        st.subheader("Correlation Heatmap")

        st.plotly_chart(
            correlation_heatmap(df),
            use_container_width=True,
        )

    # Pie Chart

    if len(categorical_cols) > 0:

        st.divider()

        st.subheader("Pie Chart")

        col = st.selectbox(
            "Category Column",
            categorical_cols,
            key="pie",
        )

        st.plotly_chart(
            pie_chart(df, col),
            use_container_width=True,
        )

        st.divider()

        st.subheader("Value Counts")

        st.plotly_chart(
            value_counts_chart(df, col),
            use_container_width=True,
        )


# ===================================================
# AI ASSISTANT
# ===================================================

elif page == "🤖 AI Assistant":

    st.title("🤖 AI Data Assistant")

    st.write(
        "Ask questions about your dataset in natural language."
    )

    if "messages" not in st.session_state:
        st.session_state.messages = []

    # Display previous chat

    for message in st.session_state.messages:

        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    prompt = st.chat_input("Ask anything about your data...")

    if prompt:

        st.session_state.messages.append(
            {
                "role": "user",
                "content": prompt,
            }
        )

        with st.chat_message("user"):
            st.markdown(prompt)

        # Try Pandas first

        response = query_engine.execute(prompt)

        # Fallback to Gemini

        if response is None:

            with st.spinner("Thinking..."):

                response = ask_gemini(
                    prompt,
                    df.describe(include="all").to_string(),
                )

        st.session_state.messages.append(
            {
                "role": "assistant",
                "content": response,
            }
        )

        with st.chat_message("assistant"):
            st.markdown(response)
# ===================================================
# REPORTS
# ===================================================

elif page == "📄 Reports":

    st.title("📄 AI Report Generator")

    st.write(
        "Generate a professional AI-powered report for your dataset."
    )

    st.divider()

    if st.button("Generate AI Report"):

        with st.spinner("Generating report..."):

            ai_report = generate_report(summary)

        st.success("Report Generated Successfully!")

        st.markdown(ai_report)

        pdf = generate_pdf_report(
            summary,
            ai_report,
        )

        st.download_button(
            label="📥 Download PDF Report",
            data=pdf,
            file_name="AI_Data_Analysis_Report.pdf",
            mime="application/pdf",
        )

    st.divider()

    st.subheader("Dataset Information")

    st.dataframe(
        pd.DataFrame(
            {
                "Metric": summary.keys(),
                "Value": summary.values(),
            }
        ),
        use_container_width=True,
    )

    st.divider()

    st.subheader("Download Dataset")

    csv = df.to_csv(index=False).encode("utf-8")

    st.download_button(
        label="⬇ Download CSV",
        data=csv,
        file_name="clean_dataset.csv",
        mime="text/csv",
    )


# ===================================================
# FOOTER
# ===================================================

st.divider()

st.caption(
    "🚀 AI Data Analysis Assistant | Built with Streamlit, Plotly & Gemini AI"
)