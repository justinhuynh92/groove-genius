from typing import List
import os
from psycopg_pool import ConnectionPool
from models.users import UserIn, UserOut

pool = ConnectionPool(conninfo=os.environ["DATABASE_URL"])


class UserRepository:
    def get_all(self) -> List[UserOut]:
        try:
            with pool.connection() as conn:
                with conn.cursor() as cur:
                    cur.execute(
                        """
                        SELECT *
                        FROM users
                        """
                    )
                    results = []
                    for record in cur:
                        user = UserOut(
                            userId=record[0], username=record[1]
                        )
                        results.append(user)
                    return results
        except Exception:
            return {"message": "Could not get all accounts"}
