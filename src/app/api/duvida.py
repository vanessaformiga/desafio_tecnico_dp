from fastapi import APIRouter, Depends, HTTPException, UploadFile, File, status
from sqlalchemy.orm import Session
from db.database import SessionLocal
from db.models import Duvida, Servidor
from pydantic import BaseModel
from datetime import datetime
import pandas as pd


class DuvidaCreate(BaseModel):
    id_servidor: int

class DuvidaOut(DuvidaCreate):
    id_duvida: int
    data_hora: datetime


router = APIRouter(
    prefix="/duvidas",
    tags=["Dúvidas"]
)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.post("/", response_model=DuvidaOut, status_code=201)
def create_duvida(duvida: DuvidaCreate, db: Session = Depends(get_db)):
    # Verifica se o servidor existe
    servidor = db.query(Servidor).filter(Servidor.matricula == duvida.id_servidor).first()
    if not servidor:
        raise HTTPException(status_code=400, detail="Servidor não encontrado")
    
    new_duvida = Duvida(**duvida.dict())
    db.add(new_duvida)
    db.commit()
    db.refresh(new_duvida)
    return new_duvida

@router.get("/", response_model=list[DuvidaOut])
def list_duvidas(db: Session = Depends(get_db)):
    return db.query(Duvida).all()


@router.post("/import", status_code=201)
def import_duvidas(file: UploadFile = File(...), db: Session = Depends(get_db)):
    try:
        df = pd.read_excel(file.file)
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Arquivo inválido: {e}")
    
    registros = []
    for _, row in df.iterrows():
        servidor = db.query(Servidor).filter(Servidor.matricula == row["id_servidor"]).first()
        if not servidor:
            continue  
    
        duvida_data = Duvida(id_servidor=row["id_servidor"])
        db.add(duvida_data)
        registros.append(duvida_data)
    db.commit()
    return {"importados": len(registros)}