from datetime import datetime
from typing import List
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database.database import get_db
from models.symptoms import Symptoms
from schemas.symptoms import SymptomsResponse, SymptomsCreate

router = APIRouter(
    prefix="/symptoms",
    tags=["symptoms"]
)


@router.get("/getsymptoms", response_model=List[SymptomsResponse])
def get_symptoms(db: Session = Depends(get_db)):
    symptoms = db.query(Symptoms).all()
    if not symptoms:
        raise HTTPException(status_code=404, detail="No symptom records found.")
    else:
        return symptoms


@router.post("/addsymptoms", response_model=SymptomsResponse)
def add_symptoms(symptoms_data: SymptomsCreate, db: Session = Depends(get_db)):
    # Create an instance of Symptoms (SQLAlchemy model) to insert into the database
    new_symptom = Symptoms(
        hair_thinning=symptoms_data.hair_thinning,
        dry_scalp=symptoms_data.dry_scalp,
        dandruff=symptoms_data.dandruff,
        itchy_scalp=symptoms_data.itchy_scalp,
        hair_loss_duration=symptoms_data.hair_loss_duration,
        hair_loss_stage=symptoms_data.hair_loss_stage,
        lifestyle=symptoms_data.lifestyle,
        medical_history=symptoms_data.medical_history,
        gut_health=symptoms_data.gut_health,
        energy_levels=symptoms_data.energy_levels,
        sleep_quality=symptoms_data.sleep_quality,
        test_taken_at=datetime.utcnow()  # Capture the current time
    )

    # Add the new symptom record to the database and commit
    try:
        db.add(new_symptom)
        db.commit()
        db.refresh(new_symptom)  # Optional, to get the latest data including the ID
    except Exception as e:
        db.rollback()  # In case of an error, rollback the transaction
        raise HTTPException(status_code=400, detail="Error adding symptoms to database.")

    # Return the newly created symptom record
    return new_symptom  # Pydantic model will serialize it to JSON
