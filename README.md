# Document Ingestion Pipeline

A document ingestion pipeline built using FastAPI and MongoDB Atlas for document registration, PDF uploads, text extraction, and future vector database ingestion.

---

## Completed Features

- FastAPI Setup
- MongoDB Atlas Integration
- Health Check API
- Database Connectivity Test API
- Document Registry API
- Unique Document ID Generation
- PDF Upload API
- Local File Storage
- PDF Text Extraction
- Document Ingestion API
- Status Tracking
- Swagger Documentation

---

## Project Structure

```text
document-ingestion-pipeline/

├── src/
│   ├── api/
│   ├── database/
│   ├── models/
│   ├── schemas/
│   ├── services/
│   └── storage/
│
├── raw/
│
├── .env
├── .gitignore
├── requirements.txt
├── README.md
└── main.py
```

---

## Available APIs

### Health Check

```http
GET /health
```

Checks whether the API is running.

---

### Database Connectivity Test

```http
GET /db-test
```

Verifies MongoDB Atlas connectivity.

---

### Create Document Registry

```http
POST /documents
```

Creates a document record in MongoDB.

Request:

```json
{
  "document_name": "Army Recruitment",
  "description": "Recruitment Notification"
}
```

Response:

```json
{
  "doc_id": "DOC-d0d1a8f0",
  "status": "NOT_STARTED"
}
```

---

### Upload PDF

```http
POST /documents/{doc_id}/upload
```

Uploads a PDF and stores it in the backend `raw/` folder.

Response:

```json
{
  "message": "PDF uploaded successfully",
  "document_path": "raw/DOC-d0d1a8f0_sample.pdf"
}
```

---

### Trigger Ingestion

```http
POST /documents/{doc_id}/ingest
```

Loads the uploaded PDF, extracts text, stores the extracted text in MongoDB, and updates document status.

Response:

```json
{
  "message": "Document ingested successfully"
}
```

---

## Document Lifecycle

```text
Create Document
       ↓
Upload PDF
       ↓
Store PDF Path
       ↓
Trigger Ingestion
       ↓
Read PDF
       ↓
Extract Text
       ↓
Store Text in MongoDB
       ↓
Status = COMPLETED
```

---

## MongoDB Document Structure

```json
{
  "doc_id": "DOC-d0d1a8f0",
  "document_name": "Army Recruitment",
  "description": "Recruitment Notification",
  "status": "COMPLETED",
  "document_path": "raw/DOC-d0d1a8f0_sample.pdf",
  "extracted_text": "..."
}
```

---

## Technologies Used

- Python
- FastAPI
- MongoDB Atlas
- PyMongo
- Pydantic
- PyPDF
- Uvicorn
- Python Dotenv

---

## Running the Project

Activate virtual environment:

```powershell
.\venv\Scripts\activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Run FastAPI:

```bash
uvicorn main:app --reload
```

Open Swagger:

```text
http://127.0.0.1:8000/docs
```

---

## Current Status

✅ Document Registry

✅ PDF Upload

✅ Text Extraction

✅ MongoDB Storage

✅ Status Tracking

---

## Next Milestone

### Vector Database Integration

Planned Flow:

```text
PDF
 ↓
Extract Text
 ↓
Chunk Text
 ↓
Generate Embeddings
 ↓
Store in Vector Database (FAISS)
```