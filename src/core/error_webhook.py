from src.config import config
from src.core.webhooks import send_webhook, WebhookEmbed, WebhookField, WebhookFooter, make_timestamp, footer_text


async def send_error_webhook(error_msg: str):
    if not config.error_webhook or config.error_webhook == "#":
        return

    embed = WebhookEmbed(
        color=0xFF0000,
        title="❌ Bot Error Report",
        description=f"**Error:** {error_msg}",
        fields=[
            WebhookField(name="📅 Timestamp", value=make_timestamp(), inline=True),
        ],
        footer=WebhookFooter(text=footer_text(config.bot_name, "Error Logger")),
        timestamp=make_timestamp(),
    )

    await send_webhook(config.error_webhook, embed)
