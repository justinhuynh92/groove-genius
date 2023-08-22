from pydantic import BaseModel


class Playlist(BaseModel):
    name: str
    user_id: int


class PlaylistOut(Playlist):
    name: str
    user_id: int
