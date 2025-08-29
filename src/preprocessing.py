import os
import pandas as pd
import re
from pathlib import Path

# Paths
RAW_PATH = Path("data/raw/IMDB Dataset.csv")
PROCESSED_PATH = Path("data/processed/")

PROCESSED_PATH.mkdir(parents=True, exist_ok=True)

# Load dataset
df = pd.read_csv(RAW_PATH)

# Text cleaning function
def clean_text(text):
    text = text.lower()
    text = re.sub(r"<.*?>", "",text)
    text = re.sub(r"[^a-zA-Z\s]", "", text)
    text = re.sub(r"\s+", " ", text).strip()
    return text

# Clean dataset
df['clean_review'] = df['review'].apply(clean_text)

# Save preprocessed data
df.to_csv(PROCESSED_PATH / "imdb_clean.csv", index=False)

# Show Results
print("Processed data saved to:", PROCESSED_PATH / "imdb_clean.csv")