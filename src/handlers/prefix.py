import importlib
import pkgutil
import traceback

import discord

from src.handlers.models import PrefixCommand, StartupData


def load_prefix_commands(bot) -> StartupData:
    data = StartupData()
    prefix_base = "src.commands.prefix"

    for importer, modname, ispkg in pkgutil.walk_packages(
        importlib.import_module(prefix_base).__path__,
        prefix=f"{prefix_base}.",
    ):
        if modname.count(".") < 3:
            continue

        try:
            module = importlib.import_module(modname)
            category = modname.split(".")[-2]

            if not hasattr(module, "command"):
                continue

            cmd: PrefixCommand = module.command
            bot.prefix_commands[cmd.name] = cmd
            data.total_prefix += 1
            print(f"  \u2705 Prefix command loaded: {config_prefix(bot)}{cmd.name} ({category})")

        except Exception as e:
            print(f"  \u274c Failed to load prefix command {modname}: {e}")
            traceback.print_exc()

    return data


def config_prefix(bot) -> str:
    return getattr(bot, "prefix", "$")
