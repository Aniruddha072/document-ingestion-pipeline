# Document Ingestion Pipeline

A FastAPI-based document ingestion service that extracts text from documents, generates embeddings, and stores vector representations using FAISS for downstream retrieval and AI applications.

## Features

- Document registration and tracking
- File upload and storage
- Multi-format document extraction
  - PDF
  - TXT
  - DOCX
- Automatic extractor selection using a factory pattern
- Document chunking using LangChain
- Embedding generation using HuggingFace models
- FAISS vector store creation
- MongoDB metadata storage
- Error handling and validation
- Configurable settings using environment variables

---

## Project Structure

```text
document-ingestion-pipeline/
│
├── config/
│   └── settings.py
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
│   ├── database/
│   │   └── mongodb.py
│   │
│   ├── extraction/
│   │   ├── extractor_factory.py
│   │   ├── pdf_extractor.py
│   │   ├── txt_extractor.py
│   │   └── docx_extractor.py
│   │
│   ├── chunking/
│   │   └── text_splitter.py
│   │
│   ├── embeddings/
│   │   └── embedding_model.py
│   │
│   ├── vectorstore/
│   │   └── faiss_manager.py
│   │
│   ├── services/
│   │   ├── document_service.py
│   │   ├── upload_service.py
│   │   ├── ingestion_service.py
│   │   └── status_service.py
│   │
│   └── schemas/
│       └── document_schema.py
│
├── storage/
│   ├── raw/
│   └── vectorstore/
│
├── .env
├── main.py
├── requirements.txt
└── README.md
```

---

## Supported File Types

| Format | Supported |
|----------|----------|
| PDF | Yes |
| TXT | Yes |
| DOCX | Yes |

---

## Processing Flow

```text
Document Upload
        │
        ▼
Document Storage
        │
        ▼
Extractor Factory
        │
 ┌──────┼──────┐
 │      │      │
 ▼      ▼      ▼
PDF    TXT    DOCX
 │      │      │
 └──────┴──────┘
        │
        ▼
Text Extraction
        │
        ▼
Chunking
        │
        ▼
Embeddings
        │
        ▼
FAISS Vector Store
        │
        ▼
Metadata Update
```

---

## Environment Variables

Create a `.env` file:

```env
mongo_uri=YOUR_MONGODB_URI
mongo_database=document_ingestion
mongo_collection=documents

chunk_size=500
chunk_overlap=50

embedding_model=sentence-transformers/all-MiniLM-L6-v2

raw_storage_path=storage/raw
vectorstore_path=storage/vectorstore
```

---

## Installation

Clone the repository:

```bash
git clone <repository-url>
cd document-ingestion-pipeline
```

Create and activate a virtual environment:

```bash
python -m venv venv
```

Windows:

```bash
.\venv\Scripts\activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

## Run the Application

```bash
uvicorn main:app --reload
```

Swagger UI:

```text
http://127.0.0.1:8000/docs
```

---

## Available Endpoints

### Create Document

```http
POST /documents
```

Creates a document record.

---

### Upload Document

```http
POST /documents/{doc_id}/upload
```

Uploads a supported document.

---

### Trigger Ingestion

```http
POST /documents/{doc_id}/ingest
```

Extracts text, creates chunks, generates embeddings, and stores vectors.

---

### Get Document Status

```http
GET /documents/{doc_id}/status
```

Returns ingestion status and metadata.

---

### Health Check

```http
GET /health
```

---

### MongoDB Connectivity Check

```http
GET /db-test
```

---

## Current Capabilities

- Multi-format document extraction
- Configurable chunking
- Embedding generation
- Vector store persistence
- MongoDB metadata management
- Factory-based extraction architecture
- Error handling and validation
- Type hints and docstrings

---

## Next Steps

- Metadata extraction
- Additional file format support
- OCR support for scanned documents
- Retrieval pipeline
- Search APIs