import csv, json, argparse, logging, sys
from pathlib import Path

logging.basicConfig(level=logging.INFO, format="%(asctime)s [%(levelname)s] %(message)s")

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
