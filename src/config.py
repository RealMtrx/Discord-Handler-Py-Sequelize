import os
from dotenv import load_dotenv

load_dotenv()


class Config:
    def __init__(self):
        self.token = os.getenv("TOKEN", "#")
        self.client_id = os.getenv("CLIENT_ID", "#")
        self.bot_name = os.getenv("BOT_NAME", "Discord Handler")
        self.prefix = os.getenv("PREFIX", "$")
        self.owner_ids = [
            x.strip() for x in os.getenv("OWNER_IDS", "#,#").split(",")
        ]
        self.db_dialect = os.getenv("DB_DIALECT", "sqlite")
        self.db_storage = os.getenv("DB_STORAGE", "discord_bot.db")
        self.db_host = os.getenv("DB_HOST", "localhost")
        self.db_port = int(os.getenv("DB_PORT", "3306"))
        self.db_username = os.getenv("DB_USERNAME", "root")
        self.db_password = os.getenv("DB_PASSWORD", "password")
        self.db_database = os.getenv("DB_DATABASE", "discord_bot")
        self.error_webhook = os.getenv("ERROR_WEBHOOK", "#")
        self.slash_command_webhook = os.getenv("SLASH_WEBHOOK", "#")
        self.prefix_command_webhook = os.getenv("PREFIX_WEBHOOK", "#")
        self.join_guild_webhook = os.getenv("JOIN_WEBHOOK", "#")
        self.leave_guild_webhook = os.getenv("LEAVE_WEBHOOK", "#")
        self.ready_webhook = os.getenv("READY_WEBHOOK", "#")


config = Config()
