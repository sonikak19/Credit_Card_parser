import streamlit as st
import pandas as pd
from readFile import extract_text_from_pdf
from parser import extract_info

st.title("📄Credit Card Statement Parser💳")

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
    st.success("Data saved to output.csv")
