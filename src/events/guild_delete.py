import traceback

import discord

from src.core.leave_guild_webhook import send_leave_guild_webhook
from src.handlers.models import EventFile


async def on_guild_remove(guild: discord.Guild):
    try:
        print(f"  \ud83d\udc4b Left guild: {guild.name} ({guild.id})")
        await send_leave_guild_webhook(
            guild_id=str(guild.id),
            guild_name=guild.name,
            member_count=guild.member_count or 0,
            remaining_servers=len(guild._state._guilds) if hasattr(guild._state, "_guilds") else 0,
        )
    except Exception as e:
        print(f"  \u274c Error in guild remove event: {e}")
        traceback.print_exc()


event_file = EventFile(
    name="on_guild_remove",
    once=False,
    handler=on_guild_remove,
)
