import discord
from discord import PartialEmoji

from karin.translate import _
from karin.models import Guilds
from karin.const import SUPPORTED_LANGUAGES_WITH_EMOJI

class SelectLangView(discord.ui.View):
    def __init__(self, timeout=180):
        super().__init__(timeout=timeout)

    @discord.ui.select(
        cls=discord.ui.Select,
        placeholder="Select your language",
        options=[
            discord.SelectOption(emoji=PartialEmoji.from_str(emoji), label=lang)
            for lang, emoji in SUPPORTED_LANGUAGES_WITH_EMOJI.items() 
        ]
    )

    async def select(self, interaction: discord.Interaction, select: discord.ui.Select):
        guild_id = interaction.guild.id
        if interaction.user.guild_permissions.manage_webhooks:
            guild_lang = select.values[0].lower()
            Guilds.change_lang(guild_id, guild_lang)
            await interaction.response.send_message(
                _(
                    guild_lang,
                    "message.selected_language",
                    selected_lang=SUPPORTED_LANGUAGES_WITH_EMOJI[guild_lang]
                )
            )
        else:
            guild_lang = Guilds.get_lang(guild_id)
            await interaction.response.send_message(_(guild_lang, "command.no_permission"), ephemeral=True)
