from fastapi import APIRouter
from pydantic import ValidationError
from .schema import Books, BookResponse
from data import books
from .services import update_books
router = APIRouter()

@router.get("/book")
async def get_book():
    # return books
    return [BookResponse(**book) for book in books]

@router.post("/book")
async def post_book(book : Books):
    books.append(book.dict())
    print(books)
    return {
        "message" : f"Book {book.title} added successfully",
        "Book_info" : BookResponse(**book.dict())
    }

@router.put("/book/{book_id}")
async def edit_book(book_id:str,book : BookResponse):
    try:
        await update_books(book_id=book_id,obtained_book=book)
    except ValidationError as e:
        print(e.errors())

    return {
        'message' : f"Book {book_id} update successfully"
    }

@router.delete("/book/{book_id}")
async def delete_book(book_id : str):
    for book in books:
        if book["book_id"] == book_id:
            books.remove(book)
    return {
        'message' :  f"Book {book_id} deleted successfully"
    }