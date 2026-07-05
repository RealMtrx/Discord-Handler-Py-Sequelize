import traceback

import discord

from src.config import config
from src.core.cooldown import CooldownManager
from src.core.slash_command_webhook import send_slash_command_usage, send_slash_command_error
from src.handlers.models import EventFile

cooldown_manager = CooldownManager()


async def on_interaction(interaction: discord.Interaction):
    if interaction.type != discord.InteractionType.application_command:
        return

    command_name = interaction.command.name if interaction.command else "unknown"

    if not interaction.guild:
        await interaction.response.send_message(
            "Commands are only available in servers!", ephemeral=True
        )
        return

    user = interaction.user
    user_id = str(user.id)
    guild_name = interaction.guild.name
    user_name = str(user)

    on_cooldown, remaining = cooldown_manager.check(user_id, command_name)
    if on_cooldown:
        await interaction.response.send_message(
            f"Please wait {remaining}s before using this command again.",
            ephemeral=True,
        )
        return

    await send_slash_command_usage(
        user_id=user_id,
        user_name=user_name,
        command_name=command_name,
        guild_name=guild_name,
        avatar_url=user.display_avatar.url if user.display_avatar else None,
    )


event_file = EventFile(
    name="on_interaction",
    once=False,
    handler=on_interaction,
)
