from uuid import uuid4

from langchain_core.documents import Document
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_chroma import Chroma

from app.paths import ARTIFACTS_DIR


class VectorStoreManager:
    def __init__(
        self, collection_name="documents", model_name="intfloat/multilingual-e5-large-instruct"
    ):
        self.embeddings = HuggingFaceEmbeddings(model_name=model_name)
        self.collection_name = collection_name
        self.persist_directory = str(ARTIFACTS_DIR / "chroma")
        self.vector_store = self._initialize_vector_store()

    def _initialize_vector_store(self):
        return Chroma(
            collection_name=self.collection_name,
            embedding_function=self.embeddings,
            persist_directory=self.persist_directory,
        )

    def delete_everything(self):
        self.vector_store.delete_collection()
        self.vector_store = self._initialize_vector_store()

    def insert_data(self, text, session_id, k=4):
        data = text.split(".")
        chunks = [".".join(data[i : i + k]) for i in range(0, len(data), k)]
        documents = [
            Document(page_content=chunk, metadata={"session_id": session_id})
            for chunk in chunks
        ]
        uuids = [str(uuid4()) for _ in documents]
        self.vector_store.add_documents(documents, ids=uuids)

    def query(self, query_text, session_id, k=5):
        return self.vector_store.similarity_search(
            query_text, k=k, filter={"session_id": session_id}
        )

    def delete_user_data(self, session_id):
        self.vector_store.delete(where={"session_id": session_id})
