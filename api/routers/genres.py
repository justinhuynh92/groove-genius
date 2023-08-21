from fastapi import (
    Depends,
    APIRouter,
)
from typing import List
from pydantic import BaseModel
from queries.genres import Genres, GenreList

router = APIRouter()


@router.get("/genres", response_model=List[Genres])
async def get_genres(genres: GenreList = Depends()):
    return genres.get_all()
