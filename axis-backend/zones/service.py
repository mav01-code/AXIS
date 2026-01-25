from sqlalchemy.orm import Session
from database.models import Zone


def create_zone(
    db: Session,
    name: str,
    center_lat,
    center_lng,
    radius_meters: int | None = None,
    polygon: dict | None = None,
    risk_score: int = 100,
    total_votes: int = 0
):
    zone = Zone(
        name=name,
        center_lat=center_lat,
        center_lng=center_lng,
        radius_meters=radius_meters,
        polygon=polygon,
        risk_score=risk_score,
        total_votes=total_votes,
    )
    db.add(zone)
    db.commit()
    db.refresh(zone)
    return zone


def get_zone(db: Session, zone_id: int):
    return db.query(Zone).filter(Zone.id == zone_id).first()


def update_zone(db: Session, zone_id: int, **updates):
    zone = db.query(Zone).filter(Zone.id == zone_id).first()
    if not zone:
        return None

    for key, value in updates.items():
        if hasattr(zone, key) and value is not None:
            setattr(zone, key, value)

    db.commit()
    db.refresh(zone)
    return zone


def delete_zone(db: Session, zone_id: int):
    zone = db.query(Zone).filter(Zone.id == zone_id).first()
    if not zone:
        return False

    db.delete(zone)
    db.commit()
    return True
