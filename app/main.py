from fastapi import FastAPI, HTTPException

from app.data import BOOKS
from app.models import Book

app = FastAPI(
    title="BookApp API",
    description="API de práctica para el caso BookApp (Aplicaciones para Dispositivos Móviles).",
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
