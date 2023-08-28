from typing import List, Optional
from models.tracks import Track, TrackOut
from pydantic import BaseModel


class NewPlaylist(BaseModel):
    name: str


class PlaylistWithTracks(BaseModel):
    id: int
    name: str
    tracks: Optional[List[TrackOut]] = None


class PlaylistWithTracksOut(PlaylistWithTracks):
    name: str
    tracks: Optional[List[TrackOut]] = None


class Playlist(BaseModel):
    name: str
    track_count: Optional[int] = None


class PlaylistOut(Playlist):
    name: str
    track_count: Optional[int] = None
