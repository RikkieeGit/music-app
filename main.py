from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=False,
    allow_methods=["GET", "HEAD", "OPTIONS"],
    allow_headers=["*"],
)

app.mount("/audio", StaticFiles(directory="songs/audio"), name="audio")
app.mount("/covers", StaticFiles(directory="songs/covers"), name="covers")
app.mount("/artists", StaticFiles(directory="songs/artists"), name="artists")

BASE_URL = "https://rikkiee-music.duckdns.org"  # ← FIXED

songs = [
    {
        "trackTitle": "Coffee Stop",
        "artistName": "Aves",
        "audioUrl": f"{BASE_URL}/audio/Coffee_Stop.mp3",
        "coverUrl": f"{BASE_URL}/covers/Coffee_Stop.webp",
        "artistUrl": f"{BASE_URL}/artists/Aves.webp"
    },
    {
        "trackTitle": "Move It",
        "artistName": "Jimit",
        "audioUrl": f"{BASE_URL}/audio/Move_It.mp3",
        "coverUrl": f"{BASE_URL}/covers/Move_It.webp",
        "artistUrl": f"{BASE_URL}/artists/Jimit.webp"
    },
    {
        "trackTitle": "Grease Monkey",
        "artistName": "Ziv Moran",
        "audioUrl": f"{BASE_URL}/audio/Grease_Monkey.mp3",
        "coverUrl": f"{BASE_URL}/covers/Grease_Monkey.webp",
        "artistUrl": f"{BASE_URL}/artists/Ziv_Moran.webp"
    },
    {
        "trackTitle": "Rhythm Rocket",
        "artistName": "Steven Beddall",
        "audioUrl": f"{BASE_URL}/audio/Rhythm_Rocket.mp3",
        "coverUrl": f"{BASE_URL}/covers/Rhythm_Rocket.webp",
        "artistUrl": f"{BASE_URL}/artists/Steven_Beddall.webp"
    },
    {
        "trackTitle": "When You Wake Up",
        "artistName": "Kashido",
        "audioUrl": f"{BASE_URL}/audio/When_You_Wake_Up.mp3",
        "coverUrl": f"{BASE_URL}/covers/When_You_Wake_Up.webp",
        "artistUrl": f"{BASE_URL}/artists/Kashido.webp"
    },
]

@app.get("/api/songs")
def get_songs():
    return songs
