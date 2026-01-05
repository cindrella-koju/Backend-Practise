from pydantic import BaseModel, Field

class UserResponse(BaseModel):
    name : str
    membership : str

class Users(UserResponse):
    id : str = Field(alias="user_id",exclude=True)
    password : str