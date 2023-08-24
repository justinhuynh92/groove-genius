import os
from fastapi import Depends
from jwtdown_fastapi.authentication import Authenticator
from queries.users import UserRepository
from models.users import UserOut, UserOutWithPassword


class MyAuthenticator(Authenticator):
    async def get_account_data(
        self,
        username: str,
        accounts: UserRepository,
    ) -> UserOutWithPassword:
        return accounts.get(username)

    def get_account_getter(
        self,
        accounts: UserRepository = Depends(),
    ):
        return accounts

    def get_hashed_password(self, account: UserOutWithPassword):
        return account.hashed_password

    def get_account_data_for_cookie(self, account: UserOut):
        return account.username, UserOutWithPassword(**account.dict())


authenticator = MyAuthenticator(os.environ["SIGNING_KEY"])
