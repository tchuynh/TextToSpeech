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