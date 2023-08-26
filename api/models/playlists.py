from typing import List
from models.tracks import Track, TrackOut
from pydantic import BaseModel


class NewPlaylist(BaseModel):
    name: str


class PlaylistWithTracks(BaseModel):
    name: str
    tracks: List[Track]


class PlaylistWithTracksOut(PlaylistWithTracks):
    name: str
    tracks: List[TrackOut]


class Playlist(BaseModel):
    name: str
    track_count: int
