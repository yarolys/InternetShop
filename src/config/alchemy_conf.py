from pydantic_settings import BaseSettings, SettingsConfigDict
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker

class AlchemySettings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env", extra='ignore')

    DB_HOST: str
    DB_PORT: int
    DB_USER: str
    DB_NAME: str
    DB_PASSWORD: str
    DEBUG: bool = False

    @property
    def pg_url(self) -> str:
        return (
            f"postgresql+asyncpg://{self.DB_USER}:{self.DB_PASSWORD}"
            f"@{self.DB_HOST}:{self.DB_PORT}/{self.DB_NAME}?async_fallback=True"
        )

    @property
    def engine(self):
        return create_async_engine(self.pg_url, echo = self.DEBUG)

    @property
    def async_session_maker(self):
        return sessionmaker(self.engine, expire_on_commit=False, class_=AsyncSession)


alchemy_settings = AlchemySettings()