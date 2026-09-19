from pydantic import BaseModel,EmailStr
from typing import Optional,List
from datetime import datetime


class NoteBase(BaseModel):
    note_text: str


class NoteResponse(NoteBase):
    id: int
    created_at: datetime

    class Config:
        from_attributes = True





class TicketCreate(BaseModel):
    customer_name: str
    subject: str
    description: str
    customer_email: EmailStr

class TicketUpdate(BaseModel):
    status:Optional[str] = None
    notes: Optional[str] = None

class TicketListItem(BaseModel):
    """Fields sent back for the main dashboard list view"""
    ticket_id: str
    customer_name: str
    subject: str
    status: str
    created_at: datetime

    class Config:
        from_attributes = True

class TicketDetail(BaseModel):
    """Complete detail view including customer details and associated notes"""
    ticket_id: str
    customer_name: str
    customer_email: EmailStr
    subject: str
    description: str
    status: str
    notes:List[NoteResponse] = []
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True


