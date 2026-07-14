# Document Ingestion Pipeline

A production-style document ingestion pipeline built with FastAPI that validates, processes, and stores documents for downstream Retrieval-Augmented Generation (RAG) systems.

---

## Overview

This project automates the complete document ingestion workflow:

- Document Registration
- File Upload
- Document Validation
- Duplicate Detection (SHA-256)
- Metadata Extraction
- Multi-format Content Extraction
- Text Chunking
- Embedding Generation
- FAISS Vector Storage
- MongoDB Persistence
- Async Background Processing

---

## Features

### Document Management
- Register documents
- Upload files
- Track processing status

### Validation
- File type validation
- File size validation
- SHA-256 duplicate detection

### Content Processing
- PDF extraction
- DOCX extraction
- TXT extraction
- Metadata generation

### AI Pipeline
- LangChain text chunking
- Sentence Transformer embeddings
- FAISS vector storage

### Engineering
- FastAPI backend
- MongoDB Atlas integration
- Dockerized deployment
- GitHub Actions CI/CD
- Unit & Integration Testing

---

## Architecture

```text
Client
   │
   ▼
FastAPI API
   │
   ├── MongoDB Atlas
   │
   ├── Raw File Storage
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
Embeddings
   │
   ▼
FAISS Vector Store
```

---

## Project Structure

```text
document-ingestion-pipeline/
│
├── src/
│   ├── api/
│   ├── services/
│   ├── extraction/
│   ├── chunking/
│   ├── embeddings/
│   ├── vectorstore/
│   ├── validation/
│   ├── database/
│   └── schemas/
│
├── tests/
│   ├── integration/
│   └── unit tests
│
├── storage/
│   ├── raw/
│   └── vectorstore/
│
├── config/
│
├── .github/workflows/
│
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
└── main.py
```

---

## Workflow

```text
Register Document
        │
        ▼
Upload Document
        │
        ▼
Validate File
        │
        ▼
Duplicate Detection
        │
        ▼
Store Raw File
        │
        ▼
Trigger Ingestion
        │
        ▼
Extract Content
        │
        ▼
Generate Metadata
        │
        ▼
Chunk Text
        │
        ▼
Generate Embeddings
        │
        ▼
Store in FAISS
        │
        ▼
Update MongoDB Status
```

---

## API Endpoints

| Method | Endpoint | Description |
|----------|----------|-------------|
| POST | `/documents` | Register a document |
| POST | `/documents/{doc_id}/upload` | Upload a file |
| POST | `/documents/{doc_id}/ingest` | Trigger ingestion |
| GET | `/documents/{doc_id}/status` | Get processing status |
| GET | `/health` | Health check |
| GET | `/db-test` | MongoDB connectivity check |

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

Windows:

```bash
venv\Scripts\activate
```

Linux/macOS:

```bash
source venv/bin/activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Configure Environment Variables

Create a `.env` file:

```env
mongo_uri=YOUR_MONGODB_URI
mongo_database=document_ingestion
mongo_collection=documents

chunk_size=500
chunk_overlap=50

embedding_model=sentence-transformers/all-MiniLM-L6-v2

vectorstore_path=storage/vectorstore
raw_storage_path=storage/raw
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

## Docker

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

### Results

```text
25 Tests Passed
0 Failed
84% Coverage
```

---

## CI/CD

GitHub Actions automatically runs on:

- Push to `main`
- Pull Requests to `main`

Pipeline stages:

```text
Checkout Repository
        │
        ▼
Setup Python
        │
        ▼
Install Dependencies
        │
        ▼
Run Tests
        │
        ▼
Generate Coverage
```

Repository secrets are used to securely provide MongoDB and application configuration during workflow execution.

---

## Technology Stack

### Backend
- FastAPI
- Uvicorn

### Database
- MongoDB Atlas

### AI / NLP
- LangChain
- Sentence Transformers

### Vector Store
- FAISS

### Testing
- Pytest
- Pytest-Cov

### DevOps
- Docker
- Docker Compose
- GitHub Actions

---

## Project Status

| Component | Status |
|------------|----------|
| Document Registration API | ✅ |
| File Upload API | ✅ |
| Validation Pipeline | ✅ |
| Duplicate Detection | ✅ |
| Metadata Extraction | ✅ |
| Multi-format Extraction | ✅ |
| Chunking Pipeline | ✅ |
| Embedding Generation | ✅ |
| FAISS Integration | ✅ |
| MongoDB Integration | ✅ |
| Async Background Processing | ✅ |
| Unit Testing | ✅ |
| Integration Testing | ✅ |
| Dockerization | ✅ |
| CI/CD Pipeline | ✅ |

---

## Author

**Aniruddha More**

GitHub: https://github.com/Aniruddha072

LinkedIn: https://www.linkedin.com/in/aniruddha-more-376660328/