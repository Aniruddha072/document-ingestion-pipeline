# Document Ingestion Pipeline

A document ingestion pipeline built using FastAPI and MongoDB Atlas for document registration, file uploads, text extraction, and future vector database ingestion.

---

## Current Progress

### Completed Features

- FastAPI Setup
- Project Structure Setup
- Health Check API
- MongoDB Atlas Integration
- Database Connectivity Test API
- Document Registry API
- Unique Document ID Generation
- PDF Upload API
- Local File Storage
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

Response:

```json
{
    "status": "healthy"
}
```

---

### Database Connectivity Test

```http
GET /db-test
```

Response:

```json
{
    "message": "MongoDB Connected Successfully"
}
```

---

### Create Document Registry

```http
POST /documents
```

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

MongoDB Record:

```json
{
    "doc_id": "DOC-d0d1a8f0",
    "document_name": "Army Recruitment",
    "description": "Recruitment Notification",
    "status": "NOT_STARTED",
    "document_path": null,
    "extracted_text": null
}
```

---

### Upload PDF

```http
POST /documents/{doc_id}/upload
```

Example:

```http
POST /documents/DOC-d0d1a8f0/upload
```

Response:

```json
{
    "message": "PDF uploaded successfully",
    "document_path": "raw/DOC-d0d1a8f0_sample.pdf"
}
```

Result:

```text
raw/
└── DOC-d0d1a8f0_sample.pdf
```

MongoDB Update:

```json
{
    "document_path": "raw/DOC-d0d1a8f0_sample.pdf"
}
```

---

## Technologies Used

- Python
- FastAPI
- Uvicorn
- MongoDB Atlas
- PyMongo
- Pydantic
- Python Dotenv

---

## Running the Project

### Activate Virtual Environment

```powershell
.\venv\Scripts\activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Run FastAPI

```bash
uvicorn main:app --reload
```

### Swagger Documentation

```text
http://127.0.0.1:8000/docs
```

---

## Current Architecture

```text
User
 │
 ▼
FastAPI
 │
 ▼
MongoDB Atlas
 │
 ▼
Document Metadata Storage

User
 │
 ▼
FastAPI
 │
 ▼
Local Storage (raw/)
 │
 ▼
PDF Files
```

---

## Next Step

### Trigger Ingestion API

```http
POST /documents/{doc_id}/ingest
```

Planned Flow:

```text
DOC_ID
   ↓
Find MongoDB Record
   ↓
Load PDF from raw/
   ↓
Extract Text
   ↓
Store extracted_text in MongoDB
   ↓
Update Status
```

Status Values:

```text
NOT_STARTED
IN_PROGRESS
COMPLETED
```