import matplotlib.pyplot as plt
from wordcloud import WordCloud
import streamlit as st
from collections import Counter

def plot_entity_bar(entities):
    labels = [label for _, label in entities]
    counts = Counter(labels)
    fig, ax = plt.subplots()
    ax.bar(counts.keys(), counts.values())
    ax.set_title("Entity Type Distribution")
    st.pyplot(fig)

def plot_wordcloud(text):
    wc = WordCloud(width=800, height=400, background_color="white").generate(text)
    fig, ax = plt.subplots(figsize=(10, 5))
    ax.imshow(wc, interpolation="bilinear")
    ax.axis("off")
    st.pyplot(fig)
