from pymongo.mongo_client import MongoClient
import gridfs

from src.core.config import get_settings

settings = get_settings()
uri = settings.MONGO_ATLAS_URI

client = MongoClient(uri)

db = client["TelegramBotDB"]
fs = gridfs.GridFS(db)

try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)
