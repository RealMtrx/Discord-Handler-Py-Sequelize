import traceback

import discord

from src.handlers.models import EventFile


async def on_error(event: str, *args, **kwargs):
    error_text = traceback.format_exc()
    print(f"  \u274c Error in event [{event}]: {error_text[:500]}")


event_file = EventFile(
    name="on_error",
    once=False,
    handler=on_error,
)
