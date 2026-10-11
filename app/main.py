from fastapi import FastAPI, HTTPException

from app.data import BOOKS, fav_books
from app.models import Book, User, FavoriteBooks

app = FastAPI(
    title="BookApp API",
    description="API de práctica para el caso de una biblioteca.",
    version="1.0.0",
)

@app.get("/api/books", response_model=list[Book], tags=["books"])
def list_books() -> list[Book]:
    """Devuelve todos los libros del catálogo."""
    return BOOKS

@app.get("/api/books/{book_id}", response_model=Book, tags=["books"])
def get_book(book_id: int) -> Book:
    """Devuelve el detalle de un libro por su id."""
    for book in BOOKS:
        if book.id == book_id:
            return book
    raise HTTPException(status_code=404, detail="Book not found")

@app.get("/api/fav_books/{user_id}", response_model=list[Book], tags=["fav_books"])
def get_fav(user_id:int)-> list[Book]:
    for fav in fav_books:
        if fav.user_id == user_id:
            return fav.books
    raise HTTPException(status_code=404, detail="Favorites books list not found")