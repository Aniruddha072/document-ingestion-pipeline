from fastapi import APIRouter
from fastapi import UploadFile
from fastapi import File

from src.services.upload_service import upload_pdf

router = APIRouter()


@router.post("/documents/{doc_id}/upload")
def upload_document(
    doc_id: str,
    file: UploadFile = File(...)
) -> dict[str, str]:
    """
    Upload a PDF file for a document.

    Args:
        doc_id: Unique document identifier.
        file: Uploaded PDF file.

    Returns:
        dict: Upload result and file information.
    """

    return upload_pdf(
        doc_id,
        file
    )