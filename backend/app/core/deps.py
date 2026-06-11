import jwt
from sqlalchemy.ext.asyncio import AsyncSession
from fastapi import Depends, HTTPException, status
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials

from app.db.postgres import get_db
from app.core.config import settings
from app.core.security import decode_access_token, decode_auth0_token

from app.models.user import User
from app.services.auth import AuthService

token_scheme = HTTPBearer()


async def get_current_user(
        credentials: HTTPAuthorizationCredentials = Depends(token_scheme),
        db: AsyncSession = Depends(get_db),
) -> User:
    token = credentials.credentials
    email = None

    try:
        payload = decode_access_token(token)
        email = payload.get("sub")
    except jwt.InvalidTokenError:
        pass

    if email is None:
        try:
            payload = decode_auth0_token(token)
            email = payload.get(f"{settings.AUTH0_AUDIENCE}/email")
        except Exception:
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid or expired token")

    service = AuthService(db)
    user = await service.get_user_by_email(email)

    if user is None:
        user = await service.create_user_from_email(email)

    return user
