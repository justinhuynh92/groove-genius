from pydantic import BaseModel


class Genres(BaseModel):
    name: str


class GenreOut(BaseModel):
    id: int
    name: str
