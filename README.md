# Document Ingestion Pipeline

A FastAPI-based document ingestion pipeline that registers documents, uploads PDFs, extracts text, stores metadata in MongoDB Atlas, and generates FAISS vector indexes for future semantic search and retrieval.

## Features

* Document Registration API
* PDF Upload API
* MongoDB Atlas Integration
* PDF Text Extraction
* FAISS Vector Index Creation
* Document Status Tracking
* Swagger API Documentation

## Project Structure

```text
document-ingestion-pipeline/
│
├── src/
│   ├── api/
│   ├── chunking/
│   ├── database/
│   ├── embeddings/
│   ├── schemas/
│   ├── services/
│   └── vectorstore/
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

## Workflow

```text
Register Document
        ↓
Upload PDF
        ↓
Extract Text
        ↓
Store Metadata in MongoDB
        ↓
Generate Embeddings
        ↓
Store in FAISS Vector Database
```

## APIs

### Health Check

```http
GET /health
```

### Test MongoDB Connection

```http
GET /db-test
```

### Register Document

```http
POST /documents
```

### Upload PDF

```http
POST /documents/{doc_id}/upload
```

### Trigger Ingestion

```http
POST /documents/{doc_id}/ingest
```

## Tech Stack

* FastAPI
* MongoDB Atlas
* PyMongo
* PyPDF
* LangChain
* Sentence Transformers
* FAISS

## Run Project

```bash
uvicorn main:app --reload
```

Swagger Documentation:

```text
http://127.0.0.1:8000/docs
```
