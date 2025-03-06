from pymongo import MongoClient
import gridfs

from core.config import get_settings

settings = get_settings()

mongo_uri = f"mongodb://{settings.MONGO_USER}" \
            f":{settings.MONGO_PASSWORD}@" \
            f"{settings.MONGO_HOST}:" \
            f"{settings.MONGO_PORT}/" \
            f"{settings.MONGO_DB}" \
            f"?authSource=admin"

client = MongoClient(mongo_uri)

db = client[settings.MONGO_DB]
fs = gridfs.GridFS(db)
