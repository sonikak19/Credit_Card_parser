# Credit_Card_parser
💳 Credit Card Statement Analyzer

An interactive Streamlit + Python project that can generate, upload, and analyze credit card statement PDFs.
It extracts key details like bank name, billing period, due date, and total due, and saves everything to a CSV file.

🚀 Features

🏦 Generate fake multi-bank credit card statements (HDFC, ICICI, SBI, Axis, Kotak)

📄 Upload any statement PDF for analysis

🔍 Automatically extract summary info using pdfplumber

💾 Export extracted data to output.csv

🌐 Simple Streamlit web interface

To install the requirements run:
pip install -r requirements.txt

🧩 Project Files
Credit_Card_Analysis/
├── requirements.txt        # Requirements
├── app.py                  # Streamlit UI
├── generate_statements.py  # Generates fake PDFs
├── parser.py               # Extracts info from PDFs
├── readFile.py             # Reads text using pdfplumber
├── statements/             # Stores PDF statements
└── output.csv              # Extracted results

💡 How It Works

Generate Fake PDFs → Creates multiple realistic statement files.

Read PDF Text → Extracted via pdfplumber.

Parse & Extract → Uses regex to identify key fields.

Streamlit App → Lets you upload or generate and view/export results.

📊 Example Output
Bank	Card Last 4	Total Due	Due Date
HDFC Bank	4821	₹23,456.00	15 Oct 2025
ICICI Bank	1943	₹27,890.00	20 Oct 2025
👨‍💻 Author

Developed by Sonika
