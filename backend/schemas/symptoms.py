from datetime import datetime
from pydantic import BaseModel


class SymptomsCreate(BaseModel):
    hair_thinning: bool
    dry_scalp: bool
    dandruff: bool
    itchy_scalp: bool
    hair_loss_duration: str
    hair_loss_stage: str
    lifestyle: str
    medical_history: str
    gut_health: str
    energy_levels: str
    sleep_quality: str

    class Config:
        orm_mode = True


class SymptomsResponse(SymptomsCreate):
    id: int
    hair_thinning: bool
    dry_scalp: bool
    dandruff: bool
    itchy_scalp: bool
    hair_loss_duration: str
    hair_loss_stage: str
    lifestyle: str
    medical_history: str
    gut_health: str
    energy_levels: str
    sleep_quality: str
    test_taken_at: datetime

    class Config:
        orm_mode = True
