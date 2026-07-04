import os

from src.extraction.pdf_extractor import (
    extract_text_from_pdf
)

from src.extraction.txt_extractor import (
    extract_text_from_txt
)

from src.extraction.docx_extractor import (
    extract_text_from_docx
)


def extract_text(
    file_path: str
) -> str:
    """
    Extract text from a supported file.

    Args:
        file_path: Path to the file.

    Returns:
        str: Extracted text.
    """

    extension = (
        os.path.splitext(
            file_path
        )[1].lower()
    )

    if extension == ".pdf":

        return extract_text_from_pdf(
            file_path
        )

    if extension == ".txt":

        return extract_text_from_txt(
            file_path
        )

    if extension == ".docx":

        return extract_text_from_docx(
            file_path
        )

    raise ValueError(
        f"Unsupported file type: {extension}"
    )