from fastapi import APIRouter
from data import transactions
from .schema import TransactionResponse
from .services import update_transacation
router = APIRouter()

@router.get("/transaction")
async def get_transaction():
    return [TransactionResponse(**transaction) for transaction in transactions]

@router.put("/transaction/{transaction_id}")
async def edit_transaction(transaction_id : str, transaction_info : TransactionResponse):
    await update_transacation(transaction_id=transaction_id, transaction_info=transaction_info )

    return {
        'message' : f"Transation {transaction_id} updated successfully"
    }