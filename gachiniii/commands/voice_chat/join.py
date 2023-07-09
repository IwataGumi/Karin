from loguru import logger
from discord import Interaction

from gachiniii import discord_bot

@discord_bot.tree.command(name="vc-join", description="ボイスチャットに接続させる")
async def vc_join(interaction: Interaction):
    logger.info("Executed vc-join command")

    if interaction.user.voice is None:
        await interaction.response.send_message("は？通話入ってから呼べよ、くそが")
    elif interaction.guild.voice_client is None:
        await interaction.response.send_message("これでいいか？")
        await interaction.user.voice.channel.connect()
    else:
        await interaction.response.send_message("仕方ねぇーな？？？")
