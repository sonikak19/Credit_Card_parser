# Credit_Card_parser
💳 Credit Card Statement Analyzer

An interactive Streamlit + Python project that can generate, upload, and analyze credit card statement PDFs.
It extracts key details like bank name, billing period, due date, and total due, and saves everything to a CSV file.

🚀 Features

🏦 Generate multi-bank credit card statements (HDFC, ICICI, SBI, Axis, Kotak)

📄 Upload any statement PDF for analysis

🔍 Automatically extract summary info using pdfplumber

💾 Export extracted data to output.csv

🌐 Simple Streamlit web interface


🧩 Installation & Setup

1️⃣ Clone the Repository

git clone https://github.com/<your-username>/credit-card-analyzer.git

cd credit-card-analyzer

2️⃣ Install Dependencies

pip install -r requirements.txt


Or manually install:

pip install streamlit reportlab pdfplumber pandas

3️⃣ Run the Streamlit App

streamlit run app.py


Then open the URL Streamlit provides.

🧮 How It Works

🏦 1. PDF Generation

generate_statements.py uses ReportLab to create realistic, multi-page fake statements for multiple banks.

Each page includes:

Customer name

Card number (last 4 digits)

Statement period

Due date

Recent transactions

🧾 2. PDF Reading

readFile.py uses pdfplumber to extract text from uploaded or generated PDFs.

🔍 3. Data Parsing

parser.py applies regular expressions (regex) and text pattern logic to identify key financial fields.

📊 4. Streamlit Interface

app.py connects everything together.
You can:

Upload a PDF

Generate PDFs

View results in a clean interface

Download extracted data as CSV

🧩 Project Files

Credit_Card_Analysis/
├── requirements.txt        # Requirements
├── app.py                  # Streamlit UI
├── generate_statements.py  # Generates dummy PDFs
├── parser.py               # Extracts info from PDFs
├── readFile.py             # Reads text using pdfplumber
├── statements/             # Stores PDF statements
└── output.csv              # Extracted results


💡 How It Works

Generate PDFs → Creates multiple realistic statement files.

Read PDF Text → Extracted via pdfplumber.

Parse & Extract → Uses regex to identify key fields.

Streamlit App → Lets you upload or generate and view/export results.

📊 Example Output
Bank	Card Last 4	Total Due	Due Date

HDFC Bank	4821	₹23,456.00	15 Oct 2025

ICICI Bank	1943	₹27,890.00	20 Oct 2025

👨‍💻 Author

Developed by Sonika
