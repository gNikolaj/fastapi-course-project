from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker

from app.core.config import settings

test_engine = create_async_engine(settings.TEST_DATABASE_URL)

TestSessionLocal = async_sessionmaker(
    test_engine,
    expire_on_commit=False,
)


async def get_test_db():
    async with TestSessionLocal() as session:
        yield session
