import pandas as pd
import re
from sklearn.feature_extraction.text import ENGLISH_STOP_WORDS

def clean_text(text):
    text = str(text).lower()
    text = re.sub(r"[^\w\s]", "", text)
    tokens = text.split()
    tokens = [w for w in tokens if w not in ENGLISH_STOP_WORDS]
    return " ".join(tokens)

def preprocess():
    df = pd.read_csv("data.csv")
    df["text"] = df["subject"] + " " + df["body"]
    df["clean_text"] = df["text"].apply(clean_text)
    return df
