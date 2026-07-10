from fastapi import (
    APIRouter,
    BackgroundTasks
)

from src.services.ingestion_service import (
    ingest_document
)

router = APIRouter()


@router.post(
    "/documents/{doc_id}/ingest"
)
def trigger_ingestion(
    doc_id: str,
    background_tasks: BackgroundTasks
) -> dict[str, str]:
    """
    Trigger document ingestion and processing.

    Args:
        doc_id: Unique document identifier.

    Returns:
        dict: Ingestion status.
    """

    background_tasks.add_task(
        ingest_document,
        doc_id
    )

    return {
        "message": "Document ingestion started"
    }