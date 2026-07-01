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
def document_status(
    doc_id: str
) -> dict[str, str]:
    """
    Retrieve the current processing status of a document.

    Args:
        doc_id: Unique document identifier.

    Returns:
        dict: Document status information.
    """

    return get_document_status(
        doc_id
    )