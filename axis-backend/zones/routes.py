from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List

from database.db import get_db
from database.models import Zone
from schemas.zone import ZoneCreate, ZoneUpdate, ZoneOut
from crud.zone import (
    create_zone,
    get_zone,
    update_zone,
    delete_zone
)

router = APIRouter(
    prefix="/zones",
    tags=["Zones"]
)

@router.post(
    "",
    response_model=ZoneOut,
    status_code=status.HTTP_201_CREATED
)
def create_zone_route(
    zone: ZoneCreate,
    db: Session = Depends(get_db)
):
    return create_zone(
        db=db,
        name=zone.name,
        center_lat=zone.center_lat,
        center_lng=zone.center_lng,
        radius_meters=zone.radius_meters,
        polygon=zone.polygon
    )

@router.get("", response_model=List[ZoneOut])
def list_zones(db: Session = Depends(get_db)):
    return db.query(Zone).all()

@router.get("/{zone_id}", response_model=ZoneOut)
def read_zone(
    zone_id: int,
    db: Session = Depends(get_db)
):
    zone = get_zone(db, zone_id)
    if not zone:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Zone not found"
        )
    return zone


@router.put("/{zone_id}", response_model=ZoneOut)
def update_zone_route(
    zone_id: int,
    updates: ZoneUpdate,
    db: Session = Depends(get_db)
):
    zone = update_zone(
        db=db,
        zone_id=zone_id,
        **updates.dict(exclude_unset=True)
    )

    if not zone:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Zone not found"
        )

    return zone

@router.delete(
    "/{zone_id}",
    status_code=status.HTTP_204_NO_CONTENT
)
def delete_zone_route(
    zone_id: int,
    db: Session = Depends(get_db)
):
    success = delete_zone(db, zone_id)
    if not success:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Zone not found"
        )
