# from fastapi import FastAPI
# from typing import Union
# from pydantic import BaseModel
# from datetime import date
# from enum import Enum


# class EnumModel(str, Enum):
#     user1 = "User1"
#     user2 = "User2"
#     user3 = "User3"

# app = FastAPI()

# class ToDoItem(BaseModel):
#     id : int
#     title : str
#     discription : str
#     complete_date : date
#     status : str
# todos = []

# @app.post("/post")
# def create_post(item:ToDoItem):
#     todos.append(item)
#     return "To Do Item added successfully"

# @app.get("/post")
# def get_post(id:int):
#     print(todos[0])
#     return todos

# @app.get("/username/{name}")
# def get_username(name : EnumModel):
#     if name is EnumModel.user1:
#         return f"The user is {name.value} "
    
#     if name.value == "User2":
#         return f"The user is {name}"
    
#     return f"The user is {name}"

# @app.get("file/{filepath:path}")
# async def read_file(filepath : str):
#     return filepath


from fastapi import FastAPI
from pydantic import BaseModel
from typing import Union

app = FastAPI()

class Books(BaseModel):
    id : Union[int, None] = None
    name : str
    author : str
    price : float

class UpdateBooks(BaseModel):
    name : Union[str,None] = None
    author : Union[str,None] = None
    price : Union[float,None] = None

all_book = []

@app.post("/book")
async def addbook(book:Books):
    all_book.append(book)
    return {
        "message"  :  "Book added successfully",
        "Book Detail" : book
    }

@app.get("/book")
async def getbook(id : Union[int,None] = None):
    if id != None:
        for book in all_book:
            if int(book.id) == id:
                return book
    else:
        return all_book
    
async def update_book_info(book_id: int,name : Union[str,None] = None, author : Union[str,None] = None, price : Union[float,None] = None):
    for book in all_book:
        if book.id == book_id:
            if name != None:
                book.name = name
            if author != None:
                book.author = author
            if price != None:
                book.price = price

@app.put("/book/{book_id}")
async def update_book(book_id: int, book : UpdateBooks ):
    if book.name:
        await update_book_info(book_id=book_id,name=book.name)
    if book.author:
        await update_book_info(book_id=book_id,author=book.author)
    if book.price:
        await update_book_info(book_id=book_id,price=book.price)
    
    return {
        "message" : f"Book of id {book_id} updated succesfully"
    }
    # return book

@app.get("/")
async def changeboolval(short : bool = False):
    if short:
        return "This is response from bool"
    else:
    
        return "This reposne is not from bool"
