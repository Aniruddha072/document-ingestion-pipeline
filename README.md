# Document Ingestion Pipeline

A production-oriented document ingestion service built with FastAPI, MongoDB, LangChain, Sentence Transformers, and FAISS.

This system provides a complete ingestion workflow for enterprise documents, including validation, duplicate detection, metadata extraction, text extraction, chunking, embedding generation, vector storage, and asynchronous background processing.

The pipeline is designed as a foundational layer for Retrieval-Augmented Generation (RAG), Knowledge Management Systems, Enterprise Search, and AI-powered document intelligence platforms.

---

# Overview

The Document Ingestion Pipeline automates the process of transforming raw documents into vectorized, searchable knowledge assets.

Supported document types are uploaded through FastAPI APIs, validated, processed asynchronously, converted into embeddings, and stored in FAISS vector indexes for downstream retrieval applications.

---

# Features

## Document Management

- Document Registration API
- Unique Document ID Generation
- MongoDB Document Tracking
- Document Status Management

## Upload Pipeline

- PDF Upload Support
- DOCX Upload Support
- TXT Upload Support
- Secure File Storage

## Validation Layer

- Empty File Validation
- File Size Validation
- Supported File Type Validation
- SHA256 Duplicate Detection

## Metadata Processing

### File Metadata

- File Name
- File Size
- File Extension

### Content Metadata

- Character Count
- Word Count
- Paragraph Count
- Page Count
- Estimated Reading Time

### Processing Metadata

- Chunk Count
- Embedding Model Used
- Ingestion Timestamp

## AI Processing Pipeline

- Multi-format Text Extraction
- Document Chunking
- Embedding Generation
- FAISS Vector Storage

## Processing Architecture

- Background Task Processing
- Asynchronous Ingestion
- Status Tracking
- Error Handling

## Engineering Features

- Service Layer Architecture
- Dependency Separation
- Environment-based Configuration
- Unit Testing
- Coverage Reporting

---

# System Architecture

```text
                           ┌─────────────────┐
                           │     Client      │
                           └────────┬────────┘
                                    │
                                    ▼
                      ┌──────────────────────────┐
                      │         FastAPI          │
                      └───────────┬──────────────┘
                                  │
        ┌─────────────────────────┼─────────────────────────┐
        │                         │                         │
        ▼                         ▼                         ▼

┌─────────────────┐   ┌─────────────────┐   ┌─────────────────┐
│ Registration API│   │   Upload API    │   │  Ingestion API  │
└────────┬────────┘   └────────┬────────┘   └────────┬────────┘
         │                     │                     │
         ▼                     ▼                     ▼

┌───────────────────────────────────────────────────────────┐
│                        MongoDB                             │
└───────────────────────────────────────────────────────────┘
                                  │
                                  ▼

                   ┌─────────────────────────────┐
                   │ Background Processing Layer │
                   └──────────────┬──────────────┘
                                  │
                                  ▼

                   ┌─────────────────────────────┐
                   │      Text Extraction        │
                   └──────────────┬──────────────┘
                                  │
                                  ▼

                   ┌─────────────────────────────┐
                   │    Metadata Extraction      │
                   └──────────────┬──────────────┘
                                  │
                                  ▼

                   ┌─────────────────────────────┐
                   │         Chunking            │
                   └──────────────┬──────────────┘
                                  │
                                  ▼

                   ┌─────────────────────────────┐
                   │     Embedding Model         │
                   └──────────────┬──────────────┘
                                  │
                                  ▼

                   ┌─────────────────────────────┐
                   │      FAISS Vector DB        │
                   └─────────────────────────────┘
```

---

# Document Lifecycle

```text
REGISTER DOCUMENT
        │
        ▼
UPLOAD FILE
        │
        ▼
VALIDATE FILE
        │
        ▼
CHECK DUPLICATES
        │
        ▼
START INGESTION
        │
        ▼
EXTRACT TEXT
        │
        ▼
EXTRACT METADATA
        │
        ▼
CHUNK DOCUMENT
        │
        ▼
GENERATE EMBEDDINGS
        │
        ▼
STORE IN FAISS
        │
        ▼
MARK COMPLETED
```

---

# Project Structure

```text
document-ingestion-pipeline/
│
├── config/
│   └── settings.py
│
├── metadata/
│   ├── metadata_extractor.py
│   └── metadata_factory.py
│
├── src/
│   │
│   ├── api/
│   │   ├── documents.py
│   │   ├── upload.py
│   │   ├── ingestion.py
│   │   ├── status.py
│   │   └── health.py
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
│   ├── validation/
│   │   ├── document_validator.py
│   │   └── duplicate_detector.py
│   │
│   ├── extraction/
│   │   ├── pdf_extractor.py
│   │   ├── docx_extractor.py
│   │   ├── txt_extractor.py
│   │   └── extractor_factory.py
│   │
│   ├── chunking/
│   │   └── text_splitter.py
│   │
│   ├── embeddings/
│   │   └── embedding_model.py
│   │
│   └── vectorstore/
│       └── faiss_manager.py
│
├── tests/
│   ├── test_document_service.py
│   ├── test_upload_service.py
│   ├── test_ingestion_service.py
│   ├── test_validation.py
│   ├── test_duplicate_detection.py
│   └── test_metadata.py
│
├── storage/
│   ├── raw/
│   └── vectorstores/
│
├── main.py
├── requirements.txt
├── pytest.ini
└── README.md
```

---

# Technology Stack

| Layer | Technology |
|---------|------------|
| Backend Framework | FastAPI |
| Database | MongoDB |
| Vector Database | FAISS |
| AI Framework | LangChain |
| Embeddings | Sentence Transformers |
| PDF Processing | PyPDF |
| DOCX Processing | python-docx |
| Testing | Pytest |
| Language | Python 3.13 |

---

# API Endpoints

## Register Document

### Request

```http
POST /documents
```

### Example Body

```json
{
  "document_name": "sample.pdf",
  "description": "Sample document"
}
```

### Response

```json
{
  "doc_id": "DOC-12345678",
  "status": "NOT_STARTED"
}
```

---

## Upload Document

### Request

```http
POST /documents/{doc_id}/upload
```

### Response

```json
{
  "message": "Document uploaded successfully"
}
```

---

## Start Ingestion

### Request

```http
POST /documents/{doc_id}/ingest
```

### Response

```json
{
  "message": "Document ingestion started"
}
```

---

## Check Status

### Request

```http
GET /documents/{doc_id}/status
```

### Example Response

```json
{
  "status": "PROCESSING"
}
```

Possible statuses:

```text
NOT_STARTED
PROCESSING
COMPLETED
FAILED
```

---

# Metadata Extraction

## File Metadata

```json
{
  "file_name": "sample.pdf",
  "file_size_mb": 2.5,
  "file_extension": ".pdf"
}
```

## Content Metadata

```json
{
  "character_count": 15000,
  "word_count": 2400,
  "paragraph_count": 120,
  "page_count": 15,
  "estimated_read_time_minutes": 10
}
```

## Processing Metadata

```json
{
  "chunk_count": 45,
  "embedding_model": "all-MiniLM-L6-v2",
  "ingested_at": "timestamp"
}
```

---

# Validation Pipeline

Before ingestion, every document passes through:

## File Validation

- File exists
- File not empty
- File size within limit
- Supported extension

## Duplicate Validation

The pipeline generates a SHA256 hash for every uploaded file.

If an identical document has already been uploaded:

```text
Duplicate document detected
```

and ingestion is prevented.

---

# Embedding Pipeline

## Step 1

Extract document text.

## Step 2

Split text into chunks using LangChain.

## Step 3

Generate embeddings using Sentence Transformers.

Model:

```text
all-MiniLM-L6-v2
```

## Step 4

Store vectors in FAISS.

---

# Background Processing

Document ingestion is executed asynchronously.

The API returns immediately:

```json
{
  "message": "Document ingestion started"
}
```

while processing continues in the background.

Advantages:

- Faster API response
- Better scalability
- Improved user experience
- Long-running jobs do not block requests

---

# Unit Testing

The project includes automated unit testing using Pytest.

Covered components:

- Validation Layer
- Duplicate Detection
- Metadata Extraction
- Document Service
- Upload Service
- Ingestion Service

---

# Current Test Coverage

Coverage generated using:

```bash
pytest --cov=src --cov=metadata
```

| Component | Coverage |
|------------|------------|
| Document Service | 100% |
| Ingestion Service | 88% |
| Upload Service | 64% |
| Validation Layer | 75%+ |
| Duplicate Detection | 83% |

### Overall Coverage

```text
57%
```

---

# Engineering Decisions

## Why MongoDB?

MongoDB provides flexible document storage suitable for storing metadata, processing status, and ingestion results.

---

## Why FAISS?

FAISS offers fast vector similarity search without requiring an external vector database.

This makes local development and experimentation significantly easier.

---

## Why Background Processing?

Embedding generation and vector creation can take several seconds depending on document size.

Running ingestion in the background prevents API blocking.

---

## Why SHA256 Duplicate Detection?

File names can change.

Document content usually does not.

Using SHA256 ensures duplicate detection is based on content rather than file name.

---

# Production Considerations

Implemented:

- Layered architecture
- Service abstraction
- Error handling
- Environment configuration
- Duplicate prevention
- Metadata enrichment
- Background processing
- Unit testing

---

# Setup

## Clone Repository

```bash
git clone <repository-url>
cd document-ingestion-pipeline
```

## Create Virtual Environment

```bash
python -m venv venv
```

### Windows

```bash
venv\Scripts\activate
```

### Linux / macOS

```bash
source venv/bin/activate
```

## Install Dependencies

```bash
pip install -r requirements.txt
```

## Configure Environment

Create:

```text
.env
```

Example:

```env
MONGO_URI=your_mongodb_uri
DATABASE_NAME=document_ingestion
EMBEDDING_MODEL=all-MiniLM-L6-v2
RAW_STORAGE_PATH=storage/raw
VECTORSTORE_PATH=storage/vectorstores
```

## Run Application

```bash
uvicorn main:app --reload
```

Application:

```text
http://localhost:8000
```

Swagger Documentation:

```text
http://localhost:8000/docs
```

---

# Project Status

| Component | Status |
|------------|---------|
| Document Registration | ✅ |
| Upload API | ✅ |
| Validation Layer | ✅ |
| Duplicate Detection | ✅ |
| Metadata Extraction | ✅ |
| Multi-format Extraction | ✅ |
| Chunking Pipeline | ✅ |
| Embedding Pipeline | ✅ |
| FAISS Storage | ✅ |
| Async Background Processing | ✅ |
| Unit Testing | ✅ |
| Integration Testing | ⬜ |
| Dockerization | ⬜ |
| CI/CD | ⬜ |

---
