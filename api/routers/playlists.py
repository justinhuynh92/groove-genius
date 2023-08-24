from fastapi import (
    Depends,
    APIRouter,
)
from typing import List
from pydantic import BaseModel
from queries.playlists import PlaylistRepository
from models.playlists import Playlist, PlaylistOut

router = APIRouter()


@router.post("/playlists", response_model=PlaylistOut)
async def create_playlist(
    playlist: Playlist, playlist_repo: PlaylistRepository = Depends()
):
    id = playlist_repo.create_playlist(playlist)
    if id is None:
        return {"message": "Could not create a playlist."}
    return {"id": id, **playlist.dict()}


@router.get("/playlists/{user_id}", response_model=List[PlaylistOut])
async def get_playlists(
    user_id: int, playlist_repo: PlaylistRepository = Depends()
):
    playlists = playlist_repo.get_playlists(user_id)
    if playlists is None:
        return {"message": "Could not get playlists."}
    return playlists
