from pydantic import BaseModel

class Track(BaseModel):
    title: str
    artist: str
    album: str
    genre_id: list[int]

class TrackOut(BaseModel):
    id:int
    title: str
    artist: str
    album: str
    genre_id: list[int]

class TrackUpdate(BaseModel):
    id:int
    title: str
    artist: str
    album: str
    genre_id: list[int]

