import os
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from redis_schemes import User as redisUser
from schemes import User


router = APIRouter()

@router.get("/")
def index():
    return JSONResponse(
        content={
            "status_code": 200,
            "msg": os.environ.get('DEFAULT_RESPONSE_MESSAGE')
        }
    )

@router.post("/create-user")
async def create_user(user: User):
    redis_user = redisUser(
        username=user.username,
        password=user.password,     # of course need to add password hashing
        email=str(user.email),
        age=user.age,
        register_date=user.register_date
    )
    redis_user.save()
    return {
        "status": 200,
        "new_username": redis_user.username
    }

@router.get("/all-users")
async def get_all_users():
    return {
            "status": 200,
            "users": [redisUser.get(user) for user in redisUser.all_pks()]
        }