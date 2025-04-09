from typing import TYPE_CHECKING
from fastapi import HTTPException
from sqlalchemy import ForeignKey, VARCHAR, select
from sqlalchemy.orm import Mapped, MappedColumn, relationship

from src.schemas.categories import CategoriesSchema

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
    async def create(cls, categories: CategoriesSchema) -> None:
        if (categories.parent_id
            and not await cls.get_by_id(categories_id = categories.parent_id)):
            raise HTTPException(
                status_code=400,
                detail=f'Category with id={categories.parent_id} not found'
            )
        async with cls.get_session() as session:
            session.add(cls(**categories.model_dump()))
            await session.commit()
        
        
    @classmethod
    async def get_by_id(cls, categories_id: int) -> "Category | None":
        async with cls.get_session() as session:
            query = select(cls).where(cls.id == categories_id)
            result = await session.execute(query)
            return result.scalar_one_or_none()
    
            
    @classmethod
    async def delete(cls, categories_id: int):
        async with cls.get_session() as session:
            categories = await cls.get_by_id(categories_id)
            if not categories:
                return
            await session.delete(categories)
            await session.commit()