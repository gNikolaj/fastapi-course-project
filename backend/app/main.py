import uvicorn
from fastapi import FastAPI

from app.routes.status import status_router
from app.core.config import settings

app = FastAPI()

app.include_router(status_router)


def main():
    uvicorn.run('app.main:app', host=settings.APP_HOST, port=settings.APP_PORT, reload=settings.APP_RELOAD)


if __name__ == "__main__":
    main()
