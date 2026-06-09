# Document Ingestion Pipeline

Learning and building a production-style document ingestion pipeline using FastAPI, MongoDB, and Vector Databases.

---

## Milestone 1 - Project Setup

Completed:

- Project structure setup
- FastAPI installation
- Virtual environment setup
- Health Check API
- Swagger Documentation

---

## Folder Structure

document-ingestion-pipeline/
│
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

---

## Health Check API

Endpoint:

GET /health

Response:

{
    "status": "healthy"
}

---

## Run Project

Activate virtual environment:

Windows:

.\venv\Scripts\activate

Start server:

uvicorn main:app --reload

Swagger:

http://127.0.0.1:8000/docs

---

## Next Milestone

Document Registry API

POST /documents

This API will create a document record in MongoDB and generate a unique document ID.