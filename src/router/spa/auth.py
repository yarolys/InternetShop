from typing import Optional

from fastapi import APIRouter, HTTPException, status

from src.resources.user import UserEntity
from src.schemas.request.login import UserLoginSchema
from src.utills.hash_passwd import verify_password
from src.utills.jwt_utills import decode_token, generate_tokens

router = APIRouter(
    prefix="/auth",
    tags=["auth"],
)

@router.post("/login", summary="login", status_code=200)
async def login(user_data: UserLoginSchema):
    if not user_data.email and not user_data.username:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Email or username is required"
        )
    if user_data.email:
        r = await UserEntity.find(email=user_data.email)
    else:
        r = await UserEntity.find(username=user_data.username)
    if not r or not verify_password(user_data.password, r.db_object.hashed_password):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Email or password is incorrect"
        )

    return generate_tokens(r.db_object.id, r.db_object.role)

@router.post("/refresh", summary="Refresh token", status_code=200)
async def refresh(refresh_token: Optional[str] = None):
    if not refresh_token:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Refresh token is required"
        )
    token_data = decode_token(refresh_token)
    return generate_tokens(token_data.user_id, token_data.role)