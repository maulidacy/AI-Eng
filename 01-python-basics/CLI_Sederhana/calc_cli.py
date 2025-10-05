import logging

logging.basicConfig(level=logging.INFO, format="%(levelname)s: %(message)s")

def add(a, b):
    return a + b

def sub(a, b):
    return a - b

def mul(a, b):
    return a * b

def div(a, b):
    if b == 0:
        return "Error: Pembagian dengan nol tidak dapat dilakukan."
    return a / b


if __name__ == "__main__":
    history = []  # simpan history di sini
    
    while True:
        op = input("Pilih operasi [+, -, *, /] atau 'q' untuk keluar, 'h' untuk cek seluruh history, atau 'c' untuk menghapus history: ").strip()
        
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
