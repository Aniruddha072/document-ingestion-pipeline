from pydantic import BaseModel


class DocumentCreate(BaseModel):

    document_name: str
    description: str

    