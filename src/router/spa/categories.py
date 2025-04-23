from typing import List

from fastapi import APIRouter

from src.depends.required_role import roles_required
from src.resources.categories import CategoriesEntity
from src.schemas.enums.user import UserRole
from src.schemas.request.categories import CategoriesCreateSchema, CategoriesGetSchema

router = APIRouter(
    prefix="/categories",
    tags=["categories"],
)

@router.post(
    "",
    summary="Create new category", status_code=201,
    dependencies=[roles_required(allowed_roles=[UserRole.ADMIN, UserRole.SUPERADMIN])
])
async def create(category_data: CategoriesCreateSchema):
    await CategoriesEntity.create(category_data)

@router.delete(
    "",  
    summary="Delete category",
    status_code=204,
)
async def delete(category_id: int): 
    await CategoriesEntity.delete(category_id=category_id)
    return


@router.get(
    "/get_all",
    response_model=List[CategoriesGetSchema], status_code=200,
)
async def get_all_category():
    return await CategoriesEntity.get_all()
    