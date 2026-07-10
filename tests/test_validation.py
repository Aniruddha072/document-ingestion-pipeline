import pytest

from src.validation.document_validator import (
    validate_file_not_empty,
    validate_file_size
)


def test_non_empty_file(
    tmp_path
):
    """
    Valid file should pass validation.
    """

    test_file = (
        tmp_path / "sample.txt"
    )

    test_file.write_text(
        "Hello World"
    )

    validate_file_not_empty(
        str(test_file)
    )


def test_empty_file(
    tmp_path
):
    """
    Empty file should raise ValueError.
    """

    test_file = (
        tmp_path / "empty.txt"
    )

    test_file.write_text("")

    with pytest.raises(
        ValueError,
        match="Uploaded file is empty."
    ):
        validate_file_not_empty(
            str(test_file)
        )


def test_missing_file():
    """
    Missing file should raise ValueError.
    """

    with pytest.raises(
        ValueError,
        match="Failed to access file"
    ):
        validate_file_not_empty(
            "does_not_exist.txt"
        )


def test_file_size_validation_passes(
    tmp_path
):
    """
    Small file should pass size validation.
    """

    test_file = (
        tmp_path / "small.txt"
    )

    test_file.write_text(
        "Hello World"
    )

    validate_file_size(
        str(test_file)
    )