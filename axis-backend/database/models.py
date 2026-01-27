from sqlalchemy import (Column, Integer, String, DECIMAL, JSON, TIMESTAMP)
from sqlalchemy.sql import func
from database.db import Base


class Zone(Base):
    __tablename__ = "zones"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255), nullable=False)
    center_lat = Column(DECIMAL(10, 7), nullable=False)
    center_lng = Column(DECIMAL(10, 7), nullable=False)
    radius_meters = Column(Integer, nullable=True)
    polygon = Column(JSON, nullable=True)
    risk_score = Column(Integer, default=100)
    total_votes = Column(Integer, default=0)
    updated_at = Column(
        TIMESTAMP,
        server_default=func.now(),
        onupdate=func.now()
    )