from pypdf import PdfReader


def extract_text_from_pdf(
    pdf_path: str
) -> str:
    """
    Extract text from a PDF file.

    Args:
        pdf_path: Path to the PDF file.

    Returns:
        str: Extracted text.
    """

    reader = PdfReader(pdf_path)

    extracted_text = ""

    for page in reader.pages:

        page_text = (
            page.extract_text() or ""
        )

        extracted_text += (
            page_text + "\n"
        )

    return extracted_text