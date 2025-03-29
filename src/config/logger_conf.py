import sys

from loguru import logger
from pydantic_settings import SettingsConfigDict, BaseSettings


class LoggerConfig(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env", extra='ignore')
    LOG_LEVEL: str

logger_settings = LoggerConfig()
logger.remove()
logger.add(
    sys.stdout,
    colorize=True,
    level=logger_settings.LOG_LEVEL,
    format='<green>{time:HH:mm:ss}</green> | {level} | <level>{message}</level>'
)
