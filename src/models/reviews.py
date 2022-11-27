from sqlalchemy import Column, ForeignKey, Integer, String, DateTime, Enum, Boolean
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship
from src.connectors.database import Base
import enum
from sqlalchemy.ext.hybrid import hybrid_property

# Reviews table
class Reviews(Base):
    __tablename__ = "reviews"

    id = Column(Integer, primary_key=True)
    bookId = Column(Integer, index=True)
    rating = Column(Integer)
    description = Column(String)