from loguru import logger
from discord import Interaction

from gachiniii import discord_bot

@discord_bot.tree.command(name="vc-leave", description="ボイスチャットから切断させる")
async def vc_leave(interaction: Interaction):
    logger.info("Executed vc-leave command")
    await interaction.response.send_message("だるくなった、抜けるわ")
