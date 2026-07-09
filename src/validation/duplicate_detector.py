import hashlib
from pymongo.collection import Collection


def generate_document_hash(file_path: str) -> str:
    """
    Generate a SHA256 hash for a file by reading it in chunks.

    Reads the file in 8 KB chunks to support large files without
    loading the entire content into memory at once.

    Args:
        file_path: Absolute or relative path to the file on disk.

    Returns:
        Hexadecimal SHA256 hash string of the file contents.

    Raises:
        ValueError: If the file cannot be read or accessed.
    """

    sha256 = hashlib.sha256()

    try:
        with open(file_path, "rb") as file:
            while True:
                chunk = file.read(8192)
                if not chunk:
                    break
                sha256.update(chunk)
    except OSError as error:
        raise ValueError(
            f"Failed to read file for hashing: {error}"
        )

    return sha256.hexdigest()


def check_duplicate_hash(
    document_hash: str,
    documents_collection: Collection
) -> None:
    """
    Check whether a document with the given hash already exists in MongoDB.

    Queries the provided MongoDB collection for a document whose
    ``document_hash`` field matches the supplied precomputed hash.
    Separating hash generation from this check ensures the hash is
    computed exactly once by the caller and reused for both duplicate
    detection and storage.

    Args:
        document_hash: Precomputed SHA256 hex digest of the file.
        documents_collection: PyMongo ``Collection`` instance to
            search for existing documents.

    Raises:
        ValueError: If a document with the same hash already exists
            in the collection.
    """

    existing_document = documents_collection.find_one(
        {"document_hash": document_hash}
    )

    if existing_document:
        raise ValueError("Document already exists.")
