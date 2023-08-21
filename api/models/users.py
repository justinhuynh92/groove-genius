from pydantic import BaseModel

class UserIn(BaseModel):
    username: str
    password: str


class UserOut(BaseModel):
    userId: str
    username: str

class UserOutWithPassword(UserOut):
    hashed_password: str
