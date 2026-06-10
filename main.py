from fastapi import FastAPI

from src.api.health import router as health_router
from src.api.test_db import router as db_router

app = FastAPI(
    title="Document Ingestion Pipeline"
)

app.include_router(health_router)
app.include_router(db_router)