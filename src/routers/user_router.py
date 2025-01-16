from typing import Annotated
from fastapi import APIRouter, FastAPI
from fastapi.responses import JSONResponse
from fastapi import Query
from responses.error_responses import NotFoundSchema
from repositories.db import FakeDatabaseHandler
from schemas.user_schemas import UserBase, UserInDB, UserCreate

app = APIRouter(tags=["Users"], prefix="/users")
db = FakeDatabaseHandler()


@app.get("/", response_model=list[UserBase])
def list_users(include_inactive: Annotated[bool, Query(default=False)], limit: Annotated[int, Query(ge=0)], offset: Annotated[int, Query(ge=0, default=0)]):
    return db.get_all_users(include_inactive, limit, offset)


@app.get("/{user_id}", response_model=UserInDB, responses={404: {"model": NotFoundSchema}})
def get_user(user_id: int):
    """
    this endpoint has to return the user details for a given user id
    """
    # ! If user exists: return user
    # ! If user does not exist: return 404
    if (user := db.get_user(user_id)):
        return user
    return JSONResponse(content={"message": "not found"}, status_code=404)

# ? Method 1 of response codes
# @app.post("/", response_model=UserInDB)
# def create_user(payload: UserCreate):
#     response = JSONResponse(content=db.create_user(
#         payload.model_dump()), status_code=201)
#     return response

# ? Method 2 of response codes (preferred)


@app.post("/", response_model=UserInDB, status_code=201)
def create_user(payload: UserCreate):
    return db.create_user(payload.model_dump())


@app.delete("/{user_id}")
def inactivate_user(user_id: int):
    return db.inactivate_user(user_id)
