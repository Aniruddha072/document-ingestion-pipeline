from src.database.mongodb import get_documents_collection


def get_document_status(
    doc_id: str
) -> dict[str, str]:
    """
    Retrieve the current status of a document.

    Args:
        doc_id: Unique document identifier.

    Returns:
        dict: Document information and processing status.
    """

    collection = get_documents_collection()

    try:
        document = collection.find_one(
            {"doc_id": doc_id}
        )
    except Exception as error:
        return {
            "error": f"Failed to fetch document: {error}"
        }

    if not document:
        return {
            "error": "Document not found"
        }

    return {
        "doc_id": document["doc_id"],
        "document_name": document["document_name"],
        "status": document["status"]
    }