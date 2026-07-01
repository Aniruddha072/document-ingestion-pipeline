from langchain_community.embeddings import HuggingFaceEmbeddings

from config.settings import settings

def get_embedding_model() -> HuggingFaceEmbeddings:
    """
    Create and return the embedding model used for
    generating document embeddings.

    Returns:
        HuggingFaceEmbeddings: Configured embedding model.
    """

    return HuggingFaceEmbeddings(
        model_name=settings.embedding_model
    )

    