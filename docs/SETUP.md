# Project Setup Guide

This document provides a comprehensive guide for setting up and working with the FastAPI Production Template.

## Architecture Overview

### Design Principles

This project follows enterprise-grade software engineering principles:

1. **SOLID Principles**
   - **Single Responsibility**: Each module has one clear purpose
   - **Open/Closed**: Extensible through configuration and inheritance
   - **Liskov Substitution**: Proper use of abstractions
   - **Interface Segregation**: Focused, minimal interfaces
   - **Dependency Inversion**: Depends on abstractions

2. **Design Patterns**
   - **Factory Pattern**: Application creation (`create_application()`)
   - **Singleton Pattern**: Settings with LRU cache
   - **Dependency Injection**: FastAPI dependencies
   - **Composite Pattern**: Settings aggregation
   - **Chain of Responsibility**: Middleware pipeline

3. **Code Quality Standards**
   - Cyclomatic complexity kept below 10
   - Comprehensive type hints
   - Docstrings for all public interfaces
   - High test coverage

## Project Structure

```
fastapi-production-template/
├── app/                        # Application source code
│   ├── api/                   # API layer
│   │   └── v1/               # API version 1
│   │       └── endpoints/    # Route handlers
│   ├── core/                 # Core functionality
│   │   ├── dependencies.py  # FastAPI dependencies
│   │   └── security.py      # Security utilities
│   ├── models/              # Database models
│   │   └── base.py          # Base model with common fields
│   ├── schemas/             # Pydantic schemas (DTOs)
│   │   └── common.py        # Common request/response schemas
│   ├── services/            # Business logic layer
│   ├── utils/               # Utility functions
│   │   └── logger.py        # Logging configuration
│   ├── config.py            # Configuration management
│   ├── database.py          # Database setup
│   └── main.py              # Application entry point
├── tests/                   # Test suite
│   ├── api/                # API tests
│   ├── conftest.py         # Pytest fixtures
│   └── test_*.py           # Test modules
├── alembic/                # Database migrations
│   ├── versions/           # Migration files
│   └── env.py              # Alembic configuration
├── docs/                   # Documentation
├── scripts/                # Utility scripts
│   └── dev.sh              # Development helper script
├── .env.example            # Environment variables template
├── .gitignore              # Git ignore rules
├── .dockerignore           # Docker ignore rules
├── .pre-commit-config.yaml # Pre-commit hooks
├── pyproject.toml          # Python project configuration
├── alembic.ini             # Alembic configuration
├── Dockerfile              # Docker image definition
├── docker-compose.yml      # Docker services
└── README.md               # Project overview
```

## Configuration Management

### Environment Variables

Configuration is managed through environment variables, defined in `.env.example`:

- **Application**: Basic app settings, version, environment
- **Server**: Host, port, workers configuration
- **Database**: PostgreSQL connection settings
- **Redis**: Redis connection and caching
- **Security**: JWT tokens, secrets, authentication
- **CORS**: Cross-origin resource sharing
- **Logging**: Log level, format, rotation, retention
- **Email**: SMTP configuration
- **Celery**: Background task processing
- **Rate Limiting**: API rate limiting
- **Monitoring**: Sentry and monitoring tools

### Configuration Classes

Configuration is organized into focused classes using Pydantic Settings:

```python
# app/config.py
class Settings:
    app: AppSettings
    server: ServerSettings
    database: DatabaseSettings
    redis: RedisSettings
    security: SecuritySettings
    # ... and more
```

This follows the **Composite Pattern** to organize related settings.

## Database Layer

### Architecture

- **ORM**: SQLAlchemy 2.0 with async support
- **Migrations**: Alembic for version control
- **Session Management**: Dependency injection pattern
- **Base Models**: DRY principle with common fields

### Database Models

All models inherit from `BaseModel` which provides:
- Automatic timestamps (`created_at`, `updated_at`)
- Common utility methods (`to_dict()`, `__repr__()`)

```python
from app.models.base import BaseModel

class User(Base, BaseModel):
    __tablename__ = "users"
    # model fields...
```

## Security

### Authentication

- **JWT Tokens**: Access and refresh tokens
- **Password Hashing**: bcrypt via passlib
- **Token Expiration**: Configurable expiration times

### Best Practices

- Secrets stored in environment variables
- Password hashing with bcrypt (12 rounds)
- JWT with configurable algorithms
- Token validation and expiration

## Logging

Structured logging with **Loguru**:

- Console output with colors and formatting
- File output with rotation and compression
- Separate error log file
- Thread-safe logging
- Automatic log cleanup

## Testing

### Test Structure

- **Unit Tests**: Test individual components
- **Integration Tests**: Test component interactions
- **Fixtures**: Reusable test setup in `conftest.py`
- **Coverage**: Aim for >80% coverage

### Running Tests

```bash
# Run all tests
pytest

# Run with coverage
pytest --cov=app

# Run specific test
pytest tests/test_main.py
```

## Docker

### Multi-Stage Build

The Dockerfile uses a multi-stage build for optimization:

1. **Builder Stage**: Install dependencies
2. **Runtime Stage**: Minimal production image

### Services

Docker Compose includes:
- **postgres**: PostgreSQL database
- **redis**: Redis cache
- **app**: FastAPI application
- **celery_worker**: Background task worker (optional)
- **celery_beat**: Scheduled tasks (optional)

## Development Workflow

### Initial Setup

```bash
# Install dependencies
poetry install

# Setup pre-commit hooks
poetry run pre-commit install

# Copy environment file
cp .env.example .env
```

### Running Locally

```bash
# Activate virtual environment
poetry shell

# Run application
python -m app.main

# Or use uvicorn
uvicorn app.main:app --reload
```

### Using Helper Script

```bash
# Setup environment
./scripts/dev.sh setup

# Run application
./scripts/dev.sh run

# Run tests
./scripts/dev.sh test

# Lint code
./scripts/dev.sh lint

# Format code
./scripts/dev.sh format
```

### Code Quality

```bash
# Format with Black
poetry run black app tests

# Lint with Ruff
poetry run ruff check app tests --fix

# Type check with MyPy
poetry run mypy app

# Run all checks
poetry run pre-commit run --all-files
```

## API Development

### Adding New Endpoints

1. Create endpoint in `app/api/v1/endpoints/`
2. Define Pydantic schemas in `app/schemas/`
3. Implement business logic in `app/services/`
4. Add tests in `tests/api/`

### Example Structure

```python
# app/api/v1/endpoints/users.py
from fastapi import APIRouter, Depends
from app.schemas.user import UserCreate, UserResponse
from app.services.user import UserService

router = APIRouter()

@router.post("/", response_model=UserResponse)
async def create_user(
    user: UserCreate,
    service: UserService = Depends()
):
    return await service.create_user(user)
```

## Database Migrations

### Creating Migrations

```bash
# Generate migration from models
alembic revision --autogenerate -m "Add users table"

# Apply migrations
alembic upgrade head

# Rollback one migration
alembic downgrade -1

# View migration history
alembic history
```

## Deployment

### Production Checklist

- [ ] Set `ENVIRONMENT=production`
- [ ] Set `DEBUG=False`
- [ ] Use strong `SECRET_KEY`
- [ ] Configure proper `DATABASE_URL`
- [ ] Set up `REDIS_URL`
- [ ] Configure `CORS_ORIGINS`
- [ ] Set up monitoring (Sentry)
- [ ] Enable HTTPS
- [ ] Configure backups
- [ ] Set up log aggregation

### Docker Deployment

```bash
# Build images
docker-compose build

# Start services
docker-compose up -d

# View logs
docker-compose logs -f app

# Stop services
docker-compose down
```

## Monitoring and Logging

### Application Logs

Logs are stored in:
- `logs/app.log`: All logs
- `logs/error.log`: Error logs only

### Log Rotation

- **Size**: 100 MB per file
- **Retention**: 30 days
- **Compression**: ZIP format

## Best Practices

### Code Organization

1. **Separation of Concerns**: Keep API, business logic, and data access separate
2. **DRY Principle**: Extract common logic into utilities
3. **Type Hints**: Use comprehensive type annotations
4. **Documentation**: Add docstrings to public interfaces

### Error Handling

1. **Fail Fast**: Detect errors early
2. **Meaningful Messages**: Provide clear error messages
3. **Logging**: Log errors with context
4. **Recovery**: Implement graceful degradation

### Testing

1. **Test Coverage**: Aim for >80% coverage
2. **Test Types**: Mix unit, integration, and e2e tests
3. **Fixtures**: Use fixtures for common setup
4. **Mocking**: Mock external dependencies

### Security

1. **Input Validation**: Validate all inputs
2. **Authentication**: Require authentication for protected routes
3. **Authorization**: Check user permissions
4. **Secrets**: Never commit secrets to version control
5. **Dependencies**: Keep dependencies updated

## Troubleshooting

### Common Issues

1. **Database Connection Failed**
   - Check `DATABASE_URL` in `.env`
   - Ensure PostgreSQL is running
   - Verify network connectivity

2. **Import Errors**
   - Ensure virtual environment is activated
   - Install dependencies: `poetry install`
   - Check Python version (3.12+)

3. **Tests Failing**
   - Run tests in isolation: `pytest tests/test_file.py`
   - Check test database configuration
   - Verify fixtures are set up correctly

4. **Docker Issues**
   - Rebuild images: `docker-compose build --no-cache`
   - Check logs: `docker-compose logs`
   - Verify port availability

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make changes following the code standards
4. Add tests for new functionality
5. Ensure all tests pass
6. Submit a pull request

## Resources

- [FastAPI Documentation](https://fastapi.tiangolo.com/)
- [SQLAlchemy Documentation](https://docs.sqlalchemy.org/)
- [Pydantic Documentation](https://docs.pydantic.dev/)
- [Alembic Documentation](https://alembic.sqlalchemy.org/)
- [Docker Documentation](https://docs.docker.com/)

## License

This project is licensed under the MIT License - see the LICENSE file for details.
