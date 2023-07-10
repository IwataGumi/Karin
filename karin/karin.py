import sys
import logging
from loguru import logger
from discord import AutoShardedClient, Intents
from discord.app_commands import CommandTree

from .translate import MyTranslator
from karin.const import LOGURU_FILTER_TYPE
from karin.intercept_logging import InterceptHandler

cogs = ["cogs.roles","cogs.users","cogs.moderation","cogs.ticket-es","cogs.ticket-en"]

class Karin:
    def __init__(self, token: str):
        self.token: str = token
        self.intents = Intents.all()
        self.client = AutoShardedClient(intents=self.intents)
        self.tree = CommandTree(self.client)

        @self.client.event
        async def on_ready():
            activate_logger = logger.bind(task="activate")
            activate_logger.info("The discord bot is ready.")

        @self.client.event
        async def setup_hook():
            await self.tree.set_translator(MyTranslator())
            await self.tree.sync()

        # Disable logging output to the terminal
        self.logging_handler = logging.basicConfig(
            handlers=[
                InterceptHandler(),
            ],
            level=0,
            force=True,
        )

        # Filter the log type of stdout in loguru
        logger.remove()
        logger.add(
            sys.stdout,
            level=LOGURU_FILTER_TYPE,
        )

    def run(self):
        self.client.run(
            token=self.token, reconnect=True, log_handler=self.logging_handler
        )
