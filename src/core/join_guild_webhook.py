from datetime import datetime, timezone

from src.config import config
from src.core.webhooks import send_webhook, WebhookEmbed, WebhookField, WebhookFooter, WebhookThumbnail, make_timestamp, footer_text


async def send_join_guild_webhook(
    guild_name: str, guild_id: str, owner_id: str,
    member_count: int, icon_url: str | None = None,
):
    if not config.join_guild_webhook or config.join_guild_webhook == "#":
        return

    embed = WebhookEmbed(
        color=0x57F287,
        title="🎉 Bot Joined New Server!",
        description=f"**Server:** {guild_name}\n**ID:** {guild_id}",
        fields=[
            WebhookField(name="👑 Owner", value=f"<@{owner_id}>", inline=True),
            WebhookField(name="👥 Members", value=f"{member_count} members", inline=True),
            WebhookField(
                name="📅 Joined At",
                value=f"<t:{int(datetime.now(timezone.utc).timestamp())}:F>",
                inline=True,
            ),
        ],
        footer=WebhookFooter(text=footer_text(config.bot_name, "Guild Join Logger")),
        timestamp=make_timestamp(),
        thumbnail=WebhookThumbnail(
            url=icon_url or "https://cdn.discordapp.com/embed/avatars/0.png"
        ),
    )

    await send_webhook(config.join_guild_webhook, embed)
