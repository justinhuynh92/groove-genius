from pydantic import BaseModel


class Track(BaseModel):
    title: str
    artist: str
    album: str
    genre: str


class TrackOut(BaseModel):
    id: int
    title: str
    artist: str
    album: str
    genre: str


class TrackUpdate(BaseModel):
    title: str
    artist: str
    album: str
    genre: str
