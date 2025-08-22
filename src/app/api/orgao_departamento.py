from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from db.database import SessionLocal
from db.models import Orgao, Departamento
from api.schemas import OrgaoCreate, OrgaoOut, DepartamentoCreate, DepartamentoOut

router = APIRouter(
    prefix="/cadastros",
    tags=["Cadastros - Órgão e Departamento"]
)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.post("/orgaos", response_model=OrgaoOut, status_code=201)
def create_orgao(orgao: OrgaoCreate, db: Session = Depends(get_db)):
    existing = db.query(Orgao).filter(Orgao.nome == orgao.nome).first()
    if existing:
        raise HTTPException(status_code=400, detail="Órgão já cadastrado")
    
    new_orgao = Orgao(**orgao.dict())
    db.add(new_orgao)
    db.commit()
    db.refresh(new_orgao)
    return new_orgao

@router.get("/orgaos", response_model=list[OrgaoOut])
def list_orgaos(db: Session = Depends(get_db)):
    return db.query(Orgao).all()


@router.post("/departamentos", response_model=DepartamentoOut, status_code=201)
def create_departamento(departamento: DepartamentoCreate, db: Session = Depends(get_db)):
    # Verifica se o órgão existe
    orgao = db.query(Orgao).filter(Orgao.id_orgao == departamento.id_orgao).first()
    if not orgao:
        raise HTTPException(status_code=400, detail="Órgão não encontrado")
    
    existing = db.query(Departamento).filter(
        Departamento.nome == departamento.nome,
        Departamento.id_orgao == departamento.id_orgao
    ).first()
    if existing:
        raise HTTPException(status_code=400, detail="Departamento já cadastrado neste órgão")
    
    new_departamento = Departamento(**departamento.dict())
    db.add(new_departamento)
    db.commit()
    db.refresh(new_departamento)
    return new_departamento

@router.get("/departamentos", response_model=list[DepartamentoOut])
def list_departamentos(db: Session = Depends(get_db)):
    return db.query(Departamento).all()