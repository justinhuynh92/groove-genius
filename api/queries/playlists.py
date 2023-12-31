from typing import List, Optional

import os
from psycopg_pool import ConnectionPool
from models.playlists import (
    PlaylistOut,
    PlaylistWithTracksOut,
    NewPlaylist,
    PlaylistTrackLink,
)
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

    def get_playlists(self) -> List[PlaylistOut]:
        try:
            with pool.connection() as conn:
                with conn.cursor() as cur:
                    cur.execute(
                        """
                        SELECT p.id, p.name, COUNT(pt.track_id) AS track_count
                        FROM playlists p
                        LEFT JOIN playlist_tracks pt ON p.id = pt.playlist_id
                        GROUP BY p.id, p.name;
                        """
                    )
                    rows = cur.fetchall()
                    return [
                        PlaylistOut(id=row[0], name=row[1], track_count=row[2])
                        for row in rows
                    ]
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))

    def delete_playlist(self, playlist_id: int) -> dict:
        try:
            with pool.connection() as conn:
                with conn.cursor() as cur:
                    cur.execute(
                        """

                        DELETE FROM playlists
                        WHERE id = %s;

                        """,
                        (playlist_id,),
                    )
                    return {"message": "Playlist deleted."}
        except Exception:
            raise HTTPException(
                status_code=400, detail="Unable to delete playlist."
            )

    def get_playlist_with_tracks(
        self, playlist_id: int
    ) -> Optional[PlaylistWithTracksOut]:
        try:
            print(f"playlist_id: {playlist_id}")
            tracks = []
            playlist_name = None
            with pool.connection() as conn:
                with conn.cursor() as cur:
                    # Query to check if playlist exists
                    cur.execute(
                        """
                    SELECT id, name FROM playlists WHERE id = %s;
                    """,
                        (playlist_id,),
                    )
                    row = cur.fetchone()
                    if not row:
                        raise HTTPException(404, "Playlist not found.")

                    playlist_name = row[1]

                    # Query to get tracks associated with playlist
                    cur.execute(
                        """
                    SELECT t.id, t.title, t.artist, t.album, t.genre
                    FROM playlist_tracks pt
                    JOIN tracks t ON pt.track_id = t.id
                    WHERE pt.playlist_id = %s;
                    """,
                        (playlist_id,),
                    )
                    rows = cur.fetchall()

                    # Build the tracks list
                    for row in rows:
                        tracks.append(
                            Track(
                                id=row[0],
                                title=row[1],
                                artist=row[2],
                                album=row[3],
                                genre=row[4],
                            )
                        )

            print(
                f"Fetched {len(tracks)} tracks for playlist ID: {playlist_id}"
            )
            return PlaylistWithTracksOut(
                id=playlist_id,
                name=playlist_name,
                tracks=tracks if tracks else [],
            )
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))

    def add_track_to_playlist(
        self, playlist_id: int, track_id: int
    ) -> PlaylistTrackLink:
        try:
            with pool.connection() as conn:
                with conn.cursor() as cur:
                    cur.execute(
                        """
                        INSERT INTO playlist_tracks
                        (playlist_id, track_id)
                        VALUES (%s, %s)
                        RETURNING playlist_id, track_id;
                        """,
                        (playlist_id, track_id),
                    )
                    row = cur.fetchone()
                    if not row:
                        return None
                    else:
                        return PlaylistTrackLink(
                            playlist_id=row[0],
                            track_id=row[1],
                        )
        except Exception:
            raise HTTPException(
                status_code=400, detail="Unable to add track to playlist."
            )

    def delete_track_from_playlist(
        self, playlist_id: int, track_id: int
    ) -> PlaylistTrackLink:
        try:
            with pool.connection() as conn:
                with conn.cursor() as cur:
                    cur.execute(
                        """
                        DELETE FROM playlist_tracks
                        WHERE playlist_id = %s AND track_id = %s
                        RETURNING playlist_id, track_id;
                        """,
                        (playlist_id, track_id),
                    )
                    row = cur.fetchone()
                    if not row:
                        return []
                    else:
                        return PlaylistTrackLink(
                            playlist_id=row[0],
                            track_id=row[1],
                        )
        except Exception:
            raise HTTPException(
                status_code=400, detail="Unable to delete track from playlist."
            )
