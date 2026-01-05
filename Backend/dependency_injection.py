from typing import Annotated
from fastapi import Depends, FastAPI, Request, Query
import time
app = FastAPI()

# async def common_parameters(q: str | None = None, skip: int = 0, limit: int = 100):
#     return {"q": q, "skip": skip, "limit": limit}


# @app.get("/items/")
# async def read_items(commons: dict = Depends(common_parameters)):
#     return commons


# @app.get("/users/")
# async def read_users(commons: Annotated[dict, Depends(common_parameters)]):
#     return commons


# Middleware

# @app.middleware("http")
# async def add_process_time_header(request: Request, call_next):
#     start_time = time.perf_counter()
#     response = await call_next(request)
#     process_time = time.perf_counter() - start_time
#     response.headers["X-Process-Time"] = str(process_time)
#     return response


# Query parameters
data = [1,3,4,6,6,7,8,8,8,3,34,5,6,5]

# Additional validation(The query params cannot be more that 50length)
@app.get('/')
async def query_params(skip : int = 0, limit : int = 10,q : Annotated[ str | None,Query(min_length=3, max_length=50, pattern="^fixedquery$")] = None):
    return data[skip:limit]