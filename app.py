import os
import uvicorn
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def root():
    return {
        "status": "Running",
        "service": "AI Video Backend"
    }

if __name__ == "__main__":
    uvicorn.run(
        app,
        host="0.0.0.0",
        port=int(os.environ.get("PORT", 8080))
    )
    @app.post("/process-video")
def process_video(req: VideoReq):
    file_url = req.file_url

    r = requests.get(file_url)
    if r.status_code != 200:
        return {"error": "download failed"}

    with open("video.mp4", "wb") as f:
        f.write(r.content)

    return {
        "status": "success",
        "file_url": file_url
    }
