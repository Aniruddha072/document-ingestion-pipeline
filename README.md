# Document Ingestion Pipeline

Document ingestion pipeline built using FastAPI and MongoDB Atlas.

## Current Progress

### Completed

- FastAPI Setup
- Project Structure Setup
- Health Check API
- MongoDB Atlas Integration
- Database Connectivity Test
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

## Run Project

Activate virtual environment:

```powershell
.\venv\Scripts\activate
```

Start server:

```bash
uvicorn main:app --reload
```

Swagger:

```text
http://127.0.0.1:8000/docs
```

---

## Next Step

Implement Document Registry API:

```http
POST /documents
```