from langchain_core.documents import Document
from src.database.mongodb import get_documents_collection

from src.chunking.text_splitter import split_documents
from src.embeddings.embedding_model import get_embedding_model
from src.vectorstore.faiss_manager import create_vectorstore
from src.extraction.pdf_extractor import extract_text_from_pdf
from datetime import datetime


def ingest_document(doc_id: str) -> dict[str, str]:
    """
    Process an uploaded PDF document.

    The document is loaded from storage, text is extracted,
    split into chunks, converted into embeddings, and stored
    in a FAISS vector database. The document status is then
    updated in MongoDB.

    Args:
        doc_id: Unique document identifier.

    Returns:
        dict: Ingestion result message or error details.
    """

    collection = get_documents_collection()

    try:
        document = collection.find_one(
            {"doc_id": doc_id}
        )
    except Exception as error:
        return {
            "error": f"Failed to fetch document: {error}"
        }

    if not document:
        return {
            "error": "Document not found"
        }

    pdf_path = document.get(
        "document_path"
    )

    if not pdf_path:
        return {
            "error": "No PDF uploaded"
        }

    try:
        extracted_text = (
            extract_text_from_pdf(
                pdf_path
            )
        )
    except Exception as error:
        return {
            "error": (
                f"Failed to extract text: {error}"
            )
        }

    documents = [
        Document(
            page_content=extracted_text
        )
    ]

    chunks = split_documents(
        documents
    )

    chunk_count = len(chunks)

    try:
        embedding_model = (
            get_embedding_model()
        )
    except Exception as error:
        return {
            "error": f"Failed to load embedding model: {error}"
        }

    try:
        create_vectorstore(
            chunks,
            embedding_model,
            doc_id
        )
    except Exception as error:
        return {
            "error": f"Failed to create vector store: {error}"
        }

    try:
        collection.update_one(
            {"doc_id": doc_id},
            {
                "$set": {
                    "extracted_text": extracted_text,
                    "status": "COMPLETED",
                    "chunk_count": chunk_count,
                    "ingested_at": datetime.utcnow()
                }
            }
        )
    except Exception as error:
        return {
            "error": f"Failed to update document status: {error}"
        }

    return {
        "message": "Document ingested successfully"
    }

    