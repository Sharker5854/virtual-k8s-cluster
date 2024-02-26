import os
from fastapi import FastAPI
from views import router
from redis_schemes import User
from redis_om import get_redis_connection


app = FastAPI()

app.include_router(router)

@app.on_event("startup")
async def startup():
    User.Meta.database = get_redis_connection(
        url=f"redis://:{os.getenv("REDIS_DEFAULT_USER_PASSWORD")}@redis-master.redis.svc.cluster.local:6379",
        decode_responses=True
    )
    print("SUCCESSFULLY CONNECTED TO REDIS.")