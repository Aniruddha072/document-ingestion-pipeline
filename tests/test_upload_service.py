from io import BytesIO
from unittest.mock import MagicMock, patch

from fastapi import UploadFile

from src.services.upload_service import upload_document


@patch("src.services.upload_service.get_documents_collection")
def test_document_not_found(mock_collection):

    fake_collection = MagicMock()
    fake_collection.find_one.return_value = None

    mock_collection.return_value = fake_collection

    file = UploadFile(
        filename="sample.pdf",
        file=BytesIO(b"test")
    )

    result = upload_document("DOC-123", file)

    assert result["error"] == "Document not found"


@patch("src.services.upload_service.get_documents_collection")
def test_unsupported_file_type(mock_collection):

    fake_collection = MagicMock()

    fake_collection.find_one.return_value = {
        "doc_id": "DOC-123"
    }

    mock_collection.return_value = fake_collection

    file = UploadFile(
        filename="virus.exe",
        file=BytesIO(b"test")
    )

    result = upload_document("DOC-123", file)

    assert "Unsupported file type" in result["error"]


@patch("src.services.upload_service.check_duplicate_hash")
@patch("src.services.upload_service.generate_document_hash")
@patch("src.services.upload_service.validate_document")
@patch("src.services.upload_service.get_documents_collection")
def test_upload_success(
    mock_collection,
    mock_validate,
    mock_hash,
    mock_duplicate
):

    fake_collection = MagicMock()

    fake_collection.find_one.return_value = {
        "doc_id": "DOC-123"
    }

    mock_collection.return_value = fake_collection

    mock_hash.return_value = "fakehash"

    file = UploadFile(
        filename="sample.pdf",
        file=BytesIO(b"pdf content")
    )

    result = upload_document(
        "DOC-123",
        file
    )

    assert result["message"] == (
        "Document uploaded successfully"
    )

    fake_collection.update_one.assert_called_once()


@patch("src.services.upload_service.check_duplicate_hash")
@patch("src.services.upload_service.generate_document_hash")
@patch("src.services.upload_service.validate_document")
@patch("src.services.upload_service.get_documents_collection")
def test_update_failure(
    mock_collection,
    mock_validate,
    mock_hash,
    mock_duplicate
):

    fake_collection = MagicMock()

    fake_collection.find_one.return_value = {
        "doc_id": "DOC-123"
    }

    fake_collection.update_one.side_effect = Exception(
        "Mongo Error"
    )

    mock_collection.return_value = fake_collection

    mock_hash.return_value = "fakehash"

    file = UploadFile(
        filename="sample.pdf",
        file=BytesIO(b"pdf content")
    )

    result = upload_document(
        "DOC-123",
        file
    )

    assert "Failed to update document" in result["error"]