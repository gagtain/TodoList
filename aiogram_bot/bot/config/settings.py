from __future__ import annotations


from dotenv import load_dotenv
from pydantic import BaseModel, Field

from pydantic_settings import BaseSettings, PydanticBaseSettingsSource, SettingsConfigDict as _SettingsConfigDict

load_dotenv('.env')



class Settings(BaseSettings):
    token: str
    api_token: str
    api_url: str
    fast_api_url: str
    admins: str
