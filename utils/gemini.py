import os
import streamlit as st
import google.generativeai as genai
from dotenv import load_dotenv

from .prompts import (
    dataset_summary_prompt,
    insight_prompt,
    report_prompt,
    question_prompt,
)
# Load local .env (ignored if it doesn't exist)
load_dotenv(override=False)

# Try local .env first
api_key = os.getenv("GEMINI_API_KEY")

# If not found, try Streamlit Cloud Secrets
if not api_key:
    api_key = st.secrets.get("GEMINI_API_KEY")

# Raise an error only if neither source provides a key
if not api_key:
    raise ValueError(
        "GEMINI_API_KEY not found. Add it to your local .env file or Streamlit Cloud Secrets."
    )

genai.configure(api_key=api_key)

model = genai.GenerativeModel("gemini-2.5-flash")

def ask_gemini(question: str, dataframe_info: str = ""):
    """
    Answer a user's question about the dataset.
    """

    try:

        prompt = question_prompt(question, dataframe_info)

        response = model.generate_content(prompt)

        return response.text

    except Exception as e:

        return f"❌ Gemini Error: {str(e)}"


def generate_dataset_summary(summary: dict):
    """
    Generate AI summary for uploaded dataset.
    """

    try:

        prompt = dataset_summary_prompt(summary)

        response = model.generate_content(prompt)

        return response.text

    except Exception as e:

        return f"❌ Gemini Error: {str(e)}"


def generate_insights(summary: dict):
    """
    Generate business insights.
    """

    try:

        prompt = insight_prompt(summary)

        response = model.generate_content(prompt)

        return response.text

    except Exception as e:

        return f"❌ Gemini Error: {str(e)}"


def generate_report(summary: dict):
    """
    Generate complete AI report.
    """

    try:

        prompt = report_prompt(summary)

        response = model.generate_content(prompt)

        return response.text

    except Exception as e:

        return f"❌ Gemini Error: {str(e)}"


def test_connection():
    """
    Test Gemini API connection.
    """

    try:

        response = model.generate_content(
            "Reply with only the word Connected."
        )

        return response.text

    except Exception as e:

        return f"Connection Failed: {str(e)}"