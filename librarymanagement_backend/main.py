from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from book.routers import router as book_router
from transaction.routers import router as transaction_router
# from librarymanagement_backend.routers.books import router

app = FastAPI()
app.include_router(book_router,tags=["book"])
app.include_router(transaction_router,tags=["transactions"])
# app.add_middleware(
#     CORSMiddleware,
#     allowed_origin = ["*"]
# )