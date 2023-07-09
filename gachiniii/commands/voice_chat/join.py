from loguru import logger
from discord import Interaction

from gachiniii import discord_bot

@discord_bot.tree.command(name="vc-join", description="ボイスチャットに接続させる")
async def vc_join(interaction: Interaction):
    logger.info("Executed vc-join command")
    await interaction.response.send_message("仕方ねぇーな？？？")
