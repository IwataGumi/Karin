from karin import discord_bot
from karin.const import DISCORD_API_TOKEN

if __name__ == "__main__":
    discord_bot.startup(token=DISCORD_API_TOKEN)
