import os
from typing import List
from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    BOT_TOKEN: str = "YOUR_BOT_TOKEN_HERE"
    ADMINS: str = "123456789"
    STORAGE_CHANNEL_ID: int = -1001234567890
    DATABASE_URL: str = "sqlite+aiosqlite:///data/bot_database.sqlite3"

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        extra="ignore"
    )

    @property
    def admin_ids(self) -> List[int]:
        if not self.ADMINS:
            return []
        ids = []
        for x in self.ADMINS.split(","):
            cleaned = x.strip()
            if cleaned.isdigit() or (cleaned.startswith("-") and cleaned[1:].isdigit()):
                ids.append(int(cleaned))
        return ids

settings = Settings()
