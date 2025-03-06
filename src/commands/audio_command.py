from telegram import Update
from telegram.ext import CallbackContext

from src.core.config import Settings, get_settings
from src.db.database import fs


class AudioCommand:
    def __init__(self):
        self.settings: Settings = get_settings()

    async def store_audio_command(self, update: Update, context: CallbackContext):
        audio = None
        if update.channel_post and update.channel_post.audio:
            audio = update.channel_post.audio
        elif update.message.chat.type == 'private':
            audio = update.message.audio

        if audio:
            # Check if the audio already exists in the database by matching title and performer
            existing_audio = fs.find_one({"title": audio.title, "performer": audio.performer})

            if existing_audio:
                return  # Avoid storing duplicates

            # Store audio in GridFS
            audio_file = await context.bot.get_file(audio.file_id)  # Get the audio file
            file_data = await audio_file.download_as_bytearray()  # Download the audio file as bytes

            # Store the audio file in GridFS
            fs.put(file_data, filename=audio.title, performer=audio.performer, title=audio.title)
            print(f"Stored audio: {audio.title} - {audio.performer}")

    async def search_audio_command(self, update: Update, context: CallbackContext):
        if not update.message.text or len(update.message.text.split()) < 2:
            await update.message.reply_text("Please provide a performer name. Example: /searchaudio Eminem")
            return

        performer_name = " ".join(update.message.text.split()[1:]).lower()

        # Search for audio in the database by performer name
        matching_audios = []
        for audio in fs.find({"performer": {"$regex": performer_name, "$options": "i"}}):  # Case-insensitive search
            matching_audios.append(audio)

        if matching_audios:
            for audio in matching_audios:
                audio_file = fs.get(audio._id)
                await update.message.reply_audio(
                    audio_file,
                    caption=f"🎵 Found: {audio.title} - {audio.performer}"
                )
            return

        await update.message.reply_text("No matching audio found.")
