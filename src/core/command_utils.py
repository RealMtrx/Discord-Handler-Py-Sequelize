from datetime import datetime, timezone


class ErrorReport:
    def __init__(self, message: str, command_name: str):
        self.message = message
        self.command_name = command_name
        self.timestamp = datetime.now(timezone.utc).isoformat()


def format_error(error: Exception, command_name: str) -> ErrorReport:
    return ErrorReport(str(error), command_name)


def log_command_usage(
    user_id: str, user_name: str, command_name: str, guild_name: str
):
    print(f"[Command] {user_name} ({user_id}) used {command_name} in {guild_name}")
