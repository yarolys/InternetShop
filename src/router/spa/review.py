from typing import List
from fastapi import APIRouter

from src.depends.required_role import roles_required
from src.resources.review import ReviewEntity
from src.schemas.enums.user import UserRole
from src.schemas.request.review import ReviewCreateSchema, ReviewGetSchema

router = APIRouter(
    prefix="/review",
    tags=["review"],
)


@router.post(
    "",
    summary="Create",
    status_code=201
)
async def create(review_data: ReviewCreateSchema):
    await ReviewEntity.create(review_data)


@router.delete(
    "/{review_id}",
    status_code=204,
    dependencies=[roles_required(allowed_roles=[UserRole.ADMIN, UserRole.SUPERADMIN])]
)
async def delete(review_id: int):
    await ReviewEntity.delete(review_id=review_id)
    return


@router.get(
    "/{get_all}",
    summary="Get all",
    response_model=List[ReviewGetSchema], status_code=200
)
async def get_all_review():
    return await ReviewEntity.get_all()