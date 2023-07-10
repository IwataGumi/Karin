import os
import pathlib
from dotenv import load_dotenv

load_dotenv()

DISCORD_BOT_NAME = os.getenv("DISCORD_BOT_NAME")
DISCORD_API_TOKEN = os.getenv("DISCORD_API_TOKEN")
LOGURU_FILTER_TYPE = os.getenv("LOGURU_FILTER_TYPE")
DEFAULT_BOT_LANGUAGE = os.getenv("DEFAULT_BOT_LANGUAGE")
DEFAULT_BOT_CONFIG = {}
# Check here languages are available in discord.py
# https://discordpy.readthedocs.io/en/stable/api.html?highlight=locale#discord.Locale
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

LOCALS_FILE_PATH = pathlib.Path("./locales")
