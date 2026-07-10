from fastapi import APIRouter
from src.database.mongodb import get_database

router = APIRouter()

@router.get("/db-test")
def test_db() -> dict[str, str]:
    """
    Verify MongoDB connectivity.

    Returns:
        dict: Database connection result.
    """

    db = get_database()

    db.command("ping")

    return {
        "message": "MongoDB Connected Successfully"
    }

    