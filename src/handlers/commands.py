import importlib
import pkgutil
import traceback

import discord
from discord import app_commands

from src.handlers.models import SlashCommand, StartupData


def load_slash_commands(bot) -> StartupData:
    data = StartupData()
    slash_base = "src.commands.slash"

    for importer, modname, ispkg in pkgutil.walk_packages(
        importlib.import_module(slash_base).__path__,
        prefix=f"{slash_base}.",
    ):
        if modname.count(".") < 3:
            continue

        try:
            module = importlib.import_module(modname)
            category = modname.split(".")[-2]

            if not hasattr(module, "command"):
                continue

            cmd = module.command

            bot.tree.add_command(cmd.data)
            bot.slash_commands[cmd.data.name] = cmd
            data.total_slash += 1
            print(f"  \u2705 Slash command loaded: /{cmd.data.name} ({category})")

        except Exception as e:
            print(f"  \u274c Failed to load slash command {modname}: {e}")
            traceback.print_exc()

    return data
