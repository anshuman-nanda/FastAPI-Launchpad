# FastAPI Production Template

Production-ready FastAPI template with PostgreSQL, Redis, and Docker.

## ⚡ Quick Start

```powershell
# 1. Start everything with Docker
docker-compose up -d

# 2. Access your API
# Open: http://localhost:8000/docs
```

That's it! 🎉

## 📋 What's Running

- **FastAPI App**: http://localhost:8000/docs
- **PostgreSQL**: localhost:5432
- **Redis**: localhost:6379

## 🛠️ Common Commands

```powershell
# View logs
docker-compose logs -f app

# Stop everything
docker-compose down

# Rebuild after code changes
docker-compose up -d --build

# Run tests
docker-compose exec app pytest

# Access database
docker-compose exec postgres psql -U postgres -d fastapi_db
```

## � Features

- ⚡ FastAPI with async support
- 🗃️ PostgreSQL + SQLAlchemy 2.0
- 🔐 JWT Authentication
- 📝 Loguru logging
- 🐳 Docker multi-stage builds
- 🧪 Pytest with async
- 🔧 Alembic migrations
- 📊 Redis caching
- 🔄 Celery for background tasks
- 🎨 Code quality (Black, Ruff, MyPy)

## 📁 Project Structure

```
app/
├── main.py              # FastAPI app
├── config.py            # Settings
├── database.py          # DB setup
├── models/              # Database models
├── schemas/             # Pydantic schemas
├── api/v1/endpoints/    # API routes
├── core/                # Security, dependencies
├── services/            # Business logic
└── utils/               # Helpers

alembic/                 # Database migrations
tests/                   # Tests
docker-compose.yml       # Docker setup
Dockerfile              # Container config
```

## 🚀 Local Development (without Docker)

```powershell
# Install Poetry if needed
# https://python-poetry.org/docs/#installation

# Install dependencies
poetry install

# Copy environment file
Copy-Item .env.example .env

# Run the app
poetry run uvicorn app.main:app --reload
```

Visit http://localhost:8000/docs
- ReDoc Documentation: `http://localhost:8000/redoc`

#### Using Docker

```bash
# Build and run all services
docker-compose up -d

# View logs
docker-compose logs -f app

# Stop services
docker-compose down
```

### Database Migrations

```bash
# Create a new migration
alembic revision --autogenerate -m "Description of changes"

# Apply migrations
alembic upgrade head

# Rollback migration
alembic downgrade -1
```

## Development

### Code Quality

This project uses multiple tools to ensure code quality:

```bash
# Format code with Black
poetry run black app tests

# Lint with Ruff
poetry run ruff check app tests --fix

# Type check with MyPy
poetry run mypy app

# Run all pre-commit hooks
poetry run pre-commit run --all-files
```

### Testing

```bash
# Run all tests
poetry run pytest

# Run with coverage
poetry run pytest --cov=app --cov-report=html

# Run specific test file
## 🧪 Testing

```powershell
# Run all tests
docker-compose exec app pytest

# With coverage
docker-compose exec app pytest --cov=app

# Local (without Docker)
poetry run pytest
```

## 🔧 Development Tools

```powershell
# Format code
poetry run black .

# Lint
poetry run ruff check .

# Type check
poetry run mypy app

# Pre-commit hooks
poetry run pre-commit install
poetry run pre-commit run --all-files
```

## 📝 Environment Variables

Copy `.env.example` to `.env` and adjust:

```bash
# Database
DATABASE_URL=postgresql://postgres:postgres@localhost:5432/fastapi_db

# Security
SECRET_KEY=your-secret-key-change-in-production

# Redis
REDIS_URL=redis://localhost:6379/0
```

## 🏗️ Architecture

- **Clean Architecture** - Separation of concerns
- **SOLID Principles** - Maintainable, extensible code
- **Design Patterns** - Factory, Singleton, Dependency Injection
- **Type Safety** - Full type hints with MyPy
- **Async/Await** - Non-blocking I/O operations

## 📄 License

MIT License - see [LICENSE](LICENSE) file

## 🤝 Contributing

1. Fork it
2. Create feature branch (`git checkout -b feature/name`)
3. Commit changes (`git commit -am 'Add feature'`)
4. Push (`git push origin feature/name`)
5. Create Pull Request
