from gachiniii.gachiniii import Gachiniii
from sqlalchemy import create_engine, URL
from gachiniii.config import DISCORD_API_TOKEN
from sqlalchemy.ext.declarative import declarative_base

from gachiniii.config import (
    POSTGRES_DRIVER,
    POSTGRES_HOST,
    POSTGRES_PORT,
    POSTGRES_USER,
    POSTGRES_PASSWORD,
    POSTGRES_DB,
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

# Register the client commands
from gachiniii.commands import *

# Register the models
from gachiniii.models import *