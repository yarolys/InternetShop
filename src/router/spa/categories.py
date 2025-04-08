from fastapi import APIRouter, Depends

from src.depends.required_role import roles_required
from src.schemas.enums.user import UserRole
from src.schemas.product import ProductSchema
from src.resources.categories import CategoriesEntity
from src.schemas.request.categories import CategoriesCreateSchema

router = APIRouter(
    prefix="/categories",
    tags=["categories"],
)

@router.post("", summary="Create new category", status_code=201, 
             dependencies=[
        roles_required(allowed_roles=[UserRole.ADMIN, UserRole.SUPERADMIN])
        ])
async def create(categories_data: CategoriesCreateSchema):
    await CategoriesEntity.create(categories_data)

@router.delete(
    "/{category_id}",
    summary="Delete category",
    status_code=201,
)
async def delete(categories_id: int):
    await CategoriesEntity.delete(category_id=categories_id)