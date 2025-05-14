# 🧠 RAG Chatbot

A **Retrieval-Augmented Generation (RAG)** chatbot powered by:

- **FastAPI** for backend API
- **LangChain** + **HuggingFace** embeddings + **ChromaDB** for vector store
- **SQLite** for persistent chat history
- **Telegram bot** for conversational interface
- **Docker** & `Makefile` for production workflow
- **Pytest** for testing suite
- **Environment variables** for secure API key management

---

## 🚀 Features

- 🗨️ Conversational chat with session memory
- 🔍 Context-aware answers with source citations
- 📚 Per-user persistent chat history using SQLite
- 🧠 Vector search using multilingual sentence embeddings
- 🤖 Telegram bot integration
- 🧪 Comprehensive testing with `pytest`
- 🐳 Containerized deployment


## ⚙️ Environment Setup

1. **Clone the repo**

```bash
git clone https://github.com/myrkuur/rag-chatbot.git
cd rag-chatbot
````

2. **Create `.env` file**


Add your API keys:

```env
OPENAI_KEY=
OPENAI_MODEL_NAME=
EMBEDDING_MODEL_NAME=
FASTAPI_BASE_URL=
TELEGRAM_BOT_TOKEN=
```

3. **Install dependencies**

```bash
conda create -n rag-chatbot python=3.10 ipython
conda activate rag-chatbot
pip install -r app_requirements.txt
pip install -r bot_requirements.txt
```

---

## 🧪 Run Tests

```bash
make test
```

* Runs `pytest` with environment variables from `.env`
* Covers FastAPI endpoints

---

## 🚀 Run Locally

### FastAPI (Backend API)

```bash
make run-api
```

Runs at `http://localhost:8000`

### Telegram Bot

```bash
make run-bot
```

---

## 🐳 Docker Deployment

Build and run using Docker Compose:

```bash
make run-prod
```

This launches:

* FastAPI server
* Telegram bot worker
* Persistent Chroma vector store (in volume)

---

## 🧠 Workflow

1. User sends a message via Telegram
2. The bot sends it to the FastAPI backend
3. Backend retrieves relevant chunks via Chroma vector store
4. LLM generates a response using the context
5. Chat history and citations are saved by session
6. Response is sent back with source references

---

## 📡 API Endpoints

* `POST /ask` — Ask a question
  **Params:** `query`, `session_id` (optional)

* `POST /ingest` — Ingest content from a URL
  **Params:** `url`, `session_id`

* `GET /delete-user-data` — Delete session data
  **Params:** `session_id`

---

## ✅ Makefile Commands

```bash
make help
```

---

## 🔐 Security Notes

* `.env` keeps secrets out of code
* Each Telegram user operates in an isolated session (via chat ID)
* API key not exposed via public endpoints

---

## 🧰 Tech Stack

| Component     | Tool/Lib                      |
| ------------- | ----------------------------- |
| Backend API   | FastAPI                       |
| Embeddings    | HuggingFace `multilingual-e5` |
| Vector DB     | ChromaDB                      |
| LLM           | OpenAI via LangChain          |
| Bot Framework | python-telegram-bot           |
| Storage       | SQLite for chat history       |
| Testing       | Pytest + unittest.mock        |
| Deployment    | Docker + Compose              |



