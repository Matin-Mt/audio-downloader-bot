from telegram import Update, BotCommand, MenuButtonCommands, ReplyKeyboardMarkup
from telegram.ext import Application, CallbackContext

from src.commands.start_command import StartCommand
from src.commands.help_command import HelpCommand
from src.commands.about_command import AboutCommand
from src.commands.settings_command import SettingsCommand
from src.commands.audio_command import AudioCommand


class BotCommandSettings:
    COMMANDS = (
        BotCommand("start", "Start the bot"),
        BotCommand("help", "Get help"),
        BotCommand("about", "About this bot"),
        BotCommand("settings", "Adjust bot settings"),
    )
    KEYBOARD = [
        ["🎵 Search Audio", "ℹ️ Help"],
        ["🔄 Refresh", "❌ Cancel"]
    ]

    def __init__(self, application: Application):
        self.application = application
        self.START_Command = StartCommand()
        self.HELP_Command = HelpCommand()
        self.ABOUT_Command = AboutCommand()
        self.SETTINGS_Command = SettingsCommand()
        self.AUDIO_Command = AudioCommand()

    def start_command(self):
        async def command(update: Update, context: CallbackContext):
            await self.START_Command.start_command(update, context)
            # reply_markup = ReplyKeyboardMarkup(self.KEYBOARD, resize_keyboard=True)
            # await update.message.reply_text("Choose an option:", reply_markup=reply_markup)
        return command

    def help_command(self):
        async def command(update: Update, context: CallbackContext):
            await self.HELP_Command.help_command(update, context)
        return command

    def about_command(self):
        async def command(update: Update, context: CallbackContext):
            await self.ABOUT_Command.about_command(update, context)
        return command

    def settings_command(self):
        async def command(update: Update, context: CallbackContext):
            await self.SETTINGS_Command.settings_command(update, context)
        return command

    def store_audio_command(self):
        async def command(update: Update, context: CallbackContext):
            await self.AUDIO_Command.store_audio_command(update, context)
        return command

    def search_audio_command(self):
        async def command(update: Update, context: CallbackContext):
            await self.AUDIO_Command.search_audio_command(update, context)
        return command

    async def set_bot_commands(self):
        await self.application.bot.set_my_commands(self.COMMANDS)

    async def set_persistence_menu(self):
        await self.application.bot.set_chat_menu_button(
            menu_button=MenuButtonCommands()
        )


__all__ = ["BotCommandSettings"]
