import importlib
import pkgutil
import traceback

import discord

from src.events.ready import set_bot, on_ready as _on_ready_raw
from src.handlers.models import EventFile, StartupData

_ready_called = False


async def _wrapped_on_ready(bot):
    global _ready_called
    if _ready_called:
        return
    _ready_called = True
    set_bot(bot)
    await _on_ready_raw()


async def load_events(bot) -> StartupData:
    data = StartupData()
    events_module = "src.events"

    for importer, modname, ispkg in pkgutil.iter_modules(
        importlib.import_module(events_module).__path__
    ):
        if modname.startswith("_"):
            continue

        try:
            module = importlib.import_module(f"{events_module}.{modname}")

            if not hasattr(module, "event_file"):
                print(f"  \u26a0\ufe0f {modname}: missing event_file attribute, skipping")
                continue

            event_file: EventFile = module.event_file

            if event_file.name == "on_ready":
                async def _on_ready_wrapper():
                    await _wrapped_on_ready(bot)
                bot.add_listener(_on_ready_wrapper, "on_ready")
            else:
                bot.add_listener(event_file.handler, event_file.name)

            data.total_events += 1
            print(f"  \u2705 Loaded event: {event_file.name}")

        except Exception as e:
            print(f"  \u274c Failed to load event {modname}: {e}")
            traceback.print_exc()

    return data
