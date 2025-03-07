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
    MONGO_ATLAS_URI: Final = os.getenv('MONGO_ATLAS_URI')


@lru_cache()
def get_settings() -> Settings:
    return Settings()
