from pydantic import BaseModel


class Playlist(BaseModel):
    name: str
    user_id: int


class PlaylistOut(Playlist):
    id: int
    name: str
