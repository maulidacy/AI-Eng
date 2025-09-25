from fastapi import FastAPI
import logging

logging.basicConfig(level=logging.INFO)
app = FastAPI()

@app.get("/predict")
def ppredict(x: int):
    logging.info(f"Request received with x={x}")
    