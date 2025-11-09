from datetime import date, timedelta

def add_habit(db: dict, name: str) -> None:
    if not name.strip():
        raise ValueError("Nama habit kosong")
    if any(h["name"] == name for h in db.get("habits", [])):
        raise ValueError("Habit sudah ada")
    db.setdefault("habits", []).append({"name": name, "done_dates": []})

def mark_done(db: dict, name: str, day: date | None = None) -> None:
    day = day or date.today()
    for h in db.get("habits", []):
        if h["name"] == name:
            iso = day.isoformat()
            if iso not in h["done_dates"]:
                h["done_dates"].append(iso)
            return
    raise ValueError("Habit tidak ditemukan")

def stats(db: dict, days: int = 7) -> list[tuple[str,int]]:
    start = date.today() - timedelta(days=days-1)
    res = []
    for h in db.get("habits", []):
        cnt = sum(start.isoformat() <= d for d in h["done_dates"])
        res.append((h["name"], cnt))
    return sorted(res, key=lambda x: (-x[1], x[0]))
