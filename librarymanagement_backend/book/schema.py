from pydantic import BaseModel, Field
from datetime import date

class BookResponse(BaseModel):
    title : str | None = None
    author : str | None = None
    copies_total : int | None = None
    copies_available : int | None = None

class Books(BookResponse):
    id : str = Field(alias="book_id")
