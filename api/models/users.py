from pydantic import BaseModel

class User(BaseModel):
    username: str


class UserIn(User):
    password: str


class UserOut(User):
    userId: str

class UserOutWithPassword(User):
    userId: str
    hashed_password: str
