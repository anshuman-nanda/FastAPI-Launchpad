# Contributing Guidelines

Thank you for considering contributing to the FastAPI Production Template! This document provides guidelines and best practices for contributing.

## Code of Conduct

- Be respectful and inclusive
- Focus on constructive feedback
- Help others learn and grow
- Follow the project's coding standards

## Getting Started

### Prerequisites

- Python 3.12+
- Poetry
- Git
- Docker (optional)

### Setup Development Environment

1. Fork the repository
2. Clone your fork:
   ```bash
   git clone https://github.com/YOUR_USERNAME/fastapi-production-template.git
   cd fastapi-production-template
   ```

3. Install dependencies:
   ```bash
   poetry install
   poetry run pre-commit install
   ```

4. Create environment file:
   ```bash
   cp .env.example .env
   ```

## Development Workflow

### Creating a Feature Branch

```bash
git checkout -b feature/your-feature-name
```

Branch naming conventions:
- `feature/` - New features
- `bugfix/` - Bug fixes
- `docs/` - Documentation updates
- `refactor/` - Code refactoring
- `test/` - Test additions or updates

### Making Changes

1. Write code following the project's standards
2. Add tests for new functionality
3. Update documentation as needed
4. Run quality checks before committing

### Code Quality Checks

```bash
# Format code
poetry run black app tests

# Lint code
poetry run ruff check app tests --fix

# Type check
poetry run mypy app

# Run all pre-commit hooks
poetry run pre-commit run --all-files

# Run tests
poetry run pytest
```

### Commit Messages

Follow the conventional commits format:

```
type(scope): subject

body (optional)

footer (optional)
```

Types:
- `feat`: New feature
- `fix`: Bug fix
- `docs`: Documentation changes
- `style`: Code style changes (formatting, etc.)
- `refactor`: Code refactoring
- `test`: Test additions or updates
- `chore`: Maintenance tasks

Examples:
```
feat(api): add user registration endpoint

fix(security): resolve JWT token validation issue

docs(readme): update installation instructions
```

## Coding Standards

### Python Style Guide

Follow PEP 8 with these specifications:

- Line length: 100 characters
- Use type hints for all functions
- Use docstrings for all public modules, classes, and functions

### Code Organization

```python
"""
Module docstring describing the module's purpose.
"""

# Standard library imports
import sys
from datetime import datetime

# Third-party imports
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

# Local application imports
from app.config import settings
from app.models.user import User
```

### Function Documentation

```python
def create_user(username: str, email: str) -> User:
    """
    Create a new user.

    Args:
        username: The user's username
        email: The user's email address

    Returns:
        The created user object

    Raises:
        ValueError: If username or email is invalid
    """
    # Implementation
```

### Complexity Guidelines

- Keep cyclomatic complexity below 10
- Break down complex functions into smaller ones
- Use early returns to reduce nesting
- Extract conditional logic into well-named functions

Example:
```python
# Bad - Complex function
def process_user(user_data: dict) -> dict:
    if user_data:
        if "email" in user_data:
            if validate_email(user_data["email"]):
                if user_data.get("age", 0) >= 18:
                    # ... complex logic
                    pass

# Good - Refactored
def process_user(user_data: dict) -> dict:
    """Process user data with validation."""
    if not user_data:
        raise ValueError("User data is required")
    
    validate_user_data(user_data)
    return create_user_record(user_data)

def validate_user_data(data: dict) -> None:
    """Validate user data."""
    if "email" not in data:
        raise ValueError("Email is required")
    
    if not validate_email(data["email"]):
        raise ValueError("Invalid email")
    
    if data.get("age", 0) < 18:
        raise ValueError("User must be 18 or older")
```

## Testing

### Writing Tests

- Write tests for all new functionality
- Aim for >80% code coverage
- Use descriptive test names
- Follow AAA pattern: Arrange, Act, Assert

Example:
```python
def test_create_user_success():
    """Test successful user creation."""
    # Arrange
    user_data = {"username": "testuser", "email": "test@example.com"}
    
    # Act
    user = create_user(**user_data)
    
    # Assert
    assert user.username == "testuser"
    assert user.email == "test@example.com"
    assert user.id is not None
```

### Test Organization

```
tests/
├── conftest.py              # Shared fixtures
├── test_main.py             # Application tests
├── api/
│   └── test_users.py        # API endpoint tests
├── services/
│   └── test_user_service.py # Service layer tests
└── models/
    └── test_user.py         # Model tests
```

### Running Tests

```bash
# Run all tests
poetry run pytest

# Run specific test file
poetry run pytest tests/test_main.py

# Run with coverage
poetry run pytest --cov=app --cov-report=html

# Run tests matching a pattern
poetry run pytest -k "test_user"
```

## Design Patterns

When implementing features, consider using appropriate design patterns:

### Creational Patterns

- **Factory Method**: Creating objects without specifying classes
- **Singleton**: Ensuring single instance (use sparingly)
- **Builder**: Constructing complex objects step by step

### Structural Patterns

- **Adapter**: Converting interfaces
- **Decorator**: Adding responsibilities dynamically
- **Facade**: Simplifying complex subsystems

### Behavioral Patterns

- **Strategy**: Interchangeable algorithms
- **Observer**: One-to-many dependencies
- **Template Method**: Defining algorithm skeletons

## API Development

### Adding New Endpoints

1. Create endpoint file in `app/api/v1/endpoints/`
2. Define schemas in `app/schemas/`
3. Implement service logic in `app/services/`
4. Add database models if needed in `app/models/`
5. Write tests in `tests/api/`
6. Update documentation

Example:
```python
# app/api/v1/endpoints/users.py
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.dependencies import get_db
from app.schemas.user import UserCreate, UserResponse
from app.services.user import UserService

router = APIRouter(prefix="/users", tags=["users"])

@router.post("/", response_model=UserResponse, status_code=status.HTTP_201_CREATED)
async def create_user(
    user_in: UserCreate,
    db: AsyncSession = Depends(get_db),
) -> UserResponse:
    """Create a new user."""
    service = UserService(db)
    user = await service.create_user(user_in)
    return UserResponse.from_orm(user)
```

## Database Changes

### Creating Migrations

```bash
# Create a new migration
alembic revision --autogenerate -m "Add users table"

# Review the generated migration
# Edit if necessary

# Apply migration
alembic upgrade head
```

### Migration Best Practices

- Review auto-generated migrations
- Test migrations in development first
- Include both upgrade and downgrade
- Make migrations idempotent when possible
- Document complex migrations

## Documentation

### Code Documentation

- Add docstrings to all public modules, classes, and functions
- Use Google or NumPy docstring format
- Include examples in docstrings for complex functions
- Keep documentation up to date with code changes

### Project Documentation

Update these files when relevant:
- `README.md`: Project overview and quick start
- `docs/SETUP.md`: Detailed setup and architecture
- `docs/API.md`: API documentation (if needed)
- `CHANGELOG.md`: Document changes in each version

## Pull Request Process

1. **Update Your Branch**
   ```bash
   git checkout main
   git pull upstream main
   git checkout your-feature-branch
   git rebase main
   ```

2. **Run Quality Checks**
   ```bash
   poetry run pre-commit run --all-files
   poetry run pytest
   ```

3. **Push Your Changes**
   ```bash
   git push origin your-feature-branch
   ```

4. **Create Pull Request**
   - Use a clear, descriptive title
   - Describe what changes you made and why
   - Reference any related issues
   - Include screenshots for UI changes
   - Ensure all CI checks pass

5. **Code Review**
   - Address review comments
   - Make requested changes
   - Push updates to the same branch

6. **Merge**
   - Wait for approval from maintainers
   - Squash commits if requested
   - Delete branch after merge

## Pull Request Template

```markdown
## Description
Brief description of changes

## Type of Change
- [ ] Bug fix
- [ ] New feature
- [ ] Breaking change
- [ ] Documentation update

## Testing
- [ ] Tests added/updated
- [ ] All tests passing
- [ ] Manual testing completed

## Checklist
- [ ] Code follows style guidelines
- [ ] Self-review completed
- [ ] Documentation updated
- [ ] No new warnings
- [ ] Tests cover changes
```

## Review Process

### For Contributors

- Be open to feedback
- Ask questions if unclear
- Make changes promptly
- Be patient with the review process

### For Reviewers

- Be constructive and respectful
- Explain reasoning for suggestions
- Acknowledge good work
- Focus on code quality and standards

## Questions?

If you have questions:
1. Check existing documentation
2. Search existing issues
3. Create a new issue with the question label
4. Join our community chat (if available)

## License

By contributing, you agree that your contributions will be licensed under the MIT License.

## Thank You!

Your contributions make this project better for everyone. Thank you for taking the time to contribute! 🎉
