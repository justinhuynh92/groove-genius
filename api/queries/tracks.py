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
                        (title, artist, album, genre)
                        VALUES (%s, %s, %s, %s)
                        RETURNING id;
                        """,
                        (
                            track.title,
                            track.artist,
                            track.album,
                            track.genre,
                        ),
                    )
                    id = cur.fetchone()[0]
                    created_track = TrackOut(
                        id=id,
                        title=track.title,
                        artist=track.artist,
                        album=track.album,
                        genre=track.genre,
                    )

                return created_track
        except Exception:
            return {"message": "Could not create track"}

    def get_track_by_id(self, track_id: int):
        try:
            with pool.connection() as conn:
                with conn.cursor() as cur:
                    # Now just fetch the track and genre as a string
                    cur.execute(
                        """
                    SELECT id, title, artist, album, genre
                    FROM tracks
                    WHERE id = %s;
                    """,
                        (track_id,),
                    )
                    row = cur.fetchone()
                    if row:
                        # Pack that data into a dict
                        response = {
                            "id": row[0],
                            "title": row[1],
                            "artist": row[2],
                            "album": row[3],
                            "genre": row[4],
                        }
                        return response
                    else:
                        return None
        except Exception as e:
            print(f"Exception: {e}")
            return {"message": "Could not retrieve track"}

    def delete_track(self, track_id: int):
        with pool.connection() as conn:
            with conn.cursor() as cur:
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
                            genre = %s
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

    def get_tracks_by_title(self, title: str):
        try:
            with pool.connection() as conn:
                with conn.cursor() as cur:
                    cur.execute(
                        """
                        SELECT *
                        FROM tracks t
                        WHERE t.title = %s
                        """,
                        (title,),
                    )
                    rows = cur.fetchall()
                    return rows
        except Exception:
            return {"message": "Could not retrieve tracks by title"}
