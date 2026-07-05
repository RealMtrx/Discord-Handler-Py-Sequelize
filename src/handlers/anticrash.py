import asyncio
import sys
import traceback

from src.config import config
from src.core.error_webhook import send_error_webhook


def setup_anticrash(bot):
    async def notify_error(title: str, error: str):
        print(f"  \u274c {title}: {error}")
        traceback.print_exc()
        await send_error_webhook(f"**{title}**\n```{error[:1900]}```")

    def exception_handler(loop, context):
        msg = context.get("exception", context["message"])
        exc = context.get("exception", None)
        error_text = f"{msg}\n{''.join(traceback.format_exception(type(exc), exc, exc.__traceback__)) if exc else ''}"
        asyncio.ensure_future(notify_error("Unhandled Exception", error_text[:1900]))

    loop = asyncio.get_event_loop()
    loop.set_exception_handler(exception_handler)

    @bot.event
    async def on_error(event: str, *args, **kwargs):
        error_text = traceback.format_exc()
        print(f"  \u274c Event Error [{event}]: {error_text[:500]}")
        await send_error_webhook(f"**Event Error: {event}**\n```{error_text[:1900]}```")

    print("  \u2705 AntiCrash handler set up")
