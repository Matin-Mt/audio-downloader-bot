from typing import Final
from dotenv import load_dotenv
from pathlib import Path
import os
from functools import lru_cache

dotenv_path = Path(__file__).parent / ".env"
load_dotenv(dotenv_path, override=True)


class Settings:
    TOKEN: Final = os.getenv('TOKEN')
    BOT_USERNAME: Final = os.getenv('BOT_USERNAME')
    CHANNEL_USERNAME: Final = os.getenv('CHANNEL_USERNAME')
    MONGO_HOST = os.getenv("MONGO_HOST")
    MONGO_PORT = int(os.getenv("MONGO_PORT"))
    MONGO_DB = os.getenv("MONGO_DB")
    MONGO_USER = os.getenv("MONGO_USER")
    MONGO_PASSWORD = os.getenv("MONGO_PASSWORD")


@lru_cache()
def get_settings() -> Settings:
    return Settings()
