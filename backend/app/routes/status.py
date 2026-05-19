from sqlalchemy import text
from redis.asyncio import Redis
from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.db.redis import get_redis
from app.db.postgres import get_db

status_router = APIRouter()


@status_router.get("/")
async def status_check(
        db: AsyncSession = Depends(get_db),
        redis: Redis = Depends(get_redis),
):
    try:
        await db.execute(text("SELECT 1"))
        postgres_status = "ok"
    except Exception:
        postgres_status = "error"

    try:
        await redis.ping()
        redis_status = "ok"
    except Exception:
        redis_status = "error"

    return {
        "status_code": 200,
        "detail": "ok",
        "result": "working",
        "postgres": postgres_status,
        "redis": redis_status,
    }
