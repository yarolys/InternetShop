from pydantic_settings import BaseSettings, SettingsConfigDict


class APISettings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env", extra='ignore')

    API_HOST: str
    API_PORT: int
    DEBUG: bool = False
    JWT_SECRET_KEY: str
    JWT_ALGORITHM: str = "HS256"
    JWT_ACCESS_TOKEN_EXPIRE_MINUTES: int = 30000
    JWT_REFRESH_TOKEN_EXPIRE_MINUTES: int = 43200
    ORIGINS: list[str]

api_settings = APISettings()
