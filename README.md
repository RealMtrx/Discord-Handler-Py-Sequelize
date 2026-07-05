# Discord Handler Py Sequelize

A modern, feature-rich Discord bot handler built with **discord.py v2**, featuring both slash commands and prefix commands with a robust modular architecture designed for scalability and maintainability. Uses **SQLAlchemy** for database persistence.

## 🚀 Features

- **Dual Command System**: Support for both slash commands and prefix commands
- **Modular Architecture**: Clean separation of concerns with dedicated handlers
- **Anti-Crash System**: Comprehensive error handling and monitoring
- **Event-Driven**: Fully event-driven async architecture
- **Webhook Logging**: Real-time logging for errors and guild events
- **SQLAlchemy Integration**: Persistent data storage with SQLAlchemy async engine (SQLite/MySQL/PostgreSQL)
- **Cooldown System**: Per-command cooldown management
- **Environment Configuration**: Secure configuration with python-dotenv

## 📁 Project Structure

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

## 🔧 Installation

1. **Clone the repository**

   ```bash
   git clone https://github.com/RealMtrx/Discord-Handler-Py-Sequelize.git
   cd Discord-Handler-Py-Sequelize
   ```

2. **Install dependencies**

   ```bash
   pip install -r requirements.txt
   ```

3. **Environment Setup**

   Copy `.env.example` to `.env` and fill in your values:

   ```env
   TOKEN=your_bot_token_here
   PREFIX=!
   BOT_NAME=Discord Handler
   DB_DIALECT=sqlite
   DB_STORAGE=discord_bot.db
   ERROR_WEBHOOK=https://discord.com/api/webhooks/your_webhook
   GUILD_LOG_WEBHOOK=https://discord.com/api/webhooks/your_webhook
   ```

4. **Run the bot**

   ```bash
   python src/main.py
   ```

## 📋 Dependencies

- **discord.py**: v2.3 - Discord API wrapper
- **SQLAlchemy**: v2.0 - Async ORM for database operations
- **aiosqlite**: v0.19 - Async SQLite driver
- **databases**: v0.9 - Async database access
- **python-dotenv**: v1.0 - Environment variable management
- **aiohttp**: v3.9 - Async HTTP client for webhooks

## 📝 Command Development

### Creating Slash Commands

Create a new file in `src/Commands/Slash/[category]/[name].py`:

```python
import discord
from discord import app_commands

@app_commands.command(name="ping", description="Replies with Pong!")
async def ping(interaction: discord.Interaction):
    await interaction.response.send_message("Pong! 🏓")
```

### Creating Prefix Commands

Create a new file in `src/Commands/Prefix/[category]/[name].py`:

```python
import discord

async def ping(message: discord.Message, args: list[str]):
    await message.reply("Pong! 🏓")
```

---

**Discord Handler** — Built by **Mtrx** — Discord: **0hu2**
