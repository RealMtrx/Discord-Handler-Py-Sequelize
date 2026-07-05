from src.config import config
from src.core.webhooks import send_webhook, WebhookEmbed, WebhookField, WebhookFooter, make_timestamp, footer_text


async def send_ready_webhook(bot_username: str, bot_id: str, server_count: int):
    if not config.ready_webhook or config.ready_webhook == "#":
        return

    embed = WebhookEmbed(
        color=0x00FF00,
        title="🟢 Bot is Online!",
        description=f"**Bot:** {bot_username}\n**Status:** Online and Ready",
        fields=[
            WebhookField(name="🤖 Bot Info", value=f"**ID:** {bot_id}", inline=True),
            WebhookField(name="🏠 Servers", value=f"{server_count} servers", inline=True),
        ],
        footer=WebhookFooter(text=footer_text(config.bot_name, "System Logger")),
        timestamp=make_timestamp(),
    )

    await send_webhook(config.ready_webhook, embed)
