import os
from src.database.mongodb import get_documents_collection
from config.settings import settings
from fastapi import UploadFile

SUPPORTED_EXTENSIONS = {
    ".pdf",
    ".txt",
    ".docx"
}

def upload_document(
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

    file_extension = os.path.splitext(
        file.filename
    )[1].lower()

    if file_extension not in SUPPORTED_EXTENSIONS:
        return {
            "error": (
                f"Unsupported file type: "
                f"{file_extension}"
            )
        }

    file_path = (
        f"{settings.raw_storage_path}/{doc_id}_{file.filename}"
    )

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
        "message": "Document uploaded successfully",
        "document_path": file_path
    }