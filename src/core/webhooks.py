from dataclasses import dataclass, field, asdict
from datetime import datetime, timezone
from typing import Optional

import aiohttp


@dataclass
class WebhookField:
    name: str
    value: str
    inline: bool = False


@dataclass
class WebhookFooter:
    text: str


@dataclass
class WebhookThumbnail:
    url: str


@dataclass
class WebhookEmbed:
    title: str
    description: str
    color: int
    fields: list[WebhookField] = field(default_factory=list)
    footer: Optional[WebhookFooter] = None
    timestamp: str = ""
    thumbnail: Optional[WebhookThumbnail] = None

    def to_dict(self) -> dict:
        d = {
            "title": self.title,
            "description": self.description,
            "color": self.color,
            "timestamp": self.timestamp or make_timestamp(),
        }
        if self.fields:
            d["fields"] = [asdict(f) for f in self.fields]
        if self.footer:
            d["footer"] = asdict(self.footer)
        if self.thumbnail:
            d["thumbnail"] = asdict(self.thumbnail)
        return d


async def send_webhook(url: str, embed: WebhookEmbed) -> bool:
    if not url or url == "#":
        return False

    payload = {"embeds": [embed.to_dict()]}

    try:
        async with aiohttp.ClientSession() as session:
            async with session.post(url, json=payload, timeout=aiohttp.ClientTimeout(10)) as resp:
                return resp.status < 400
    except Exception:
        return False


def make_timestamp() -> str:
    return datetime.now(timezone.utc).isoformat()


def footer_text(bot_name: str, suffix: str) -> str:
    return f"{bot_name} \u2022 {suffix}"
