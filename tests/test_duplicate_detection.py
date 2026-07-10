import pytest

from src.validation.duplicate_detector import (
    generate_document_hash
)


def test_same_file_same_hash(
    tmp_path
):
    """
    Hashing the same file twice should
    produce the same SHA256 hash.
    """

    file_path = (
        tmp_path / "sample.txt"
    )

    file_path.write_text(
        "Hello World"
    )

    hash_one = (
        generate_document_hash(
            str(file_path)
        )
    )

    hash_two = (
        generate_document_hash(
            str(file_path)
        )
    )

    assert hash_one == hash_two


def test_different_files_different_hashes(
    tmp_path
):
    """
    Different file contents should
    generate different hashes.
    """

    file_one = (
        tmp_path / "one.txt"
    )

    file_two = (
        tmp_path / "two.txt"
    )

    file_one.write_text(
        "Hello World"
    )

    file_two.write_text(
        "Different Content"
    )

    hash_one = (
        generate_document_hash(
            str(file_one)
        )
    )

    hash_two = (
        generate_document_hash(
            str(file_two)
        )
    )

    assert hash_one != hash_two


def test_missing_file_hash_generation():
    """
    Missing file should raise ValueError.
    """

    with pytest.raises(
        ValueError,
        match="Failed to read file for hashing"
    ):
        generate_document_hash(
            "missing_file.txt"
        )