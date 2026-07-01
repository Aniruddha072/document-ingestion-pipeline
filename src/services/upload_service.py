import os
from src.database.mongodb import get_documents_collection
from config.settings import settings


def upload_pdf(doc_id, file):

    collection = get_documents_collection()

    document = collection.find_one(
        {"doc_id": doc_id}
    )

    if not document:
        return {
            "error": "Document not found"
        }

    file_path = (f"{settings.raw_storage_path}/{doc_id}_{file.filename}")

    with open(file_path, "wb") as buffer:
        buffer.write(file.file.read())

    collection.update_one(  
        {"doc_id": doc_id},
        {
            "$set": {
                "document_path": file_path
            }
        }
    )

    return {
        "message": "PDF uploaded successfully",
        "document_path": file_path
    }