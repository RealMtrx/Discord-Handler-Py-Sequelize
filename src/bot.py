import traceback

import discord
from discord import app_commands
from discord.ext import commands

from src.config import config
from src.core.slash_command_webhook import send_slash_command_error


class Bot(commands.Bot):
    def __init__(self):
        intents = discord.Intents.default()
        intents.message_content = True
        intents.members = True
        intents.guilds = True

        super().__init__(
            command_prefix=config.prefix,
            intents=intents,
            application_id=config.client_id if config.client_id != "#" else None,
        )

        self.config = config
        self.slash_commands: dict[str, object] = {}
        self.prefix_commands: dict[str, object] = {}

    async def setup_hook(self):
        await self._setup_tree_error_handler()

    async def _setup_tree_error_handler(self):
        async def on_tree_error(
            interaction: discord.Interaction,
            error: app_commands.AppCommandError,
        ):
            error_msg = str(error)
            traceback.print_exc()

            embed = discord.Embed(
                title="\u274c An error occurred",
                description=f"**Error:** {error_msg[:2000]}",
                color=0xFF0000,
            )

            try:
                if not interaction.response.is_done():
                    await interaction.response.send_message(embed=embed, ephemeral=True)
                else:
                    await interaction.followup.send(embed=embed, ephemeral=True)
            except Exception:
                pass

            await send_slash_command_error(
                user_id=str(interaction.user.id),
                user_name=str(interaction.user),
                command_name=interaction.command.name if interaction.command else "unknown",
                guild_name=interaction.guild.name if interaction.guild else "DM",
                error_msg=error_msg,
            )

        self.tree.on_error = on_tree_error
