# Makefile

.PHONY: help setup install run dev test test-cov lint format clean migrate migration docker-up docker-down docker-logs

help:
	@echo "Available commands:"
	@echo "  setup          - Initial project setup"
	@echo "  install        - Install dependencies"
	@echo "  run            - Run the application"
	@echo "  dev            - Run with auto-reload"
	@echo "  test           - Run tests"
	@echo "  test-cov       - Run tests with coverage"
	@echo "  lint           - Run linters"
	@echo "  format         - Format code"
	@echo "  migrate        - Run migrations"
	@echo "  migration      - Create new migration"
	@echo "  docker-up      - Start docker services"
	@echo "  docker-down    - Stop docker services"
	@echo "  clean          - Remove cache and build files"

setup: install
	poetry run pre-commit install
	@if [ ! -f .env ]; then cp .env.example .env; echo "Created .env file"; fi

install:
	poetry install

run:
	poetry run python -m app.main

dev:
	poetry run uvicorn app.main:app --reload --host 0.0.0.0 --port 8000

test:
	poetry run pytest

test-cov:
	poetry run pytest --cov=app --cov-report=html --cov-report=term

lint:
	poetry run ruff check app tests
	poetry run mypy app

format:
	poetry run black app tests
	poetry run ruff check app tests --fix

migrate:
	poetry run alembic upgrade head

migration:
	@read -p "Migration message: " msg; \
	poetry run alembic revision --autogenerate -m "$$msg"


docker:
	docker compose build && docker compose up -d
	
docker:
	docker compose up -d

docker-down:
	docker compose down

docker-logs:
	docker compose logs -f

clean:
	find . -type d -name "__pycache__" -exec rm -rf {} + 2>/dev/null || true
	find . -type d -name "*.egg-info" -exec rm -rf {} + 2>/dev/null || true
	find . -type d -name ".pytest_cache" -exec rm -rf {} + 2>/dev/null || true
	find . -type d -name ".mypy_cache" -exec rm -rf {} + 2>/dev/null || true
	find . -type d -name ".ruff_cache" -exec rm -rf {} + 2>/dev/null || true
	rm -rf build/ dist/ htmlcov/ .coverage

