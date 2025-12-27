# Contributing to FastAPI-Launchpad

First off, thank you for considering contributing to FastAPI-Launchpad! It's people like you that make FastAPI-Launchpad such a great template.

## Code of Conduct

This project and everyone participating in it is governed by our commitment to providing a welcoming and inspiring community for all. Please be respectful and constructive in your interactions.

## How Can I Contribute?

### Reporting Bugs

Before creating bug reports, please check the existing issues to avoid duplicates. When you create a bug report, include as many details as possible:

- **Use a clear and descriptive title**
- **Describe the exact steps to reproduce the problem**
- **Provide specific examples to demonstrate the steps**
- **Describe the behavior you observed and what you expected**
- **Include screenshots if relevant**
- **Include your environment details** (OS, Python version, etc.)

### Suggesting Enhancements

Enhancement suggestions are tracked as GitHub issues. When creating an enhancement suggestion, include:

- **Use a clear and descriptive title**
- **Provide a detailed description of the suggested enhancement**
- **Explain why this enhancement would be useful**
- **List any alternative solutions you've considered**

### Pull Requests

1. **Fork the repository** and create your branch from `main`:
   ```bash
   git checkout -b feature/your-feature-name
   ```

2. **Make your changes**:
   - Follow the existing code style
   - Write or update tests as needed
   - Update documentation if needed

3. **Ensure the test suite passes**:
   ```bash
   pytest
   ```

4. **Format your code**:
   ```bash
   black app tests
   ruff check app tests --fix
   ```

5. **Commit your changes** using a descriptive commit message:
   ```bash
   git commit -m "Add feature: description of your changes"
   ```

6. **Push to your fork**:
   ```bash
   git push origin feature/your-feature-name
   ```

7. **Open a Pull Request** against the `main` branch

## Development Setup

1. **Clone your fork**:
   ```bash
   git clone https://github.com/your-username/FastAPI-Launchpad.git
   cd FastAPI-Launchpad
   ```

2. **Set up the development environment**:
   ```bash
   python -m venv .venv
   source .venv/bin/activate  # On Windows: .venv\Scripts\activate
   pip install -r requirements-dev.txt
   ```

3. **Install pre-commit hooks**:
   ```bash
   pre-commit install
   ```

## Style Guidelines

### Python Style Guide

- Follow [PEP 8](https://www.python.org/dev/peps/pep-0008/)
- Use [Black](https://github.com/psf/black) for code formatting
- Use [Ruff](https://github.com/astral-sh/ruff) for linting
- Write docstrings for all public modules, functions, classes, and methods
- Use type hints where appropriate

### Git Commit Messages

- Use the present tense ("Add feature" not "Added feature")
- Use the imperative mood ("Move cursor to..." not "Moves cursor to...")
- Limit the first line to 72 characters or less
- Reference issues and pull requests liberally after the first line

### Testing

- Write tests for all new features
- Ensure all tests pass before submitting a PR
- Aim for high code coverage
- Use descriptive test names that explain what is being tested

## Project Structure

```
FastAPI-Launchpad/
├── app/              # Application code
├── tests/            # Test files
├── docs/             # Documentation
├── docker/           # Docker configurations
└── .github/          # GitHub Actions workflows
```

## Questions?

Feel free to open an issue or start a discussion if you have any questions!

## License

By contributing to FastAPI-Launchpad, you agree that your contributions will be licensed under the MIT License.

---

Thank you for contributing to FastAPI-Launchpad! 🚀
