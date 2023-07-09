from loguru import logger
from discord import Interaction

from gachiniii import discord_bot

@discord_bot.tree.command(name="vc-leave", description="ボイスチャットから切断させる")
async def vc_leave(interaction: Interaction):
    logger.info("Executed vc-leave command")
    if interaction.guild.voice_client is None:
        await interaction.response.send_message("おれ通話入ってないけど？頭大丈夫？")
    else:
        await interaction.guild.voice_client.disconnect()
        await interaction.response.send_message("やっと終わったわぁ、パチンコ行ってくるから呼ぶなよ")
