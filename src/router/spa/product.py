from fastapi import APIRouter

from src.depends.required_role import roles_required
from src.schemas.enums.user import UserRole

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
    ]

)
async def create():
    pass
