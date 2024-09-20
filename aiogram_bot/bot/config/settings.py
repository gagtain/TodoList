from __future__ import annotations


from dotenv import load_dotenv
from pydantic import BaseModel, Field

from pydantic_settings import BaseSettings, PydanticBaseSettingsSource, SettingsConfigDict as _SettingsConfigDict

load_dotenv('.env')


class BotTexts(BaseModel):
    start_message: str = Field(default="Привет! Выберите действие: 🎈", title="Приветственное сообщение")




class Settings(BaseSettings):
    token: str
    api_token: str
    api_url: str
    fast_api_url: str
    texts: BotTexts = Field(default_factory=BotTexts)
    admins: str
