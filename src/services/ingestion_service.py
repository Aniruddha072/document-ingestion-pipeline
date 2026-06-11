from pypdf import PdfReader

from langchain_core.documents import Document

from src.database.mongodb import documents_collection

from src.chunking.text_splitter import split_documents
from src.embeddings.embedding_model import get_embedding_model
from src.vectorstore.faiss_manager import create_vectorstore

from datetime import datetime


def ingest_document(doc_id):

    document = documents_collection.find_one(
        {"doc_id": doc_id}
    )

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

    reader = PdfReader(pdf_path)

    extracted_text = ""

    for page in reader.pages:

        extracted_text += (
            page.extract_text() + "\n"
        )

    documents = [
        Document(
            page_content=extracted_text
        )
    ]

    chunks = split_documents(
        documents
    )

    chunk_count = len(chunks)

    embedding_model = (
        get_embedding_model()
    )

    create_vectorstore(
        chunks,
        embedding_model,
        doc_id
    )

    documents_collection.update_one(
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

    return {
        "message": "Document ingested successfully"
    }