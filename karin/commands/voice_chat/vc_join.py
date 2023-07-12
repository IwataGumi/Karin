from loguru import logger
from discord.ext import commands
from discord import app_commands, Integration

from karin import Karin
from karin.translate import _t
from karin.models import Guilds
from karin.const import SUPPORTED_LANGUAGES

class VCJoin(commands.Cog):
    logger = logger.bind(task="VoiceChat")

    def __int__(self, bot: Karin):
        self.bot = bot

    @app_commands.command(
        name="vc-join", description="command.vc_join.description"
    )
    async def vc_join(self, integration: Integration):
        logger.info("Executed /vc-join command")

        guild_id = integration.guild.id
        guild_lang = Guilds.get_lang(guild_id, default=SUPPORTED_LANGUAGES[0])
        bot_name = _t(guild_lang, "bot_info.name")    

        if integration.user.voice is None:
            await integration.response.send_message(
                _t(guild_lang, "command.vc_join.not_found_call", bot_name=bot_name)
            )
        elif integration.guild.voice_client is None:
            await integration.response.send_message(_t(guild_lang, "command.vc_join.join_call"))
            await integration.user.voice.channel.connect()
        else:
            await integration.response.send_message(
                _t(guild_lang, "command.vc_join.already_in_call", bot_name=bot_name)
            )
