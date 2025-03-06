from telegram import Update
from telegram.ext import CallbackContext

from src.core.config import Settings, get_settings


class SettingsCommand:
    def __init__(self):
        self.settings: Settings = get_settings()

    async def settings_command(self, update: Update, context: CallbackContext) -> None:
        await update.message.reply_text(
            f"Not Available"
        )
