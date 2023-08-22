from fastapi import (
    Depends,
    APIRouter,
    HTTPException,
)
from typing import List
from pydantic import BaseModel
from queries.tracks import TrackRepository
from models.tracks import Track, TrackOut

router = APIRouter()


@router.post("/tracks", response_model=TrackOut)
async def create_track(track: Track, track_repo: TrackRepository = Depends()):
    created_track = track_repo.create_track(track)
    return created_track

@router.get("/tracks/{track_id}", response_model=dict)
async def get_track_by_id(track_id: int, track_repo: TrackRepository = Depends()):
    track = track_repo.get_track_by_id(track_id)
    if track is None:
        raise HTTPException(status_code=404, detail="Track not found")
    return track