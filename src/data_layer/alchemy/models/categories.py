from typing import TYPE_CHECKING, List

from sqlalchemy import ForeignKey, VARCHAR, select
from sqlalchemy.orm import Mapped, MappedColumn, relationship

from src.schemas.categories import CategoriesSchema
from .base import Base

if TYPE_CHECKING:
    from src.data_layer.alchemy.models.product import Product

class Category(Base):
    __tablename__ = "categories"

    id: Mapped[int] = MappedColumn(primary_key=True, autoincrement=True)
    name: Mapped[str] = MappedColumn(VARCHAR(255), nullable=False, unique=False)
    parent_id: Mapped[int] = MappedColumn(ForeignKey("categories.id"), nullable=True)

    products: Mapped[list["Product"]] = relationship(back_populates="category")


    @classmethod
    async def create(cls, category: CategoriesSchema) -> CategoriesSchema:
        async with cls.get_session() as session:
            new_category = cls(**category.model_dump())
            session.add(new_category)
            await session.commit()

            await session.refresh(new_category)

            return CategoriesSchema.model_validate(new_category)


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
