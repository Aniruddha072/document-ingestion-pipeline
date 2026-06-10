from fastapi import APIRouter

from src.schemas.document_schema import DocumentCreate
from src.services.document_service import create_document

router = APIRouter()


@router.post("/documents")
def register_document(document: DocumentCreate):

    return create_document(document)