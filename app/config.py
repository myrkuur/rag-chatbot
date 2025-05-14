import os

from langchain.globals import set_llm_cache
from langchain_openai import ChatOpenAI
from langchain_community.cache import InMemoryCache
from langchain_core.messages import SystemMessage

from app.db import VectorStoreManager


vector_store_manager = VectorStoreManager()

llm = ChatOpenAI(model=os.getenv("OPENAI_MODEL_NAME"), api_key=os.getenv("OPENAI_KEY"))

set_llm_cache(InMemoryCache())

SYSTEM_PROMPT = SystemMessage(
    content="""You are an assistant answering questions based on the provided context. Cite sources like [1], [2], etc. If the question is specific and not answered by the context answer with I don't know. If it is a general question rather than a specific question answer based on your own knowledge."""
)
