# 🎵 Brainrot Music Player
A full-stack music player — frontend on Framer, backend self-hosted on Oracle Cloud.

🌐 [brainrot.framer.ai](https://brainrot.framer.ai/)

---

## How I Built It

### Frontend — Framer
Built a custom React component inside Framer that fetches songs and plays audio directly in the browser. Supports play/pause, skip, next/prev track, mute, and a progress bar. Fully customizable colors and fonts via Framer's property panel.

### Backend — Python (FastAPI)
Wrote a REST API in Python using FastAPI that serves the song list and streams audio/image files. Runs on an Oracle Cloud free-tier Ubuntu server with a free domain from DuckDNS and an SSL certificate from Let's Encrypt.

### Infrastructure — Docker + nginx + CI/CD
Containerized the API with Docker so it runs the same everywhere. nginx sits in front as a reverse proxy — handling SSL termination and forwarding requests to the container. GitHub Actions automatically rebuilds and redeploys the container on every push — no manual SSH needed.

---

## Stack

| What | How |
|---|---|
| Frontend | Framer |
| Domain | [brainrot.framer.ai](https://brainrot.framer.ai/) |
| API | Python (FastAPI) |
| Server | Oracle Cloud (Ubuntu) |
| Reverse Proxy | nginx |
| DNS | DuckDNS — `rikkiee-music.duckdns.org` |
| SSL | Let's Encrypt |
| Container | Docker + Docker Compose |
| CI/CD | GitHub Actions → Docker Hub |

---

## Architecture

Internet
↓
nginx (port 443) → handles SSL
↓
music-api container (port 8000) → serves JSON + audio files
↓
Framer frontend → renders music player

---

## Project Structure

music-app/
├── .github/
│   └── workflows/
│       └── deploy.yml
├── nginx/
│   └── music-app.conf
├── .gitignore
├── Dockerfile
├── docker-compose.yml
├── main.py
├── README.md
└── requirements.txt

