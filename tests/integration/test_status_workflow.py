from fastapi.testclient import TestClient

from main import app

client = TestClient(app)


def test_document_not_found():

    response = client.get(
        "/documents/INVALID_DOC/status"
    )

    assert response.status_code == 200

    assert response.json() == {
        "error": "Document not found"
    }