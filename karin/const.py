import os
import pathlib
from dotenv import load_dotenv

load_dotenv()

# VoiceVox
VOICEVOX_HOST = os.getenv("VOICEVOX_HOST")
VOICEVOX_PORT = os.getenv("VOICEVOX_PORT")
VOICEVOX_SCHEME = os.getenv("VOICEVOX_SCHEME")
VOICEVOX_URI = f"{VOICEVOX_SCHEME}://{VOICEVOX_HOST}:{VOICEVOX_PORT}"
VOICEVOX_AUDIO_QUERY = "/audio_query?text={text}&speaker={speaker}"
VOICEVOX_SYNTHESIS = "/synthesis?speaker={speaker}"
VOICEVOX_DEFAULT_SPEAKER = os.getenv("VOICEVOX_DEFAULT_SPEAKER")


DISCORD_BOT_NAME = os.getenv("DISCORD_BOT_NAME")
DISCORD_BOT_DESCRIPTION = os.getenv("DISCORD_BOT_DESCRIPTION")
DISCORD_API_TOKEN = os.getenv("DISCORD_API_TOKEN")
LOGURU_FILTER_TYPE = os.getenv("LOGURU_FILTER_TYPE")
DEFAULT_BOT_LANGUAGE = os.getenv("DEFAULT_BOT_LANGUAGE")
DEFAULT_BOT_CONFIG = {"chat_speaker": 3}

# i18n
# Check here languages are available in discord.py
# https://discordpy.readthedocs.io/en/stable/api.html?highlight=locale#discord.Locale
LOCALS_FILE_PATH = pathlib.Path("./locales")
SUPPORTED_LANGUAGES_WITH_EMOJI = {
    "en-US": "🇺🇸",
    "ja": "🇯🇵",
}
SUPPORTED_LANGUAGES = [lang for lang in SUPPORTED_LANGUAGES_WITH_EMOJI.keys()]

# PostgreSQL
POSTGRES_DRIVER = os.getenv("POSTGRES_DRIVER")
POSTGRES_USER = os.getenv("POSTGRES_USER")
POSTGRES_PASSWORD = os.getenv("POSTGRES_PASSWORD")
POSTGRES_DB = os.getenv("POSTGRES_DB")
POSTGRES_HOST = os.getenv("POSTGRES_HOST")
POSTGRES_PORT = os.getenv("POSTGRES_PORT")
