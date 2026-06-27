from fastapi import FastAPI
from pydantic import BaseModel
import requests

app = FastAPI()

class VideoReq(BaseModel):
    file_url: str

@app.get("/")
def home():
    return {"status": "ok"}

@app.post("/process-video")
def process_video(req: VideoReq):
    try:
        r = requests.get(req.file_url)

        if r.status_code != 200:
            return {"error": "download failed"}

        with open("video.mp4", "wb") as f:
            f.write(r.content)

        return {
            "status": "success",
            "message": "video received"
        }

    except Exception as e:
        return {"error": str(e)}
