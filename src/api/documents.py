from fastapi import APIRouter

from src.schemas.document_schema import DocumentCreate
from src.services.document_service import create_document

router = APIRouter()


@router.post("/documents")
def register_document(
    document: DocumentCreate
) -> dict[str, str]:
    """
    Register a new document in the system.

    Args:
        document: Document metadata supplied by the user.

    Returns:
        dict: Created document information.
    """

    return create_document(document)