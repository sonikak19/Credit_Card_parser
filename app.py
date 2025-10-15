import streamlit as st
import pandas as pd
import os
from readFile import extract_text_from_pdf
from parser import extract_info
from generate_statements import generate_statements

st.set_page_config(page_title="Credit Card Analyzer", layout="wide")

st.title("📄 Credit Card Statement Analyzer 💳")

mode = st.radio("Choose Mode:", ["Upload Statement", "Generate Statements"])

if mode == "Upload Statement":
    uploaded_file = st.file_uploader("Upload your credit card statement (PDF)", type=["pdf"])
    if uploaded_file is not None:
        with open("temp.pdf", "wb") as f:
            f.write(uploaded_file.read())
        text = extract_text_from_pdf("temp.pdf")
        info = extract_info(text)
        st.subheader("✅ Extracted Information")
        st.json(info)
        df = pd.DataFrame([info])
        df.to_csv("output.csv", index=False)
        st.download_button("⬇️ Download CSV", df.to_csv(index=False), "output.csv", "text/csv")

else:
    if st.button("🚀 Generate Statements"):
        os.makedirs("statements", exist_ok=True)
        generate_statements()
        st.success("✅ Statements generated in the 'statements/' folder.")
        pdfs = [f for f in os.listdir("statements") if f.endswith(".pdf")]
        all_info = []
        for pdf in pdfs:
            text = extract_text_from_pdf(os.path.join("statements", pdf))
            info = extract_info(text)
            all_info.append(info)
        df = pd.DataFrame(all_info)
        st.dataframe(df)
        st.download_button("⬇️ Download Extracted Data", df.to_csv(index=False), "output.csv", "text/csv")
