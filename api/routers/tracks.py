from fastapi import (
    Depends,
    APIRouter,
)
from typing import List
from pydantic import BaseModel
from queries.tracks import TrackRepository
from models.tracks import Track, TrackOut

router = APIRouter()


@router.post("/tracks", response_model=List[TrackOut])
async def create_track(track: Track, track_repo: TrackRepository = Depends()):
    id = track_repo.create_track(track)
