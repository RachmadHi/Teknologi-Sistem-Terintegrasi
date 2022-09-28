from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def helloWorld()-> dict :
    return { "message" : "Hello, World!"}