import math
import os
from pypdf import PdfReader


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
    extracted_text: str,
    file_path: str
) -> dict[str, int | None]:
    """
    Extract content-level metadata.

    Args:
        extracted_text: Extracted document text.
        file_path: Path to uploaded document.

    Returns:
        dict: Content metadata.
    """

    word_count = len(
        extracted_text.split()
    )

    paragraphs = [
        paragraph.strip()
        for paragraph in extracted_text.split(
            "\n\n"
        )
        if paragraph.strip()
    ]

    page_count = None

    if file_path.lower().endswith(
        ".pdf"
    ):
        try:
            reader = PdfReader(
                file_path
            )

            page_count = len(
                reader.pages
            )

        except Exception:
            page_count = None

    return {
        "word_count": word_count,

        "character_count": len(
            extracted_text
        ),

        "line_count": len(
            extracted_text.splitlines()
        ),

        "paragraph_count": len(
            paragraphs
        ),

        "page_count": page_count,

        "estimated_read_time_minutes":
            max(
                1,
                math.ceil(
                    word_count / 200
                )
            )
    }