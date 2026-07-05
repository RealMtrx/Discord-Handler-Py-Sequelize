import traceback

import discord

from src.config import config
from src.core.ready_webhook import send_ready_webhook

_bot_ref = None


def set_bot(bot):
    global _bot_ref
    _bot_ref = bot


async def on_ready():
    bot = _bot_ref
    if bot and bot.user:
        print(f"  \u2705 Logged in as {bot.user} (ID: {bot.user.id})")

        await bot.change_presence(
            activity=discord.Activity(
                type=discord.ActivityType.watching,
                name=f"{config.bot_name} | {config.prefix}help",
            )
        )

        await send_ready_webhook(
            bot_username=str(bot.user),
            bot_id=str(bot.user.id),
            server_count=len(bot.guilds),
        )


event_file = EventFile(
    name="on_ready",
    once=False,
    handler=on_ready,
)
