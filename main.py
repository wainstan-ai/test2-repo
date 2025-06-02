from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class EchoRequest(BaseModel):
    word: str

@app.get("/")
def home():
    return {"hello": "Render!"}

@app.post("/echo")
def echo(req: EchoRequest):
    return {"echo": req.word}
