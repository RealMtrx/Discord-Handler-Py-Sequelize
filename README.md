<div align="center">
  <h1>Discord Handler — Python (SQL Edition)</h1>
  <p><strong>A production-ready Discord bot framework built with discord.py and SQLAlchemy — supports SQLite, PostgreSQL, and MySQL with a modular src/ architecture.</strong></p>

  <p>
    <a href="https://github.com/RealMtrx/Discord-Handler-Py-Sequelize/blob/main/LICENSE"><img src="https://img.shields.io/badge/license-MIT-blue.svg" alt="License"></a>
    <a href="https://github.com/RealMtrx/Discord-Handler-Py-Sequelize/releases"><img src="https://img.shields.io/badge/version-0.9.0--beta-yellow" alt="Version 0.9.0 Beta"></a>
    <a href="https://github.com/RealMtrx/Discord-Handler-Py-Sequelize/stargazers"><img src="https://img.shields.io/github/stars/RealMtrx/Discord-Handler-Py-Sequelize" alt="Stars"></a>
    <a href="https://github.com/RealMtrx/Discord-Handler-Py-Sequelize/issues"><img src="https://img.shields.io/github/issues/RealMtrx/Discord-Handler-Py-Sequelize" alt="Issues"></a>
    <a href="https://github.com/RealMtrx/Discord-Handler-Py-Sequelize/network"><img src="https://img.shields.io/github/forks/RealMtrx/Discord-Handler-Py-Sequelize" alt="Forks"></a>
    <a href="https://github.com/RealMtrx/Discord-Handler/graphs/contributors"><img src="https://img.shields.io/badge/ecosystem-26%20repos-brightgreen" alt="26 Repos"></a>
    <a href="https://discord.gg/0hu2"><img src="https://img.shields.io/badge/discord-0hu2-5865F2" alt="Discord"></a>
  </p>

  <br>

  <p>
    <a href="#-features">Features</a> •
    <a href="#-quick-start">Quick Start</a> •
    <a href="#-project-structure">Structure</a> •
    <a href="#-database-configuration">Database Config</a> •
    <a href="#-api-reference">API</a> •
    <a href="#-mongodb-edition">MongoDB Edition</a> •
    <a href="#-related-repositories">Ecosystem</a>
  </p>
</div>

---

## Overview

Discord Handler Python (SQL Edition) is a **SQLAlchemy-powered Discord bot framework** built with `discord.py` (^2.4). It provides an async, event-driven foundation for Discord bots with dual command support (slash via `app_commands` + prefix), SQL persistence via SQLAlchemy (^2.0) async engine, webhook-based logging, and an anti-crash layer. Instead of MongoDB, this edition uses SQLAlchemy to support SQLite, PostgreSQL, and MySQL.

The entry point (`src/main.py`) boots in a predictable async sequence: load configuration, connect to the database via SQLAlchemy async engine, register slash commands and prefix commands, attach event handlers, and finally start the bot via `bot.run()`. A graceful shutdown handler is also registered.

## Features

- **Dual Command System** — Slash commands via `app_commands` and prefix commands with dedicated loader
- **Modular Architecture** — Separated concerns across `Core/`, `Database/`, `Events/`, `Handlers/`, `Models/`, and `Commands/`
- **Anti-Crash** — Global exception handling via `AntiCrash.py`
- **Webhook Logging** — Webhook utilities for errors, guild events, and command usage via `aiohttp`
- **SQLAlchemy Integration** — Persistent storage via SQLAlchemy (^2.0) async engine with SQLite, PostgreSQL, and MySQL
- **Cooldown System** — Per-command cooldown management in `Core/commandUtils.py`
- **Async Runtime** — Fully async with `asyncio` and `discord.py`'s native async support
- **Environment Configuration** — All secrets managed via `python-dotenv`

## Quick Start

```bash
git clone https://github.com/RealMtrx/Discord-Handler-Py-Sequelize.git
cd Discord-Handler-Py-Sequelize
pip install -r requirements.txt
```

Copy `.env.example` to `.env` and configure:

```env
TOKEN=your_bot_token
CLIENT_ID=your_client_id
BOT_NAME=Discord Handler
OWNER_IDS=owner_id_1,owner_id_2
PREFIX=$

DB_DIALECT=sqlite
DB_STORAGE=discord_bot.db

DB_HOST=localhost
DB_PORT=3306
DB_USERNAME=root
DB_PASSWORD=password
DB_DATABASE=discord_bot
```

```bash
python src/main.py
```

### Dependencies

| Package          | Version | Purpose                          |
|------------------|---------|----------------------------------|
| `discord.py`     | >=2.4.0 | Discord API wrapper              |
| `sqlalchemy`     | >=2.0.0 | Async ORM for database operations|
| `aiosqlite`      | >=0.19.0| Async SQLite driver              |
| `databases`      | >=0.9.0 | Async database access            |
| `python-dotenv`  | >=1.0.0 | Environment variable management  |
| `aiohttp`        | >=3.9.0 | Async HTTP client for webhooks   |

## Project Structure

```
Discord-Handler-Py-Sequelize/
├── requirements.txt              # Python dependencies
├── src/                          # Source code
│   ├── main.py                   # Main bot entry point
│   ├── config.py                 # Bot configuration from .env
│   ├── bot.py                    # Bot initialization
│   ├── Core/                     # Core utilities
│   │   ├── commandUtils.py       # Cooldown and utilities
│   │   ├── emojis.py             # Centralized emoji definitions
│   │   └── webhookUtil.py        # Webhook utility
│   ├── Database/
│   │   └── sqlalchemy.py         # SQLAlchemy async engine setup
│   ├── Events/                   # Discord event handlers
│   │   ├── guildCreate.py        # Handler when bot joins a server
│   │   ├── guildDelete.py        # Handler when bot leaves a server
│   │   ├── interactionCreate.py  # Handles slash command interactions
│   │   ├── messageCreate.py      # Handles prefix commands
│   │   └── ready.py              # Bot ready event
│   ├── Handlers/                 # Handlers for modularity
│   │   ├── AntiCrash.py          # Crash prevention and error handling
│   │   └── logger.py             # Logger for bot activity
│   ├── Models/
│   │   └── user.py               # User data model (SQLAlchemy)
│   └── Commands/
│       ├── Prefix/               # Prefix commands
│       │   └── ping.py           # Example prefix ping command
│       └── Slash/                # Slash commands
│           └── ping.py           # Example slash ping command
```

## Database Configuration

The handler uses SQLAlchemy with a configurable dialect. Set `DB_DIALECT` in your `.env`:

| Dialect     | Driver to install                   |
|-------------|-------------------------------------|
| `sqlite`    | `aiosqlite` (included)              |
| `postgres`  | `pip install asyncpg`               |
| `mysql`     | `pip install asyncmy`               |

Example PostgreSQL configuration:

```env
DB_DIALECT=postgres
DB_HOST=localhost
DB_PORT=5432
DB_USERNAME=postgres
DB_PASSWORD=your_password
DB_DATABASE=discord_bot
```

The connection URL is built automatically from the `DB_*` environment variables.

## API Reference

### Entry Point — `src/main.py`

```python
async def main()
```

Loads configuration, initializes the SQLAlchemy async engine, creates the bot instance, registers slash command trees and prefix command handlers, attaches event listeners, and starts the bot via `bot.run(config.token)`. Handles graceful shutdown on `SIGINT`/`SIGTERM`.

### Configuration — `src/config.py`

| Key | Type | Description |
|-----|------|-------------|
| `TOKEN` | `str` | Discord bot token |
| `CLIENT_ID` | `str` | Discord application client ID |
| `BOT_NAME` | `str` | Display name |
| `PREFIX` | `str` | Prefix for text commands |
| `OWNER_IDS` | `list[str]` | Bot owner Discord IDs |
| `DB_DIALECT` | `str` | SQL dialect (`sqlite`, `postgres`, `mysql`) |
| `DB_STORAGE` | `str` | File path for SQLite |
| `DB_HOST` | `str` | Database host |
| `DB_PORT` | `int` | Database port |
| `DB_USERNAME` | `str` | Database user |
| `DB_PASSWORD` | `str` | Database password |
| `DB_DATABASE` | `str` | Database name |

### Bot — `src/bot.py`

The `Bot` class extends `discord.ext.commands.Bot` and holds the SQLAlchemy async engine, command registries, and configuration. It provides methods for registering slash commands, prefix commands, and event listeners.

### Events

| Event | File | Trigger |
|-------|------|---------|
| `on_ready` | `Events/ready.py` | Bot goes online — logs startup info |
| `on_guild_join` | `Events/guildCreate.py` | Bot joins a server — sends join webhook |
| `on_guild_remove` | `Events/guildDelete.py` | Bot leaves a server — sends leave webhook |
| `on_interaction` | `Events/interactionCreate.py` | Slash command used — routes to handler |
| `on_message` | `Events/messageCreate.py` | Message sent — checks prefix, routes command |

## Adding Commands

### Slash Command

Create `src/Commands/Slash/[Category]/[name].py`:

```python
import discord
from discord import app_commands

@app_commands.command(name="ping", description="Replies with Pong!")
async def ping(interaction: discord.Interaction):
    await interaction.response.send_message("Pong! 🏓")
```

### Prefix Command

Create `src/Commands/Prefix/[Category]/[name].py`:

```python
import discord

async def ping(message: discord.Message, args: list[str]):
    await message.reply("Pong! 🏓")
```

Commands are automatically loaded from their respective directories during startup.

## MongoDB Edition

Prefer MongoDB over SQL? The **MongoDB edition** of this handler is available:

[RealMtrx/Discord-Handler-Py](https://github.com/RealMtrx/Discord-Handler-Py)

It replaces `Database/sqlalchemy.py` with a `motor` (async MongoDB) connection. All other modules remain structurally identical.

## Related Repositories

The Discord Handler ecosystem spans **26 repositories** across 13 languages, each available in both MongoDB and Sequelize editions.

### Base Repositories (MongoDB)

| Language   | Repository |
|------------|-----------|
| C++        | [RealMtrx/Discord-Handler-Cpp](https://github.com/RealMtrx/Discord-Handler-Cpp) |
| C#         | [RealMtrx/Discord-Handler-Cs](https://github.com/RealMtrx/Discord-Handler-Cs) |
| Dart       | [RealMtrx/Discord-Handler-Dart](https://github.com/RealMtrx/Discord-Handler-Dart) |
| Go         | [RealMtrx/Discord-Handler-Go](https://github.com/RealMtrx/Discord-Handler-Go) |
| Java       | [RealMtrx/Discord-Handler-Java](https://github.com/RealMtrx/Discord-Handler-Java) |
| JavaScript | [RealMtrx/Discord-Handler-Js](https://github.com/RealMtrx/Discord-Handler-Js) |
| Kotlin     | [RealMtrx/Discord-Handler-Kt](https://github.com/RealMtrx/Discord-Handler-Kt) |
| Lua        | [RealMtrx/Discord-Handler-Lua](https://github.com/RealMtrx/Discord-Handler-Lua) |
| PHP        | [RealMtrx/Discord-Handler-Php](https://github.com/RealMtrx/Discord-Handler-Php) |
| Python     | [RealMtrx/Discord-Handler-Py](https://github.com/RealMtrx/Discord-Handler-Py) |
| Ruby       | [RealMtrx/Discord-Handler-Rb](https://github.com/RealMtrx/Discord-Handler-Rb) |
| Rust       | [RealMtrx/Discord-Handler-Rs](https://github.com/RealMtrx/Discord-Handler-Rs) |
| TypeScript | [RealMtrx/Discord-Handler](https://github.com/RealMtrx/Discord-Handler) ← hub |

### Sequelize (SQL) Editions

| Language   | Repository |
|------------|-----------|
| C++        | [RealMtrx/Discord-Handler-Cpp-Sequelize](https://github.com/RealMtrx/Discord-Handler-Cpp-Sequelize) |
| C#         | [RealMtrx/Discord-Handler-Cs-Sequelize](https://github.com/RealMtrx/Discord-Handler-Cs-Sequelize) |
| Dart       | [RealMtrx/Discord-Handler-Dart-Sequelize](https://github.com/RealMtrx/Discord-Handler-Dart-Sequelize) |
| Go         | [RealMtrx/Discord-Handler-Go-Sequelize](https://github.com/RealMtrx/Discord-Handler-Go-Sequelize) |
| Java       | [RealMtrx/Discord-Handler-Java-Sequelize](https://github.com/RealMtrx/Discord-Handler-Java-Sequelize) |
| JavaScript | [RealMtrx/Discord-Handler-Js-Sequelize](https://github.com/RealMtrx/Discord-Handler-Js-Sequelize) |
| Kotlin     | [RealMtrx/Discord-Handler-Kt-Sequelize](https://github.com/RealMtrx/Discord-Handler-Kt-Sequelize) |
| Lua        | [RealMtrx/Discord-Handler-Lua-Sequelize](https://github.com/RealMtrx/Discord-Handler-Lua-Sequelize) |
| PHP        | [RealMtrx/Discord-Handler-Php-Sequelize](https://github.com/RealMtrx/Discord-Handler-Php-Sequelize) |
| Python     | [RealMtrx/Discord-Handler-Py-Sequelize](https://github.com/RealMtrx/Discord-Handler-Py-Sequelize) |
| Ruby       | [RealMtrx/Discord-Handler-Rb-Sequelize](https://github.com/RealMtrx/Discord-Handler-Rb-Sequelize) |
| Rust       | [RealMtrx/Discord-Handler-Rs-Sequelize](https://github.com/RealMtrx/Discord-Handler-Rs-Sequelize) |
| TypeScript | [RealMtrx/Discord-Handler-Ts-Sequelize](https://github.com/RealMtrx/Discord-Handler-Ts-Sequelize) |

> **[RealMtrx/Discord-Handler](https://github.com/RealMtrx/Discord-Handler)** — the TypeScript hub and flagship repository. Star it to support the ecosystem.

## License

Distributed under the MIT License. See `LICENSE` for more information.

---

Built by **Mtrx** — Discord: **0hu2**
