import streamlit as st


def inject_css():
    st.markdown("""
    <style>

    .main .block-container{
        padding-top:1rem;
        padding-bottom:2rem;
    }

    .hero{
        background:linear-gradient(90deg,#2563eb,#4f46e5);
        padding:30px;
        border-radius:18px;
        color:white;
        margin-bottom:25px;
    }

    .hero h1{
        color:white;
        margin:0;
        font-size:40px;
    }

    .hero p{
        margin-top:10px;
        font-size:18px;
        opacity:.95;
    }

    div[data-testid="stMetric"]{
    background: rgba(38,39,48,0.9);
    border:1px solid #3f4254;
    border-radius:16px;
    padding:18px;
    box-shadow:0 4px 15px rgba(0,0,0,0.25);
    }
    div[data-testid="column"]{
        padding:8px;
    }

    div[data-testid="stMetric"] label{
        color:#B8C1EC !important;
        font-size:15px;
        font-weight:600;
    }

    div[data-testid="stMetric"] div[data-testid="stMetricValue"]{
        color:white !important;
        font-size:32px;
        font-weight:bold;
    }

        .feature-card{
            background:#f8fafc;
            padding:18px;
            border-radius:14px;
            text-align:center;
            border:1px solid #e5e7eb;
    }

    </style>
    """, unsafe_allow_html=True)


def hero():

    st.markdown("""
    <div class="hero">

    <h1>📊 AI Data Analysis Assistant</h1>

    <p>
    Upload a CSV or Excel dataset, explore interactive visualizations,
    and ask questions using Gemini AI.
    </p>

    </div>
    """, unsafe_allow_html=True)


def feature_cards():

    c1, c2, c3, c4 = st.columns(4)

    cards = [
        ("📊", "EDA", "Explore your dataset"),
        ("📈", "Charts", "Interactive visualizations"),
        ("🤖", "Gemini AI", "Natural language insights"),
        ("📄", "Reports", "Generate PDF reports"),
    ]

    for col, (icon, title, desc) in zip([c1, c2, c3, c4], cards):

        with col:

            st.markdown(
                f"""
                <div style="
                    background:#262730;
                    padding:22px;
                    border-radius:18px;
                    text-align:center;
                    border:1px solid #3f4254;
                    height:220px;
                    padding:25px 20px 35px 20px;
                    margin-bottom:30px;
                ">

                <div style="
                    font-size:42px;
                    margin-bottom:12px;
                ">
                    {icon}
                </div>

                <div style="
                    font-size:20px;
                    font-weight:bold;
                    color:white;
                ">
                    {title}
                </div>

                <div style="
                    color:#B8C1EC;
                    margin-top:8px;
                    font-size:14px;
                ">
                    {desc}
                </div>

                </div>
                """,
                unsafe_allow_html=True,
            )

def sidebar():

    st.sidebar.title("📊 AI Analytics")

    st.sidebar.caption("Powered by Gemini")

    st.sidebar.divider()

    page = st.sidebar.radio(

        "Navigation",

        [

            "🏠 Dashboard",

            "📈 Charts",

            "🤖 AI Assistant",

            "📄 Reports"

        ]

    )

    st.sidebar.divider()

    st.sidebar.success("Ready")

    return page


def dataset_metrics(summary):

    c1, c2, c3, c4 = st.columns(4)

    c1.metric("📄 Rows", f"{summary['Rows']:,}")

    c2.metric("📑 Columns", summary["Columns"])

    c3.metric("⚠ Missing", summary["Missing Values"])

    c4.metric("🔁 Duplicates", summary["Duplicate Rows"])