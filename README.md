# 🎵 Brainrot Music Player

A full-stack music player — frontend on Framer, backend self-hosted on Oracle Cloud.

🌐 [brainrot.framer.ai](https://brainrot.framer.ai/)

---

## How I Built It

### Frontend — Framer
Built a custom React component inside Framer that fetches songs and plays audio directly in the browser. Supports play/pause, skip, next/prev track, mute, and a progress bar. Fully customizable colors and fonts via Framer's property panel.

### Backend — Python (FastAPI)
Wrote a REST API in Python using FastAPI that serves the song list and streams audio/image files. Runs on an Oracle Cloud free-tier Ubuntu server with a free domain from DuckDNS and an SSL certificate from Let's Encrypt.

### Infrastructure — Docker + CI/CD
Containerized the API with Docker so it runs the same everywhere. Set up GitHub Actions to automatically rebuild and redeploy the container on every push — no manual SSH needed.

---

## Stack

| What | How |
|---|---|
| Frontend | Framer |
| Domain | [brainrot.framer.ai](https://brainrot.framer.ai/) |
| API | Python (FastAPI) |
| Server | Oracle Cloud (Ubuntu) |
| DNS | DuckDNS — `rikkiee-music.duckdns.org` |
| SSL | Let's Encrypt |
| Container | Docker + Docker Compose |
| CI/CD | GitHub Actions → Docker Hub |

---

## Project Structure

```
music-api/
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
├── main.py
└── songs/
    ├── audio/
    ├── covers/
    └── artists/
```
