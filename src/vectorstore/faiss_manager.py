from config.settings import settings
from langchain_community.vectorstores import FAISS
from langchain_core.documents import Document


def create_vectorstore(
    chunks: list[Document],
    embedding_model,
    doc_id: str
) -> FAISS:
    """
    Create and save a FAISS vector store from document chunks.

    Args:
        chunks: List of document chunks.
        embedding_model: Embedding model used to generate vectors.
        doc_id: Unique document identifier.

    Returns:
        FAISS: Persisted FAISS vector store.
    """

    vectorstore = FAISS.from_documents(
        chunks,
        embedding_model
    )

    vectorstore.save_local(
        f"{settings.vectorstore_path}/{doc_id}"
    )

    return vectorstore

    