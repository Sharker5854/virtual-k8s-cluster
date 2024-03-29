import datetime
from pydantic import BaseModel, EmailStr


class User(BaseModel):
    username: str
    password: str
    email: EmailStr
    age: int
    register_date: datetime.date