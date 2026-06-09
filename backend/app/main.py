import uvicorn
from fastapi import FastAPI
from contextlib import asynccontextmanager
from fastapi.middleware.cors import CORSMiddleware

from app.core.logger import log
from app.core.config import settings
from app.db.redis import redis_client
from app.routes.user import users_router
from app.routes.status import status_router


@asynccontextmanager
async def lifespan(_):
    log("Connecting to Redis...")
    await redis_client.connect()
    log("Redis connected")
    yield
    log("Disconnecting from Redis...")
    await redis_client.disconnect()
    log("Redis disconnected")


app = FastAPI(lifespan=lifespan)

app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.CORS_ORIGINS,
    allow_methods=settings.CORS_METHODS,
    allow_headers=settings.CORS_HEADERS,
    allow_credentials=settings.CORS_CREDENTIALS,
)

app.include_router(users_router)
app.include_router(status_router)


def main():
    uvicorn.run('app.main:app', host=settings.APP_HOST, port=settings.APP_PORT, reload=settings.APP_RELOAD)


if __name__ == "__main__":
    main()
