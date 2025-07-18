# SummarizePodcast

## 🚀 Summarize YouTube

This application fetches a YouTube transcript, summarizes it via the OpenAI API, and serves it as a Cloud Run service.

---

## 📋 Table of Contents
- [Prerequisites](#-prerequisites)
- [Build & Deploy](#-build--deploy)
- [Sample .env File](#-sample-env-file)

---

## ✅ Prerequisites

- `app.py` (Flask application)
- `requirements.txt` listing:
  - Flask
  - Gunicorn
  - youtube-transcript-api
  - openai
  - etc.
- `.env` file with required environment variables (see below)
- Docker installed
- Google Cloud SDK (`gcloud`) installed and initialized
- Billing enabled on your Google Cloud project

---

## 🗂️ Sample .env File

```
OPENAI_API_KEY=your_openai_api_key_here
PROXY_CREDS=your_proxy_creds_here
```

---

## 📦 Build & Deploy

### 1. Enable Necessary Google Cloud Services

```bash
gcloud services enable run.googleapis.com artifactregistry.googleapis.com
```

### 2. Create Artifact Registry (One-Time Setup)

```bash
gcloud artifacts repositories create voicegen-repo `
  --repository-format=docker `
  --location=us-central1
```

### 3. Build and Tag Your Docker Image

- To see project names:

```bash
gcloud projects list
```

- Build images:

```bash
docker build -t tts-app:latest .
```


- 3. Authenticate Docker with Google Cloud
```bash
gcloud auth login
gcloud config set project tts-app
gcloud auth configure-docker us-central1-docker.pkg.dev

docker build -t tts-app:latest .
docker tag tts-app:latest us-central1-docker.pkg.dev/voicegen-465413/voicegen-repo/tts-app:latest
docker push us-central1-docker.pkg.dev/voicegen-465413/voicegen-repo/tts-app:latest

gcloud run deploy tts-app `
  --image=us-central1-docker.pkg.dev/voicegen-465413/voicegen-repo/tts-app:latest `
  --platform managed `
  --region us-central1 `
  --allow-unauthenticated `
  --memory=4Gi `
  --timeout=3600

```







```bash
gcloud auth configure-docker us-central1-docker.pkg.dev
```


#### 3.2 Authenticate with Google Cloud

```bash
gcloud auth login
gcloud config set project tts-app
gcloud auth configure-docker us-central1-docker.pkg.dev
```

### 4. Push the Image

```bash

docker push us-central1-docker.pkg.dev/voicegen-465413/voicegen-repo/tts-app:latest

```

### 5. Deploy to Cloud Run

```bash
gcloud run deploy tts-app `
  --image=us-central1-docker.pkg.dev/voicegen-465413/voicegen-repo/tts-app:latest `
  --platform managed `
  --region us-central1 `
  --allow-unauthenticated
```



#### 3.1 Run and Test App Locally

```bash
docker run -p 8080:8080 --env-file .env tts-app

docker run -p 8080:8080 tts-app

docker run -p 8080:8080 us-central1-docker.pkg.dev/voicegen-465413/voicegen-repo/tts-app:latest


```



  curl -X POST https://tts-app-12899517732.us-central1.run.app/api/tts -H "Content-Type: application/json" -d '{"text":"hello"}'


---



Summary of Steps
Build:
docker build -t tts-app:latest .
Tag:
docker tag tts-app:latest us-central1-docker.pkg.dev/voicegen-465413/voicegen-repo/tts-app:latest
Authenticate:
gcloud auth configure-docker us-central1-docker.pkg.dev
Push:
docker push us-central1-docker.pkg.dev/voicegen-465413/voicegen-repo/tts-app:latest
Deploy (optional):
gcloud run deploy ...