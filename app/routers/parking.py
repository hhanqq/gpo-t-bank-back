from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.schemas.floor import FloorCreate, FloorOut
from app.schemas.parking_spot import ParkingSpotCreate, ParkingSpotOut, ParkingSpotUpdate
from app.crud.floor import create_floor, get_all_floors
from app.crud.parking_spot import create_parking_spot, get_all_parking_spots, update_parking_spot
from app.config.database import get_db
from app.core.security import get_current_user


router = APIRouter()

@router.post("/floors/", response_model=FloorOut)
def add_floor(floor: FloorCreate, db: Session = Depends(get_db)):
    return create_floor(db, floor)

@router.get("/floors/", response_model=list[FloorOut])
def list_floors(db: Session = Depends(get_db)):
    return get_all_floors(db)

@router.post("/spots/", response_model=ParkingSpotOut)
def add_spot(spot: ParkingSpotCreate, db: Session = Depends(get_db)):
    return create_parking_spot(db, spot)

@router.get("/spots/", response_model=list[ParkingSpotOut])
def list_spots(db: Session = Depends(get_db)):
    return get_all_parking_spots(db)

@router.put("/spots/{spot_id}", response_model=ParkingSpotOut)
def update_spot(
    spot_id: int,
    spot_update: ParkingSpotUpdate,
    db: Session = Depends(get_db),
    current_user: dict = Depends(get_current_user)
):
    db_spot = update_parking_spot(
        db=db,
        spot_id=spot_id,
        is_occupied=spot_update.is_occupied,
        user_id=current_user.id
    )
    if not db_spot:
        raise HTTPException(status_code=404, detail="Место не найдено")
    return db_spot