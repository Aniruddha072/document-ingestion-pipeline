from unittest.mock import MagicMock, patch

from src.services.ingestion_service import (
    ingest_document
)


@patch("src.services.ingestion_service.get_documents_collection")
def test_document_not_found(mock_collection):

    fake_collection = MagicMock()

    fake_collection.find_one.return_value = None

    mock_collection.return_value = fake_collection

    result = ingest_document("DOC-123")

    assert result["error"] == "Document not found"


@patch("src.services.ingestion_service.get_documents_collection")
def test_no_uploaded_document(mock_collection):

    fake_collection = MagicMock()

    fake_collection.find_one.return_value = {
        "doc_id": "DOC-123",
        "document_path": None
    }

    mock_collection.return_value = fake_collection

    result = ingest_document("DOC-123")

    assert result["error"] == "No document uploaded"


@patch("src.services.ingestion_service.create_vectorstore")
@patch("src.services.ingestion_service.get_embedding_model")
@patch("src.services.ingestion_service.split_documents")
@patch("src.services.ingestion_service.extract_content_metadata")
@patch("src.services.ingestion_service.extract_file_metadata")
@patch("src.services.ingestion_service.extract_text")
@patch("src.services.ingestion_service.get_documents_collection")
def test_ingestion_success(
    mock_collection,
    mock_extract_text,
    mock_file_metadata,
    mock_content_metadata,
    mock_split,
    mock_embedding,
    mock_vectorstore
):

    fake_collection = MagicMock()

    fake_collection.find_one.return_value = {
        "doc_id": "DOC-123",
        "document_path": "sample.pdf"
    }

    mock_collection.return_value = fake_collection

    mock_extract_text.return_value = (
        "sample extracted text"
    )

    mock_file_metadata.return_value = {}

    mock_content_metadata.return_value = {}

    mock_split.return_value = [
        MagicMock(),
        MagicMock()
    ]

    mock_embedding.return_value = MagicMock()

    result = ingest_document(
        "DOC-123"
    )

    assert result["message"] == (
        "Document ingested successfully"
    )


@patch("src.services.ingestion_service.extract_text")
@patch("src.services.ingestion_service.get_documents_collection")
def test_extraction_failure(
    mock_collection,
    mock_extract_text
):

    fake_collection = MagicMock()

    fake_collection.find_one.return_value = {
        "doc_id": "DOC-123",
        "document_path": "sample.pdf"
    }

    mock_collection.return_value = fake_collection

    mock_extract_text.side_effect = Exception(
        "Extraction Error"
    )

    result = ingest_document(
        "DOC-123"
    )

    assert "Failed to extract text" in result["error"]


@patch("src.services.ingestion_service.get_embedding_model")
@patch("src.services.ingestion_service.split_documents")
@patch("src.services.ingestion_service.extract_content_metadata")
@patch("src.services.ingestion_service.extract_file_metadata")
@patch("src.services.ingestion_service.extract_text")
@patch("src.services.ingestion_service.get_documents_collection")
def test_embedding_failure(
    mock_collection,
    mock_extract_text,
    mock_file_metadata,
    mock_content_metadata,
    mock_split,
    mock_embedding
):

    fake_collection = MagicMock()

    fake_collection.find_one.return_value = {
        "doc_id": "DOC-123",
        "document_path": "sample.pdf"
    }

    mock_collection.return_value = fake_collection

    mock_extract_text.return_value = (
        "sample text"
    )

    mock_file_metadata.return_value = {}

    mock_content_metadata.return_value = {}

    mock_split.return_value = [
        MagicMock()
    ]

    mock_embedding.side_effect = Exception(
        "Embedding Error"
    )

    result = ingest_document(
        "DOC-123"
    )

    assert "Failed to load embedding model" in result["error"]


@patch("src.services.ingestion_service.create_vectorstore")
@patch("src.services.ingestion_service.get_embedding_model")
@patch("src.services.ingestion_service.split_documents")
@patch("src.services.ingestion_service.extract_content_metadata")
@patch("src.services.ingestion_service.extract_file_metadata")
@patch("src.services.ingestion_service.extract_text")
@patch("src.services.ingestion_service.get_documents_collection")
def test_vectorstore_failure(
    mock_collection,
    mock_extract_text,
    mock_file_metadata,
    mock_content_metadata,
    mock_split,
    mock_embedding,
    mock_vectorstore
):

    fake_collection = MagicMock()

    fake_collection.find_one.return_value = {
        "doc_id": "DOC-123",
        "document_path": "sample.pdf"
    }

    mock_collection.return_value = fake_collection

    mock_extract_text.return_value = (
        "sample text"
    )

    mock_file_metadata.return_value = {}

    mock_content_metadata.return_value = {}

    mock_split.return_value = [
        MagicMock()
    ]

    mock_embedding.return_value = MagicMock()

    mock_vectorstore.side_effect = Exception(
        "FAISS Error"
    )

    result = ingest_document(
        "DOC-123"
    )

    assert "Failed to create vector store" in result["error"]