"""
- Membaca dataset dari CSV
- Eksplorasi awal (EDA sederhana)
- Menggunakan fungsi dasar: head(), info(), describe(), value_counts()
- Mulai biasakan logging untuk mencatat langkah-langkah penting
"""

# Baca dataset dari CSV
import pandas as pd
import logging

logging.basicConfig(level=logging.INFO, format="%(levelname)s: %(message)s")

df = pd.read_csv("../01-python-basics/csv/Titanic-Dataset.csv")
logging.info("Dataset dibaca dengan %d baris dan %d kolom", df.shape[0], df.shape[1])
print("5 baris pertama dataset:", df.head(), sep="\n")

#----------------------------------- Eksplorasi Awal (EDA) -----------------------------------
# Info umum
print("\nInfo DataFrame:")
print(df.info())