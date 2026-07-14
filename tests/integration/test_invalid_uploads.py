from fastapi.testclient import TestClient

from main import app

client = TestClient(app)


def test_invalid_file_type():

    register_response = client.post(
        "/documents",
        json={
            "document_name": "invalid_file",
            "description": "Testing invalid uploads"
        }
    )

    doc_id = register_response.json()["doc_id"]

    with open(
        "tests/sample_files/test.exe",
        "rb"
    ) as file:

        upload_response = client.post(
            f"/documents/{doc_id}/upload",
            files={
                "file": (
                    "test.exe",
                    file,
                    "application/octet-stream"
                )
            }
        )

    assert "error" in upload_response.json()

    assert (
        "unsupported"
        in upload_response.json()["error"].lower()
    )