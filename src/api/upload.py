from fastapi import APIRouter
from fastapi import UploadFile
from fastapi import File

from src.services.upload_service import upload_pdf

router = APIRouter()


@router.post("/documents/{doc_id}/upload")
def upload_document(
    doc_id: str,
    file: UploadFile = File(...)
):

    return upload_pdf(
        doc_id,
        file
    )