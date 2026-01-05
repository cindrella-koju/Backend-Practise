from pydantic import BaseModel, Field
from datetime import date

class TransactionResponse(BaseModel):
    book_id : str | None = None
    user_id : str | None = None
    borrowed_date : date | None = None
    due_date : date | None = None
    returned_date :  date | None = None
    fine_amount : float | None = None

class Transaction(TransactionResponse):
    id : str = Field(alias="transaction_id",exclude=True)