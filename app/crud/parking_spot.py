from sqlalchemy.orm import Session
from app.models.parking_spot import ParkingSpot
from app.schemas.parking_spot import ParkingSpotCreate
from app.schemas.parking_spot import ParkingSpotUpdate

from datetime import datetime

def create_parking_spot(db: Session, spot: ParkingSpotCreate):
    db_spot = ParkingSpot(**spot.dict())
    db.add(db_spot)
    db.commit()
    db.refresh(db_spot)
    return db_spot

def get_all_parking_spots(db: Session):
    return db.query(ParkingSpot).all()


def update_parking_spot(db: Session, spot_id: int, is_occupied: bool, user_id: int = None):
    db_spot = db.query(ParkingSpot).filter(ParkingSpot.id == spot_id).first()
    if not db_spot:
        return None

    db_spot.is_occupied = is_occupied
    if is_occupied:
        db_spot.occupied_by_id = user_id
    else:
        db_spot.occupied_by_id = None

    db_spot.updated_at = datetime.utcnow()
    db.commit()
    db.refresh(db_spot)
    return db_spot