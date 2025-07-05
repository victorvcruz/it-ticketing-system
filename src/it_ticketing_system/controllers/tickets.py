from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from src.it_ticketing_system.db import get_session
from src.it_ticketing_system.schemas.ticket_schema import TicketCreate, TicketRead, TicketStatus
from src.it_ticketing_system.dao.ticket_dao import TicketDAO
from src.it_ticketing_system.models.ticket import Ticket
from src.it_ticketing_system.schemas.ticket_schema import TicketStatusUpdate

router = APIRouter(prefix="/tickets", tags=["Tickets"])

@router.post("/", response_model=TicketRead)
async def create_ticket(data: TicketCreate, session: AsyncSession = Depends(get_session)):
    dao = TicketDAO(session)
    ticket = Ticket(
        title=data.title,
        description=data.description,
        user_id=data.user_id
    )
    return await dao.create(ticket)

@router.get("/", response_model=list[TicketRead])
async def list_tickets(session: AsyncSession = Depends(get_session)):
    dao = TicketDAO(session)
    return await dao.get_all()

@router.get("/status/{status}", response_model=list[TicketRead])
async def list_by_status(status: TicketStatus, session: AsyncSession = Depends(get_session)):
    dao = TicketDAO(session)
    return await dao.get_by_status(status)

@router.patch("/{ticket_id}/status", response_model=TicketRead)
async def update_ticket_status(
    ticket_id: int,
    status_update: TicketStatusUpdate,
    session: AsyncSession = Depends(get_session)
):
    dao = TicketDAO(session)
    ticket = await dao.get_by_id(ticket_id)
    if not ticket:
        raise HTTPException(status_code=404, detail="Ticket not found")

    updated_ticket = await dao.update_status(ticket, status_update.status)
    return updated_ticket