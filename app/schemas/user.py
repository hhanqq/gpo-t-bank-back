from pydantic import BaseModel, EmailStr, validator
from typing import Optional

class UserBase(BaseModel):
    email: EmailStr
    first_name: str
    last_name: str
    middle_name: Optional[str] = None
    telegram_username: Optional[str] = None
    office_address: str

class UserCreate(UserBase):
    password: str

    # @validator('password')
    # def password_not_empty(cls, v):
    #     if not v or len(v.strip()) == 0:
    #         raise ValueError("Пароль не может быть пустым")
    #     return v

class UserOut(UserBase):
    id: int
    is_active: bool
    is_admin: bool
    is_email_verified: bool

    class Config:
        from_attributes = True


class UserUpdate(BaseModel):
    is_active: Optional[bool] = None
    is_admin: Optional[bool] = None