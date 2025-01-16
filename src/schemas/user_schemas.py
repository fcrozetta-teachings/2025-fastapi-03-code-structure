from pydantic import BaseModel


class UserCreate(BaseModel):
    username: str


class UserBase(UserCreate):
    user_id: int


class UserInDB(UserBase):
    addresses: list[str]
    is_active: bool
