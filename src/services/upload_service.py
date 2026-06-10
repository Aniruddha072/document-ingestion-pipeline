import os
from src.database.mongodb import documents_collection


def upload_pdf(doc_id, file):

    document = documents_collection.find_one(
        {"doc_id": doc_id}
    )

    if not document:
        return {
            "error": "Document not found"
        }

    file_path = f"raw/{doc_id}_{file.filename}"

    with open(file_path, "wb") as buffer:
        buffer.write(file.file.read())

    documents_collection.update_one(
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