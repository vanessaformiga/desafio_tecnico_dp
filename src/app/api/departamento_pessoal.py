from fastapi import APIRouter, Depends, HTTPException, UploadFile, File, status
from sqlalchemy.orm import Session
from db.database import SessionLocal
from db.models import DepartamentoPessoal
from pydantic import BaseModel
from typing import Optional
import pandas as pd


class DepartamentoPessoalCreate(BaseModel):
    nome: str
    responsavel: Optional[str] = None
    contato: Optional[str] = None
    observacao: Optional[str] = None

class DepartamentoPessoalOut(DepartamentoPessoalCreate):
    id_dp: int


router = APIRouter(
    prefix="/dp",
    tags=["Departamento Pessoal"]
)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.post("/", response_model=DepartamentoPessoalOut, status_code=201)
def create_dp(dp: DepartamentoPessoalCreate, db: Session = Depends(get_db)):
    existing = db.query(DepartamentoPessoal).filter(
        DepartamentoPessoal.nome == dp.nome
    ).first()
    if existing:
        raise HTTPException(status_code=400, detail="Departamento Pessoal já cadastrado")
    
    new_dp = DepartamentoPessoal(**dp.dict())
    db.add(new_dp)
    db.commit()
    db.refresh(new_dp)
    return new_dp


@router.get("/", response_model=list[DepartamentoPessoalOut])
def list_dp(db: Session = Depends(get_db)):
    return db.query(DepartamentoPessoal).all()


@router.post("/import", status_code=201)
def import_dp(file: UploadFile = File(...), db: Session = Depends(get_db)):
    try:
        df = pd.read_excel(file.file)
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Arquivo inválido: {e}")
    
    registros = []
    for _, row in df.iterrows():
        dp_data = DepartamentoPessoal(**row.to_dict())
        db.add(dp_data)
        registros.append(dp_data)
    db.commit()
    return {"importados": len(registros)}