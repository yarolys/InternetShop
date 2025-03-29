from contextlib import asynccontextmanager
from datetime import datetime, UTC

from sqlalchemy import text, DateTime
from sqlalchemy.orm import DeclarativeBase, Mapped, MappedColumn
from sqlalchemy.ext.asyncio import AsyncSession

from src.config.alchemy_conf import alchemy_settings

class Base(DeclarativeBase):
    created_at: Mapped[datetime] = MappedColumn(DateTime(timezone=UTC), nullable=False)

    @classmethod
    @asynccontextmanager
    async def get_session(cls) -> AsyncSession:
        async with alchemy_settings.async_session_maker() as session:
            yield session