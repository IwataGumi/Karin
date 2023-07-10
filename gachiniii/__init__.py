from pyi18n import PyI18n
from loguru import logger
from gachiniii.gachiniii import Gachiniii
from sqlalchemy import create_engine, URL
from pyi18n.loaders import PyI18nYamlLoader
from gachiniii.config import DISCORD_API_TOKEN
from sqlalchemy.ext.declarative import declarative_base

from gachiniii.config import (
    POSTGRES_DRIVER,
    POSTGRES_HOST,
    POSTGRES_PORT,
    POSTGRES_USER,
    POSTGRES_PASSWORD,
    POSTGRES_DB,
    LOCALS_FILE_PATH,
)

discord_bot = Gachiniii(token=DISCORD_API_TOKEN)
db_url = URL.create(
    drivername=POSTGRES_DRIVER,
    username=POSTGRES_USER,
    password=POSTGRES_PASSWORD,
    host=POSTGRES_HOST,
    port=int(POSTGRES_PORT),
    database=POSTGRES_DB,
)
db_engine = create_engine(db_url)
Base = declarative_base()

# i18n support
loader: PyI18nYamlLoader = PyI18nYamlLoader(LOCALS_FILE_PATH, namespaced=True)
i18n = PyI18n(("ja", "en"), loader=loader)
_: callable = i18n.gettext

# Register the client commands
from gachiniii.commands import *

# Register the models
from gachiniii.models import *
