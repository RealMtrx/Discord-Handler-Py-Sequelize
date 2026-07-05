import time
from threading import Timer


class CooldownManager:
    def __init__(self):
        self.cooldowns: dict[str, dict[str, float]] = {}

    def check(self, user_id: str, command: str, cooldown_ms: int = 3000):
        now = time.time() * 1000

        if command not in self.cooldowns:
            self.cooldowns[command] = {}

        user_map = self.cooldowns[command]
        expires = user_map.get(user_id)

        if expires and now < expires:
            remaining = int((expires - now) / 1000)
            return True, remaining

        user_map[user_id] = now + cooldown_ms

        Timer(
            cooldown_ms / 1000,
            lambda: self._cleanup(user_id, command),
        ).start()

        return False, 0

    def _cleanup(self, user_id: str, command: str):
        if command in self.cooldowns:
            self.cooldowns[command].pop(user_id, None)
