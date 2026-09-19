import datetime

from sqlalchemy import Column, Integer,String,Boolean,DateTime
from sqlalchemy.orm import relationship
from app.database import Base

class Ticket(Base):
      __tablename__ ='tickets'
      id=Column(Integer,primary_key=True,index=True)
      ticket_id=Column(Integer,index=True,unique=True,nullable=False)
      customer_name=Column(String,nullable=False)
      customer_email=Column(String,nullable=False)
      created_at=Column(DateTime,default=datetime.datetime.utcnow)
      updated_at=Column(DateTime,default=datetime.datetime.utcnow,onupdate=datetime.datetime.utcnow)
      subject=Column(String,nullable=False)
      status = Column(String, default="Open", nullable=False)
      description=Column(String,nullable=False)
      notes = relationship(
          "Note", back_populates="ticket", cascade="all, delete-orphan"
      )
