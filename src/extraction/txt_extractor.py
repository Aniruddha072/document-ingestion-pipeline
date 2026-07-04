def extract_text_from_txt(
    file_path: str
) -> str:
    """
    Extract text from a TXT file.

    Args:
        file_path: Path to the TXT file.

    Returns:
        str: Extracted text.
    """

    with open(
        file_path,
        "r",
        encoding="utf-8"
    ) as file:

        return file.read()