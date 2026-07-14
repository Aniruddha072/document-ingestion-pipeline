from fastapi.testclient import TestClient

from main import app

client = TestClient(app)


def test_ingestion_without_upload():

    register_response = client.post(
        "/documents",
        json={
            "document_name": "no_upload",
            "description": "No upload test"
        }
    )

    doc_id = register_response.json()["doc_id"]

    ingest_response = client.post(
        f"/documents/{doc_id}/ingest"
    )

    assert ingest_response.status_code == 200

    assert (
        ingest_response.json()["message"]
        == "Document ingestion started"
    )

    status_response = client.get(
        f"/documents/{doc_id}/status"
    )

    assert status_response.status_code == 200

    status_data = status_response.json()

    assert "status" in status_data