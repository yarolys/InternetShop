from datetime import datetime, timedelta, UTC

from fastapi import HTTPException, status
from jose import jwt, JWTError, ExpiredSignatureError

from src.config.api_conf import api_settings
from src.schemas.enums.user import UserRole
from src.schemas.token import TokenSchema, TokenPayloadSchema


def create_access_token(
        user_id: int,
        role: UserRole,
        expires_delta: timedelta = timedelta(minutes=api_settings.JWT_ACCESS_TOKEN_EXPIRE_MINUTES)
) -> str:
    now = datetime.now(UTC)
    to_encode = {
        "sub": str(user_id),
        "role": role.value,
        "exp": now + expires_delta,
        "iat": now,
    }
    return jwt.encode(
        to_encode,
        api_settings.JWT_SECRET_KEY,
        algorithm=api_settings.JWT_ALGORITHM
    )

def create_refresh_token(
        user_id: int,
        role: UserRole,
        expires_delta: timedelta = timedelta(
            days=api_settings.JWT_REFRESH_TOKEN_EXPIRE_MINUTES
        )
) -> str:
    now = datetime.now(UTC)
    to_encode = {
        "sub": str(user_id),
        "role": role.value,
        "exp": now + expires_delta,
        "iat": now,
    }
    return jwt.encode(
        to_encode,
        api_settings.JWT_SECRET_KEY,
        algorithm=api_settings.JWT_ALGORITHM
    )

def decode_token(token: str) -> TokenPayloadSchema:
    """
    Raises:
        HTTPException(HTTP_401_UNAUTHORIZED)
    """
    try:
        payload = TokenPayloadSchema(
            **jwt.decode(
            token, api_settings.JWT_SECRET_KEY,
                algorithms=[api_settings.JWT_ALGORITHM]
            )
        )
        user_id = payload.user_id
        role = payload.role
        if payload.exp < datetime.now(UTC):
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Token expired")

        if user_id is None or role is None:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid token"
            )

        return payload
    except ExpiredSignatureError:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Token expired"
        )

    except JWTError:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Token decode error"
        )

def generate_tokens(user_id: int, role: UserRole):
    return TokenSchema(
        access_token=create_access_token(user_id, role),
        refresh_token=create_refresh_token(user_id, role)
    )
