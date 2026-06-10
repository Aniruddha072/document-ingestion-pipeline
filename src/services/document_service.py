from src.database.mongodb import documents_collection
import uuid


def create_document(document_data):

    doc_id = f"DOC-{uuid.uuid4().hex[:8]}"

    document = {
        "doc_id": doc_id,
        "document_name": document_data.document_name,
        "description": document_data.description,
        "status": "NOT_STARTED",
        "document_path": None,
        "extracted_text": None
    }

    documents_collection.insert_one(document)

    return {
        "doc_id": doc_id,
        "status": document["status"]
    }