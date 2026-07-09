from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    mongo_uri: str
    mongo_database: str
    mongo_collection: str

    chunk_size: int
    chunk_overlap: int

    embedding_model: str
    vectorstore_path: str
    raw_storage_path: str

    max_file_size_mb: int = 20
    
    class Config:
        env_file = ".env"


settings = Settings()