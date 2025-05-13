import re
import os
from uuid import uuid4
from langchain_community.chat_message_histories import SQLChatMessageHistory
from langchain_core.messages import HumanMessage

from app.config import llm, SYSTEM_PROMPT, vector_store_manager
from app.paths import ARTIFACTS_DIR


def delete_user_data(session_id):
    db_path = f"{ARTIFACTS_DIR}/chat_history.db"
    if os.path.exists(db_path):
        from sqlalchemy import create_engine, text

        engine = create_engine(f"sqlite:///{db_path}")
        with engine.connect() as conn:
            conn.execute(
                text("DELETE FROM message_store WHERE session_id = :sid"),
                {"sid": session_id},
            )
            conn.commit()
    vector_store_manager.delete_user_data(session_id)


def insert_data_to_vectorstore(text, session_id, k=4):
    vector_store_manager.insert_data(text, session_id=session_id, k=k)


def query_vectorstore(query, session_id, k=5):
    return vector_store_manager.query(query, session_id=session_id, k=k)


def answer_query(query, session_id=None):
    if session_id is None:
        session_id = str(uuid4())

    chat_message_history = SQLChatMessageHistory(
        session_id=session_id,
        connection_string=f"sqlite:///{ARTIFACTS_DIR}/chat_history.db",
    )
    history = chat_message_history.messages
    if not history:
        history = [SYSTEM_PROMPT]
        chat_message_history.add_messages([SYSTEM_PROMPT])

    docs = query_vectorstore(query, session_id=session_id)
    context = {i + 1: doc.page_content for i, doc in enumerate(docs)}
    prompt = HumanMessage(content=f"QUERY: {query}\n\nCONTEXT: {context}")
    response = llm.invoke(history + [prompt])
    chat_message_history.add_messages([prompt, response])

    used_indices = set(map(int, re.findall(r"\[(\d+)\]", response.text())))
    used_citations = {i: context[i] for i in sorted(used_indices) if i in context}
    citation_text = "\n".join(f"[{i}] {used_citations[i]}" for i in used_citations)

    return {
        "response": str(response.text() + "\n\nREFERENCES:\n\n" + citation_text),
        "session_id": session_id,
    }
