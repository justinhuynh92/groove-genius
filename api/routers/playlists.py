from fastapi import (
    Depends,
    APIRouter,
)
from typing import List
from pydantic import BaseModel
from queries.playlists import PlaylistRepository
from models.playlists import Playlist, PlaylistOut

router = APIRouter()


@router.post("/playlists", response_model=List[PlaylistOut])
async def create_playlist(
    playlist: Playlist, playlist_repo: PlaylistRepository = Depends()
):
    id = playlist_repo.create_playlist(playlist)
    return {"id": id, **playlist.dict()}
