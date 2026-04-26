import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.core.config import settings
from app.routes.status import status_router

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.CORS_ORIGINS,
    allow_methods=settings.CORS_METHODS,
    allow_headers=settings.CORS_HEADERS,
    allow_credentials=settings.CORS_CREDENTIALS,
)

app.include_router(status_router)


def main():
    uvicorn.run('app.main:app', host=settings.APP_HOST, port=settings.APP_PORT, reload=settings.APP_RELOAD)


if __name__ == "__main__":
    main()
