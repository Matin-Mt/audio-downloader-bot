import asyncio

from telegram.ext import Application, CommandHandler, MessageHandler, filters

from core.config import get_settings, Settings
from commands import BotCommandSettings


class Main:
    settings: Settings = get_settings()

    def __init__(self):
        self.app = Application.builder().token(self.settings.TOKEN).build()
        self.BotCommands = BotCommandSettings(self.app)

    def add_command_handlers(self):
        self.app.add_handler(
            CommandHandler(
                "start",
                self.BotCommands.start_command()
            )
        )
        self.app.add_handler(
            CommandHandler(
                "help",
                self.BotCommands.help_command()
            )
        )
        self.app.add_handler(
            CommandHandler(
                "about",
                self.BotCommands.about_command()
            )
        )
        self.app.add_handler(
            CommandHandler(
                "settings",
                self.BotCommands.settings_command()
            )
        )
        self.app.add_handler(
            CommandHandler(
                "searchaudio",
                self.BotCommands.search_audio_command()
            )
        )

    def add_message_handlers(self):
        self.app.add_handler(
            MessageHandler(
                filters.AUDIO,
                self.BotCommands.store_audio_command()
            )
        )

    async def initialize(self):
        await self.BotCommands.set_bot_commands()
        await self.BotCommands.set_persistence_menu()
        self.add_command_handlers()
        self.add_message_handlers()

    def run(self):
        loop = asyncio.get_event_loop()  # Get the existing event loop
        loop.run_until_complete(self.initialize())  # Run async tasks without closing the loop
        print('running...')
        self.app.run_polling(poll_interval=0.5)  # Now this works fine


if __name__ == "__main__":
    main = Main()
    main.run()
