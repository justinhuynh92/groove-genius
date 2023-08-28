from typing import List
import os
from psycopg_pool import ConnectionPool
from models.genres import Genres, GenreOut

pool = ConnectionPool(conninfo=os.environ["DATABASE_URL"])


class GenreRepository:
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
                        genre = GenreOut(
                            id=record[0],
                            name=record[1],
                        )
                        results.append(genre)
                    return results
        except Exception:
            return {"message": "Could not retreive data"}

    def create_genre(self, genre: Genres) -> int:
        try:
            with pool.connection() as conn:
                with conn.cursor() as cur:
                    cur.execute(
                        """
                        INSERT INTO Genres
                        (name)
                        VALUES (%s)
                        RETURNING id;
                        """,
                        (genre.name,),
                    )
                    id = cur.fetchone()[0]
                    return id
        except Exception:
            return {"message": "Could not create genre"}

    def delete_genre(self, genre_id: int) -> None:
        with pool.connection() as conn:
            with conn.cursor() as cur:
                cur.execute(
                    """
                    DELETE FROM track_genres
                    WHERE genre_id = %s;
                    """,
                    (genre_id,),
                )

                cur.execute(
                    """
                    DELETE FROM genres
                    WHERE id = %s;
                    """,
                    (genre_id,),
                )

    def genre_by_id(self, id: int) -> dict:
        try:
            with pool.connection() as conn:
                with conn.cursor() as cur:
                    cur.execute(
                        """
                        SELECT id, name
                        FROM Genres
                        WHERE id = %s;
                        """,
                        (id,),
                    )
                    genre_by_id = cur.fetchone()
                    if genre_by_id:
                        response = {
                            "id": genre_by_id[0],
                            "name": genre_by_id[1],
                        }
                    return response
        except Exception:
            return {"message": "Could not retrieve data"}

    def update_genre(self, id: int, genre: Genres) -> dict:
        try:
            with pool.connection() as conn:
                with conn.cursor() as cur:
                    cur.execute(
                        """
                        UPDATE genres
                        SET name = %s
                        WHERE id = %s;
                        """,
                        (
                            genre.name,
                            id,
                        ),
                    )
                    genre_data = genre.dict()
                    return Genres(**genre_data)
        except Exception:
            return {"message": "Could not change fields"}
