from sqlalchemy import select, func
from sqlalchemy.ext.asyncio import AsyncSession

from app.models.user import User
from app.core.mixins import LogMixin
from app.schemas.user import SignUpRequest, UserUpdate
from app.utils.password import hash_password


class UserService(LogMixin):
    def __init__(self, db: AsyncSession):
        self.db = db

    async def get_users(self, offset: int = 0, limit: int = 10):
        result = await self.db.execute(select(User).offset(offset).limit(limit))
        users = result.scalars().all()

        total = await self.db.execute(select(func.count(User.id)))
        total_count = total.scalar()

        return users, total_count

    async def get_user_by_id(self, user_id: int):
        result = await self.db.execute(select(User).where(User.id == user_id))
        return result.scalar_one_or_none()

    async def create_user(self, data: SignUpRequest):
        user = User(
            email=data.email,
            password=hash_password(data.password),
        )
        self.db.add(user)
        await self.db.commit()
        await self.db.refresh(user)
        self.log(f"User created: {user.email}")
        return user

    async def update_user(self, user_id: int, data: UserUpdate):
        user = await self.get_user_by_id(user_id)
        if not user:
            return None

        if data.email is not None:
            user.email = data.email
        if data.password is not None:
            user.password = hash_password(data.password)
        if data.is_active is not None:
            user.is_active = data.is_active

        await self.db.commit()
        await self.db.refresh(user)
        self.log(f"User updated: {user.email}")
        return user

    async def delete_user(self, user_id: int):
        user = await self.get_user_by_id(user_id)
        if not user:
            return None

        await self.db.delete(user)
        await self.db.commit()
        self.log(f"User deleted: {user_id}")
        return user
