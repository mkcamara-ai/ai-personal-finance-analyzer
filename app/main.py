
from fastapi import FastAPI, UploadFile, File
from .analyzer import analyze_transactions
import shutil
import os

app = FastAPI(title="AI Personal Finance Analyzer - by mkcamara")

@app.get("/")
def home():
    return {"message": "AI Personal Finance Analyzer is running 🚀"}

@app.post("/analyze")
async def analyze(file: UploadFile = File(...)):
    temp_file = "temp.csv"

    with open(temp_file, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    result = analyze_transactions(temp_file)

    os.remove(temp_file)

    return result
