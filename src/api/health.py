from fastapi import APIRouter

router = APIRouter()


@router.get("/health")
def health_check() -> dict[str, str]:
    """
    Check whether the API service is running.

    Returns:
        dict: Service health status.
    """

    return {
        "status": "healthy"
    }