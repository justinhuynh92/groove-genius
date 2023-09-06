from fastapi import (
    Depends,
    APIRouter,
    HTTPException,
)

# from pydantic import BaseModel
from queries.tracks import TrackRepository
from models.tracks import Track, TrackOut, TrackUpdate
from authenticator import authenticator

router = APIRouter()


@router.post("/tracks", response_model=TrackOut)
async def create_track(
    track: Track,
    track_repo: TrackRepository = Depends(),
):
    created_track = track_repo.create_track(track)
    return created_track


@router.get("/tracks/{track_id}", response_model=dict)
async def get_track_by_id(
    track_id: int, track_repo: TrackRepository = Depends()
):
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


@router.put("/tracks/{track_id}", response_model=dict)
async def update_track(
    track_id: int,
    track: TrackUpdate,
    track_repo: TrackRepository = Depends(),
    account_data: dict = Depends(authenticator.get_current_account_data),
) -> TrackOut:
    response = track_repo.update_tracks(track_id, track)

    if response:
        return {"message": "Track updated successfully"}
    else:
        raise HTTPException(status_code=400, detail="Track can't update")
    
@router.get("/tracks", response_model=list)
async def get_tracks_by_title(
    title: str, track_repo: TrackRepository = Depends()
):
    tracks = track_repo.get_tracks_by_title(title)

    if not tracks:
        raise HTTPException(status_code=404, detail="No tracks found for this username")

    return tracks
