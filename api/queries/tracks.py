from typing import List
import os
from psycopg_pool import ConnectionPool
from models.tracks import Track, TrackOut, TrackUpdate

pool = ConnectionPool(conninfo=os.environ["DATABASE_URL"])


class TrackRepository:
    def create_track(self, track: Track) -> TrackOut:
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
                    created_track = TrackOut(
                        id=id,
                        title=track.title,
                        artist=track.artist,
                        album=track.album,
                        genre_id=track.genre_id,
                    )

                return created_track
        except Exception:
            return {"message": "Could not create track"}

    def get_track_by_id(self, track_id: int):
        try:
            with pool.connection() as conn:
                with conn.cursor() as cur:
                    cur.execute(
                        """
                        SELECT genre_id
                        FROM tracks
                        WHERE id = %s;
                        """,
                        (track_id,),
                    )
                    genre_ids = cur.fetchone()

                    if genre_ids:
                        genre_ids = genre_ids[0]
                        for genre_id in genre_ids:
                            cur.execute(
                                """
                                SELECT track_id
                                FROM track_genres
                                WHERE track_id = %s AND genre_id = %s;
                                """,
                                (track_id, genre_id),
                            )
                            association_exists = cur.fetchone()
                            if not association_exists:
                                cur.execute(
                                    """
                                    INSERT INTO track_genres (track_id, genre_id)
                                    VALUES (%s, %s);
                                    """,
                                    (track_id, genre_id),
                                )

                    cur.execute(
                        """
                        SELECT t.id, t.title, t.artist, t.album, array_agg(g.id) AS genre_ids, array_agg(g.name) AS genre_names
                        FROM tracks t
                        JOIN track_genres tg ON t.id = tg.track_id
                        JOIN genres g ON tg.genre_id = g.id
                        WHERE t.id = %s
                        GROUP BY t.id, t.title, t.artist, t.album;
                        """,
                        (track_id,),
                    )
                    row = cur.fetchone()
                    if row:
                        response = {
                            "id": row[0],
                            "title": row[1],
                            "artist": row[2],
                            "album": row[3],
                            "genre_names": row[5],
                        }
                        return response
                    else:
                        return None
        except Exception:
            return {"message": "Could not retrieve track"}

    def delete_track(self, track_id: int):
        with pool.connection() as conn:
            with conn.cursor() as cur:
                cur.execute(
                    """
                    DELETE FROM track_genres
                    WHERE track_id = %s;
                    """,
                    (track_id,),
                )

                cur.execute(
                    """
                    DELETE FROM tracks
                    WHERE id = %s;
                    """,
                    (track_id,),
                )

                deletion_successful = cur.rowcount > 0

        return deletion_successful

    def update_tracks(self, track_id: int, track: TrackUpdate) -> TrackOut:
        try:
            with pool.connection() as conn:
                with conn.cursor() as cur:
                    cur.execute(
                        """
                        UPDATE track
                        SET title = %s
                            artist = %s,
                            album = %s,
                            genre_id = %s
                        WHERE track_id = %s
                        """,
                        (
                            track.title,
                            track.artist,
                            track.album,
                            track.genre_id,
                            track_id,
                        ),
                    )
                    account_data = track.dict()
                    return TrackUpdate(**account_data)
        except Exception:
            return {"message": "Could not update track"}
