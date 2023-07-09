import sys
import logging
from loguru import logger
from discord import AutoShardedClient, Intents, app_commands

from config import LOGURU_FILTER_TYPE
from intercept_logging import InterceptHandler


class Gachiniii:
    def __init__(self, token: str):
        self.token: str = token
        self.intents = Intents.all()
        self.client = AutoShardedClient(intents=self.intents)
        self.tree = app_commands.CommandTree(self.client)

        @self.client.event
        async def on_ready():
            activate_logger = logger.bind(task="activate")
            activate_logger.info("The discord bot is ready.")
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
