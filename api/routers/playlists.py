from fastapi import (
    Depends,
    APIRouter,
)
from typing import List
from pydantic import BaseModel
from authenticator import authenticator
from queries.playlists import PlaylistRepository
from models.playlists import (
    Playlist,
    PlaylistOut,
    PlaylistWithTracksOut,
    PlaylistWithTracks,
)

router = APIRouter()


@router.post("/playlists", response_model=PlaylistOut)
async def create_playlist(
    playlist: Playlist,
    playlist_repo: PlaylistRepository = Depends(),
    account_data=Depends(authenticator.get_current_account_data),
):
    id = playlist_repo.create_playlist(playlist)
    if id is None:
        return {"message": "Could not create a playlist."}
    return {"id": id, **playlist.dict()}


@router.get("/users/{user_id}/playlists", response_model=List[PlaylistOut])
async def get_playlists(
    user_id: int, playlist_repo: PlaylistRepository = Depends()
):
    playlists = playlist_repo.get_playlists(user_id)
    if playlists is None:
        return {"message": "Could not get playlists."}
    return playlists


@router.get(
    "/playlists/{playlist_id}",
    response_model=PlaylistWithTracksOut,
)
async def get_playlist_with_tracks(
    playlist_id: int,
    playlist_repo: PlaylistRepository = Depends(),
):
    playlist = playlist_repo.get_playlist_with_tracks(playlist_id)
    if playlist is None:
        return {"message": "Could not get playlist."}
    return playlist
