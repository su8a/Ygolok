import uuid

from pydantic import BaseModel
from pydantic import EmailStr


class TunedModel(BaseModel):
    class Config:
        """tells pydantic to convert even non dict obj to json"""

        orm_mode = True


class ShowUser(TunedModel):
    id: uuid.UUID
    name: str
    email: EmailStr
    is_active: bool


class UserCreate(BaseModel):
    name: str
    email: EmailStr
    password: str


class Token(BaseModel):
    access_token: str
    token_type: str