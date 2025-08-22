from fastapi import APIRouter, Depends, UploadFile, File, HTTPException
from fastapi.security import OAuth2PasswordBearer
from sqlalchemy.orm import Session
from db.models import Certificacao, Servidor, Departamento, User
from db.database import SessionLocal
from api.schemas import CertificacaoCreate, CertificacaoOut
from api.core.jwt import verify_access_token
import pandas as pd

router = APIRouter(
    prefix="/certificacoes",
    tags=["Certificações"]
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


@router.post("/", response_model=CertificacaoOut)
def create_certificacao(
    certificacao: CertificacaoCreate,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    if certificacao.id_servidor:
        servidor = db.query(Servidor).filter(Servidor.matricula == certificacao.id_servidor).first()
        if not servidor:
            raise HTTPException(status_code=400, detail="Servidor não encontrado")
    if certificacao.id_departamento:
        departamento = db.query(Departamento).filter(Departamento.id_departamento == certificacao.id_departamento).first()
        if not departamento:
            raise HTTPException(status_code=400, detail="Departamento não encontrado")
    new_certificacao = Certificacao(**certificacao.dict())
    db.add(new_certificacao)
    db.commit()
    db.refresh(new_certificacao)
    return new_certificacao

@router.post("/upload-excel", response_model=list[CertificacaoOut])
async def upload_certificacoes_excel(
    file: UploadFile = File(...),
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    try:
        df = pd.read_excel(file.file)
    except Exception:
        raise HTTPException(status_code=400, detail="Arquivo inválido")

    certificacoes = []
    for _, row in df.iterrows():
        data = row.to_dict()
        if data.get("id_servidor") and not db.query(Servidor).filter(Servidor.matricula == data["id_servidor"]).first():
            continue
        if data.get("id_departamento") and not db.query(Departamento).filter(Departamento.id_departamento == data["id_departamento"]).first():
            continue
        certificacao = Certificacao(**data)
        db.add(certificacao)
        certificacoes.append(certificacao)

    db.commit()
    for c in certificacoes:
        db.refresh(c)

    return certificacoes


@router.get("/", response_model=list[CertificacaoOut])
def list_certificacoes(
    id_servidor: int | None = None,
    id_departamento: int | None = None,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    query = db.query(Certificacao)
    
    if id_servidor:
        query = query.filter(Certificacao.id_servidor == id_servidor)
    if id_departamento:
        query = query.filter(Certificacao.id_departamento == id_departamento)
    
    certificacoes = query.all()
    
    return certificacoes

@router.get("/{certificacao_id}", response_model=CertificacaoOut)
def get_certificacao(
    certificacao_id: int,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    certificacao = db.query(Certificacao).filter(Certificacao.id_certificacao == certificacao_id).first()
    if not certificacao:
        raise HTTPException(status_code=404, detail="Certificação não encontrada")
    return certificacao