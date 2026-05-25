from redis.asyncio import Redis
from app.core.config import settings


class RedisClient:
    _instance: Redis | None = None
    _self = None

    def __new__(cls):
        if cls._self is None:
            cls._self = super().__new__(cls)
        return cls._self

    async def connect(self):
        self._instance = Redis.from_url(
            settings.REDIS_URL,
            encoding="utf-8",
            decode_responses=True,
        )

    async def disconnect(self):
        if self._instance:
            await self._instance.aclose()

    def get(self) -> Redis:
        return self._instance


redis_client = RedisClient()
