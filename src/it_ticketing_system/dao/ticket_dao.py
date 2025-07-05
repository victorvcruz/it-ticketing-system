from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from src.it_ticketing_system.models.ticket import Ticket
from src.it_ticketing_system.models.ticket import TicketStatus

class TicketDAO:
    def __init__(self, session: AsyncSession):
        self.session = session

    async def create(self, ticket: Ticket) -> Ticket:
        self.session.add(ticket)
        await self.session.commit()
        await self.session.refresh(ticket)
        return ticket

    async def get_by_id(self, ticket_id: int) -> Ticket | None:
        result = await self.session.execute(
            select(Ticket).where(Ticket.id == ticket_id)
        )
        return result.scalar_one_or_none()

    async def get_all(self) -> list[Ticket]:
        result = await self.session.execute(select(Ticket))
        return result.scalars().all()

    async def get_by_status(self, status: TicketStatus) -> list[Ticket]:
        result = await self.session.execute(
            select(Ticket).where(Ticket.status == status)
        )
        return result.scalars().all()

    async def update_status(self, ticket: Ticket, new_status: TicketStatus) -> Ticket:
        ticket.status = new_status
        await self.session.commit()
        await self.session.refresh(ticket)
        return ticket

    async def delete(self, ticket: Ticket) -> None:
        await self.session.delete(ticket)
        await self.session.commit()
