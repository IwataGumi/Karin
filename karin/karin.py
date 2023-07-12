import sys
import logging
from loguru import logger
from discord import Intents

from discord.ext import commands


from karin.const import LOGURU_FILTER_TYPE
from karin.intercept_logging import InterceptHandler


class Karin(commands.Bot):
    def __init__(self):
        super().__init__(command_prefix="/", intents=Intents.all(), help_command=None)
        self.initial_extensions = ["karin.events", "karin.commands"]

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

    async def on_ready(self):
        activate_logger = logger.bind(task="activate")
        activate_logger.info("The discord bot is ready.")

    async def setup_hook(self):
        for extension in self.initial_extensions:
            try:
                await self.load_extension(extension)
            except Exception as e:
                logger.error(str(e), task="setup_hook")
        # await self.tree.set_translator(MyTranslator)
        await self.tree.sync()

    def startup(self, token: str, reconnect=True):
        self.run(token, reconnect=reconnect, log_handler=self.logging_handler)
