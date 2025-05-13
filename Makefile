# === Variables ===
PYTHON := python3
PIP := pip
APP_MODULE := app:app
BOT_MODULE := bot.py

# === Targets ===

## Install all dependencies
install:
	$(PIP) install --upgrade pip
	$(PIP) install -r requirements.txt
	$(PIP) install pytest pytest-asyncio httpx python-dotenv

## Run tests with pytest
test:
	PYTHONPATH=. pytest
	pytest tests/

## Run FastAPI app
run-api:
	uvicorn $(APP_MODULE) --reload --host 0.0.0.0 --port 8000

## Run Telegram bot
run-bot:
	$(PYTHON) $(BOT_MODULE)

## Create .env file if not exists
env:
	@test -f .env || cp .env.example .env && echo ".env created"

## Clean up __pycache__ and .pyc files
clean:
	find . -type d -name "__pycache__" -exec rm -r {} +
	find . -type f -name "*.pyc" -delete

## Show all commands
help:
	@echo "Makefile commands:"
	@echo "  install     - Install all dependencies"
	@echo "  test        - Run pytest test suite"
	@echo "  run-api     - Run FastAPI app"
	@echo "  run-bot     - Run Telegram bot"
	@echo "  env         - Create .env from .env.example if not exists"
	@echo "  clean       - Remove __pycache__ and .pyc files"
