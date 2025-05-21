from sqlalchemy.orm import Session
from app.models.floor import Floor
from app.schemas.floor import FloorCreate

def create_floor(db: Session, floor: FloorCreate):
    db_floor = Floor(**floor.dict())
    db.add(db_floor)
    db.commit()
    db.refresh(db_floor)
    return db_floor

def get_all_floors(db: Session):
    return db.query(Floor).all()