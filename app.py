from fastapi import FastAPI
from pydantic import BaseModel
import requests

app = FastAPI()

class VideoReq(BaseModel):
    file_url: str

@app.get("/")
def home():
    return {"status": "ok"}
