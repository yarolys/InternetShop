from typing import Annotated

from fastapi import APIRouter, HTTPException, Depends
from pydantic import EmailStr

from src.depends.get_current_token import get_current_token
from src.resources.user import UserEntity
from src.schemas.request.user import UserCreateSchema
from src.schemas.response.user import UserDetailSchema
from src.schemas.token import TokenPayloadSchema
from src.utills.jwt_utills import decode_token

router = APIRouter(
    prefix="/user",
    tags=["user"],
)

@router.post("", summary="Create user", status_code=201)
async def create(user_data: UserCreateSchema):
    await UserEntity.create(user_data)

@router.get("/me", summary="Get user", status_code=200)
async def get_user(token_data: Annotated[TokenPayloadSchema, Depends(get_current_token)]):

    user = await UserEntity.find(user_id=token_data.user_id)
    return UserDetailSchema.model_validate(user.db_object)

@router.get("/check_email/{email}", summary="is email is free", status_code=200)
async def get_user_by_email(email: EmailStr):
    if await UserEntity.check_is_exists(email=email):
        raise HTTPException(status_code=400, detail="Email is taken")
    return {"details": "Email is free"}

@router.get("/check_username/{username}", summary="is username is free", status_code=200)
async def get_user_by_username(username: str):
    if await UserEntity.check_is_exists(username=username):
        raise HTTPException(status_code=400, detail="Username is taken")
    return {"details": "Username is free"}
