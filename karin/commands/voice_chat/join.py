from loguru import logger
from discord import Interaction

from karin import discord_bot
from karin.translate import _
from karin.const import DISCORD_BOT_NAME, SUPPORTED_LANGUAGES
from karin.models import Guilds


@discord_bot.tree.command(
    name="vc-join", description="command.vc_join.description"
)
async def vc_join(interaction: Interaction):
    logger.info("Executed /vc-join command")

    guild_id = interaction.guild.id
    guild_lang = Guilds.get_lang(guild_id, default_value=SUPPORTED_LANGUAGES[0])
    if interaction.user.voice is None:
        await interaction.response.send_message(
            _(guild_lang, "command.vc_join.not_found_call", bot_name=DISCORD_BOT_NAME)
        )
    elif interaction.guild.voice_client is None:
        await interaction.response.send_message(_(guild_lang, "command.vc_join.join_call"))
        await interaction.user.voice.channel.connect()
    else:
        await interaction.response.send_message(
            _(guild_lang, "command.vc_join.already_in_call", bot_name=DISCORD_BOT_NAME)
        )
