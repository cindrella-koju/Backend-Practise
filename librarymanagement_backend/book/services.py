from data import books
from .schema import BookResponse

async def update_books(book_id:str,obtained_book : BookResponse):
    for book in books:
        if book["book_id"] == book_id:
            if obtained_book.title != None:
                book["title"] = obtained_book.title
            if obtained_book.author != None:
                book["author"] = obtained_book.author
            if obtained_book.copies_total != None:
                book["copies_total"] = obtained_book.copies_total
            if obtained_book.copies_available != None:
                book["copies_available"] = obtained_book.copies_available
    return True
