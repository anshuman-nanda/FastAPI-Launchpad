# Getting Started with FastAPI-Launchpad

This guide will walk you through setting up FastAPI-Launchpad and creating your first API endpoint.

## Prerequisites

Before you begin, ensure you have the following installed:

- **Python 3.8 or higher**: [Download Python](https://www.python.org/downloads/)
- **pip** (Python package manager): Usually comes with Python
- **Git**: [Download Git](https://git-scm.com/downloads)
- **Optional**: [Docker](https://www.docker.com/get-started) for containerized deployment

## Installation

### Step 1: Get the Template

You have two options:

**Option A: Use as a GitHub Template**
1. Click the "Use this template" button at the top of the GitHub repository
2. Create a new repository from the template
3. Clone your new repository:
   ```bash
   git clone https://github.com/your-username/your-project-name.git
   cd your-project-name
   ```

**Option B: Clone Directly**
```bash
git clone https://github.com/anshuman-nanda/FastAPI-Launchpad.git
cd FastAPI-Launchpad
```

### Step 2: Set Up Virtual Environment

Create and activate a virtual environment:

```bash
# Using venv (built-in)
python -m venv .venv

# Activate on macOS/Linux
source .venv/bin/activate

# Activate on Windows
.venv\Scripts\activate
```

**Using uv (recommended for faster installation)**:
```bash
# Install uv if you haven't
pip install uv

# Create and activate virtual environment
uv venv
source .venv/bin/activate  # or .venv\Scripts\activate on Windows
```

### Step 3: Install Dependencies

```bash
# Using pip
pip install -r requirements.txt

# Using uv (faster)
uv pip install -r requirements.txt
```

For development (includes testing and linting tools):
```bash
pip install -r requirements-dev.txt
```

### Step 4: Configure Environment Variables

Create a `.env` file in the project root:

```bash
cp .env.example .env  # If .env.example exists
# or create a new .env file
```

Edit `.env` with your configuration:
```env
# Application
APP_NAME=FastAPI-Launchpad
DEBUG=True
API_VERSION=v1
ENVIRONMENT=development

# Server
HOST=0.0.0.0
PORT=8000

# Security
SECRET_KEY=your-secret-key-change-this-in-production
ALLOWED_ORIGINS=http://localhost:3000,http://localhost:8000

# Database (if using)
DATABASE_URL=sqlite:///./app.db
# For PostgreSQL: postgresql://user:password@localhost/dbname

# Logging
LOG_LEVEL=INFO
```

### Step 5: Run the Application

Start the development server:

```bash
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
```

The `--reload` flag enables auto-reloading when you make code changes.

### Step 6: Verify Installation

Open your browser and navigate to:

- **API Root**: http://localhost:8000
- **Interactive API Docs**: http://localhost:8000/docs
- **Alternative Docs**: http://localhost:8000/redoc
- **Health Check**: http://localhost:8000/health

You should see the API documentation and be able to test endpoints interactively.

## Creating Your First Endpoint

### 1. Create a New Route Module

Create a new file `app/api/v1/endpoints/hello.py`:

```python
from fastapi import APIRouter

router = APIRouter()

@router.get("/hello")
async def hello_world():
    """
    Simple hello world endpoint.
    """
    return {"message": "Hello from FastAPI-Launchpad!"}

@router.get("/hello/{name}")
async def hello_name(name: str):
    """
    Personalized hello endpoint.
    """
    return {"message": f"Hello, {name}!"}
```

### 2. Register the Router

Update `app/api/v1/__init__.py` to include your new router:

```python
from fastapi import APIRouter
from app.api.v1.endpoints import hello

api_router = APIRouter()
api_router.include_router(hello.router, prefix="/hello", tags=["hello"])
```

### 3. Test Your Endpoint

Visit http://localhost:8000/docs and you'll see your new endpoints in the API documentation.

Try them out:
- `GET /api/v1/hello`
- `GET /api/v1/hello/YourName`

## Next Steps

Now that you have FastAPI-Launchpad running, you can:

1. **Add Database Models**: Learn about [database integration](./database.md)
2. **Implement Authentication**: Set up [authentication and authorization](./authentication.md)
3. **Write Tests**: Create [tests for your endpoints](./testing.md)
4. **Deploy Your API**: Follow the [deployment guide](./deployment.md)
5. **Configure CI/CD**: Set up [continuous integration](./ci-cd.md)

## Common Issues

### Port Already in Use

If port 8000 is already in use, specify a different port:
```bash
uvicorn app.main:app --reload --port 8001
```

### Import Errors

Make sure you're in the project root directory and your virtual environment is activated:
```bash
cd /path/to/FastAPI-Launchpad
source .venv/bin/activate  # or .venv\Scripts\activate on Windows
```

### Python Version Issues

Check your Python version:
```bash
python --version  # Should be 3.8 or higher
```

If you have multiple Python versions, use:
```bash
python3.11 -m venv .venv  # Replace with your Python version
```

## Getting Help

- 📚 Check the full [documentation](./index.md)
- 🐛 [Report issues](https://github.com/anshuman-nanda/FastAPI-Launchpad/issues)
- 💬 [Join discussions](https://github.com/anshuman-nanda/FastAPI-Launchpad/discussions)

---

Ready to build something amazing? Let's go! 🚀
