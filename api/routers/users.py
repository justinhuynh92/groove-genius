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
from models.users import UserIn, UserOut, UserOutWithPassword, User

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

@router.delete("/users/{id}", response_model=UserOut)
async def delete_user(id: int, user_repo: UserRepository = Depends()):
    deletion_successful = user_repo.delete_user(id)

    if deletion_successful:
        return {"message": "User deleted successfully"}
    else:
        raise HTTPException(status_code=404, detail="User not found")
    
@router.put("/users/{id}", response_model=dict)
async def update_user(
    id: int,
    user: User,
    user_repo: UserRepository = Depends(),
    account_data: dict = Depends(authenticator.get_current_account_data),
):
    response = user_repo.update_user(id, user)
    if response is None:
        return {"message": "Could not change user"}
    return response
