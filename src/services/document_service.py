from src.database.mongodb import get_documents_collection
from src.schemas.document_schema import DocumentCreate
import uuid
from datetime import datetime

def create_document(
    document_data: DocumentCreate
) -> dict[str, str]:
    """
    Create a new document record in MongoDB.

    Args:
        document_data: Document metadata received from the request.

    Returns:
        dict: Document ID and initial status.
    """

    collection = get_documents_collection()

    doc_id = f"DOC-{uuid.uuid4().hex[:8]}"

    document = {
        "doc_id": doc_id,
        "document_name": document_data.document_name,
        "description": document_data.description,
        "status": "NOT_STARTED",
        "document_path": None,
        "extracted_text": None,
        "created_at": datetime.utcnow()
    }

    try:
        collection.insert_one(document)
    except Exception as error:
        return{
            "error": f"Failed to create document: {error}"
        }

    return {
        "doc_id": doc_id,
        "status": document["status"]
    }
