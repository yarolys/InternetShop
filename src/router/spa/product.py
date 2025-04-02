from fastapi import APIRouter

from src.depends.required_role import roles_required
from src.schemas.enums.user import UserRole
<<<<<<< HEAD
from src.schemas.product import ProductSchema
from src.resources.product import ProductEntity
=======
>>>>>>> main

router = APIRouter(
    prefix="/product",
    tags=["product"],
)

@router.post(
    "",
    summary="Create product",
    status_code=201,
    dependencies=[
        roles_required(allowed_roles=[UserRole.ADMIN, UserRole.SUPERADMIN])
<<<<<<< HEAD
        ])
async def create(user_data: ProductSchema):
    await ProductEntity.create(user_data)
=======
    ]

)
async def create():
    pass
>>>>>>> main
