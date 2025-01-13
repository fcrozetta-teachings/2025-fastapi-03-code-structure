from fastapi import APIRouter
from repositories.db import FakeDatabaseHandler
from src.repositories import db

app = APIRouter(tags=["Users"], prefix="/users/{user_id}/adresses")
db = FakeDatabaseHandler()


@app.get("/")
def list_user_adresses(user_id: int):
    """
    This endpoint should return all user adresses
    """
    return db.get_user_adresses(user_id)


@app.post("/")
def add_user_address(user_id: int, address: str):
    return db.add_user_address(user_id, address)
