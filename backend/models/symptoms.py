from sqlalchemy import Integer, String, DateTime, Column, ForeignKey, Boolean, JSON
from sqlalchemy.sql import func
from database.database import Base


class Symptoms(Base):
    __tablename__ = "symptoms"
    id = Column(Integer, primary_key=True, nullable=False, index=True)
    hair_thinning = Column(Boolean, nullable=False)
    dry_scalp = Column(Boolean, nullable=False)
    dandruff = Column(Boolean, nullable=False)
    itchy_scalp = Column(Boolean, nullable=False)
    hair_loss_duration = Column(String, nullable=False)
    hair_loss_stage = Column(String, nullable=False)
    lifestyle = Column(String, nullable=False)
    medical_history = Column(String, nullable=False)
    gut_health = Column(String, nullable=False)
    energy_levels = Column(String, nullable=False)
    sleep_quality = Column(String, nullable=False)
    test_taken_at = Column(DateTime(timezone=True), server_default=func.now())