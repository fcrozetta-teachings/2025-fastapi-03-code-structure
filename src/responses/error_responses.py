from pydantic import BaseModel


class NotFoundSchema(BaseModel):
    message: str = "Resource not found"
