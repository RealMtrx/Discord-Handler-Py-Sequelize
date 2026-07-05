from datetime import datetime, timezone

from src.config import config
from src.core.webhooks import send_webhook, WebhookEmbed, WebhookField, WebhookFooter, make_timestamp, footer_text


async def send_leave_guild_webhook(
    guild_id: str, guild_name: str,
    member_count: int, remaining_servers: int,
):
    if not config.leave_guild_webhook or config.leave_guild_webhook == "#":
        return

    embed = WebhookEmbed(
        color=0xFF0000,
        title="👋 Bot Left Server",
        description=f"**Server:** {guild_name}\n**ID:** {guild_id}",
        fields=[
            WebhookField(name="👥 Members", value=f"{member_count} members", inline=True),
            WebhookField(
                name="📅 Left At",
                value=f"<t:{int(datetime.now(timezone.utc).timestamp())}:F>",
                inline=True,
            ),
            WebhookField(name="📊 Remaining Servers", value=f"{remaining_servers} servers", inline=True),
        ],
        footer=WebhookFooter(text=footer_text(config.bot_name, "Guild Leave Logger")),
        timestamp=make_timestamp(),
    )

    await send_webhook(config.leave_guild_webhook, embed)
