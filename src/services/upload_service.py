import os
from src.database.mongodb import get_documents_collection
from config.settings import settings
from fastapi import UploadFile
from src.validation.document_validator import validate_document
from src.validation.duplicate_detector import (
    generate_document_hash,
    check_duplicate_hash
)

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
        validate_document(file_path)
    except ValueError as error:
        if os.path.exists(file_path):
            try:
                os.remove(file_path)
            except Exception:
                pass
        return {
            "error": str(error)
        }

    document_hash = generate_document_hash(file_path)

    try:
        check_duplicate_hash(document_hash, collection)
    except ValueError as error:
        if os.path.exists(file_path):
            try:
                os.remove(file_path)
            except Exception:
                pass
        return {
            "error": str(error)
        }

    try:
        collection.update_one(
            {"doc_id": doc_id},
            {
                "$set": {
                    "document_path": file_path,
                    "document_hash": document_hash
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