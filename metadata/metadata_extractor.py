import os


def extract_file_metadata(
    file_path: str
) -> dict[str, str | int]:
    """
    Extract file-level metadata.

    Args:
        file_path: Path to the uploaded document.

    Returns:
        dict: File metadata.
    """

    return {
        "file_name": os.path.basename(
            file_path
        ),

        "file_type": os.path.splitext(
            file_path
        )[1].lower(),

        "file_size": os.path.getsize(
            file_path
        )
    }


def extract_content_metadata(
    extracted_text: str
) -> dict[str, int]:
    """
    Extract content-level metadata.

    Args:
        extracted_text: Extracted document text.

    Returns:
        dict: Content metadata.
    """

    return {
        "word_count": len(
            extracted_text.split()
        ),

        "character_count": len(
            extracted_text
        ),

        "line_count": len(
            extracted_text.splitlines()
        )
    }