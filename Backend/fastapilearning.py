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


from fastapi import FastAPI, Query, HTTPException
from pydantic import BaseModel, Field, EmailStr
from typing import Union, Annotated
from fastapi.middleware.cors import CORSMiddleware
import random

app = FastAPI()

# Handling CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins = ["http://localhost:5173"],
    allow_methods = ["*"],
    allow_credentials = True,
    allow_headers = ["*"]
)

class Books(BaseModel):
    id : Union[int, None] = None
    # Adding Validation to name field
    name : str = Field(
        min_length=4,
        max_length=10,
        description="The name of the books"
    )
    author : str
    price : float

class User(BaseModel):
    username : str
    email : EmailStr

class UpdateBooks(BaseModel):
    name : Union[str,None] = None
    author : Union[str,None] = None
    price : Union[float,None] = None

all_book = []

@app.post("/book",tags=["Books"])
async def addbook(book:Books):
    all_book.append(book)
    return {
        "message"  :  "Book added successfully",
        "Book Detail" : book,
        # "User Detail" : user
    }

@app.get("/book", tags=["Books"], response_model=list[Books])
async def getbook(id: Union[int, None] = None):
    if id is not None:
        return [book for book in all_book if book.id == id]
    return all_book


@app.get("/check",response_model=Books,response_model_include={"id"})
async def check_reponse_model_exclude():
    return {
        "id" : 3,
        "name" : "DASDD",
        "author" : "fsdf",
        "price" : 500.00
    }
    
async def update_book_info(book_id: int,name : Union[str,None] = None, author : Union[str,None] = None, price : Union[float,None] = None):
    for book in all_book:
        if book.id == book_id:
            if name != None:
                book.name = name
            if author != None:
                book.author = author
            if price != None:
                book.price = price

@app.put("/book/{book_id}",tags=["Books"])
async def update_book(book_id: int, book : UpdateBooks ):
    if book_id not in all_book:
        raise HTTPException(status_code=404,detail = "Book does not Exist")
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
    
@app.post("/check")
async def check_for_query(q : Annotated[str | None,Query(max_length=20,pattern="hello$")] = None):
    if q == None:
        return "No query params"
    else:
        return f"There is query {q}"
    

@app.get("/items")
async def read_items(q: Annotated[list[str] | None, Query(alias="Dsad")] = None):
    query_items = {"q": q}
    return query_items

@app.get("/random-between")
def get_random_number_between(
        min_value: Annotated[int, Query(
            title="Minimum Value",
            description="The minimum random number",
            ge=1,
            le=1000
        )] = 1,
        max_value: Annotated[int, Query(
            title="Maximum Value",
            description="The maximum random number",
            ge=1,
            le=1000
        )] = 99
    ):
    if min_value > max_value:
        raise HTTPException(status_code=400, detail="min_value can't be greater than max_value")

    return {
        "min": min_value,
        "max": max_value,
        "random_number": random.randint(min_value, max_value)
    }
