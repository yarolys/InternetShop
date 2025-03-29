from fastapi import Security, HTTPException, status
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer

from src.schemas.token import TokenPayloadSchema
from src.utills.jwt_utills import decode_token


def get_current_token(
        credentials: HTTPAuthorizationCredentials = Security(HTTPBearer(auto_error=False))
) -> TokenPayloadSchema:
    if credentials is None or credentials.scheme.lower() != "bearer":
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Missing Authorization token",
        )
    return decode_token(credentials.credentials)