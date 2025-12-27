# Deployment Guide

This guide covers various deployment options for FastAPI-Launchpad applications.

## Deployment Checklist

Before deploying to production:

- [ ] Set `DEBUG=False` in production environment
- [ ] Use strong `SECRET_KEY` (32+ characters)
- [ ] Configure proper CORS origins
- [ ] Set up HTTPS/TLS
- [ ] Configure database connection pooling
- [ ] Set up monitoring and logging
- [ ] Enable rate limiting
- [ ] Configure health checks
- [ ] Set up automated backups
- [ ] Review security headers

## Docker Deployment

### Basic Docker Deployment

**Build the image:**
```bash
docker build -t fastapi-launchpad:latest .
```

**Run the container:**
```bash
docker run -d \
  --name fastapi-launchpad \
  -p 8000:8000 \
  -e SECRET_KEY=your-secret-key \
  -e DATABASE_URL=postgresql://user:pass@host/db \
  fastapi-launchpad:latest
```

### Docker Compose

Create `docker-compose.yml`:

```yaml
version: '3.8'

services:
  api:
    build: .
    ports:
      - "8000:8000"
    environment:
      - DEBUG=False
      - DATABASE_URL=postgresql://user:pass@db:5432/appdb
    env_file:
      - .env.production
    depends_on:
      - db
    restart: unless-stopped
    healthcheck:
      test: ["CMD", "curl", "-f", "http://localhost:8000/health"]
      interval: 30s
      timeout: 10s
      retries: 3

  db:
    image: postgres:15-alpine
    volumes:
      - postgres_data:/var/lib/postgresql/data
    environment:
      - POSTGRES_USER=user
      - POSTGRES_PASSWORD=pass
      - POSTGRES_DB=appdb
    restart: unless-stopped

volumes:
  postgres_data:
```

**Deploy:**
```bash
docker-compose up -d
```

### Optimized Dockerfile

```dockerfile
# Multi-stage build for smaller image
FROM python:3.11-slim as builder

WORKDIR /app
COPY requirements.txt .
RUN pip install --user --no-cache-dir -r requirements.txt

FROM python:3.11-slim

WORKDIR /app
COPY --from=builder /root/.local /root/.local
COPY . .

ENV PATH=/root/.local/bin:$PATH
ENV PYTHONUNBUFFERED=1

EXPOSE 8000

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
```

## Cloud Platform Deployments

### Deploy to AWS (ECS/Fargate)

**1. Create ECR repository:**
```bash
aws ecr create-repository --repository-name fastapi-launchpad
```

**2. Build and push image:**
```bash
# Login to ECR
aws ecr get-login-password --region us-east-1 | docker login --username AWS --password-stdin <account-id>.dkr.ecr.us-east-1.amazonaws.com

# Build and tag
docker build -t fastapi-launchpad .
docker tag fastapi-launchpad:latest <account-id>.dkr.ecr.us-east-1.amazonaws.com/fastapi-launchpad:latest

# Push
docker push <account-id>.dkr.ecr.us-east-1.amazonaws.com/fastapi-launchpad:latest
```

**3. Create ECS task definition** (`task-definition.json`):
```json
{
  "family": "fastapi-launchpad",
  "networkMode": "awsvpc",
  "requiresCompatibilities": ["FARGATE"],
  "cpu": "256",
  "memory": "512",
  "containerDefinitions": [
    {
      "name": "fastapi-launchpad",
      "image": "<account-id>.dkr.ecr.us-east-1.amazonaws.com/fastapi-launchpad:latest",
      "portMappings": [
        {
          "containerPort": 8000,
          "protocol": "tcp"
        }
      ],
      "environment": [
        {"name": "DEBUG", "value": "False"}
      ],
      "secrets": [
        {
          "name": "SECRET_KEY",
          "valueFrom": "arn:aws:secretsmanager:us-east-1:account-id:secret:api-secret-key"
        }
      ]
    }
  ]
}
```

### Deploy to Google Cloud Run

```bash
# Build and deploy in one command
gcloud run deploy fastapi-launchpad \
  --source . \
  --platform managed \
  --region us-central1 \
  --allow-unauthenticated \
  --set-env-vars DEBUG=False \
  --set-secrets SECRET_KEY=api-secret-key:latest
```

### Deploy to Azure Container Instances

```bash
# Create resource group
az group create --name fastapi-rg --location eastus

# Create container
az container create \
  --resource-group fastapi-rg \
  --name fastapi-launchpad \
  --image fastapi-launchpad:latest \
  --dns-name-label fastapi-app \
  --ports 8000 \
  --environment-variables DEBUG=False \
  --secure-environment-variables SECRET_KEY=your-secret
```

### Deploy to Heroku

**1. Create `Procfile`:**
```
web: uvicorn app.main:app --host 0.0.0.0 --port $PORT
```

**2. Deploy:**
```bash
# Login to Heroku
heroku login

# Create app
heroku create your-app-name

# Set environment variables
heroku config:set SECRET_KEY=your-secret-key
heroku config:set DEBUG=False

# Deploy
git push heroku main
```

### Deploy to Railway

**1. Create `railway.json`:**
```json
{
  "$schema": "https://railway.app/railway.schema.json",
  "build": {
    "builder": "DOCKERFILE"
  },
  "deploy": {
    "startCommand": "uvicorn app.main:app --host 0.0.0.0 --port $PORT",
    "restartPolicyType": "ON_FAILURE",
    "restartPolicyMaxRetries": 10
  }
}
```

**2. Deploy:**
```bash
# Install Railway CLI
npm i -g @railway/cli

# Login and deploy
railway login
railway init
railway up
```

## Kubernetes Deployment

### Basic Kubernetes Manifests

**Deployment (`k8s/deployment.yaml`):**
```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: fastapi-launchpad
spec:
  replicas: 3
  selector:
    matchLabels:
      app: fastapi-launchpad
  template:
    metadata:
      labels:
        app: fastapi-launchpad
    spec:
      containers:
      - name: api
        image: fastapi-launchpad:latest
        ports:
        - containerPort: 8000
        env:
        - name: DEBUG
          value: "False"
        envFrom:
        - secretRef:
            name: api-secrets
        livenessProbe:
          httpGet:
            path: /health
            port: 8000
          initialDelaySeconds: 30
          periodSeconds: 10
        readinessProbe:
          httpGet:
            path: /health
            port: 8000
          initialDelaySeconds: 5
          periodSeconds: 5
```

**Service (`k8s/service.yaml`):**
```yaml
apiVersion: v1
kind: Service
metadata:
  name: fastapi-launchpad
spec:
  selector:
    app: fastapi-launchpad
  ports:
  - port: 80
    targetPort: 8000
  type: LoadBalancer
```

**Deploy:**
```bash
kubectl apply -f k8s/
```

## Reverse Proxy Setup

### Nginx Configuration

```nginx
upstream fastapi_backend {
    server 127.0.0.1:8000;
    # Add more servers for load balancing
    # server 127.0.0.1:8001;
}

server {
    listen 80;
    server_name api.yourdomain.com;
    
    # Redirect HTTP to HTTPS
    return 301 https://$server_name$request_uri;
}

server {
    listen 443 ssl http2;
    server_name api.yourdomain.com;
    
    ssl_certificate /path/to/cert.pem;
    ssl_certificate_key /path/to/key.pem;
    
    location / {
        proxy_pass http://fastapi_backend;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto $scheme;
    }
}
```

## Monitoring and Logging

### Health Checks

Ensure your application has a health check endpoint:

```python
@app.get("/health")
async def health_check():
    return {
        "status": "healthy",
        "timestamp": datetime.utcnow().isoformat()
    }
```

### Logging

Use structured logging in production:

```python
import logging
import json

logging.basicConfig(
    level=logging.INFO,
    format='%(message)s'
)

logger = logging.getLogger(__name__)

# Log as JSON
logger.info(json.dumps({
    "event": "request",
    "path": "/api/endpoint",
    "status": 200
}))
```

### Monitoring Tools

- **Prometheus**: Metrics collection
- **Grafana**: Metrics visualization
- **Sentry**: Error tracking
- **DataDog**: APM and monitoring
- **New Relic**: Application monitoring

## Performance Optimization

### Use Production ASGI Server

```bash
# Gunicorn with Uvicorn workers
gunicorn app.main:app \
  --workers 4 \
  --worker-class uvicorn.workers.UvicornWorker \
  --bind 0.0.0.0:8000 \
  --access-logfile - \
  --error-logfile -
```

### Enable Caching

Use Redis for caching:
```python
from fastapi_cache import FastAPICache
from fastapi_cache.backends.redis import RedisBackend
from redis import asyncio as aioredis

@app.on_event("startup")
async def startup():
    redis = aioredis.from_url("redis://localhost")
    FastAPICache.init(RedisBackend(redis), prefix="fastapi-cache")
```

## Security Best Practices

1. **Use HTTPS in production**
2. **Set security headers**
3. **Enable rate limiting**
4. **Validate all inputs**
5. **Use secrets management**
6. **Regular security updates**
7. **Implement proper authentication**

## Troubleshooting

### Common Issues

**Port binding errors:**
```bash
# Check if port is in use
lsof -i :8000
# Kill process if needed
kill -9 <PID>
```

**Database connection issues:**
- Verify DATABASE_URL is correct
- Check network connectivity
- Ensure database is running
- Check firewall rules

**Memory issues:**
- Increase container memory limits
- Optimize database queries
- Implement pagination
- Use caching

---

Need deployment help? [Open an issue](https://github.com/anshuman-nanda/FastAPI-Launchpad/issues)
