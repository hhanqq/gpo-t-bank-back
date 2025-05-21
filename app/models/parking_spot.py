from sqlalchemy import Column, Integer, String, Boolean, DateTime, ForeignKey
from datetime import datetime
from sqlalchemy.orm import relationship
from app.config.database import Base

class ParkingSpot(Base):
    __tablename__ = "parking_spots"

    id = Column(Integer, primary_key=True, index=True)
    number = Column(String, unique=True)
    is_occupied = Column(Boolean, default=False)
    occupied_by_id = Column(Integer, ForeignKey("users.id"), nullable=True)
    floor_id = Column(Integer, ForeignKey("floors.id"))
    updated_at = Column(DateTime, default=datetime.utcnow)

    user = relationship("User")
    floor = relationship("Floor")