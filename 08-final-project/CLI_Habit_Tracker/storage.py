import json, os
PATH = os.path.join(os.path.dirname(__file__), "data.json")

def load_db() -> dict:
    if not os.path.exists(PATH):
        return {"habits": []}
    with open(PATH, "r", encoding="utf-8") as f:
        return json.load(f)

def save_db(db: dict) -> None:
    with open(PATH, "w", encoding="utf-8") as f:
        json.dump(db, f, ensure_ascii=False, indent=2)
