from fastapi import APIRouter
from fastapi import UploadFile
from fastapi import File

from src.services.upload_service import upload_document

router = APIRouter()


@router.post("/documents/{doc_id}/upload")

#API Route
def upload_file(
    doc_id: str,
    file: UploadFile = File(...)
) -> dict[str, str]:
    """
    Upload a supported document file.

    Args:
        doc_id: Unique document identifier.
        file: Uploaded document file.

    Returns:
        dict: Upload result and file information.
    """
    
    #Service Layer
    return upload_document(
        doc_id,
        file
    )