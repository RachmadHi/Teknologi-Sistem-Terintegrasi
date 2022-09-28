from http.client import HTTPException
import json
from fastapi import FastAPI

app = FastAPI()

with open("data_mahasiswa.json", "r") as r_file :
    data = json.load(r_file)

@app.get("/data_mahasiswa/{NIM}")
async def read_mahasiswa (NIM : str):
    for mahasiswa_item in data["data_mahasiswa"] :
        if mahasiswa_item["NIM"] == NIM :
            return mahasiswa_item
    raise HTTPException(
        status_code = 404, detail = f"Data not found"
    )

