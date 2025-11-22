# FastAPI Production Template

A production-ready FastAPI template with best practices, design patterns, and enterprise-grade features.

## Features

- ⚡ **FastAPI** - Modern, fast web framework for building APIs
- 🗃️ **SQLAlchemy 2.0** - Async ORM with PostgreSQL support
- 🔐 **JWT Authentication** - Secure token-based authentication
- 📝 **Loguru** - Structured logging with rotation and retention
- 🐳 **Docker** - Multi-stage Dockerfile for optimized images
- 🧪 **Pytest** - Comprehensive testing setup with async support
- 🔧 **Alembic** - Database migrations
- 📊 **Redis** - Caching and session management
- 🔄 **Celery** - Background tasks and scheduled jobs
- 🎨 **Code Quality** - Black, Ruff, MyPy, and pre-commit hooks
- 🏗️ **Best Practices** - SOLID principles, design patterns, and clean architecture

## Project Structure

```
fastapi-production-template/
├── app/
│   ├── __init__.py
│   ├── main.py              # FastAPI application entry point
│   ├── config.py            # Configuration management
│   ├── database.py          # Database setup and sessions
│   ├── models/              # SQLAlchemy models
│   │   ├── __init__.py
│   │   └── base.py          # Base model with common fields
│   ├── schemas/             # Pydantic schemas
│   │   └── __init__.py
│   ├── api/                 # API endpoints
│   │   ├── __init__.py
│   │   └── v1/
│   │       ├── __init__.py
│   │       └── endpoints/
│   ├── core/                # Core functionality
│   │   ├── __init__.py
│   │   ├── security.py      # Security utilities
│   │   └── dependencies.py  # FastAPI dependencies
│   ├── services/            # Business logic
│   │   └── __init__.py
│   └── utils/               # Utility functions
│       ├── __init__.py
│       └── logger.py        # Logging setup
├── tests/                   # Test suite
│   ├── __init__.py
│   ├── conftest.py          # Pytest fixtures
│   └── api/
├── alembic/                 # Database migrations
│   └── versions/
├── docs/                    # Documentation
├── scripts/                 # Utility scripts
├── .env.example             # Environment variables example
├── .gitignore
├── .dockerignore
├── .pre-commit-config.yaml  # Pre-commit hooks
├── pyproject.toml           # Project dependencies and config
├── Dockerfile               # Multi-stage Docker build
├── docker-compose.yml       # Docker Compose configuration
└── README.md
```

## Quick Start

### Prerequisites

- Python 3.12+
- Poetry
- Docker and Docker Compose (optional)

### Installation

1. Clone the repository:
```bash
git clone https://github.com/anshuman-nanda/fastapi-production-template.git
cd fastapi-production-template
```

2. Install dependencies:
```bash
poetry install
```

3. Set up environment variables:
```bash
cp .env.example .env
# Edit .env with your configuration
```

4. Install pre-commit hooks:
```bash
poetry run pre-commit install
```

### Running the Application

#### Local Development

```bash
# Activate virtual environment
poetry shell

# Run the application
python -m app.main

# Or use uvicorn directly
uvicorn app.main:app --reload
```

The API will be available at `http://localhost:8000`.

- API Documentation: `http://localhost:8000/docs`
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
poetry run pytest tests/test_main.py

# Run tests in parallel
poetry run pytest -n auto
```

## Configuration

Configuration is managed through environment variables and the `app/config.py` file. All settings are validated using Pydantic.

### Key Configuration Sections

- **Application**: Basic app settings, version, environment
- **Server**: Host, port, workers configuration
- **Database**: PostgreSQL connection settings
- **Redis**: Redis connection and caching settings
- **Security**: JWT tokens, secrets, authentication
- **CORS**: Cross-origin resource sharing settings
- **Logging**: Log level, format, rotation, retention
- **Email**: SMTP configuration for email sending
- **Celery**: Background task processing
- **Rate Limiting**: API rate limiting configuration
- **Monitoring**: Sentry and other monitoring tools

## Architecture

This project follows clean architecture principles and implements several design patterns:

### SOLID Principles

- **Single Responsibility**: Each module has one clear purpose
- **Open/Closed**: Extensible through configuration and inheritance
- **Liskov Substitution**: Proper use of abstractions and interfaces
- **Interface Segregation**: Focused, minimal interfaces
- **Dependency Inversion**: Depends on abstractions, not concretions

### Design Patterns Used

- **Factory Pattern**: Application creation in `main.py`
- **Singleton Pattern**: Settings with LRU cache
- **Dependency Injection**: FastAPI dependencies
- **Repository Pattern**: Data access abstraction
- **Composite Pattern**: Settings aggregation
- **Chain of Responsibility**: Middleware pipeline
- **Strategy Pattern**: Interchangeable algorithms
- **Template Method**: Base models and classes

### Code Quality Standards

- **Cyclomatic Complexity**: Kept below 10 for all functions
- **Type Hints**: Comprehensive type annotations
- **Documentation**: Docstrings for all public interfaces
- **Error Handling**: Comprehensive exception handling
- **Testing**: High test coverage with unit and integration tests

## Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- FastAPI for the amazing framework
- SQLAlchemy for the powerful ORM
- All the open-source contributors

## Support

For support, email anshuman@example.com or open an issue on GitHub.
