#--------------------------------- Logging Dasar -----------------------------------

#---------------------------------- Sistem Keamanan -----------------------------------
import logging
logging.basicConfig(level=logging.INFO)

def login(user, password):
    if password != "rahasia":
        logging.error("Gagal login untuk user %s", user)
        return False
    logging.info("User %s berhasil login", user)
    return True

login("admin", "salah")
login("admin", "rahasia")   

exit()
#---------------------------------- Model Training -----------------------------------
import logging
logging.basicConfig(level=logging.INFO)

for epoch in range(1, 6):
    loss = 1 / epoch
    logging.info(f"Epoch {epoch}, loss={loss:.4f}")

exit()
#--------------------------------- API prediksi dengan FastAPI ---------------------------------
# fastapi_app.py
from fastapi import FastAPI
import logging

logging.basicConfig(level=logging.INFO)
app = FastAPI()

@app.get("/predict")
def ppredict(x: int):
    logging.info(f"Request received with x={x}")
    if x < 0:
        logging.warning(f"Input negatif, hasil mungkin tidak valid")
    y = x * 2
    logging.info(f"Hasil prediksi: {y}")
    return {"hasil": y}
    