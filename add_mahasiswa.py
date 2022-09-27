# Tugas TST Introduction To FastAPI
# Nama  : Rachmad Hidayat
# NIM   : 18220049

from fastapi import FastAPI, Form
from pydantic import BaseModel

app = FastAPI()

class Mahasiswa(BaseModel):
    NIM : str
    Nama: str

data_mahasiswa = {}

@app.get("/")
async def root():
    return {"Page": "Root"}

@app.get("/get-data")
def get_data():
    return data_mahasiswa

@app.post("/add-mahasiswa")
def add_mahasiswa(mahasiswa: Mahasiswa) :
    id = len(data_mahasiswa)+1
    data_mahasiswa[id] = mahasiswa
    return data_mahasiswa[id]

@app.post("/add-mahasiswa-v2")
def add_mahasiswa_v2(NIM : str = Form(), Nama : str = Form()) :
    id = len(data_mahasiswa)+1
    mahasiswa = Mahasiswa(NIM = NIM, Nama = Nama)
    data_mahasiswa[id] = mahasiswa
    return data_mahasiswa[id]

@app.get("/get-by-NIM/{NIM}")
def get_by_NIM(NIM : str):
    for id in data_mahasiswa :
        if data_mahasiswa[id].NIM == NIM :
            return data_mahasiswa[id].Nama
    return {"Data": "Not found"}