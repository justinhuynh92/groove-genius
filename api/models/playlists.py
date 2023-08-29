from typing import List, Optional
from models.tracks import Track
from pydantic import BaseModel


class NewPlaylist(BaseModel):
    name: str


class PlaylistWithTracks(BaseModel):
    name: str
    tracks: Optional[List[Track]] = None


class PlaylistWithTracksOut(PlaylistWithTracks):
    id: int
    name: str
    tracks: Optional[List[Track]] = None


class Playlist(BaseModel):
    name: str
    track_count: Optional[int] = None


class PlaylistOut(Playlist):
    id: int
    name: str
    track_count: Optional[int] = None


class PlaylistTrackLink(BaseModel):
    playlist_id: int
    track_id: int
