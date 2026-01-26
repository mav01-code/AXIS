from pydantic import BaseModel
from typing import Optional, Dict, Any


class ZoneBase(BaseModel):
    name: str
    center_lat: float
    center_lng: float
    radius_meters: Optional[int] = None
    polygon: Optional[Dict[str, Any]] = None


class ZoneCreate(ZoneBase):
    pass


class ZoneUpdate(BaseModel):
    name: Optional[str] = None
    center_lat: Optional[float] = None
    center_lng: Optional[float] = None
    radius_meters: Optional[int] = None
    polygon: Optional[Dict[str, Any]] = None
    risk_score: Optional[int] = None
    total_votes: Optional[int] = None


class ZoneOut(ZoneBase):
    id: int
    risk_score: int
    total_votes: int

    class Config:
        orm_mode = True
