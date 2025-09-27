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
        with path.open("r", encoding="utf-8") as f:
            return list(csv.DictReader(f))
    except Exception as e:
        logging.error("Gagal membaca file CSV: %s", e)
        sys.exit(1)

def validate(rows: list[dict], required: list[str]) -> list[dict]:
    """Memvalidasi apakah semua kolom yang dibutuhkan ada di setiap baris"""
    for i, row in enumerate(rows):
        missing = [col for col in required if col not in row or not row[col]]
        if missing:
            logging.error("Row %d missing fields: %s", i, missing)
    return rows

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Convert CSV to JSON")
    parser.add_argument("src", help="Path ke file CSV")
    parser.add_argument("dst", help="Path ke file JSON output")
    parser.add_argument("--req", nargs="*", default=[], help="Kolom wajib")
    args = parser.parse_args()

    # Baca dan validasi CSV
    rows = read_csv(Path(args.src)) 
    rows = validate(rows, args.req)

    # Simpan hasil ke JSON
    Path(args.dst).write_text(json.dumps(rows, indent=2, ensure_ascii=False), encoding="utf-8")
    logging.info("Berhasil konversi %d baris", len(rows))

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
