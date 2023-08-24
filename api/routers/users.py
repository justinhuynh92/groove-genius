from fastapi import (
    Depends,
    HTTPException,
    status,
    Response,
    APIRouter,
    Request,
)
from jwtdown_fastapi.authentication import Token
from authenticator import authenticator
from pydantic import BaseModel
from queries.users import UserRepository
from models.users import UserIn, UserOut, UserOutWithPassword

class AccountForm(BaseModel):
    username: str
    password: str

class AccountToken(Token):
    account: UserOut

class HttpError(BaseModel):
    detail: str

router = APIRouter()


@router.post("/users", response_model=AccountToken)
async def create_account(
    info: UserIn,
    request: Request,
    response: Response,
    repo: UserRepository = Depends(),
):
    hashed_password = authenticator.hash_password(info.password)
    account = repo.create_user(info, hashed_password)
    form = AccountForm(username=info.username, password=info.password)
    token = await authenticator.login(response, request, form, repo)
    return AccountToken(account=account, **token.dict())