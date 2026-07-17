"""
Prompt templates for Gemini AI
"""


def dataset_summary_prompt(summary: dict) -> str:

    return f"""
You are an expert Data Analyst.

Analyze the following dataset information and provide a concise business-friendly summary.

Dataset Information:
{summary}

Your response should include:

1. Dataset overview
2. Key observations
3. Data quality issues
4. Interesting trends
5. Potential business insights
6. Recommendations for further analysis

Keep the response under 300 words.
"""


def question_prompt(question: str, dataframe_info: str) -> str:

    return f"""
You are an AI Data Analyst.

Dataset Information:
{dataframe_info}

User Question:
{question}

Instructions:

- Answer only using the dataset context.
- Be clear and concise.
- Explain calculations if required.
- If the answer cannot be determined from the dataset, clearly state that.
- Avoid making assumptions.

Answer:
"""


def report_prompt(summary: dict) -> str:

    return f"""
Generate a professional data analysis report.

Dataset Details:
{summary}

The report should include:

# Executive Summary

# Dataset Overview

# Data Quality Assessment

# Key Statistics

# Major Insights

# Business Recommendations

# Conclusion

Write in a professional report format.
"""


def insight_prompt(summary: dict) -> str:

    return f"""
You are a Senior Business Intelligence Analyst.

Analyze the dataset summary below.

Dataset:
{summary}

Generate:

• Top 5 insights
• Potential anomalies
• Interesting patterns
• Suggested visualizations
• Business recommendations

Keep the response easy to understand.
"""


def chart_prompt(chart_name: str, column: str) -> str:

    return f"""
Explain the purpose of a {chart_name} created using the column '{column}'.

Include:

- What this chart shows
- How to interpret it
- Important observations users should look for

Limit to around 120 words.
"""