from loguru import logger
from discord import Message
from discord.ext import commands

from karin import Karin

class ReadMessage(commands.Cog):
    logger = logger.bind(task="ReadMessage")

    def __init__(self, bot: Karin):
        self.bot = bot

    @commands.Cog.listener("on_message")
    async def read_message(self, message: Message):
        pass
