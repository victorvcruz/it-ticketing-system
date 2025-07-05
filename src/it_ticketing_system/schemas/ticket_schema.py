from pydantic import BaseModel
from enum import Enum
from datetime import datetime

class TicketStatus(str, Enum):
    open = "open"
    in_progress = "in_progress"
    resolved = "resolved"
    closed = "closed"

class TicketCreate(BaseModel):
    title: str
    description: str
    user_id: int

class TicketRead(BaseModel):
    id: int
    title: str
    description: str
    status: TicketStatus
    created_at: datetime
    updated_at: datetime
    user_id: int
    technician_id: int | None = None

    class Config:
        orm_mode = True

class TicketStatusUpdate(BaseModel):
    status: TicketStatus