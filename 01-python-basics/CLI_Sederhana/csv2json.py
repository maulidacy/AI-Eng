import csv, json
from pathlib import Path

# Fix the path to point to the correct location of the CSV file
path = Path("../csv/Titanic-Dataset.csv")
rows = list(csv.DictReader(path.open(encoding='utf-8')))
print(json.dumps(rows, indent=2, ensure_ascii=False))
