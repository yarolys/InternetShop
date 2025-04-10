from typing import TYPE_CHECKING, List
from fastapi import HTTPException
from sqlalchemy import ForeignKey, VARCHAR, select
from sqlalchemy.orm import Mapped, MappedColumn, relationship

from src.schemas.categories import CategoriesSchema
from src.schemas.request.categories import CategoriesGetSchema

from .base import Base

if TYPE_CHECKING:
    from src.data_layer.alchemy.models.product import Product

class Category(Base):
    __tablename__ = "categories"

    id: Mapped[int] = MappedColumn(primary_key=True, autoincrement=True)
    name: Mapped[str] = MappedColumn(VARCHAR(255), nullable=False, unique=True)
    parent_id: Mapped[int] = MappedColumn(ForeignKey("categories.id"), nullable=True)

    products: Mapped[list["Product"]] = relationship(back_populates="category")

    class Config:
        from_attributes = True


    @classmethod
    async def create(cls, category: CategoriesSchema) -> None:
        if (category.parent_id
            and not await cls.get_by_id(category_id = category.parent_id)):
            raise HTTPException(
                status_code=400,
                detail=f'Category with id={category.parent_id} not found'
            )
        async with cls.get_session() as session:
            session.add(cls(**category.model_dump()))
            await session.commit()


    @classmethod
    async def delete(cls, category_id: int):
        async with cls.get_session() as session:
            category = await cls.get_by_id(category_id)
            if not category:
                return
            await session.delete(category)
            await session.commit()
        
        
    @classmethod
    async def get_by_id(cls, category_id: int) -> "Category | None":
        async with cls.get_session() as session:
            query = select(cls).where(cls.id == category_id)
            result = await session.execute(query)
            return result.scalar_one_or_none()
    

    @classmethod
    async def get_all(cls) -> List["Category"]:
        async with cls.get_session() as session:
            query = select(cls)
            result = await session.execute(query)
            return result.scalars().all()