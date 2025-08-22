from fastapi import APIRouter, Depends, UploadFile, File, HTTPException
from fastapi.security import OAuth2PasswordBearer
from sqlalchemy.orm import Session
from db.models import ClimaOrganizacional, Servidor, Departamento, User
from db.database import SessionLocal
from api.schemas import ClimaOrganizacionalCreate, ClimaOrganizacionalOut
from api.core.jwt import verify_access_token
import pandas as pd

router = APIRouter(
    prefix="/clima-organizacional",
    tags=["Clima Organizacional"]
)

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/users/login")


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Dependência para pegar o usuário atual
def get_current_user(token: str = Depends(oauth2_scheme), db: Session = Depends(get_db)):
    user_id = verify_access_token(token)
    if user_id is None:
        raise HTTPException(status_code=401, detail="Token inválido ou expirado")
    user = db.query(User).filter(User.id_usuario == user_id).first()
    if not user:
        raise HTTPException(status_code=401, detail="Usuário não encontrado")
    return user


@router.post("/", response_model=ClimaOrganizacionalOut)
def create_clima(
    clima: ClimaOrganizacionalCreate,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    if clima.id_servidor:
        servidor = db.query(Servidor).filter(Servidor.matricula == clima.id_servidor).first()
        if not servidor:
            raise HTTPException(status_code=400, detail="Servidor não encontrado")
    if clima.id_departamento:
        departamento = db.query(Departamento).filter(Departamento.id_departamento == clima.id_departamento).first()
        if not departamento:
            raise HTTPException(status_code=400, detail="Departamento não encontrado")
    new_clima = ClimaOrganizacional(**clima.dict())
    db.add(new_clima)
    db.commit()
    db.refresh(new_clima)
    return new_clima


@router.post("/upload-excel", response_model=list[ClimaOrganizacionalOut])
async def upload_clima_excel(
    file: UploadFile = File(...),
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    try:
        df = pd.read_excel(file.file)
    except Exception:
        raise HTTPException(status_code=400, detail="Arquivo inválido")

    registros = []
    for _, row in df.iterrows():
        data = row.to_dict()
        if data.get("id_servidor") and not db.query(Servidor).filter(Servidor.matricula == data["id_servidor"]).first():
            continue
        if data.get("id_departamento") and not db.query(Departamento).filter(Departamento.id_departamento == data["id_departamento"]).first():
            continue
        clima = ClimaOrganizacional(**data)
        db.add(clima)
        registros.append(clima)

    db.commit()
    for r in registros:
        db.refresh(r)

    return registros


@router.get("/", response_model=list[ClimaOrganizacionalOut])
def list_clima(
    id_servidor: int | None = None,
    id_departamento: int | None = None,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    query = db.query(ClimaOrganizacional)
    
    if id_servidor:
        query = query.filter(ClimaOrganizacional.id_servidor == id_servidor)
    if id_departamento:
        query = query.filter(ClimaOrganizacional.id_departamento == id_departamento)
    
    registros = query.all()
    return registros


@router.get("/{clima_id}", response_model=ClimaOrganizacionalOut)
def get_clima(
    clima_id: int,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    clima = db.query(ClimaOrganizacional).filter(ClimaOrganizacional.id_clima == clima_id).first()
    if not clima:
        raise HTTPException(status_code=404, detail="Registro não encontrado")
    return clima