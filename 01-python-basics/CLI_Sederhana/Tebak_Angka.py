import random
import logging
logging.basicConfig(level=logging.INFO)

# Langkah 1: Inisialisasi Game
# Komputer memilih satu angka acak dari 1 sampai 10.
# Kita gunakan modul `random` untuk ini.
angka_rahasia = random.randint(1, 10)

# Variabel kontrol untuk perulangan
sudah_benar = False

logging.info("Komputer telah memilih sebuah angka rahasia antara 1 dan 10.")
logging.info("Silakan tebak angkanya!")

# Langkah 2: Perulangan Utama (Loop)
# Loop akan terus berjalan selama `sudah_benar` bernilai False
while not sudah_benar:
    try:
        # Langkah 3: Meminta Input
        tebakan = int(input("Masukkan angka tebakan Anda: "))

        # Langkah 4: Logika Pengecekan
        if tebakan < angka_rahasia:
            logging.info("Tebakan terlalu kecil!")
        elif tebakan > angka_rahasia:
            logging.info("Tebakan terlalu besar!")
        else:
            logging.info("Selamat! Tebakan Anda benar!")
            # Ubah nilai `sudah_benar` menjadi True agar loop berhenti
            sudah_benar = True
    except ValueError:
        logging.error("Input tidak valid. Harap masukkan angka bulat.")