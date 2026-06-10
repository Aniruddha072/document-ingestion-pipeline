from fastapi import FastAPI

from src.api.health import router as health_router
from src.api.test_db import router as db_router
from src.api.documents import router as documents_router
from src.api.upload import router as upload_router

app = FastAPI(
    title="Document Ingestion Pipeline"
)

app.include_router(health_router)
app.include_router(db_router)
app.include_router(documents_router)
app.include_router(upload_router)