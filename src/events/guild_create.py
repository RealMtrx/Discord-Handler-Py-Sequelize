import traceback

import discord

from src.core.join_guild_webhook import send_join_guild_webhook
from src.handlers.models import EventFile


async def on_guild_join(guild: discord.Guild):
    try:
        icon = guild.icon.url if guild.icon else None
        print(f"  \ud83c\udfe5 Joined guild: {guild.name} ({guild.id})")
        await send_join_guild_webhook(
            guild_name=guild.name,
            guild_id=str(guild.id),
            owner_id=str(guild.owner_id),
            member_count=guild.member_count or 0,
            icon_url=icon,
        )
    except Exception as e:
        print(f"  \u274c Error in guild join event: {e}")
        traceback.print_exc()


event_file = EventFile(
    name="on_guild_join",
    once=False,
    handler=on_guild_join,
)
