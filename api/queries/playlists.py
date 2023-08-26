from typing import List
import os
from psycopg_pool import ConnectionPool
from models.playlists import Playlist, PlaylistWithTracks, NewPlaylist
from models.tracks import Track

pool = ConnectionPool(conninfo=os.environ["DATABASE_URL"])


class PlaylistRepository:
    def create_playlist(self, playlist: NewPlaylist) -> int:
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
            return {"message": "Could not create playlist."}

    def get_playlists(self, user_id: int) -> List[Playlist]:
        try:
            with pool.connection() as conn:
                with conn.cursor() as cur:
                    cur.execute(
                        """

                        SELECT name, user_id
                        FROM playlists
                        WHERE user_id = %s;

                        """,
                        (user_id,),
                    )
                    playlists = cur.fetchall()
                    return playlists
        except Exception:
            return {"message": "Could not get playlists."}

    def get_playlist_with_tracks(self, playlist_id: int) -> PlaylistWithTracks:
        try:
            with pool.connection() as conn:
                with conn.cursor() as cur:
                    cur.execute(
                        """

                        SELECT p.name AS playlist_name, t.*
                        FROM playlists p
                        JOIN playlist_tracks pt ON p.id = pt.playlist_id
                        JOIN tracks t ON pt.track_id = t.id
                        WHERE p.id = %s;
                        
                        """,
                        (playlist_id,),
                    )
                    rows = cur.fetchall()
                    if rows:
                        playlist_name = rows[0][0]
                        tracks = [
                            Track(
                                id=row[1],
                                title=row[2],
                                artist=row[3],
                                album=row[4],
                                genre_id=row[5],
                            )
                            for row in rows
                        ]
                        return PlaylistWithTracks(
                            id=playlist_id, name=playlist_name, tracks=tracks
                        )
                    else:
                        return None
        except Exception:
            return {"message": "Could not get playlist."}
