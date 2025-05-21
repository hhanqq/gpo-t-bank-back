from sqlalchemy import Column, Integer, String
from app.config.database import Base

class Floor(Base):
    __tablename__ = "floors"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True)  # Например: B1, B2