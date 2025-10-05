import logging
from calc_ops import add, sub, mul, div

logging.basicConfig(level=logging.INFO, format="%(levelname)s: %(message)s")

if __name__ == "__main__":
    history = []  # simpan history di sini
    
    while True:
        print("\n1. Pilih operasi [+, -, *, /] \n2. 'q' untuk keluar \n3. 'h' untuk cek seluruh history \n4. 'c' untuk menghapus history")
        op = input("Masukkan operasi: ").strip()
        
        if op == 'q':
            print("Program selesai.")
            break
        elif op == 'h':
            if not history:
                print("Belum ada history.")
            else:
                print("History:")
                for i, (a, op_hist, b, result) in enumerate(history, 1):
                    print(f"{i}. {a} {op_hist} {b} = {result}")
            with open("history.txt", "a") as f:
                f.write(f"{a} {op} {b} = {result}\n ")
            continue  # kembali ke menu utama tanpa minta angka
        elif op == 'c':
            if not history:
                print("Belum ada history.")
                continue
            else:
                history.clear()
                print("History berhasil dihapus.")
            continue

        try:
            a = float(input("Masukkan angka pertama: "))
            b = float(input("Masukkan angka kedua: "))
            
            ops = {'+': add, '-': sub, '*': mul, '/': div}
            if op in ops:
                result = ops[op](a, b)
                print(f"Hasil: {a} {op} {b} = {result}")
                # simpan ke history
                history.append((a, op, b, result))
            else:
                print("Operasi tidak valid.")
        except ValueError:
            print("Input tidak valid! Harap masukkan angka.")
