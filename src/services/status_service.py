from src.database.mongodb import documents_collection


def get_document_status(doc_id):

    document = documents_collection.find_one(
        {"doc_id": doc_id}
    )

    if not document:
        return {
            "error": "Document not found"
        }

    return {
        "doc_id": document["doc_id"],
        "document_name": document["document_name"],
        "status": document["status"]
    }