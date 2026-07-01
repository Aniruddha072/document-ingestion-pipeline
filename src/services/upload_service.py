import os
from src.database.mongodb import get_documents_collection
from config.settings import settings
from fastapi import UploadFile


def upload_pdf(
    doc_id: str,
    file: UploadFile
) -> dict[str, str]:
    """
    Upload and store a PDF file for a document.

    Args:
        doc_id: Unique document identifier.
        file: Uploaded PDF file.

    Returns:
        dict: Upload result and stored file path.
    """

    collection = get_documents_collection()

    document = collection.find_one(
        {"doc_id": doc_id}
    )

    if not document:
        return {
            "error": "Document not found"
        }

    file_path = (f"{settings.raw_storage_path}/{doc_id}_{file.filename}")

    try:
        with open(file_path, "wb") as buffer:
            buffer.write(file.file.read())
    except Exception as error:
        return {
            "error": f"Failed to save file: {error}"
        }

    try:
        collection.update_one(
            {"doc_id": doc_id},
            {
                "$set": {
                    "document_path": file_path
                }
            }
        )
    except Exception as error:
        return {
            "error": f"Failed to update document: {error}"
        }

    return {
        "message": "PDF uploaded successfully",
        "document_path": file_path
    }