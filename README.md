# 📊 AI Data Analysis Assistant

An AI-powered data analysis web application built with **Streamlit**, **Plotly**, and **Google Gemini AI**. Upload your dataset, explore interactive visualizations, generate AI-powered insights, ask questions in natural language, and export professional PDF reports.

---

## 🚀 Features

- 📂 Upload CSV or Excel datasets
- 📊 Automatic Exploratory Data Analysis (EDA)
- 📈 Interactive Plotly visualizations
- 🤖 AI-powered insights using Google Gemini
- 💬 Ask questions about your dataset in natural language
- 📄 Generate downloadable PDF reports
- 📥 Export analysis results

---

## 🛠️ Tech Stack

- Python
- Streamlit
- Pandas
- NumPy
- Plotly
- Google Gemini API
- ReportLab
- OpenPyXL

---

## 📁 Project Structure

```
AI-Data-Analysis-Assistant/
│
├── app.py
├── requirements.txt
├── README.md
├── .env
├── .gitignore
│
├── utils/
│   ├── loader.py
│   ├── analysis.py
│   ├── charts.py
│   ├── gemini.py
│   ├── prompts.py
│   ├── query_engine.py
│   ├── report_generator.py
│   ├── helper.py
│   └── ui.py
```

---

## ⚙️ Installation

### Clone the repository

```bash
git clone https://github.com/yourusername/AI-Data-Analysis-Assistant.git

cd AI-Data-Analysis-Assistant
```

### Create a virtual environment

Windows

```bash
python -m venv .venv

.venv\Scripts\activate
```

Mac/Linux

```bash
python3 -m venv .venv

source .venv/bin/activate
```

### Install dependencies

```bash
pip install -r requirements.txt
```

---

## 🔑 Configure Gemini API

Create a `.env` file in the project root.

```env
GEMINI_API_KEY=YOUR_GEMINI_API_KEY
```

Get your API key from:

https://aistudio.google.com/app/apikey

---

## ▶️ Run the application

```bash
streamlit run app.py
```

---

## 📊 Application Modules

### Dashboard

- Dataset overview
- Dataset health score
- Missing values
- Statistical summary
- Duplicate detection

### Charts

- Histogram
- Box Plot
- Scatter Plot
- Line Chart
- Bar Chart
- Pie Chart
- Correlation Heatmap

### AI Assistant

- Automatic dataset summary
- AI-generated insights
- Natural language question answering

### Reports

- AI-generated report
- PDF export
- Downloadable summaries

---

## 📸 Screenshots

Add screenshots here.

Example:

```
screenshots/
    dashboard.png
    charts.png
    ai_assistant.png
    reports.png
```

---

## 📦 Requirements

```
streamlit
pandas
numpy
plotly
openpyxl
python-dotenv
google-generativeai
reportlab
```

---

## 🔮 Future Enhancements

- Multiple dataset comparison
- Machine Learning model integration
- Automatic feature engineering
- Interactive dashboard customization
- User authentication
- Cloud deployment

---

## 👨‍💻 Author

**Kakarla Sai Ranga Saketh**

B.Tech CSE (AI & ML)

Interested in Artificial Intelligence, Generative AI, LLMs, Data Analytics, and Machine Learning.

---

## ⭐ Support

If you found this project useful, consider giving it a ⭐ on GitHub.