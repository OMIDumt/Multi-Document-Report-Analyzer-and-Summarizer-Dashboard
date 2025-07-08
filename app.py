import streamlit as st
from utils import load_pdf_text, load_txt_text
from analyzer import generate_summary, extract_entities, detect_sentiment
from visualizer import plot_entity_bar, plot_wordcloud
from collections import Counter
import pandas as pd

import os
os.system("python -m spacy download en_core_web_sm")
os.system("python -m textblob.download_corpora")

st.set_page_config(layout="wide", page_title="📊 Report Analyzer Dashboard")
st.title("📊 Multi-Document Report Analyzer")

uploaded_files = st.file_uploader("Upload PDFs or TXT files", type=["pdf", "txt"], accept_multiple_files=True)

if uploaded_files:
    summaries = []
    all_entities = []
    sentiments = []

    for file in uploaded_files:
        st.subheader(f"📄 {file.name}")

        # Load text
        text = load_pdf_text(file) if file.name.endswith(".pdf") else load_txt_text(file)

        # Summary
        summary = generate_summary(text)
        st.markdown(f"**📝 Summary:** {summary}")
        summaries.append(summary)

        # Entities
        entities = extract_entities(text)
        entity_df = pd.DataFrame(entities, columns=["Entity", "Type"])
        st.dataframe(entity_df)
        all_entities.extend(entities)

        # Sentiment (optional)
        sentiment = detect_sentiment(text)
        st.markdown(f"**📈 Sentiment Score:** `{sentiment:.2f}`")
        sentiments.append(sentiment)

        st.markdown("---")

    # Overall stats
    st.header("📊 Overall Insights")

    st.subheader("Top Entity Types")
    plot_entity_bar(all_entities)

    st.subheader("📌 Word Cloud (Summaries)")
    combined_summary = " ".join(summaries)
    plot_wordcloud(combined_summary)
