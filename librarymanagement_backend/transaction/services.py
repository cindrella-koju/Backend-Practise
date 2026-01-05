from .schema import TransactionResponse
from data import transactions

async def update_transacation(transaction_id : str, transaction_info : TransactionResponse):
    for transaction in transactions:
        if transaction["transaction_id"] == transaction_id:
            if transaction_info.borrowed_date:
                transaction["borrowed_date"] = transaction_info.borrowed_date
            if transaction_info.due_date:
                transaction["due_date"] = transaction_info.due_date
            if transaction_info.fine_amount:
                transaction["fine_amount"] = transaction_info.fine_amount