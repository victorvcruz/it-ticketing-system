from pydantic import BaseModel, EmailStr
from enum import Enum

class UserType(str, Enum):
    technician = "technician"
    employee = "employee"
    admin = "admin"

class UserCreate(BaseModel):
    name: str
    email: EmailStr
    password: str
    type: UserType

class UserRead(BaseModel):
    id: int
    name: str
    email: EmailStr
    type: UserType

    class Config:
        orm_mode = True
