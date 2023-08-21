from typing import List
import os
from psycopg_pool import ConnectionPool
from models.tracks import Track

pool = ConnectionPool(conninfo=os.environ["DATABASE_URL"])


class TrackRepository:
    def create_track(self, track: Track) -> int:
        try:
            with pool.connection() as conn:
                with conn.cursor() as cur:
                    cur.execute(
                        """
                        INSERT INTO tracks
                        (title, artist, album, genre_id)
                        VALUES (%s, %s, %s, %s)
                        RETURNING id;
                        """,
                        (
                            track.title,
                            track.artist,
                            track.album,
                            track.genre_id,
                        ),
                    )
                    id = cur.fetchone()[0]
                    return id
        except Exception:
            return {"message": "Could not create track"}