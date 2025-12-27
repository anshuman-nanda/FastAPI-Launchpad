# Configuration Guide

FastAPI-Launchpad uses environment variables for configuration, following the [12-factor app](https://12factor.net/) methodology.

## Environment Variables

### Application Settings

| Variable | Description | Default | Required |
|----------|-------------|---------|----------|
| `APP_NAME` | Application name | `FastAPI-Launchpad` | No |
| `DEBUG` | Enable debug mode | `False` | No |
| `API_VERSION` | API version prefix | `v1` | No |
| `ENVIRONMENT` | Environment name (dev, staging, prod) | `development` | No |

### Server Configuration

| Variable | Description | Default | Required |
|----------|-------------|---------|----------|
| `HOST` | Server host | `0.0.0.0` | No |
| `PORT` | Server port | `8000` | No |
| `WORKERS` | Number of worker processes | `1` | No |

### Security Settings

| Variable | Description | Default | Required |
|----------|-------------|---------|----------|
| `SECRET_KEY` | Secret key for JWT signing | - | Yes |
| `ALLOWED_ORIGINS` | CORS allowed origins (comma-separated) | `*` | No |
| `ACCESS_TOKEN_EXPIRE_MINUTES` | JWT token expiration | `30` | No |

### Database Configuration

| Variable | Description | Default | Required |
|----------|-------------|---------|----------|
| `DATABASE_URL` | Database connection string | `sqlite:///./app.db` | No |
| `DB_POOL_SIZE` | Connection pool size | `5` | No |
| `DB_MAX_OVERFLOW` | Max overflow connections | `10` | No |

### Logging Configuration

| Variable | Description | Default | Required |
|----------|-------------|---------|----------|
| `LOG_LEVEL` | Logging level (DEBUG, INFO, WARNING, ERROR) | `INFO` | No |
| `LOG_FORMAT` | Log format (json, text) | `json` | No |

## Configuration File

Create a `.env` file in your project root:

```env
# Application Configuration
APP_NAME=FastAPI-Launchpad
DEBUG=False
API_VERSION=v1
ENVIRONMENT=production

# Server Configuration
HOST=0.0.0.0
PORT=8000
WORKERS=4

# Security Configuration
SECRET_KEY=your-super-secret-key-change-this
ALLOWED_ORIGINS=https://yourdomain.com,https://www.yourdomain.com
ACCESS_TOKEN_EXPIRE_MINUTES=60

# Database Configuration
DATABASE_URL=postgresql://user:password@localhost:5432/dbname
DB_POOL_SIZE=10
DB_MAX_OVERFLOW=20

# Logging Configuration
LOG_LEVEL=INFO
LOG_FORMAT=json
```

## Environment-Specific Configurations

### Development Environment

Create `.env.development`:

```env
APP_NAME=FastAPI-Launchpad-Dev
DEBUG=True
ENVIRONMENT=development
LOG_LEVEL=DEBUG
DATABASE_URL=sqlite:///./dev.db
ALLOWED_ORIGINS=*
```

### Production Environment

Create `.env.production`:

```env
APP_NAME=FastAPI-Launchpad
DEBUG=False
ENVIRONMENT=production
LOG_LEVEL=WARNING
DATABASE_URL=postgresql://user:password@prod-db:5432/dbname
ALLOWED_ORIGINS=https://api.yourdomain.com
SECRET_KEY=use-strong-secret-from-secrets-manager
```

## Loading Configuration

FastAPI-Launchpad uses Pydantic Settings for configuration management:

```python
# app/config.py
from pydantic_settings import BaseSettings
from typing import List

class Settings(BaseSettings):
    # Application
    app_name: str = "FastAPI-Launchpad"
    debug: bool = False
    api_version: str = "v1"
    environment: str = "development"
    
    # Server
    host: str = "0.0.0.0"
    port: int = 8000
    
    # Security
    secret_key: str
    allowed_origins: List[str] = ["*"]
    access_token_expire_minutes: int = 30
    
    # Database
    database_url: str = "sqlite:///./app.db"
    
    # Logging
    log_level: str = "INFO"
    
    class Config:
        env_file = ".env"
        case_sensitive = False

settings = Settings()
```

## Using Configuration

Access configuration in your application:

```python
from app.config import settings

@app.get("/info")
async def get_info():
    return {
        "app_name": settings.app_name,
        "version": settings.api_version,
        "environment": settings.environment
    }
```

## Best Practices

### 1. Never Commit Secrets

Add `.env` to `.gitignore`:
```gitignore
.env
.env.*
!.env.example
```

### 2. Use .env.example

Create a template with dummy values:
```env
# .env.example
APP_NAME=FastAPI-Launchpad
SECRET_KEY=change-this-secret-key
DATABASE_URL=postgresql://user:pass@localhost/db
```

### 3. Use Secret Management in Production

For production, use:
- **AWS Secrets Manager**
- **HashiCorp Vault**
- **Azure Key Vault**
- **Google Secret Manager**

### 4. Validate Configuration

Add validation to your settings:

```python
from pydantic import validator

class Settings(BaseSettings):
    secret_key: str
    
    @validator('secret_key')
    def validate_secret_key(cls, v):
        if len(v) < 32:
            raise ValueError('SECRET_KEY must be at least 32 characters')
        return v
```

### 5. Environment-Specific Loading

```python
import os
from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    class Config:
        env_file = f".env.{os.getenv('ENVIRONMENT', 'development')}"
        case_sensitive = False
```

## Docker Configuration

When running in Docker, pass environment variables:

```yaml
# docker-compose.yml
services:
  api:
    build: .
    environment:
      - APP_NAME=FastAPI-Launchpad
      - DEBUG=False
      - DATABASE_URL=postgresql://user:pass@db:5432/dbname
    env_file:
      - .env.production
```

Or use Docker secrets:
```yaml
services:
  api:
    build: .
    secrets:
      - db_password
    environment:
      - DATABASE_PASSWORD_FILE=/run/secrets/db_password

secrets:
  db_password:
    external: true
```

## Testing Configuration

Override settings in tests:

```python
# tests/conftest.py
import pytest
from app.config import Settings

@pytest.fixture
def test_settings():
    return Settings(
        debug=True,
        database_url="sqlite:///./test.db",
        secret_key="test-secret-key"
    )
```

## Configuration Hierarchy

Configuration is loaded in this order (later sources override earlier ones):

1. Default values in Settings class
2. `.env` file
3. Environment variables
4. Command-line arguments (if implemented)

---

Need help with configuration? [Open an issue](https://github.com/anshuman-nanda/FastAPI-Launchpad/issues)
