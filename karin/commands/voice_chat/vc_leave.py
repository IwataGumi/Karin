from loguru import logger
from discord.ext import commands
from discord import app_commands, Integration

from karin import Karin
from karin.translate import _t
from karin.models import Guilds
from karin.const import SUPPORTED_LANGUAGES


class VCLeave(commands.Cog):
    logger = logger.bind(task="VoiceChat")

    def __init__(self, bot: Karin):
        self.bot = bot

    @app_commands.command(name="vc-leave", description="command.vc_leave.description")
    async def vc_leave(self, integration: Integration):
        logger.info("Executed /vc-leave command")

        guild_id = integration.guild.id
        guild_lang = Guilds.get_lang(guild_id, default=SUPPORTED_LANGUAGES[0])
        bot_name = _t(guild_lang, "bot_info.name")

        if integration.guild.voice_client is None:
            await integration.response.send_message(
                _t(guild_lang, "command.vc_leave.not_joined", bot_name=bot_name)
            )
        else:
            await integration.guild.voice_client.disconnect()
            await integration.response.send_message(
                _t(guild_lang, "command.vc_leave.leave_call")
            )
