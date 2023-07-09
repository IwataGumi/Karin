import os
from dotenv import load_dotenv

load_dotenv()

DISCORD_API_TOKEN = os.getenv("DISCORD_API_TOKEN")
LOGURU_FILTER_TYPE = os.getenv("LOGURU_FILTER_TYPE")
