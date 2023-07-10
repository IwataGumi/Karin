from loguru import logger
from discord import Interaction

from karin import discord_bot
from karin.translate import _
from karin.const import DISCORD_BOT_NAME


@discord_bot.tree.command(
    name="vc-leave", description="command.vc_leave.description"
)
async def vc_leave(interaction: Interaction):
    logger.info("Executed /vc-leave command")
    if interaction.guild.voice_client is None:
        await interaction.response.send_message(
            _("ja", "command.vc_leave.not_joined", bot_name=DISCORD_BOT_NAME)
        )
    else:
        await interaction.guild.voice_client.disconnect()
        await interaction.response.send_message(_("ja", "command.vc_leave.leave_call"))
