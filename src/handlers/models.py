from dataclasses import dataclass, field
from typing import Any, Callable, Coroutine

import discord
from discord import app_commands


@dataclass
class StartupData:
    total_slash: int = 0
    total_prefix: int = 0
    total_events: int = 0


SlashCommandFunc = Callable[
    [discord.Interaction],
    Coroutine[Any, Any, None],
]

PrefixCommandFunc = Callable[
    [discord.Message, list[str]],
    Coroutine[Any, Any, None],
]

EventFunc = Callable[
    [...],
    Coroutine[Any, Any, None],
]


@dataclass
class SlashCommand:
    data: app_commands.Command
    category: str = "public"


@dataclass
class PrefixCommand:
    name: str
    description: str
    category: str
    aliases: list[str]
    handler: PrefixCommandFunc


@dataclass
class EventFile:
    name: str
    once: bool
    handler: EventFunc
