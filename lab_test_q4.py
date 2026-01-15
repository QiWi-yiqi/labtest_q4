import streamlit as st
from PyPDF2 import PdfReader
import nltk
from nltk.tokenize import sent_tokenize

st.title("PDF Text Chunking using NLTK Sentence Tokenizer")

# Download tokenizer safely
nltk.download("punkt", quiet=True)

uploaded_file = st.file_uploader("Upload a PDF file", type="pdf")

if uploaded_file is not None:
    reader = PdfReader(uploaded_file)
    full_text = ""

    # Extract text from all pages
    for page in reader.pages:
        text = page.extract_text()
        if text:
            full_text += text + " "

    # Sentence tokenization
    sentences = sent_tokenize(full_text)

    st.subheader("Extracted Sentence Sample (Index 58–68)")

    if len(sentences) >= 69:
        sample_sentences = sentences[58:69]
        for i, s in enumerate(sample_sentences, start=58):
            st.write(f"{i}: {s}")
    else:
        st.warning("PDF does not contain enough sentences (minimum 69 required).")
