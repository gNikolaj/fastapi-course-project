from fastapi import APIRouter

status_router = APIRouter()


@status_router.get("/")
def status_check():
    return {
        "status_code": 200,
        "detail": "ok",
        "result": "working"
    }
