from fastapi import APIRouter
from src.database.mongodb import get_database

router = APIRouter()

@router.get("/db-test")
def test_db():

    db = get_database()

    db.command("ping")

    return {
        "message": "MongoDB Connected Successfully"
    }

    