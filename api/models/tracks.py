from pydantic import BaseModel

class Track(BaseModel):
    title: str
    artist: str
    album: str
    genre_id: int

class TrackOut(Track):
    id:int
    title: str
