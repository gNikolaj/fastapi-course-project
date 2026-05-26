from sqlalchemy import text
from redis.asyncio import Redis
from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.db.postgres import get_db
from app.db.redis import redis_client

status_router = APIRouter()


@status_router.get("/")
async def status_check():
    return {
        "status_code": 200,
        "detail": "ok",
        "result": "working",
    }


@status_router.get("/postgres")
async def postgres_status_check(
        db: AsyncSession = Depends(get_db),
):
    try:
        await db.execute(text("SELECT 1"))
        postgres_status = "ok"
    except Exception:
        postgres_status = "error"

    return {
        "postgres": postgres_status,
    }


@status_router.get("/redis")
async def redis_status_check(
        redis: Redis = Depends(redis_client.get),
):
    try:
        await redis.ping()
        redis_status = "ok"
    except Exception:
        redis_status = "error"

    return {
        "redis": redis_status,

    }
