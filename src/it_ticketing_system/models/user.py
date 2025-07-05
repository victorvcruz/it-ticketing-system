from sqlalchemy import String, Integer, Enum
from sqlalchemy.orm import Mapped, mapped_column
from .base import Base
import enum

class UserType(str, enum.Enum):
    TECHNICIAN = "technician"
    EMPLOYEE = "employee"
    ADMIN = "admin"

class User(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    name: Mapped[str] = mapped_column(String(100), nullable=False)
    email: Mapped[str] = mapped_column(String(100), unique=True, nullable=False)
    password_hash: Mapped[str] = mapped_column(String(255), nullable=False)
    type: Mapped[UserType] = mapped_column(Enum(UserType), nullable=False)
