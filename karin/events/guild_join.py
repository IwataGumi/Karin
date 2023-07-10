from typing import List
from discord import Guild, TextChannel

from karin import discord_bot
from karin.translate import _
from karin.models import Guilds
from karin.views import SelectLangView
from karin.const import DEFAULT_BOT_CONFIG

@discord_bot.client.event
async def on_guild_join(guild: Guild):
    def found_channel_can_send(channels: List[TextChannel]):
        for channel in guild.text_channels:
            if channel.permissions_for(guild.me).send_messages:
                return channel
        else:
            return None

    if not Guilds.has_guild(guild.id):
        channel = found_channel_can_send(guild.text_channels)
        if channel is not None:
            bot_name = _('en-US', "bot_info.name")
            await channel.send(
                _("en-US", "message.self_introduction", bot_name=bot_name),
                view=SelectLangView()
            )

        Guilds.create(guild.id, "en-US", DEFAULT_BOT_CONFIG.copy())
    else:
        channel = found_channel_can_send(guild.text_channels)
        if channel is not None:
            guild_lang = Guilds.get_lang(guild.id)
            bot_name = _(guild_lang, "bot_info.name")
            await channel.send(
                _(guild_lang, "message.rejoin", bot_name=bot_name)
            )
