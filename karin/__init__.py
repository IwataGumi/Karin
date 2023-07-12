from sqlalchemy import create_engine, URL
from sqlalchemy.orm import sessionmaker, scoped_session
from sqlalchemy.ext.declarative import declarative_base


from karin.karin import Karin
from karin.const import DISCORD_API_TOKEN
from karin.const import (
    POSTGRES_DRIVER,
    POSTGRES_HOST,
    POSTGRES_PORT,
    POSTGRES_USER,
    POSTGRES_PASSWORD,
    POSTGRES_DB,
)

discord_bot = Karin()
db_url = URL.create(
    drivername=POSTGRES_DRIVER,
    username=POSTGRES_USER,
    password=POSTGRES_PASSWORD,
    host=POSTGRES_HOST,
    port=int(POSTGRES_PORT),
    database=POSTGRES_DB,
)
db_engine = create_engine(db_url)
Session = scoped_session(
    sessionmaker(
        autoflush=True,
        autocommit=False,
        bind=db_engine,
    )
)
Base = declarative_base()
Base.query = Session.query_property()
