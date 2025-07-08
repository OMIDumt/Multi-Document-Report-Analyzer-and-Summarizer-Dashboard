from transformers import pipeline
import spacy
from textblob import TextBlob

# 🔁 Load summarization model once (Streamlit will cache it in memory)
summarizer = pipeline("summarization", model="facebook/bart-large-cnn")

def generate_summary(text, max_len=130):
    if len(text.strip()) == 0:
        return ""
    input_text = text[:1024]  # Limit for BART
    summary = summarizer(input_text, max_length=max_len, min_length=30, do_sample=False)
    return summary[0]['summary_text']

def extract_entities(text):
    # ✅ Load spaCy model here after it's downloaded in app.py
    nlp = spacy.load("en_core_web_sm")
    doc = nlp(text)
    return [(ent.text, ent.label_) for ent in doc.ents]

def detect_sentiment(text):
    return TextBlob(text).sentiment.polarity  # Range: -1 (negative) to 1 (positive)
