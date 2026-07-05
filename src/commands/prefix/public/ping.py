import discord

from src.handlers.models import PrefixCommand


async def ping_handler(message: discord.Message, args: list[str]):
    sent = await message.reply("Pinging...")
    latency = round(message.created_at.timestamp() * 1000)

    embed = discord.Embed(
        title="\ud83c\udfd3 Pong!",
        description=f"> **Message Latency:** `{latency}ms`",
        color=0x5865F2,
    )
    embed.set_footer(text=f"{message.author.name} \u2022 Ping")

    await sent.edit(content=None, embed=embed)


command = PrefixCommand(
    name="ping",
    description="\ud83c\udfd3 Show bot latency",
    category="public",
    aliases=["pong"],
    handler=ping_handler,
)
