from fastapi import (
    Depends,
    APIRouter,
    HTTPException,
)
from typing import List
from pydantic import BaseModel
from queries.tracks import TrackRepository
from models.tracks import Track, TrackOut, TrackUpdate
from authenticator import authenticator

router = APIRouter()


@router.post("/tracks", response_model=TrackOut)
async def create_track(track: Track, track_repo: TrackRepository = Depends(), account_data: dict = Depends(authenticator.get_current_account_data),):
    created_track = track_repo.create_track(track)
    return created_track

@router.get("/tracks/{track_id}", response_model=dict)
async def get_track_by_id(track_id: int, track_repo: TrackRepository = Depends()):
    track = track_repo.get_track_by_id(track_id)
    if track is None:
        raise HTTPException(status_code=404, detail="Track not found")
    return track

@router.delete("/tracks/{track_id}", response_model=dict)
async def delete_track(track_id: int, track_repo: TrackRepository = Depends()):
    deletion_successful = track_repo.delete_track(track_id)

    if deletion_successful:
        return {"message": "Track deleted successfully"}
    else:
        raise HTTPException(status_code=404, detail="Track not found")

@router.put("/tracks/{track_id}", response_model=TrackUpdate)
async def update_track(
    track_id: int,
    track: TrackUpdate,
    track_repo: TrackRepository = Depends(),
) -> TrackOut:
    response = track_repo.update_track(track_id, track)

    if response:
        return {"message": "Track updated successfully"}
    else:
        raise HTTPException(status_code = 400, detail="Track can't update")
