from telegram import Update
from telegram.ext import CallbackContext

from src.core.config import Settings, get_settings


class HelpCommand:
    def __init__(self):
        self.settings: Settings = get_settings()

    async def help_command(self, update: Update, context: CallbackContext) -> None:
        await update.message.reply_text(
            f"Help: \n"
            f"If you got stuck somewhere, use /start command to restart the bot.\n\n"
            f"Commands: \n"
            f"/start - to start/restart the bot\n"
            f"/help - to get help\n"
            f"/about - to get information about the bot\n"
            f"/settings - to adjust bot settings\n"
            f"/searchaudio - to search for audio by performer's name\n"
        )
