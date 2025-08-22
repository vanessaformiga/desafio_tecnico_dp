from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from db.database import SessionLocal
from db.models import Servidor, Orgao, Departamento
from api.schemas import UserOut
from pydantic import BaseModel
from datetime import date

router = APIRouter(
    prefix="/servidores",
    tags=["Servidor"]
)


class ServidorCreate(BaseModel):
    matricula: int
    nome: str
    id_orgao: int
    id_departamento: int
    cargo: str | None = None
    data_admissao: date | None = None
    tipo_servidor: str | None = None


class ServidorOut(ServidorCreate):
    pass
    # Pode adicionar orm_mode se quiser:
    # class Config:
    #     orm_mode = True


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/", response_model=ServidorOut, status_code=201)
def create_servidor(servidor: ServidorCreate, db: Session = Depends(get_db)):
    # Verifica se o órgão existe
    orgao = db.query(Orgao).filter(Orgao.id_orgao == servidor.id_orgao).first()
    if not orgao:
        raise HTTPException(status_code=400, detail="Órgão não encontrado")
    
  
    departamento = db.query(Departamento).filter(Departamento.id_departamento == servidor.id_departamento).first()
    if not departamento:
        raise HTTPException(status_code=400, detail="Departamento não encontrado")
    
    
    existing = db.query(Servidor).filter(Servidor.matricula == servidor.matricula).first()
    if existing:
        raise HTTPException(status_code=400, detail="Servidor com essa matrícula já existe")
  
    new_servidor = Servidor(**servidor.dict())
    db.add(new_servidor)
    db.commit()
    db.refresh(new_servidor)
    return new_servidor


@router.get("/", response_model=list[ServidorOut])
def list_servidores(db: Session = Depends(get_db)):
    return db.query(Servidor).all()