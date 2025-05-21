from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.core.security import get_current_user
from app.crud.user import get_all_users, update_user
from app.crud.parking_spot import get_all_parking_spots, update_parking_spot
from app.schemas.user import UserOut, UserUpdate
from app.schemas.parking_spot import ParkingSpotAdminUpdate, ParkingSpotOut
from app.config.database import get_db


router = APIRouter(prefix="/admin", tags=["Admin"])

def check_admin(user):
    if not user.is_admin:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Доступ запрещён"
        )

@router.get("/spots", response_model=list[ParkingSpotOut])
def list_spots(user: dict = Depends(get_current_user), db: Session = Depends(get_db)):
    check_admin(user)
    return get_all_parking_spots(db)

@router.put("/spots/{spot_id}", response_model=ParkingSpotOut)
def update_spot(spot_id: int, spot_update: ParkingSpotAdminUpdate, user: dict = Depends(get_current_user), db: Session = Depends(get_db)):
    check_admin(user)
    updated = update_parking_spot(db, spot_id=spot_id, spot_update=spot_update)
    if not updated:
        raise HTTPException(status_code=404, detail="Место не найдено")
    return updated

@router.get("/users", response_model=list[UserOut])
def list_users(user: dict = Depends(get_current_user), db: Session = Depends(get_db)):
    check_admin(user)
    return get_all_users(db)

@router.put("/users/{user_id}", response_model=UserOut)
def edit_user(user_id: int, user_update: UserUpdate, current_user: dict = Depends(get_current_user), db: Session = Depends(get_db)):
    check_admin(current_user)
    updated = update_user(db, user_id=user_id, user_update=user_update)
    if not updated:
        raise HTTPException(status_code=404, detail="Пользователь не найден")
    return updated