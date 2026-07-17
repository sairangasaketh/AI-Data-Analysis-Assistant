from io import BytesIO

from reportlab.lib import colors
from reportlab.lib.enums import TA_CENTER
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus import (
    SimpleDocTemplate,
    Paragraph,
    Spacer,
    Table,
    TableStyle,
)


def generate_pdf_report(summary: dict, ai_report: str):

    buffer = BytesIO()

    doc = SimpleDocTemplate(buffer)

    styles = getSampleStyleSheet()

    title_style = styles["Heading1"]
    title_style.alignment = TA_CENTER

    heading = styles["Heading2"]
    normal = styles["BodyText"]

    elements = []

    # --------------------------------------------------
    # Title
    # --------------------------------------------------

    elements.append(Paragraph("AI Data Analysis Report", title_style))
    elements.append(Spacer(1, 20))

    # --------------------------------------------------
    # Dataset Overview
    # --------------------------------------------------

    elements.append(Paragraph("Dataset Overview", heading))
    elements.append(Spacer(1, 10))

    table_data = [
        ["Metric", "Value"],
        ["Rows", summary.get("Rows", "")],
        ["Columns", summary.get("Columns", "")],
        ["Missing Values", summary.get("Missing Values", "")],
        ["Duplicate Rows", summary.get("Duplicate Rows", "")],
        ["Memory Usage", summary.get("Memory Usage", "")],
    ]

    table = Table(table_data, colWidths=[180, 220])

    table.setStyle(
        TableStyle(
            [
                ("BACKGROUND", (0, 0), (-1, 0), colors.HexColor("#4F81BD")),
                ("TEXTCOLOR", (0, 0), (-1, 0), colors.white),

                ("GRID", (0, 0), (-1, -1), 1, colors.grey),

                ("FONTNAME", (0, 0), (-1, 0), "Helvetica-Bold"),

                ("BOTTOMPADDING", (0, 0), (-1, 0), 10),

                ("BACKGROUND", (0, 1), (-1, -1), colors.beige),

                ("ALIGN", (0, 0), (-1, -1), "CENTER"),
            ]
        )
    )

    elements.append(table)

    elements.append(Spacer(1, 25))

    # --------------------------------------------------
    # AI Report
    # --------------------------------------------------

    elements.append(Paragraph("AI Insights", heading))

    elements.append(Spacer(1, 10))

    for paragraph in ai_report.split("\n"):

        if paragraph.strip():

            elements.append(Paragraph(paragraph.strip(), normal))

            elements.append(Spacer(1, 6))

    elements.append(Spacer(1, 20))

    # --------------------------------------------------
    # Footer
    # --------------------------------------------------

    elements.append(Paragraph("Generated using AI Data Analysis Assistant", styles["Italic"]))

    doc.build(elements)

    buffer.seek(0)

    return buffer