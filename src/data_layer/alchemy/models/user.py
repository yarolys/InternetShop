from typing import TYPE_CHECKING
from pydantic import EmailStr
from typing import List
from sqlalchemy import VARCHAR, Enum, select
from sqlalchemy.orm import Mapped, MappedColumn, relationship

from src.schemas.enums.user import UserRole
from src.schemas.user import UserSchema
from .base import Base

if TYPE_CHECKING:
    from .order import Order

class User(Base):
    __tablename__ = "users"

    id: Mapped[int] = MappedColumn(primary_key=True, autoincrement=True)
    email: Mapped[EmailStr] = MappedColumn(VARCHAR(255), unique=True, nullable=False, index=True)
    username: Mapped[str] = MappedColumn(VARCHAR(32), unique=True, nullable=False, index=True)
    hashed_password: Mapped[str] = MappedColumn(nullable=False)
    role: Mapped[UserRole] = MappedColumn(Enum(UserRole), default=UserRole.USER)
    balance: Mapped[int] = MappedColumn(default=0)
    active_order_id: Mapped[int] = MappedColumn(default=0)  # TODO: feature foreign key

    orders: Mapped[List["Order"]] = relationship("Order", back_populates="user", cascade="all, delete-orphan")

    class Config:
        from_attributes = True

    @classmethod
    async def create(cls, user: UserSchema) -> None:
        async with cls.get_session() as session:
            session.add(cls(**user.model_dump()))
            await session.commit()

    @classmethod
    async def get_db_obj(
            cls,
            *,
            user_id: int | None = None,
            email: EmailStr | None = None,
            username: str | None = None
    ):
        async with cls.get_session() as session:
            query = select(cls)
            if user_id:
                query = query.where(cls.id == user_id)
            elif username:
                query = query.where(cls.username == username)
            elif email:
                query = query.where(cls.email == email)
            else:
                return None
            result = await session.execute(query)
            return result.scalar_one_or_none()