# Document Ingestion Pipeline

A FastAPI-based document ingestion pipeline that registers documents, uploads PDFs, extracts text, stores metadata in MongoDB Atlas, generates embeddings, and creates FAISS vector indexes for semantic search and retrieval.

## Features

* Document Registration API
* PDF Upload API
* PDF Text Extraction
* MongoDB Atlas Integration
* FAISS Vector Indexing
* Document Status Tracking
* Ingestion Metadata Tracking
* Swagger API Documentation

---

## Project Structure

```text
document-ingestion-pipeline/
│
├── src/
│   ├── api/
│   │   ├── documents.py
│   │   ├── upload.py
│   │   ├── ingestion.py
│   │   ├── status.py
│   │   ├── health.py
│   │   └── test_db.py
│   │
│   ├── chunking/
│   │   └── text_splitter.py
│   │
│   ├── embeddings/
│   │   └── embedding_model.py
│   │
│   ├── database/
│   │   └── mongodb.py
│   │
│   ├── schemas/
│   │   └── document_schema.py
│   │
│   ├── services/
│   │   ├── document_service.py
│   │   ├── upload_service.py
│   │   ├── ingestion_service.py
│   │   └── status_service.py
│   │
│   └── vectorstore/
│       └── faiss_manager.py
│
├── storage/
│   ├── raw/
│   └── vectorstore/
│
├── .env
├── .gitignore
├── main.py
├── requirements.txt
└── README.md
```

---

## Workflow

```text
Register Document
        ↓
Upload PDF
        ↓
Store PDF in storage/raw
        ↓
Extract Text
        ↓
Store Metadata in MongoDB
        ↓
Chunk Text
        ↓
Generate Embeddings
        ↓
Create FAISS Vector Index
        ↓
Update Document Status
        ↓
Retrieve Document Status
```

---

## Available APIs

### Health Check

```http
GET /health
```

Checks whether the FastAPI application is running.

### MongoDB Connection Test

```http
GET /db-test
```

Verifies connectivity with MongoDB Atlas.

### Register Document

```http
POST /documents
```

Creates a document entry in MongoDB with:

* Document ID
* Document Name
* Description
* Status (`NOT_STARTED`)
* Creation Timestamp

### Upload PDF

```http
POST /documents/{doc_id}/upload
```

Uploads a PDF file and stores it in:

```text
storage/raw/
```

Updates the document record with the PDF path.

### Trigger Ingestion

```http
POST /documents/{doc_id}/ingest
```

Performs:

1. PDF Loading
2. Text Extraction
3. Text Chunking
4. Embedding Generation
5. FAISS Index Creation
6. MongoDB Metadata Update

Stores:

* Extracted Text
* Chunk Count
* Ingestion Timestamp
* Status (`COMPLETED`)

### Get Document Status

```http
GET /documents/{doc_id}/status
```

Example Response:

```json
{
  "doc_id": "DOC-d0d1a8f0",
  "document_name": "Army Recruitment",
  "status": "COMPLETED"
}
```

---

## Document Metadata Stored in MongoDB

Example document:

```json
{
  "doc_id": "DOC-d0d1a8f0",
  "document_name": "Army Recruitment",
  "description": "Recruitment Notification",
  "status": "COMPLETED",
  "document_path": "storage/raw/DOC-d0d1a8f0_sample.pdf",
  "extracted_text": "...",
  "chunk_count": 12,
  "created_at": "...",
  "ingested_at": "..."
}
```

---

## Technologies Used

* FastAPI
* MongoDB Atlas
* PyMongo
* PyPDF
* LangChain
* Sentence Transformers
* FAISS
* Python Dotenv

---

## Running the Application

Install dependencies:

```bash
pip install -r requirements.txt
```

Run the server:

```bash
uvicorn main:app --reload
```

---

## Swagger Documentation

After starting the server:

```text
http://127.0.0.1:8000/docs
```

Use Swagger UI to test all APIs interactively.

---

## Current Status

Completed:

* FastAPI Project Setup
* MongoDB Atlas Integration
* Document Registry API
* PDF Upload API
* PDF Storage Management
* PDF Text Extraction
* Text Chunking
* Embedding Generation
* FAISS Vector Indexing
* Document Status API
* Ingestion Metadata Tracking
* Swagger Documentation

## Version

**v1.0 - Complete Document Ingestion Pipeline**

This project implements a complete document ingestion workflow that can serve as the foundation for Retrieval-Augmented Generation (RAG), enterprise search systems, and document processing platforms.
