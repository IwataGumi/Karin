from loguru import logger
from discord import Interaction

from gachiniii import discord_bot, _
from gachiniii.config import DISCORD_BOT_NAME


@discord_bot.tree.command(
    name="vc-join", description=_("ja", "command.vc_join.description")
)
async def vc_join(interaction: Interaction):
    logger.info("Executed /vc-join command")

    if interaction.user.voice is None:
        await interaction.response.send_message(
            _("ja", "command.vc_join.not_found_call", bot_name=DISCORD_BOT_NAME)
        )
    elif interaction.guild.voice_client is None:
        await interaction.response.send_message(_("ja", "command.vc_join.join_call"))
        await interaction.user.voice.channel.connect()
    else:
        await interaction.response.send_message(
            _("ja", "command.vc_join.already_in_call", bot_name=DISCORD_BOT_NAME)
        )
