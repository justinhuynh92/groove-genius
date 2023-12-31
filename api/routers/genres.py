from fastapi import (
    Depends,
    APIRouter,
    # HTTPException,
)
from typing import List

# from pydantic import BaseModel
from queries.genres import GenreRepository
from models.genres import Genres, GenreOut
from authenticator import authenticator

router = APIRouter()


@router.get("/genres", response_model=List[GenreOut])
async def get_genres(
    genre: GenreRepository = Depends(),
    # account_data: dict = Depends(authenticator.get_current_account_data),
):
    return genre.get_all()


@router.get("/genres/{id}", response_model=dict)
async def genre_by_id(id: int, genre_repo: GenreRepository = Depends()):
    id_genre = genre_repo.genre_by_id(id)
    if id_genre is None:
        return {"message": "Could not retrieve genre"}
    return id_genre


@router.post("/genres/new", response_model=dict)
async def create_genre(
    genre: Genres,
    genre_repo: GenreRepository = Depends(),
):
    created_genre = genre_repo.create_genre(genre)
    return {"id": created_genre, **genre.dict()}


@router.delete("/genres/{genre_id}", response_model=bool)
async def delete_genre(
    genre_id: int,
    queries: GenreRepository = Depends(),
    # account_data: dict = Depends(authenticator.get_current_account_data),
):
    queries.delete_genre(genre_id)
    return True


@router.put("/genres/{id}", response_model=dict)
async def update_genre(
    id: int,
    genre: Genres,
    genre_repo: GenreRepository = Depends(),
    account_data: dict = Depends(authenticator.get_current_account_data),
):
    response = genre_repo.update_genre(id, genre)
    if response is None:
        return {"message": "Could not change data"}
    return response
