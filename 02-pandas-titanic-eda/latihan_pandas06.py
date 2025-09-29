import pandas as pd
import logging

# Set up logging configuration
logging.basicConfig(level=logging.INFO, format="%(levelname)s: %(message)s")

# 1. Buat DataFrame
data = {
    "nama": ["Alice", "Bob", "Charlie", "David", "Eva"],
    "umur": [20, 22, 19, 21],
    "nilai": [85, 90, 78, 60, 88]
}

df = pd.DataFrame(data)
logging.info("DataFrame dibuat dengan %d baris", len(df))
print("DataFrame awal:", df, sep="\n")