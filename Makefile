# === Variables ===
PYTHON := python3
PIP := pip
APP_MODULE := app:app
BOT_MODULE := bot.py

## Run tests with pytest
test:
	PYTHONPATH=. pytest
	pytest tests/

## Run FastAPI app
run-api:
	uvicorn $(APP_MODULE) --reload --host 0.0.0.0 --port 8000 --env-file .env

## Run Telegram bot
run-bot:
	$(PYTHON) $(BOT_MODULE)

run-prod:
	docker compose up --build -d

## Show all commands
help:
	@echo "Makefile commands:"
	@echo "  test        - Run pytest test suite"
	@echo "  run-api     - Run FastAPI app"
	@echo "  run-bot     - Run Telegram bot"
	@echo "  run-prod     - Run production docker"
