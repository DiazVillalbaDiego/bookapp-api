from pydantic import BaseModel, Field


class Book(BaseModel):
    """Libro tal como lo devuelve la API (nombres en inglés, como pide la rúbrica)."""

    id: int = Field(gt=0)
    title: str
    author: str
    year: int
    publisher: str
    genre: str
    synopsis: str
    rating: float = Field(ge=0, le=5)
    image_url: str



class FavoriteBooks(BaseModel):
    user_id: int =Field(gt=0)
    books: list[Book]

class User(BaseModel):
    id: int = Field(gt=0)
    name: str
