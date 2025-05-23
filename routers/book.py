# built-in libraries
from uuid import UUID
# installed libraries
from fastapi import APIRouter, HTTPException
# code libraries/folder
from database import books
from schemas.book import Response, BookCreate, BookUpdate
from services.book import book_service


book_router = APIRouter()


@book_router.get("/books")
def get_books():
    return books


@book_router.get("/books/{id}")
def get_book_by_id(id: UUID):
    book = book_service.get_book_by_id(id)
    if not book:
        # return {status_code : 404, detail  "book not found."}
        return Response(message="book not found", has_error=True, status_code=404)
    return book


@book_router.post("/books")
def add_book(book_in: BookCreate):
    book = book_service.create_book(book_in)
    return Response(message="Book added successfully", data=book.model_dump())


@book_router.put("/{id}")
def update_book(id: UUID, book_in: BookUpdate):
    book = book_service.update_book(id, book_in)
    if not book:
        raise HTTPException(
            status_code=404,
            detail=f"Book with id: {id} not found"
        )
    return Response(message="Book updated successfully", data=book)


@book_router.delete("/{id}")
def delete_book(id: UUID):
    is_deleted = book_service.delete_book(id)
    if not is_deleted:
        raise HTTPException(
            status_code=404,
            detail=f"Book with id: {id} not found"
        )
    return Response(message="Book deleted successfully")

