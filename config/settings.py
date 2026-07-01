from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    mongo_uri: str
    mongo_database: str
    mongo_collection: str

    chunk_size: int
    chunk_overlap: int

    class Config:
        env_file = ".env"


settings = Settings()