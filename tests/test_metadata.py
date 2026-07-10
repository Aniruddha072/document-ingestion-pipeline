from metadata.metadata_extractor import (
    extract_content_metadata
)


def test_metadata_extraction():
    """
    Verify metadata extraction fields.
    """

    text = """
    First paragraph.

    Second paragraph.

    Third paragraph.
    """

    metadata = (
        extract_content_metadata(
            text,
            "sample.txt"
        )
    )

    assert metadata["word_count"] > 0
    assert metadata["character_count"] > 0
    assert metadata["line_count"] > 0
    assert metadata["paragraph_count"] == 3
    
    assert (
        metadata[
            "estimated_read_time_minutes"
        ]
        == 1
    )

    assert (
        metadata["page_count"]
        is None
    )