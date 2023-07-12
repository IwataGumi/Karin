from loguru import logger
from typing import Any, Dict, Union
from sqlalchemy.orm.exc import NoResultFound
from sqlalchemy import Column, Integer, String
from sqlalchemy.dialects.postgresql import JSONB

from karin import Base, Session
from karin.models.mixins import TimestampMixin
from karin.const import SUPPORTED_LANGUAGES, DEFAULT_BOT_CONFIG


class Guilds(Base, TimestampMixin):
    __tablename__ = 'guilds'
    __table_args__ = {"comment": "Discord Server"}

    id = Column(Integer, primary_key=True)
    guild_id = Column(String(255), unique=True, nullable=False)
    language = Column(String(10), nullable=False, default="en-US")
    config = Column(JSONB, nullable=False, default=DEFAULT_BOT_CONFIG)

    logger = logger.bind(task="GuildsTable")

    def __init__(self, guild_id: Union[int, str], language: str, config=Dict[str, Any]):
        self.guild_id = self.convert_guild_id(guild_id)
        self.language = language
        self.config = config.copy()

    @classmethod
    def convert_guild_id(cls, guild_id: Union[int, str]) -> str:
        if isinstance(guild_id, int):
            return str(guild_id)
        return guild_id

    @classmethod
    def get_lang(cls, guild_id: Union[int, str], default: str=None) -> str:
        guild_id = cls.convert_guild_id(guild_id)
        guild = cls.get_guild(guild_id, default=default)

        return guild.language

    @classmethod
    def change_lang(cls, guild_id: Union[int, str], lang: str) -> None:
        guild_id = cls.convert_guild_id(guild_id)
        if lang in SUPPORTED_LANGUAGES:
            with Session() as session:
                guild = cls.query.filter_by(guild_id=guild_id).one_or_none()
                if guild is None:
                    cls.logger.error(
                        f"Not found Guild_id:{guild_id} at Guilds table."
                    )
                    raise NoResultFound(f"Not found Guild_id:{guild_id} at Guilds table.")

                guild.language = lang
                session.commit()

        else:
            cls.logger.error(
                f"Not Supported Language: {lang}"
            )
            raise "Not Supported Language"

    @classmethod
    def create(cls, *args, **kwargs):
        with Session() as session:
            guild = cls(*args, **kwargs)
            session.add(guild)
            session.commit()

        return guild

    @classmethod
    def has_guild(cls, guild_id: Union[int, str]) -> bool:
        guild_id = cls.convert_guild_id(guild_id) 
        guild = cls.query.filter_by(guild_id=guild_id).one_or_none()

        return guild is not None

    @classmethod
    def get_guild(cls, guild_id: Union[int, str], default: Any=None):
        guild_id = cls.convert_guild_id(guild_id) 
        guild = cls.query.filter_by(guild_id=guild_id).one_or_none()
        if guild is None:
            if default is not None:
                return default

            cls.logger.error(
                f"Not found Guild_id:{guild_id} at Guilds table."
            )
            raise NoResultFound(f"Not found Guild_id:{guild_id} at Guilds table.")

        return guild
