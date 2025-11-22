#!/bin/bash
# Development utility script

set -e

case "$1" in
  setup)
    echo "Setting up development environment..."
    poetry install
    poetry run pre-commit install
    cp .env.example .env
    echo "Setup complete! Edit .env with your configuration."
    ;;
  
  run)
    echo "Starting application..."
    poetry run python -m app.main
    ;;
  
  test)
    echo "Running tests..."
    poetry run pytest "${@:2}"
    ;;
  
  lint)
    echo "Running linters..."
    poetry run black app tests
    poetry run ruff check app tests --fix
    poetry run mypy app
    ;;
  
  format)
    echo "Formatting code..."
    poetry run black app tests
    ;;
  
  migrate)
    echo "Running database migrations..."
    poetry run alembic upgrade head
    ;;
  
  makemigrations)
    echo "Creating new migration..."
    poetry run alembic revision --autogenerate -m "${2:-Auto-generated migration}"
    ;;
  
  docker-build)
    echo "Building Docker images..."
    docker-compose build
    ;;
  
  docker-up)
    echo "Starting Docker services..."
    docker-compose up -d
    ;;
  
  docker-down)
    echo "Stopping Docker services..."
    docker-compose down
    ;;
  
  docker-logs)
    echo "Showing Docker logs..."
    docker-compose logs -f "${2:-app}"
    ;;
  
  *)
    echo "Usage: $0 {setup|run|test|lint|format|migrate|makemigrations|docker-build|docker-up|docker-down|docker-logs}"
    echo ""
    echo "Commands:"
    echo "  setup           - Set up development environment"
    echo "  run             - Start the application"
    echo "  test [args]     - Run tests with optional pytest arguments"
    echo "  lint            - Run all linters and formatters"
    echo "  format          - Format code with black"
    echo "  migrate         - Run database migrations"
    echo "  makemigrations  - Create new migration"
    echo "  docker-build    - Build Docker images"
    echo "  docker-up       - Start Docker services"
    echo "  docker-down     - Stop Docker services"
    echo "  docker-logs     - Show Docker logs"
    exit 1
    ;;
esac
