import requests
from bs4 import BeautifulSoup

from fastapi import FastAPI
from app import utils

app = FastAPI(
    title="RAG ChatBot",
    description=(
        "Ingest text from CTXT.io shares, store them in a vector database, "
        "and query via chat interfaces. "
        "Use the `/ingest` endpoint to push new documents, `/ask` to query, "
        "and `/delete-user-data` to clean up session data."
    ),
    version="1.0.0",
    swagger_ui_parameters={
        "docExpansion": "none",  # Collapse all sections initially
        "defaultModelsExpandDepth": -1,  # Hide schema models by default
        "syntaxHighlight": True,  # Enable syntax highlighting
        "syntaxHighlight.theme": "obsidian",  # Use a dark theme for code samples
    },
)


@app.get("/delete-user-data")
async def clean_up(session_id: str):
    utils.delete_user_data(session_id=session_id)
    return {"result": "SUCCESS", "session_id": session_id}


@app.post("/ingest")
async def save_doc_to_vector_db(url: str, session_id: str):
    text = BeautifulSoup(requests.get(url).content).find("p").get_text()
    utils.insert_data_to_vectorstore(text, session_id=session_id)
    return {"result": "SUCCESS", "session_id": session_id}


@app.post("/ask")
async def chat(query: str, session_id: str = None):
    return utils.answer_query(query, session_id)
