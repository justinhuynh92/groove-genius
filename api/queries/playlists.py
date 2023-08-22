from typing import List
import os
from psycopg_pool import ConnectionPool
from models.playlists import Playlist

pool = ConnectionPool(conninfo=os.environ["DATABASE_URL"])


class PlaylistRepository:
    def create_playlist(self, playlist: Playlist) -> int:
        try:
            with pool.connection() as conn:
                with conn.cursor() as cur:
                    cur.execute(
                        """
                        INSERT INTO playlists
                        (name, user_id)
                        VALUES (%s, %s)
                        RETURNING name, user_id;
                        """,
                        (
                            playlist.name,
                            playlist.user_id,
                        ),
                    )
                    id = cur.fetchone()[0]
                    return id
        except Exception:
            return {"message": "Could not create playlist"}
