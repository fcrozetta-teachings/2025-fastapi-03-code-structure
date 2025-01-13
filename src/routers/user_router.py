from fastapi import APIRouter
from repositories.db import FakeDatabaseHandler

app = APIRouter(tags=["Users"], prefix="/users")
db = FakeDatabaseHandler()


@app.get("/")
def list_users(include_inactive: bool = False, limit: int = 10, offset: int = 0):
    return db.get_all_users(include_inactive, limit, offset)


@app.get("/{user_id}")
def get_user(user_id: int):
    """
    this endpoint has to return the user details for a given user id
    """
    return db.get_user(user_id)


@app.post("/")
def create_user(payload: dict):
    return db.create_user(payload)


@app.delete("/{user_id}")
def inactivate_user(user_id: int):
    return db.inactivate_user(user_id)
