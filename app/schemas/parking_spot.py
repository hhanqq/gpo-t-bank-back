from datetime import datetime

from pydantic import BaseModel
from typing import Optional

class ParkingSpotBase(BaseModel):
    number: str
    floor_id: int

class ParkingSpotCreate(ParkingSpotBase):
    pass

class ParkingSpotUpdate(BaseModel):
    is_occupied: Optional[bool] = None

class ParkingSpotOut(BaseModel):
    id: int
    number: str
    is_occupied: bool
    floor_id: int
    occupied_by_id: Optional[int] = None
    updated_at: datetime

    class Config:
        from_attributes = True


class ParkingSpotAdminUpdate(BaseModel):
    is_occupied: Optional[bool] = None
    occupied_by_id: Optional[int] = None