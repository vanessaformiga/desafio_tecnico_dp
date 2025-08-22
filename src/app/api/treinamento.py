from fastapi import APIRouter, Depends, UploadFile, File, HTTPException
from fastapi.security import OAuth2PasswordBearer
from sqlalchemy.orm import Session
from db.models import Treinamento, Servidor, Departamento, User
from db.database import SessionLocal
from api.schemas import TreinamentoCreate, TreinamentoOut
from api.core.jwt import verify_access_token
import pandas as pd

router = APIRouter(
    prefix="/treinamentos",
    tags=["Treinamentos"]
)

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/users/login")


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

def get_current_user(token: str = Depends(oauth2_scheme), db: Session = Depends(get_db)):
    user_id = verify_access_token(token)
    if user_id is None:
        raise HTTPException(status_code=401, detail="Token inválido ou expirado")
    user = db.query(User).filter(User.id_usuario == user_id).first()
    if not user:
        raise HTTPException(status_code=401, detail="Usuário não encontrado")
    return user

@router.post("/", response_model=TreinamentoOut)
def create_treinamento(
    treinamento: TreinamentoCreate,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    if treinamento.id_servidor:
        servidor = db.query(Servidor).filter(Servidor.matricula == treinamento.id_servidor).first()
        if not servidor:
            raise HTTPException(status_code=400, detail="Servidor não encontrado")
    if treinamento.id_departamento:
        departamento = db.query(Departamento).filter(Departamento.id_departamento == treinamento.id_departamento).first()
        if not departamento:
            raise HTTPException(status_code=400, detail="Departamento não encontrado")
    new_treinamento = Treinamento(**treinamento.dict())
    db.add(new_treinamento)
    db.commit()
    db.refresh(new_treinamento)
    return new_treinamento


@router.post("/upload-excel", response_model=list[TreinamentoOut])
async def upload_treinamentos_excel(
    file: UploadFile = File(...),
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    try:
        df = pd.read_excel(file.file)
    except Exception:
        raise HTTPException(status_code=400, detail="Arquivo inválido")

    treinamentos = []
    for _, row in df.iterrows():
        data = row.to_dict()
        if data.get("id_servidor") and not db.query(Servidor).filter(Servidor.matricula == data["id_servidor"]).first():
            continue
        if data.get("id_departamento") and not db.query(Departamento).filter(Departamento.id_departamento == data["id_departamento"]).first():
            continue
        treinamento = Treinamento(**data)
        db.add(treinamento)
        treinamentos.append(treinamento)

    db.commit()
    for t in treinamentos:
        db.refresh(t)

    return treinamentos


@router.get("/", response_model=list[TreinamentoOut])
def list_treinamentos(
    id_servidor: int | None = None,
    id_departamento: int | None = None,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    query = db.query(Treinamento)
    
    if id_servidor:
        query = query.filter(Treinamento.id_servidor == id_servidor)
    if id_departamento:
        query = query.filter(Treinamento.id_departamento == id_departamento)
    
    treinamentos = query.all()
    
    return treinamentos

@router.get("/{treinamento_id}", response_model=TreinamentoOut)
def get_treinamento(
    treinamento_id: int,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    treinamento = db.query(Treinamento).filter(Treinamento.id_treinamento == treinamento_id).first()
    if not treinamento:
        raise HTTPException(status_code=404, detail="Treinamento não encontrado")
    return treinamento