from unittest.mock import MagicMock, patch

from src.services.document_service import create_document
from src.schemas.document_schema import DocumentCreate


@patch("src.services.document_service.get_documents_collection")
def test_create_document_success(mock_collection):

    fake_collection = MagicMock()
    mock_collection.return_value = fake_collection

    document = DocumentCreate(
        document_name="sample.pdf",
        description="Test document"
    )

    result = create_document(document)

    fake_collection.insert_one.assert_called_once()

    assert "doc_id" in result
    assert result["status"] == "NOT_STARTED"


@patch("src.services.document_service.get_documents_collection")
def test_create_document_insert_failure(mock_collection):

    fake_collection = MagicMock()

    fake_collection.insert_one.side_effect = Exception(
        "Database Error"
    )

    mock_collection.return_value = fake_collection

    document = DocumentCreate(
        document_name="sample.pdf",
        description="Test document"
    )

    result = create_document(document)

    assert "error" in result
    assert "Database Error" in result["error"]