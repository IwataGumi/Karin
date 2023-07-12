from karin import Karin
from .vc_join import VCJoin
from .vc_leave import VCLeave

async def setup(bot: Karin):
    await bot.add_cog(VCJoin(bot))
    await bot.add_cog(VCLeave(bot))
