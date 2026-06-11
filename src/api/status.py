from fastapi import APIRouter

from src.services.status_service import (
    get_document_status
)

router = APIRouter()


@router.get(
    "/documents/{doc_id}/status",
    tags=["Documents"],
    summary="Get Document Status"
)
def document_status(doc_id: str):

    return get_document_status(
        doc_id
    )