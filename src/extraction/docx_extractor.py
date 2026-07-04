from docx import Document


def extract_text_from_docx(
    file_path: str
) -> str:
    """
    Extract text from a DOCX file.

    Args:
        file_path: Path to the DOCX file.

    Returns:
        str: Extracted text.
    """

    document = Document(
        file_path
    )

    extracted_text = ""

    for paragraph in document.paragraphs:

        extracted_text += (
            paragraph.text + "\n"
        )

    return extracted_text