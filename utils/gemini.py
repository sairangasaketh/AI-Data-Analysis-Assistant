import os

import google.generativeai as genai
from dotenv import load_dotenv

from utils.prompts import (
    dataset_summary_prompt,
    question_prompt,
    report_prompt,
    insight_prompt,
)

load_dotenv()

API_KEY = os.getenv("GEMINI_API_KEY")

if not API_KEY:
    raise ValueError(
        "GEMINI_API_KEY not found. Please add it to your .env file."
    )

genai.configure(api_key=API_KEY)

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