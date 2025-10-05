import logging
from calc_ops import add, sub, mul, div

# Konfigurasi logging
logging.basicConfig(level=logging.INFO, format="%(levelname)s: %(message)s")

if __name__ == "__main__":
    history = []  # simpan history di sini
    ops = {'+': add, '-': sub, '*': mul, '/': div}

    while True:
        print("\n=== MENU KALKULATOR ===")
        print("1. Pilih operasi [+, -, *, /]")
        print("2. 'q' untuk keluar")
        print("3. 'h' untuk cek seluruh history")
        print("4. 'c' untuk menghapus history")

        op = input("Masukkan operasi: ").strip()

        if op == 'q':
            print("Program selesai.")
            logging.info("Program dihentikan oleh pengguna.")
            break

        elif op == 'h':
            if not history:
                print("Belum ada history.")
            else:
                print("\n=== HISTORY ===")
                for i, (a, op_hist, b, result) in enumerate(history, 1):
                    print(f"{i}. {a} {op_hist} {b} = {result}")
            continue

        elif op == 'c':
            if not history:
                print("Belum ada history untuk dihapus.")
            else:
                # Buka file history, kosongkan isinya, lalu tutup kembali.
                history.clear()
                open("history.txt", "w").close()  # hapus isi file history
                print("History berhasil dihapus.")
                logging.info("History dihapus.")
            continue # untuk melanjutkan ke menu utama

        elif op in ops:
            try:
                a = float(input("Masukkan angka pertama: "))
                b = float(input("Masukkan angka kedua: "))

                result = ops[op](a, b)
                print(f"Hasil: {a} {op} {b} = {result}")

                # simpan ke history
                history.append((a, op, b, result))
                with open("history.txt", "a") as f:
                    f.write(f"{a} {op} {b} = {result}\n")

                logging.info(f"Operasi {a} {op} {b} = {result} berhasil disimpan ke history.")
            
            except ValueError:
                print("Input tidak valid! Harap masukkan angka.")
                logging.warning("User memasukkan input non-numerik.")

        else:
            print("Operasi tidak valid.")
