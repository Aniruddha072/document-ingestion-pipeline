from fastapi import APIRouter
from src.database.mongodb import db

router = APIRouter()

@router.get("/db-test")
def test_db():

    db.command("ping")

    return {
        "message": "MongoDB Connected Successfully"
    }