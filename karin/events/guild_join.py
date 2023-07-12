from loguru import logger
from typing import Optional
from discord.ext import commands
from discord import Guild, TextChannel


from karin import Karin
from karin.translate import _t
from karin.models import Guilds
from karin.views import SelectLangView
from karin.const import DEFAULT_BOT_CONFIG, SUPPORTED_LANGUAGES


class GuildJoin(commands.Cog):
    logger = logger.bind(task="GuildJoin")

    def __init__(self, bot: Karin):
        self.bot = bot

    @commands.Cog.listener()
    async def on_guild_join(self, guild: Guild):
        def found_channel_can_send(guild: Guild) -> Optional[TextChannel]:
            for channel in guild.text_channels:
                if channel.permissions_for(guild.me).send_messages:
                    return channel
            else:
                return None

        channel = found_channel_can_send(guild)

        if not Guilds.has_guild(guild.id):
            logger.info("The bot joined new guild!")
            if channel is not None:
                guild_lang = guild.preferred_locale.value
                if guild_lang not in SUPPORTED_LANGUAGES:
                    guild_lang = SUPPORTED_LANGUAGES[0]

                bot_name = _t(guild_lang, "bot_info.name")
                await channel.send(
                    _t(guild_lang, "message.self_introduction", bot_name=bot_name),
                    view=SelectLangView(),
                )

            Guilds.create(guild.id, guild_lang, DEFAULT_BOT_CONFIG.copy())
        else:
            logger.info("The bot rejoined the guild!")
            if channel is not None:
                guild_lang = Guilds.get_lang(guild.id)
                bot_name = _t(guild_lang, "bot_info.name")
                await channel.send(_t(guild_lang, "message.rejoin", bot_name=bot_name))


async def setup(bot: Karin):
    await bot.add_cog(GuildJoin(bot))
