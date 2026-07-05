import asyncio
import time

from src.bot import Bot
from src.config import config
from src.database.sqlalchemy import setup_database, close_database
from src.handlers.anticrash import setup_anticrash
from src.handlers.commands import load_slash_commands
from src.handlers.events import load_events
from src.handlers.logger import print_startup_banner
from src.handlers.models import StartupData
from src.handlers.prefix import load_prefix_commands


async def main():
    start_time = time.time()

    bot = Bot()

    data = StartupData()

    print()
    print("=" * 50)
    print(f"  Starting {config.bot_name}...")
    print("=" * 50)
    print()

    print("  🛡️ Setting up anti-crash...")
    setup_anticrash(bot)

    print("  📠 Loading events...")
    event_data = await load_events(bot)
    data.total_events = event_data.total_events

    print("  ⚡ Loading slash commands...")
    slash_data = load_slash_commands(bot)
    data.total_slash = slash_data.total_slash

    print("  💬 Loading prefix commands...")
    prefix_data = load_prefix_commands(bot)
    data.total_prefix = prefix_data.total_prefix

    print("  🏛️ Setting up database...")
    await setup_database()

    print_startup_banner(data, start_time)

    try:
        await bot.start(config.token)
    except KeyboardInterrupt:
        pass
    finally:
        await close_database()
        await bot.close()


if __name__ == "__main__":
    asyncio.run(main())
