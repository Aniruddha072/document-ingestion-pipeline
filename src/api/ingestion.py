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
) -> dict[str, str]:
    """
    Trigger document ingestion and processing.

    Args:
        doc_id: Unique document identifier.

    Returns:
        dict: Ingestion result.
    """

    return ingest_document(
        doc_id
    )