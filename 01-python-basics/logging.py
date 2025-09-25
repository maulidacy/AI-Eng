from fastapi import FastAPI
import logging

logging.basicConfig(level=logging.INFO)
app = FastAPI()

@app.get("/predict")