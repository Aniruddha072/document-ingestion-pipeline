from fastapi import APIRouter

from src.services.ingestion_service import (
    ingest_document
)

router = APIRouter()


@router.post(
    "/documents/{doc_id}/ingest"
)
def trigger_ingestion(
    doc_id: str
):

    return ingest_document(
        doc_id
    )