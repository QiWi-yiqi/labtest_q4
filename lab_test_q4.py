import streamlit as st
from PyPDF2 import PdfReader
import nltk
from nltk.tokenize import sent_tokenize

st.title("PDF Text Chunking using NLTK Sentence Tokenizer")

# REQUIRED for Streamlit Cloud / Python 3.13
nltk.download("punkt", quiet=True)
nltk.download("punkt_tab", quiet=True)

uploaded_file = st.file_uploader("Upload a PDF file", type="pdf")

if uploaded_file is not None:
    reader = PdfReader(uploaded_file)
    full_text = ""

    for page in reader.pages:
        text = page.extract_text()
        if text:
            full_text += text + " "

    sentences = sent_tokenize(full_text)

    st.subheader("Extracted Sentence Sample (Index 58–68)")

    if len(sentences) >= 69:
        for i in range(58, 69):
            st.write(f"{i}: {sentences[i]}")
    else:
        st.warning("PDF does not contain enough sentences (minimum 69 required).")

