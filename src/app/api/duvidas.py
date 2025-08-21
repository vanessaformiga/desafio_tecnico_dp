from fastapi import APIRouter, Depends, UploadFile, File, HTTPException, Request
from fastapi.security import OAuth2PasswordBearer
from sqlalchemy.orm import Session
from deep_translator import GoogleTranslator
from db.models import User
from db.database import SessionLocal
from api.core.jwt import verify_access_token
from api.core.securete import hash_password
from api.carregar_faq import processar_arquivo_para_chroma
from api.rag import criar_pipeline_rag
from fastapi.templating import Jinja2Templates
import os
import shutil
from pydantic import BaseModel

router = APIRouter(
    prefix="/rag",
    tags=["Chat Sobre Afastamentos e Licenças"]
)

templates = Jinja2Templates(directory="templates")
qa_chain = None  # Pipeline RAG global

# ----------------------
# Dependências
# ----------------------
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Instância real de OAuth2PasswordBearer
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/users/login")

def get_current_user(token: str = Depends(oauth2_scheme), db: Session = Depends(get_db)):
    user_id = verify_access_token(token)
    if user_id is None:
        raise HTTPException(status_code=401, detail="Token inválido ou expirado")
    user = db.query(User).filter(User.id_usuario == user_id).first()
    if not user:
        raise HTTPException(status_code=401, detail="Usuário não encontrado")
    return user

# ----------------------
# Schemas Pydantic
# ----------------------
class PerguntaInput(BaseModel):
    pergunta: str

# ----------------------
# Endpoints de RAG
# ----------------------
@router.post("/upload-faq")
async def upload_faq(
    file: UploadFile = File(...), 
    tipo: str = "pdf", 
    current_user: User = Depends(get_current_user)
):
    os.makedirs("uploads", exist_ok=True)
    file_path = os.path.join("uploads", file.filename)
    with open(file_path, "wb") as f:
        shutil.copyfileobj(file.file, f)

    try:
        global qa_chain
        # Processa o arquivo e cria/atualiza a base vetorial
        vectordb = processar_arquivo_para_chroma(file_path, tipo)
        # Cria a pipeline RAG com o Chroma
        qa_chain = criar_pipeline_rag(vectordb)

        if qa_chain is None:
            raise HTTPException(status_code=500, detail="Erro ao criar a pipeline RAG")
        
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Erro ao processar arquivo: {str(e)}")

    return {"mensagem": f"Base vetorial criada com sucesso a partir do {tipo.upper()}."}


@router.post("/pergunta")
def responder_pergunta(
    input: PerguntaInput, 
    current_user: User = Depends(get_current_user)
):
    if not qa_chain:
        raise HTTPException(status_code=500, detail="Base vetorial não carregada...")
    try:
        # Executa a RAG para obter resposta
        resposta = qa_chain.run(input.pergunta)
        # Traduz a resposta para português
        resposta_traduzida = GoogleTranslator(source='auto', target='pt').translate(resposta)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Erro ao processar pergunta: {str(e)}")
    return {"resposta": resposta_traduzida}


@router.get("/resposta")
def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})