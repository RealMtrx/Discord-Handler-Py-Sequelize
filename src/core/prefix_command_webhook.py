from datetime import datetime, timezone

from src.config import config
from src.core.emojis import Emojis
from src.core.webhooks import send_webhook, WebhookEmbed, WebhookField, WebhookFooter, WebhookThumbnail, make_timestamp, footer_text


async def send_prefix_command_usage(
    user_id: str, user_name: str, command_name: str,
    guild_name: str, avatar_url: str | None = None,
):
    if not config.prefix_command_webhook or config.prefix_command_webhook == "#":
        return

    embed = WebhookEmbed(
        color=0x57F287,
        title=f"{Emojis.SLASH} Prefix Command Used",
        description=f"**Command:** `{config.prefix}{command_name}`",
        fields=[
            WebhookField(
                name=f"{Emojis.USER} User Info",
                value=f"**UserName:** {user_name}\n**ID:** {user_id}",
                inline=True,
            ),
            WebhookField(name=f"{Emojis.SERVER} Server", value=guild_name, inline=True),
            WebhookField(
                name=f"{Emojis.LOADING} Time",
                value=f"<t:{int(datetime.now(timezone.utc).timestamp())}:R>",
                inline=True,
            ),
        ],
        footer=WebhookFooter(text=footer_text(config.bot_name, "Prefix Command Logger")),
        timestamp=make_timestamp(),
        thumbnail=WebhookThumbnail(
            url=avatar_url or "https://cdn.discordapp.com/embed/avatars/0.png"
        ),
    )

    await send_webhook(config.prefix_command_webhook, embed)


async def send_prefix_command_error(
    user_id: str, user_name: str, command_name: str,
    guild_name: str, error_msg: str,
):
    if not config.prefix_command_webhook or config.prefix_command_webhook == "#":
        return

    embed = WebhookEmbed(
        color=0xFF0000,
        title=f"{Emojis.ERROR} Prefix Command Error",
        description=f"**Command:** `{config.prefix}{command_name}`\n**Error:** {error_msg}",
        fields=[
            WebhookField(
                name=f"{Emojis.USER} User Info",
                value=f"{user_name} ({user_id})",
                inline=True,
            ),
            WebhookField(name=f"{Emojis.SERVER} Server", value=guild_name, inline=True),
            WebhookField(
                name=f"{Emojis.LOADING} Time",
                value=f"<t:{int(datetime.now(timezone.utc).timestamp())}:F>",
                inline=True,
            ),
        ],
        footer=WebhookFooter(text=footer_text(config.bot_name, "Error Logger")),
        timestamp=make_timestamp(),
    )

    await send_webhook(config.prefix_command_webhook, embed)
