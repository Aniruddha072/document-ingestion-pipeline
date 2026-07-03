from src.extraction.pdf_extractor import (
    extract_text_from_pdf
)


def extract_text(
    file_path: str
) -> str:

    if file_path.endswith(".pdf"):
        return extract_text_from_pdf(
            file_path
        )

    raise ValueError(
        "Unsupported file type"
    )