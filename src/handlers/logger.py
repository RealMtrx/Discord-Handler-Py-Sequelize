import time
from datetime import datetime, timezone

from src.config import config
from src.handlers.models import StartupData


def print_startup_banner(data: StartupData, start_time: float):
    elapsed = time.time() - start_time
    now = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M:%S UTC")

    print("\n" + "=" * 50)
    print(f"  {config.bot_name}")
    print("=" * 50)
    print(f"  \u23f0 Started at: {now}")
    print(f"  \u2699\ufe0f Loaded {data.total_slash} slash commands")
    print(f"  \ud83d\udce0 Loaded {data.total_prefix} prefix commands")
    print(f"  \ud83c\udf89 Loaded {data.total_events} events")
    print(f"  \u26a1 Ready in {elapsed:.2f}s")
    print("=" * 50 + "\n")
