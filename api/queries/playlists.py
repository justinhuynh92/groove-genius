from typing import List, Optional
import os
from psycopg_pool import ConnectionPool
from models.playlists import Playlist, PlaylistWithTracks, NewPlaylist
from models.tracks import Track
from fastapi import HTTPException

pool = ConnectionPool(conninfo=os.environ["DATABASE_URL"])


class PlaylistRepository:
    def create_playlist(self, playlist: NewPlaylist) -> int:
        try:
            with pool.connection() as conn:
                with conn.cursor() as cur:
                    cur.execute(
                        """

                        INSERT INTO playlists
                        (name)
                        VALUES (%s)
                        RETURNING id;
                        
                        """,
                        (playlist.name,),
                    )
                    id = cur.fetchone()[0]
                    return id
        except Exception:
            raise HTTPException(
                status_code=400, detail="Cannot create playlist."
            )

    def get_playlists(
        self,
    ) -> List[Playlist]:
        try:
            with pool.connection() as conn:
                with conn.cursor() as cur:
                    cur.execute(
                        """

                        SELECT *
                        FROM playlists

                        """
                    )
                    playlists = cur.fetchall()
                    columns = [desc[0] for desc in cur.description]
                    return [dict(zip(columns, row)) for row in playlists]
        except Exception:
            raise HTTPException(status_code=404, detail="Playlists not found.")

    def get_playlist_with_tracks(
        self, playlist_id: int
    ) -> Optional[PlaylistWithTracks]:
        try:
            with pool.connection() as conn:
                with conn.cursor() as cur:
                    cur.execute(
                        """
    
                        SELECT p.name AS playlist_name
                        FROM playlists p
                        WHERE p.id = %s;
                        
                        """,
                        (playlist_id,),
                    )
                    row = cur.fetchone()
                    if not row:
                        return None
                    playlist_name = row[0]

                    cur.execute(
                        """
    
                        SELECT t.*
                        FROM playlists p
                        JOIN playlist_tracks pt ON p.id = pt.playlist_id
                        JOIN tracks t ON pt.track_id = t.id
                        WHERE p.id = %s;
                        
                        """,
                        (playlist_id,),
                    )
                    rows = cur.fetchall()
                    tracks = [
                        Track(
                            id=row[0],
                            title=row[1],
                            artist=row[2],
                            album=row[3],
                            genre_id=row[4],
                        )
                        for row in rows
                    ]
                    return PlaylistWithTracks(
                        id=playlist_id,
                        name=playlist_name,
                        tracks=tracks if tracks else None,
                    )
        except Exception:
            raise HTTPException(status_code=404, detail="Playlist not found.")
