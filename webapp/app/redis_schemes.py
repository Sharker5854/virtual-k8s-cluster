import datetime
from redis_om import HashModel


class User(HashModel):
    username: str
    password: str
    email: str
    age: int
    register_date: datetime.date