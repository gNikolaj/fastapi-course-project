from sqlalchemy.ext.asyncio import AsyncSession
from fastapi import APIRouter, Depends, HTTPException, status

from app.db.postgres import get_db
from app.services.user import UserService
from app.schemas.user import SignUpRequest, UserUpdate, UserDetail, UsersList

users_router = APIRouter(prefix="/users", tags=["users"])


@users_router.get("/", response_model=UsersList)
async def get_users(
        offset: int = 0,
        limit: int = 10,
        db: AsyncSession = Depends(get_db),
):
    service = UserService(db)
    users, total = await service.get_users(offset=offset, limit=limit)
    return UsersList(users=users, total=total, offset=offset, limit=limit)


@users_router.get("/{user_id}", response_model=UserDetail)
async def get_user(
        user_id: int,
        db: AsyncSession = Depends(get_db),
):
    service = UserService(db)
    user = await service.get_user_by_id(user_id)
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")
    return user


@users_router.post("/", response_model=UserDetail, status_code=status.HTTP_201_CREATED)
async def create_user(
        data: SignUpRequest,
        db: AsyncSession = Depends(get_db),
):
    service = UserService(db)
    return await service.create_user(data)


@users_router.put("/{user_id}", response_model=UserDetail)
async def update_user(
        user_id: int,
        data: UserUpdate,
        db: AsyncSession = Depends(get_db),
):
    service = UserService(db)
    user = await service.update_user(user_id, data)
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")
    return user


@users_router.delete("/{user_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_user(
        user_id: int,
        db: AsyncSession = Depends(get_db),
):
    service = UserService(db)
    user = await service.delete_user(user_id)
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")
