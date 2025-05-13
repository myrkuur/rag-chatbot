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

---

## 📁 Project Structure

```
rag-chatbot/
├── app.py               # FastAPI app endpoints
├── bot.py               # Telegram bot logic
├── config.py            # Shared constants and session config
├── utils.py             # Core logic: retrieval, query, ingestion
├── paths.py             # File paths used across app
├── tests/               # Unit tests
├── Dockerfile           # API Dockerfile
├── bot.Dockerfile       # Telegram bot Dockerfile
├── docker-compose.yml   # Run both containers
├── Makefile             # Common dev commands
├── .env.example         # Template for environment variables
├── README.md            # Project documentation

````

---

## ⚙️ Environment Setup

1. **Clone the repo**

```bash
git clone https://github.com/yourusername/rag-chatbot.git
cd rag-chatbot
````

2. **Create `.env` file**

```bash
cp .env.example .env
```

Add your API keys:

```env
OPENAI_API_KEY=your-openai-key
TELEGRAM_BOT_TOKEN=your-telegram-bot-token
```

3. **Install dependencies**

```bash
make install
```

---

## 🧪 Run Tests

```bash
make test
```

* Runs `pytest` with environment variables from `.env`
* Covers FastAPI endpoints and Telegram bot logic

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
docker-compose up --build
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
  **Params:** `url`

* `GET /delete-everything` — Delete session data
  **Params:** `session_id`

---

## ✅ Makefile Commands

```bash
make install        # Install dependencies from requirements.txt
make test           # Run pytest
make run-api        # Launch FastAPI server
make run-bot        # Start Telegram bot
make env            # Create .env file from template
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

---

## 🙋 FAQ

**Q:** How do I ingest content?
**A:** Use `/ingest <URL>` in Telegram or call `/ingest?url=...` via API.

**Q:** How do I reset my data?
**A:** Use `/delete` in Telegram to wipe your session’s vector store and history.

