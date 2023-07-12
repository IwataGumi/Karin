from karin import Karin
from .guild_join import GuildJoin

async def setup(bot: Karin):
    await bot.add_cog(GuildJoin(bot))
