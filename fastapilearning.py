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

app = FastAPI()


@app.get("/")
async def changeboolval(short : bool = False):
    if short:
        return "This is response from bool"
    else:
    
        return "This reposne is not from bool"
