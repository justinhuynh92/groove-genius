from fastapi import (
    Depends,
    APIRouter,
    HTTPException,
)
from typing import List
from pydantic import BaseModel
from queries.genres import Genres, GenreList
# from authenticator import MyAuthenticator

router = APIRouter()


@router.get("/genres", response_model=List[Genres])
async def get_genres(genres: GenreList = Depends()):
    return genres.get_all()

@router.delete("/api/genre/{genre_id}", response_model=bool)
def delete_genre(
    genre_id: int,
    queries: GenreList = Depends(),
    # account_data: dict = Depends(MyAuthenticator.get_account_data),
):
    if genre_id == account_data["id"]:
        queries.delete_genre(genre_id)
        # MyAuthenticator.logout()
        return True
    else:
        raise HTTPException(
            status_code=403, detail="You can only delete your own genre you made."
        )
