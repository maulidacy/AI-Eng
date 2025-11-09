import sys
from storage import load_db, save_db
from core import add_habit, mark_done, stats

def main(argv: list[str]) -> int:
    if len(argv) < 2:
        print("usage: habit [add|done|stat] ..."); return 1
    db = load_db()
    cmd = argv[1]
    try:
        if cmd == "add":
            add_habit(db, " ".join(argv[2:]))
            save_db(db); print("ok")
        elif cmd == "done":
            mark_done(db, " ".join(argv[2:]))
            save_db(db); print("ok")
        elif cmd == "stat":
            days = int(argv[2]) if len(argv) > 2 else 7
            for name, cnt in stats(db, days):
                print(f"{name}: {cnt}/{days}")
        else:
            print("unknown command"); return 1
    except Exception as e:
        print(f"error: {e}"); return 2
    return 0

if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
