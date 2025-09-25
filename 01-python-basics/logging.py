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
    return{"hasil": y}
    