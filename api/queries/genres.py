from typing import List
import os
from psycopg_pool import ConnectionPool
from models.genres import Genres

pool = ConnectionPool(conninfo=os.environ["DATABASE_URL"])


class GenreList:
    def get_all(self) -> List[Genres]:
        try:
            with pool.connection() as conn:
                with conn.cursor() as cur:
                    cur.execute(
                        """
                        SELECT *
                        FROM Genres
                        """
                    )
                    results = []
                    for record in cur:
                        genre = Genres(
                            id=record[0],
                            name=record[1],
                        )
                        results.append(genre)
                    return results
        except Exception:
            return {"message": "Could not retreive data"}
