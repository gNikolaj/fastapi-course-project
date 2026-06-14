from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.models.user import User
from app.core.mixins import LogMixin

from app.utils.password import verify_password


class AuthService(LogMixin):
    def __init__(self, db: AsyncSession):
        self.db = db

    async def get_user_by_email(self, email: str) -> User | None:
        result = await self.db.execute(select(User).where(User.email == email))
        return result.scalar_one_or_none()

    async def authenticate(self, email: str, password: str) -> User | None:
        user = await self.get_user_by_email(email)
        if not user or not user.password or not verify_password(password, user.password):
            return None
        self.log(f"User authenticated: {email}")
        return user

    async def create_user_from_email(self, email: str) -> User:
        user = User(email=email, password="")
        self.db.add(user)
        await self.db.commit()
        await self.db.refresh(user)
        self.log(f"User created from Auth0: {email}")
        return user
