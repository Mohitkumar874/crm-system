import uuid
from typing import List, Optional

from fastapi import APIRouter, Depends, HTTPException, Query, status
from sqlalchemy.orm import Session

from app.database import get_db
from app.models.note import Note
from app.models.ticket import Ticket
from app.schemas.ticket import (
    NoteResponse,
    TicketCreate,
    TicketDetail,
    TicketListItem,
    TicketUpdate,
)

router = APIRouter(prefix="/tickets", tags=["Tickets"])


def generate_ticket_id() -> str:
    """Generates a unique ticket ID like TKT-A1B2"""
    return f"TKT-{uuid.uuid4().hex[:4].upper()}"


# 1. CREATE TICKET
@router.post("", status_code=status.HTTP_201_CREATED)
def create_ticket(ticket_data: TicketCreate, db: Session = Depends(get_db)):
    new_ticket_id = generate_ticket_id()
    db_ticket = Ticket(
        ticket_id=new_ticket_id,
        customer_name=ticket_data.customer_name,
        customer_email=ticket_data.customer_email,
        subject=ticket_data.subject,
        description=ticket_data.description,
        status="Open",
    )
    db.add(db_ticket)
    db.commit()
    db.refresh(db_ticket)
    return {"ticket_id": db_ticket.ticket_id, "created_at": db_ticket.created_at}


# 2. LIST ALL TICKETS (WITH SEARCH & FILTER)
@router.get("", response_model=List[TicketListItem])
def get_tickets(
    status: Optional[str] = None,
    search: Optional[str] = Query(None),
    db: Session = Depends(get_db),
):
    query = db.query(Ticket)

    # Filter by status if query parameter is provided (Open, In Progress, Closed)
    if status:
        query = query.filter(Ticket.status == status)

    # Search across customer name, email, subject, description, and ticket_id
    if search:
        search_pattern = f"%{search}%"
        query = query.filter(
            (Ticket.customer_name.ilike(search_pattern))
            | (Ticket.customer_email.ilike(search_pattern))
            | (Ticket.subject.ilike(search_pattern))
            | (Ticket.description.ilike(search_pattern))
            | (Ticket.ticket_id.ilike(search_pattern))
        )

    return query.order_by(Ticket.created_at.desc()).all()


# 3. VIEW TICKET DETAILS
@router.get("/{ticket_id}", response_model=TicketDetail)
def get_ticket_detail(ticket_id: str, db: Session = Depends(get_db)):
    ticket = db.query(Ticket).filter(Ticket.ticket_id == ticket_id).first()
    if not ticket:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Ticket not found"
        )
    return ticket


# 4. UPDATE TICKET STATUS & ADD NOTES
@router.put("/{ticket_id}")
def update_ticket(
    ticket_id: str, update_data: TicketUpdate, db: Session = Depends(get_db)
):
    ticket = db.query(Ticket).filter(Ticket.ticket_id == ticket_id).first()
    if not ticket:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Ticket not found"
        )

    # Update status if provided
    if update_data.status:
        ticket.status = update_data.status

    # Append note if provided
    if update_data.notes:
        new_note = Note(ticket_id=ticket.ticket_id, note_text=update_data.notes)
        db.add(new_note)

    db.commit()
    db.refresh(ticket)
    return {"success": True, "updated_at": ticket.updated_at}