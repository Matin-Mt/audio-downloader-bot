from telegram import Update
from telegram.ext import CallbackContext

from src.core.config import Settings, get_settings


class StartCommand:
    def __init__(self):
        self.settings: Settings = get_settings()

    async def start_command(self, update: Update, context: CallbackContext) -> None:
        await update.message.reply_text(f"Hello {update.effective_user.first_name}! I am {self.settings.BOT_USERNAME}")
