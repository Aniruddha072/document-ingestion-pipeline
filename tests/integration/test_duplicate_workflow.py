import os
import tempfile
import uuid

from fastapi.testclient import TestClient

from main import app

client = TestClient(app)


def test_duplicate_document_upload():

    # Create ONE file
    with tempfile.NamedTemporaryFile(
        suffix=".txt",
        delete=False,
        mode="w",
        encoding="utf-8"
    ) as temp_file:

        temp_file.write(
            f"Duplicate Detection Integration Test {uuid.uuid4()}"
        )

    temp_path = temp_file.name

    try:

        # First document
        response_1 = client.post(
            "/documents",
            json={
                "document_name": "doc1",
                "description": "First document"
            }
        )

        assert response_1.status_code == 200

        doc_id_1 = response_1.json()["doc_id"]

        with open(temp_path, "rb") as file:

            upload_response_1 = client.post(
                f"/documents/{doc_id_1}/upload",
                files={
                    "file": (
                        "duplicate_test.txt",
                        file,
                        "text/plain"
                    )
                }
            )

        assert upload_response_1.status_code == 200

        assert (
            upload_response_1.json()["message"]
            == "Document uploaded successfully"
        )

        # Second document
        response_2 = client.post(
            "/documents",
            json={
                "document_name": "doc2",
                "description": "Second document"
            }
        )

        assert response_2.status_code == 200

        doc_id_2 = response_2.json()["doc_id"]

        # Upload SAME file again
        with open(temp_path, "rb") as file:

            upload_response_2 = client.post(
                f"/documents/{doc_id_2}/upload",
                files={
                    "file": (
                        "duplicate_test.txt",
                        file,
                        "text/plain"
                    )
                }
            )

        assert upload_response_2.status_code == 200

        duplicate_response = upload_response_2.json()

        assert "error" in duplicate_response

        assert (
            "already exists"
            in duplicate_response["error"].lower()
        )

    finally:

        if os.path.exists(temp_path):
            os.remove(temp_path)