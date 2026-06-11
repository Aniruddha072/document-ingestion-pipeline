from pypdf import PdfReader

from src.database.mongodb import documents_collection


def ingest_document(doc_id):

    document = documents_collection.find_one(
        {"doc_id": doc_id}
    )

    if not document:
        return {
            "error": "Document not found"
        }

    pdf_path = document.get(
        "document_path"
    )

    if not pdf_path:
        return {
            "error": "No PDF uploaded"
        }

    reader = PdfReader(pdf_path)

    extracted_text = ""

    for page in reader.pages:

        extracted_text += (
            page.extract_text() + "\n"
        )

    documents_collection.update_one(
        {"doc_id": doc_id},
        {
            "$set": {
                "extracted_text": extracted_text,
                "status": "COMPLETED"
            }
        }
    )

    return {
        "message": "Document ingested successfully"
    }