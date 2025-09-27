import csv
import json
import logging
import sys

# Konfigurasi logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s: [%(levelname)s] %(message)s"
)

def read_csv(path):
    """Membaca file CSV dan mengembalikan list of dictionary"""
    try:
       with open(path) as f:
           logging.info(f"Membaca file {path}")
           return list(csv.DictReader(f))
    except FileNotFoundError:
        logging.error(f"File tidak ditemukan: {path}")
        sys.exit(1)

def validate(rows, required):
    """Memvalidasi apakah semua kolom yang dibutuhkan ada di setiap baris"""
    for i, row in enumerate(rows):
        for col in required:
            if col not in row or row[col] == "":
                logging.warning(f"Baris {i} kolom  '{col}' koaong!")
    return rows

def save_json(data, path):
    """Menyimpan data ke file JSON"""
    with open(path, "w") as f:
        json.dump(rows, f, indent=2, ensure_ascii=False)
    logging.info(f"Berhasil simpan JSON ke {path}")


if __name__ == "__main__":
    rows = read_csv("csv/Titanic-Dataset.csv")
    rows = validate(rows, ["Name", "Age"])
    save_json(rows, "data.json")    
    logging.info("Selesai konversi CSV -> JSON")
exit()

#=================================== CSV to JSON ==================================
import csv, json
from pathlib import Path

# Path relatif terhadap file script ini
BASE_DIR = Path(__file__).resolve().parent
path = BASE_DIR.parent / "csv" / "Titanic-Dataset.csv"

'''
path.open() membuka file CSV.
csv.DictReader() membaca CSV baris per baris dan mengubahnya jadi list of dictionary.
'''
rows = list(csv.DictReader(path.open(encoding='utf-8')))
print(json.dumps(rows, indent=2, ensure_ascii=False))
