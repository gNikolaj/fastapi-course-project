from sqlalchemy.ext.asyncio import AsyncSession
from fastapi import APIRouter, Depends, HTTPException, status

from app.models.user import User
from app.services.auth import AuthService
from app.schemas.user import SignInRequest, TokenResponse, UserDetail

from app.db.postgres import get_db
from app.core.deps import get_current_user
from app.core.security import create_access_token

auth_router = APIRouter(tags=["auth"])


@auth_router.post("/auth/login", response_model=TokenResponse)
async def login(data: SignInRequest, db: AsyncSession = Depends(get_db)):
    user = await AuthService(db).authenticate(data.email, data.password)
    if not user:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Incorrect email or password")
    return TokenResponse(access_token=create_access_token(user.email))


@auth_router.get("/me", response_model=UserDetail)
async def me(current_user: User = Depends(get_current_user)):
    return current_user
