import time
import traceback

import discord

from src.config import config
from src.core.cooldown import CooldownManager
from src.core.prefix_command_webhook import send_prefix_command_usage, send_prefix_command_error
from src.handlers.models import PrefixCommand

cooldown_manager = CooldownManager()


async def on_message(message: discord.Message):
    if message.author.bot:
        return

    if not message.guild:
        return

    prefix = config.prefix

    if not message.content.startswith(prefix):
        return

    content = message.content[len(prefix):].strip()
    parts = content.split()
    cmd_name = parts[0].lower()
    args = parts[1:] if len(parts) > 1 else []

    bot = message._state._get_client()
    if not bot or not hasattr(bot, "prefix_commands"):
        return

    cmd: PrefixCommand | None = bot.prefix_commands.get(cmd_name)

    if not cmd:
        for c in bot.prefix_commands.values():
            if cmd_name in c.aliases:
                cmd = c
                break

    if not cmd:
        return

    user_id = str(message.author.id)
    on_cooldown, remaining = cooldown_manager.check(user_id, cmd.name)
    if on_cooldown:
        await message.reply(f"Please wait {remaining}s before using this command again.")
        return

    try:
        await cmd.handler(message, args)

        await send_prefix_command_usage(
            user_id=user_id,
            user_name=str(message.author),
            command_name=cmd.name,
            guild_name=message.guild.name,
            avatar_url=message.author.display_avatar.url if message.author.display_avatar else None,
        )

    except Exception as e:
        error_msg = str(e)
        traceback.print_exc()
        await message.reply(f"\u274c **Error:** {error_msg[:2000]}")

        await send_prefix_command_error(
            user_id=user_id,
            user_name=str(message.author),
            command_name=cmd.name,
            guild_name=message.guild.name,
            error_msg=error_msg,
        )


event_file = EventFile(
    name="on_message",
    once=False,
    handler=on_message,
)
