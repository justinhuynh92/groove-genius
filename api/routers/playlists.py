from fastapi import (
    Depends,
    APIRouter,
)
from typing import List
from pydantic import BaseModel
from authenticator import authenticator
from queries.playlists import PlaylistRepository
from models.playlists import (
    PlaylistOut,
    PlaylistWithTracksOut,
    NewPlaylist,
    PlaylistTrackLink,
)

router = APIRouter()


@router.post("/playlists", response_model=NewPlaylist)
async def create_playlist(
    playlist: NewPlaylist,
    playlist_repo: PlaylistRepository = Depends(),
    # account_data=Depends(authenticator.get_current_account_data),
):
    id = playlist_repo.create_playlist(playlist)
    return {"id": id, **playlist.dict()}


@router.get("/playlists", response_model=List[PlaylistOut])
async def get_playlists(
    playlist_repo: PlaylistRepository = Depends(),
    # account_data=Depends(authenticator.get_current_account_data),
):
    return playlist_repo.get_playlists()


@router.get(
    "/playlists/{playlist_id}",
    response_model=PlaylistWithTracksOut,
)
async def get_playlist_with_tracks(
    playlist_id: int,
    playlist_repo: PlaylistRepository = Depends(),
    # account_data=Depends(authenticator.get_current_account_data),
):
    return playlist_repo.get_playlist_with_tracks(playlist_id)


@router.post(
    "/playlists/{playlist_id}/tracks", response_model=PlaylistTrackLink
)
async def add_track_to_playlist(
    playlist_id: int,
    track_id: int,
    playlist_repo: PlaylistRepository = Depends(),
    # account_data=Depends(authenticator.get_current_account_data),
):
    return playlist_repo.add_track_to_playlist(playlist_id, track_id)


@router.delete("/playlists/{playlist_id}", response_model=dict)
async def delete_playlist(
    playlist_id: int,
    playlist_repo: PlaylistRepository = Depends(),
    # account_data=Depends(authenticator.get_current_account_data),
):
    return playlist_repo.delete_playlist(playlist_id)


@router.delete(
    "/playlists/{playlist_id}/tracks/{track_id}",
    response_model=PlaylistTrackLink,
)
async def delete_track_from_playlist(
    playlist_id: int,
    track_id: int,
    playlist_repo: PlaylistRepository = Depends(),
    # account_data=Depends(authenticator.get_current_account_data),
):
    return playlist_repo.delete_track_from_playlist(playlist_id, track_id)
