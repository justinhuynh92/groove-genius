from pydantic import BaseModel


class Genres(BaseModel):
    id: int
    name: str
