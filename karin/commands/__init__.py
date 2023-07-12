from .voice_chat import *

async def setup(bot: Karin):
    await bot.add_cog(VCJoin(bot))
    await bot.add_cog(VCLeave(bot))