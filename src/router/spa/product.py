from fastapi import APIRouter

from src.depends.required_role import roles_required
from src.resources.product import ProductEntity
from src.schemas.enums.user import UserRole
from src.schemas.request.product import ProductCreateSchema

router = APIRouter(
    prefix="/product",
    tags=["product"],
)

@router.post(
    "",
    summary="Create product",
    status_code=201,
    description='for work with this area, firstly you should create the category of product because product connect to category_id and cant work without category',
    dependencies=[roles_required(allowed_roles=[UserRole.ADMIN, UserRole.SUPERADMIN])
])
async def create(product_data: ProductCreateSchema):
    await ProductEntity.create(product_data)

@router.delete(
    "/{product_id}",
    status_code=204,
)
async def delete(product_id: int):
    await ProductEntity.delete(product_id=product_id)