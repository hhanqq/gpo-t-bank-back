from pydantic import BaseModel

class FloorBase(BaseModel):
    name: str

class FloorCreate(FloorBase):
    pass

class FloorOut(FloorBase):
    id: int

    class Config:
        from_attributes = True