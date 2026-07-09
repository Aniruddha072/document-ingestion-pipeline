import os
from config.settings import settings

def validate_file_not_empty(
    file_path: str
) -> None:
    """
    Validate uploaded file is not empty.

    Args:
        file_path: Path to uploaded file.

    Raises:
        ValueError: If file is empty or cannot be accessed.
    """

    try:
        size = os.path.getsize(file_path)
    except OSError as error:
        raise ValueError(
            f"Failed to access file: {error}"
        )

    if size == 0:
        raise ValueError(
            "Uploaded file is empty."
        )


def validate_file_size(
    file_path: str
) -> None:
    """
    Validate uploaded file size.

    Args:
        file_path: Path to uploaded file.

    Raises:
        ValueError: If file exceeds size limit or cannot be accessed.
    """

    try:
        size = os.path.getsize(file_path)
    except OSError as error:
        raise ValueError(
            f"Failed to access file: {error}"
        )

    file_size_mb = size / (1024 * 1024)

    if file_size_mb > settings.max_file_size_mb:
        raise ValueError(
            f"File exceeds "
            f"{settings.max_file_size_mb} MB limit."
        )


def validate_document(
    file_path: str
) -> None:
    """
    Run all validation checks.

    Args:
        file_path: Path to uploaded file.

    Raises:
        ValueError: If any validation check fails.
    """

    validate_file_not_empty(
        file_path
    )

    validate_file_size(
        file_path
    )