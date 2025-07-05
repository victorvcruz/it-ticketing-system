from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from src.it_ticketing_system.db import get_session
from src.it_ticketing_system.schemas.user_schema import UserCreate, UserRead
from src.it_ticketing_system.dao.user_dao import UserDAO
from src.it_ticketing_system.models.user import User
import hashlib

router = APIRouter(prefix="/users", tags=["Users"])

def hash_password(password: str) -> str:
    return hashlib.sha256(password.encode()).hexdigest()

@router.post("/", response_model=UserRead)
async def create_user(user_data: UserCreate, session: AsyncSession = Depends(get_session)):
    dao = UserDAO(session)
    existing = await dao.get_by_email(user_data.email)
    if existing:
        raise HTTPException(status_code=400, detail="Email already registered")

    user = User(
        name=user_data.name,
        email=user_data.email,
        password_hash=hash_password(user_data.password),
        type=user_data.type
    )
    return await dao.create(user)

@router.get("/", response_model=list[UserRead])
async def list_users(session: AsyncSession = Depends(get_session)):
    dao = UserDAO(session)
    return await dao.get_all()
