from pydantic import BaseModel, EmailStr
from datetime import datetime

# User schemas
class UserCreate(BaseModel):
    id_servidor: int | None = None
    id_dp: int | None = None
    nome: str
    email: EmailStr
    senha: str
    tipo_usuario: str | None = None

class UserOut(BaseModel):
    id_usuario: int
    id_servidor: int | None
    id_dp: int | None
    nome: str
    email: EmailStr
    tipo_usuario: str | None
    data_criacao: datetime | None
    ultimo_login: datetime | None

# Login schema
class LoginData(BaseModel):
    email: str
    senha: str



class Token(BaseModel):
    access_token:str
    token_type:str

class LoginData(BaseModel):
    email:str
    password: str


class FaqCreate(BaseModel):
    
   
    pergunta: str
    resposta: str

class FaqUpdate(BaseModel):
   
    pergunta: str | None = None
    resposta: str | None = None

class FaqOut(BaseModel):
   
    id: int
    pergunta: str
    resposta: str

    class Config:
        orm_mode = True