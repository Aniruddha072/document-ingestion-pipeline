# Document Ingestion Pipeline

A production-style document ingestion pipeline built with FastAPI that processes uploaded documents, extracts content, generates embeddings, and stores them for downstream Retrieval-Augmented Generation (RAG) applications.

---

## Overview

This project automates the document ingestion workflow by:

- Registering documents
- Uploading files
- Validating document formats
- Extracting document content
- Generating metadata
- Detecting duplicate files
- Chunking text
- Creating embeddings
- Storing vectors in FAISS
- Persisting document information in MongoDB

The pipeline is designed as a backend service that can be integrated into larger AI and RAG systems.

---

## Features

### Document Management
- Document registration
- File upload support
- Document status tracking

### Validation
- File type validation
- File size validation
- Duplicate document detection using SHA-256 hashing

### Content Processing
- PDF extraction
- DOCX extraction
- TXT extraction
- Metadata generation

### AI Pipeline
- Text chunking using LangChain
- Embedding generation using Sentence Transformers
- FAISS vector storage

### Background Processing
- Asynchronous ingestion workflow
- Non-blocking API responses

### Testing
- Unit tests with Pytest
- Code coverage reporting

---

## Tech Stack

### Backend
- FastAPI
- Uvicorn

### Database
- MongoDB Atlas

### AI / NLP
- LangChain
- Sentence Transformers
- FAISS

### Utilities
- PyPDF2
- python-docx
- Pydantic

### Testing
- Pytest
- Pytest-Cov

### Deployment
- Docker
- Docker Compose

---

## Project Structure

```text
document-ingestion-pipeline/
│
├── src/
│   ├── api/
│   ├── services/
│   ├── database/
│   ├── models/
│   └── utils/
│
├── tests/
│
├── storage/
│   ├── raw/
│   └── vectorstore/
│
├── config/
│
├── main.py
├── requirements.txt
├── Dockerfile
└── docker-compose.yml
```

---

## Workflow

```text
Register Document
        │
        ▼
Upload File
        │
        ▼
Validation
        │
        ▼
Duplicate Detection
        │
        ▼
Content Extraction
        │
        ▼
Metadata Generation
        │
        ▼
Chunking
        │
        ▼
Embedding Generation
        │
        ▼
FAISS Storage
        │
        ▼
MongoDB Update
```

---

## API Endpoints

### Register Document

```http
POST /documents
```

Creates a new document record.

---

### Upload Document

```http
POST /documents/{document_id}/upload
```

Uploads a document and triggers ingestion.

---

### Get Document Status

```http
GET /documents/{document_id}
```

Returns current processing status and metadata.

---

## Local Setup

### Clone Repository

```bash
git clone https://github.com/Aniruddha072/document-ingestion-pipeline.git
cd document-ingestion-pipeline
```

### Create Virtual Environment

```bash
python -m venv venv
```

Activate:

Windows:

```bash
venv\Scripts\activate
```

Linux / Mac:

```bash
source venv/bin/activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Configure Environment

Create a `.env` file:

```env
MONGODB_URI=<your_mongodb_connection_string>
DATABASE_NAME=document_ingestion
COLLECTION_NAME=documents
```

### Run Application

```bash
uvicorn main:app --reload
```

Swagger UI:

```text
http://localhost:8000/docs
```

---

## Docker Deployment

Build image:

```bash
docker build -t document-ingestion-pipeline .
```

Run container:

```bash
docker run -p 8000:8000 --env-file .env document-ingestion-pipeline
```

Using Docker Compose:

```bash
docker compose up --build
```

Stop:

```bash
docker compose down
```

---

## Testing

Run all tests:

```bash
pytest -v
```

Generate coverage report:

```bash
pytest --cov=src --cov-report=term-missing
```

Current Results:

```text
20 passed
57% coverage
```

---

## Completed Milestones

- Document Registration API
- File Upload API
- Validation Pipeline
- Metadata Extraction
- Duplicate Detection
- Multi-format Content Extraction
- Chunking Pipeline
- Embedding Generation
- FAISS Integration
- MongoDB Integration
- Async Background Processing
- Unit Testing
- Dockerization

---

## Upcoming Work

- Integration Testing
- CI/CD Pipeline

---

## Author

**Aniruddha More**

GitHub:
https://github.com/Aniruddha072

LinkedIn:
https://www.linkedin.com/in/aniruddha-more-376660328/