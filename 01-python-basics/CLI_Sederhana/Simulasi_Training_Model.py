import logging

# Konfigurasi logging untuk menampilkan informasi di konsol (bisa atur format level dan pesan)
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

losses = [0.9, 0.7, 0.75, 0.6, 0.55]  # Contoh data loss per epoch