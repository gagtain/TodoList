from dotenv import load_dotenv

from pydantic_settings import BaseSettings

load_dotenv()


class Settings(BaseSettings):
    DB_ECHO: bool
    PROJECT_NAME: str
    VERSION: str
    DEBUG: bool
    CORS_ALLOWED_ORIGINS: str
    REDIS_HOST: str
    REDIS_PORT: str
    REDIS_DB: str
    TASK_API_URL: str
    api_token: str

settings = Settings()