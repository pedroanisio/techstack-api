from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from .models import TechStackDB, VersionDB
from .schemas import TechStackItem, Version
from .dependencies import get_db
from typing import List
import logging

logger = logging.getLogger(__name__)

router = APIRouter()

TECH_STACK_NOT_FOUND = "Tech stack '{}' not found."

@router.get("/health", response_model=dict)
def health_check():
    return {"status": "ok"}

@router.get("/techstack", response_model=List[TechStackItem])
def get_tech_stack(db: Session = Depends(get_db)):
    tech_stacks = db.query(TechStackDB).all()
    return tech_stacks

@router.get("/techstack/{name}", response_model=TechStackItem)
def get_techstack_by_name(name: str, db: Session = Depends(get_db)):
    tech_stack = db.query(TechStackDB).filter(TechStackDB.name == name).first()
    if not tech_stack:
        raise HTTPException(status_code=404, detail=TECH_STACK_NOT_FOUND.format(name))
    return tech_stack


@router.get("/techstack/{name}/versions", response_model=List[Version])
def get_techstack_versions(name: str, db: Session = Depends(get_db)):
    tech_stack = db.query(TechStackDB).filter(TechStackDB.name == name).first()
    if not tech_stack:
        logger.error(f"Tech stack '{name}' not found.")
        raise HTTPException(status_code=404, detail=f"Tech stack '{name}' not found.")
    return tech_stack.versions



@router.post("/techstack", response_model=TechStackItem)
def create_tech_stack(tech_stack: TechStackItem, db: Session = Depends(get_db)):
    existing_stack = db.query(TechStackDB).filter(TechStackDB.name == tech_stack.name).first()
    if existing_stack:
        raise HTTPException(status_code=400, detail="Tech stack with this name already exists.")

    db_tech_stack = TechStackDB(name=tech_stack.name, description=tech_stack.description)
    db.add(db_tech_stack)
    db.commit()
    db.refresh(db_tech_stack)

    for version in tech_stack.versions:
        db_version = VersionDB(version=version.version, description=version.description, tech_stack_id=db_tech_stack.id)
        db.add(db_version)

    db.commit()
    return db_tech_stack

@router.post("/techstack/{name}/versions", response_model=Version)
def add_version(name: str, version: Version, db: Session = Depends(get_db)):
    tech_stack = db.query(TechStackDB).filter(TechStackDB.name == name).first()
    if not tech_stack:
        raise HTTPException(status_code=404, detail=f"Tech stack '{name}' not found.")
    db_version = VersionDB(version=version.version, description=version.description, tech_stack_id=tech_stack.id)
    db.add(db_version)
    db.commit()
    db.refresh(db_version)
    return db_version
