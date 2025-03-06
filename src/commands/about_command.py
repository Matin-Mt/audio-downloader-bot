from telegram import Update
from telegram.ext import CallbackContext

from src.core.config import Settings, get_settings


class AboutCommand:
    def __init__(self):
        self.settings: Settings = get_settings()

    async def about_command(self, update: Update, context: CallbackContext) -> None:
        await update.message.reply_text(
            f"About:\n"
            f"I am a bot to help you in your music adventure\n"
        )
