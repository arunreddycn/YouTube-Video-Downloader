from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
import yt_dlp

app = FastAPI()

# Allow all origins (for development purposes only)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Use specific origins for production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/download")
async def download_video(request: Request):
    try:
        data = await request.json()
        video_url = data.get("url")

        if not video_url:
            return {"error": "No video URL provided."}

        ydl_opts = {
            'outtmpl': '%(title)s.%(ext)s',
        }

        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([video_url])

        return {"message": "Video download completed!"}
    
    except Exception as e:
        return {"error": f"An error occurred: {e}"}

