from pydantic import BaseModel
from datetime import date
from fastapi import FastAPI

class Users(BaseModel):
    id : str
    name : str
    membership : str

class Books(BaseModel):
    id : str
    title : str
    author : str
    copies_total : int
    copies_available : int

class Transactions(BaseModel):
    id : str
    book_id : str
    user_id : str
    borrowed_date : date
    due_date : date
    returned_date :  date
    fine_amount : int

app = FastAPI()

