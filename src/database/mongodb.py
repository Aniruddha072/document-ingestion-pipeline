from pymongo import MongoClient
from pymongo.database import Database
from pymongo.collection import Collection

from config.settings import settings


def get_database() -> Database:
    """
    Create and return MongoDB database instance.
    """

    client = MongoClient(
        settings.mongo_uri
    )

    return client[
        settings.mongo_database
    ]


def get_documents_collection() -> Collection:
    """
    Return documents collection.
    """

    database = get_database()

    return database[
        settings.mongo_collection
    ]