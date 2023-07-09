from gachiniii.gachiniii import Gachiniii
from gachiniii.config import DISCORD_API_TOKEN

discord_bot = Gachiniii(token=DISCORD_API_TOKEN)

# Register the client commands
from gachiniii.commands import *