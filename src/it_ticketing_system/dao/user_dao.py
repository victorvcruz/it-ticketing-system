from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from src.it_ticketing_system.models.user import User

class UserDAO:
    def __init__(self, session: AsyncSession):
        self.session = session

    async def create(self, user: User) -> User:
        self.session.add(user)
        await self.session.commit()
        await self.session.refresh(user)
        return user

    async def get_by_id(self, user_id: int) -> User | None:
        result = await self.session.execute(
            select(User).where(User.id == user_id)
        )
        return result.scalar_one_or_none()

    async def get_all(self) -> list[User]:
        result = await self.session.execute(select(User))
        return result.scalars().all()

    async def get_by_email(self, email: str) -> User | None:
        result = await self.session.execute(
            select(User).where(User.email == email)
        )
        return result.scalar_one_or_none()

    async def delete(self, user: User) -> None:
        await self.session.delete(user)
        await self.session.commit()
