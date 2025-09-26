import logging

# Konfigurasi logging untuk menampilkan informasi di konsol (bisa atur format level dan pesan)
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

losses = [0.9, 0.7, 0.75, 0.6, 0.55]  # Contoh data loss per epoch

prev_loss = None
for epoch, loss in enumerate(losses, start=1):
    logging.info(f"Epoch {epoch}, lss = {loss:.2f}")
    if prev_loss is not None and loss > prev_loss:
        logging.warning(f"Loss naik di epoch {epoch}! ({loss:.2f} > {prev_loss:.2f})")
    prev_loss = loss