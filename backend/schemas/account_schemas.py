from pydantic import BaseModel
from datetime import date
from typing import Optional


class AccountBase(BaseModel):
    id: int
    name: str
    hashed_password: str
    created_at: date
    updated_at: date

    class Config:
        from_attributes = True
