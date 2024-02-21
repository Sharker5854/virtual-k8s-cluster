import os
from fastapi import APIRouter
from fastapi.responses import JSONResponse


router = APIRouter()

@router.get("/")
def index():
    return JSONResponse(
        content={
            "status_code": 200,
            "msg": os.environ.get('DEFAULT_RESPONSE_MESSAGE')
        }
    )