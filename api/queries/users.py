from typing import List, Union
import os
from psycopg_pool import ConnectionPool
from models.users import UserIn, UserOut, UserOutWithPassword, User

pool = ConnectionPool(conninfo=os.environ["DATABASE_URL"])


class UserRepository:
    def get(self, username: str) -> Union[UserOutWithPassword, None]:
        try:
            with pool.connection() as conn:
                with conn.cursor() as cur:
                    cur.execute(
                        """
                        SELECT id, username, password
                        FROM users
                        WHERE username = %s;
                        """,
                        [username],
                    )
                    ac = cur.fetchone()
                    if ac is None:
                        raise Exception("No account found")
                    else:
                        return UserOutWithPassword(
                            userId=ac[0],
                            username=ac[1],
                            hashed_password=ac[2]
                        )
        except Exception:
            return None
    def create_user(self, account: UserIn, hashed_password: str) -> UserOutWithPassword:
        with pool.connection() as conn:
            with conn.cursor() as cur:
                cur.execute(
                    """
                    INSERT INTO users
                    (username, password)
                    VALUES (%s, %s)
                    RETURNING ID;
                    """,
                    (
                        account.username,
                        hashed_password,
                    ),
                )
                id = cur.fetchone()[0]
                data = account.dict()
                return UserOutWithPassword(userId=id, **data, hashed_password=hashed_password)
    
    def delete_user(self, pk: int):
        with pool.connection() as conn:
            with conn.cursor() as cur:
                cur.execute(
                    """
                    DELETE FROM users
                    WHERE id = %s
                    RETURNING *;
                    """,
                    (pk,),
                )
                id = cur.fetchone()
                return id
    
    def update_user(self, id: int, user: User) -> dict:
        try:
            with pool.connection() as conn:
                with conn.cursor() as cur:
                    cur.execute(
                        """
                        UPDATE users
                        SET username = %s
                        WHERE id = %s;
                        """,
                        (
                            user.username,
                            id,
                        ),
                    )
                    user_data = user.dict()
                    return user_data
        except Exception:
            return {"message": "Could not change fields"}
