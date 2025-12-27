# FastAPI-Launchpad 🚀

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.8+](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.100+-green.svg)](https://fastapi.tiangolo.com)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

**A production-ready FastAPI template to launch your API projects in minutes, not hours.**

FastAPI-Launchpad is a modern, batteries-included template for building production-grade APIs with FastAPI. Skip the boilerplate and focus on building features that matter.

## ✨ Features

- 🚀 **Production-Ready**: Pre-configured for deployment with Docker, logging, and monitoring
- 🔒 **Security First**: Built-in authentication, CORS, rate limiting, and security headers
- 📊 **Observability**: Structured logging, metrics, and health checks out of the box
- 🧪 **Testing Ready**: Pre-configured pytest setup with coverage reporting
- 📝 **API Documentation**: Auto-generated OpenAPI docs with FastAPI
- 🔄 **CI/CD Ready**: GitHub Actions workflows for testing and deployment
- 🎨 **Code Quality**: Pre-commit hooks, linting with Ruff, and formatting with Black
- 🐳 **Docker Support**: Optimized Dockerfile and docker-compose setup
- 🌍 **Database Ready**: SQLAlchemy integration with Alembic migrations
- ⚡ **Async Support**: Built for high-performance async operations

## 🚀 Quick Start

### Prerequisites

- Python 3.8 or higher
- pip or uv (recommended)

### Installation

1. **Use this template** by clicking the "Use this template" button above, or clone it:

```bash
git clone https://github.com/anshuman-nanda/FastAPI-Launchpad.git
cd FastAPI-Launchpad
```

2. **Set up your environment**:

```bash
# Using uv (recommended)
uv venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
uv pip install -r requirements.txt

# Or using pip
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

3. **Run the development server**:

```bash
uvicorn app.main:app --reload
```

4. **Access your API**:
   - API: http://localhost:8000
   - Interactive docs: http://localhost:8000/docs
   - Alternative docs: http://localhost:8000/redoc

## 📁 Project Structure

```
FastAPI-Launchpad/
├── app/
│   ├── __init__.py
│   ├── main.py           # Application entry point
│   ├── config.py         # Configuration management
│   ├── api/              # API routes
│   ├── models/           # Database models
│   ├── schemas/          # Pydantic schemas
│   ├── services/         # Business logic
│   └── utils/            # Utility functions
├── tests/                # Test suite
├── docs/                 # Documentation
├── docker/               # Docker configurations
├── .github/              # GitHub Actions workflows
└── scripts/              # Utility scripts
```

## 🧪 Testing

Run the test suite:

```bash
pytest
```

With coverage:

```bash
pytest --cov=app --cov-report=html
```

## 🐳 Docker Deployment

Build and run with Docker:

```bash
docker build -t fastapi-launchpad .
docker run -p 8000:8000 fastapi-launchpad
```

Or use docker-compose:

```bash
docker-compose up
```

## 🔧 Configuration

Configuration is managed through environment variables. Create a `.env` file:

```env
APP_NAME=FastAPI-Launchpad
DEBUG=False
API_VERSION=v1
DATABASE_URL=postgresql://user:pass@localhost/db
SECRET_KEY=your-secret-key-here
```

## 📚 Documentation

For detailed documentation, see the [docs/](./docs/) directory:

- [Getting Started](./docs/getting-started.md)
- [Configuration Guide](./docs/configuration.md)
- [Deployment Guide](./docs/deployment.md)
- [Contributing](./CONTRIBUTING.md)

## 🤝 Contributing

Contributions are welcome! Please read our [Contributing Guide](./CONTRIBUTING.md) for details on our code of conduct and the process for submitting pull requests.

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](./LICENSE) file for details.

## 🌟 Acknowledgments

Built with:
- [FastAPI](https://fastapi.tiangolo.com/) - Modern, fast web framework
- [Pydantic](https://pydantic-docs.helpmanual.io/) - Data validation
- [SQLAlchemy](https://www.sqlalchemy.org/) - Database ORM
- [Uvicorn](https://www.uvicorn.org/) - ASGI server

## 📧 Support

- 📫 [Open an issue](https://github.com/anshuman-nanda/FastAPI-Launchpad/issues)
- 💬 [Start a discussion](https://github.com/anshuman-nanda/FastAPI-Launchpad/discussions)

---

Made with ❤️ by the FastAPI community
