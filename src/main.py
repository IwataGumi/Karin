from gachiniii import Gachiniii
from config import DISCORD_API_TOKEN

if __name__ == "__main__":
    discord_bot = Gachiniii(token=DISCORD_API_TOKEN)
    discord_bot.run()
