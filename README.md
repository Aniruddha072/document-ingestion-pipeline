# Document Ingestion Pipeline

A document ingestion pipeline built using FastAPI and MongoDB Atlas.

## Current Progress

### Completed

- FastAPI Setup
- Project Structure Setup
- Health Check API
- MongoDB Atlas Integration
- Database Connectivity Test API
- Document Registry API
- Unique Document ID Generation
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

### Database Test

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
    "doc_id": "DOC-a1b2c3d4",
    "status": "NOT_STARTED"
}
```

Document stored in MongoDB:

```json
{
    "doc_id": "DOC-a1b2c3d4",
    "document_name": "Army Recruitment",
    "description": "Recruitment Notification",
    "status": "NOT_STARTED",
    "document_path": null,
    "extracted_text": null
}
```

---

## Technologies Used

- FastAPI
- Uvicorn
- MongoDB Atlas
- PyMongo
- Pydantic
- Python Dotenv

---

## Run Project

Activate virtual environment:

```powershell
.\venv\Scripts\activate
```

Run server:

```bash
uvicorn main:app --reload
```

Open Swagger:

```text
http://127.0.0.1:8000/docs
```

---

## Next Step

Implement PDF Upload API:

```http
POST /documents/{doc_id}/upload
```

Upload a PDF file, store it in the backend `raw/` folder, and update the document record with the file path.