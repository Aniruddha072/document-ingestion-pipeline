from langchain_core.documents import Document
from langchain_text_splitters import RecursiveCharacterTextSplitter

from config.settings import settings


def split_documents(
    documents: list[Document]
) -> list[Document]:
    """
    Split documents into smaller chunks.

    Args:
        documents (list[Document]):
            Documents to split.

    Returns:
        list[Document]:
            Chunked documents.
    """

    splitter = RecursiveCharacterTextSplitter(
        chunk_size=settings.chunk_size,
        chunk_overlap=settings.chunk_overlap,
    )

    return splitter.split_documents(documents)