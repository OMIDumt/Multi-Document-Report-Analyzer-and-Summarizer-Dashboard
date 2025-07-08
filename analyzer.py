from transformers import pipeline
import spacy
from textblob import TextBlob

# Load models once
summarizer = pipeline("summarization", model="facebook/bart-large-cnn")
nlp = spacy.load("en_core_web_sm")

def generate_summary(text, max_len=130):
    if len(text.strip()) == 0:
        return ""
    input_text = text[:1024]  # max for BART
    summary = summarizer(input_text, max_length=max_len, min_length=30, do_sample=False)
    return summary[0]['summary_text']

def extract_entities(text):
    doc = nlp(text)
    entities = [(ent.text, ent.label_) for ent in doc.ents]
    return entities

def detect_sentiment(text):
    return TextBlob(text).sentiment.polarity  # -1 to 1
