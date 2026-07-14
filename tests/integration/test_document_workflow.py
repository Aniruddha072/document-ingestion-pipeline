import os
import tempfile

from fastapi.testclient import TestClient

from main import app

client = TestClient(app)


def test_complete_document_workflow():

    # Step 1: Register document
    register_response = client.post(
        "/documents",
        json={
            "document_name": "integration_test",
            "description": "Integration Test"
        }
    )

    assert register_response.status_code == 200

    document_data = register_response.json()

    assert "doc_id" in document_data

    doc_id = document_data["doc_id"]

    # Step 2: Create unique file
    with tempfile.NamedTemporaryFile(
        suffix=".txt",
        delete=False,
        mode="w",
        encoding="utf-8"
    ) as temp_file:

        temp_file.write(
            f"Workflow Integration Test {doc_id}"
        )

        temp_path = temp_file.name

    try:

        # Step 3: Upload file
        with open(temp_path, "rb") as file:

            upload_response = client.post(
                f"/documents/{doc_id}/upload",
                files={
                    "file": (
                        "workflow_test.txt",
                        file,
                        "text/plain"
                    )
                }
            )

        assert upload_response.status_code == 200

        upload_data = upload_response.json()

        assert "message" in upload_data

        assert (
            upload_data["message"]
            == "Document uploaded successfully"
        )

        # Step 4: Trigger ingestion
        ingest_response = client.post(
            f"/documents/{doc_id}/ingest"
        )

        assert ingest_response.status_code == 200

        ingest_data = ingest_response.json()

        assert (
            ingest_data["message"]
            == "Document ingestion started"
        )

        # Step 5: Check status
        status_response = client.get(
            f"/documents/{doc_id}/status"
        )

        assert status_response.status_code == 200

        status_data = status_response.json()

        assert status_data["doc_id"] == doc_id

        assert "status" in status_data

    finally:

        if os.path.exists(temp_path):
            os.remove(temp_path)