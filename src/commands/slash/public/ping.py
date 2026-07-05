import discord
from discord import app_commands

from src.handlers.models import SlashCommand


async def ping_callback(interaction: discord.Interaction):
    latency = round(interaction.client.latency * 1000)

    embed = discord.Embed(
        title="\ud83c\udfd3 Pong!",
        description=(
            f"> **WebSocket Latency:** `{latency}ms`\n"
            f"> **API Latency:** `{latency}ms`"
        ),
        color=0x5865F2,
    )
    embed.set_footer(text=f"{interaction.client.user.name} \u2022 Ping")

    await interaction.response.send_message(embed=embed)


cmd_data = app_commands.Command(
    name="ping",
    description="\ud83c\udfd3 Show bot latency",
    callback=ping_callback,
)

command = SlashCommand(data=cmd_data, category="public")
