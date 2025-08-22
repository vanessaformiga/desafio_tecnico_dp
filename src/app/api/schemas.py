from pydantic import BaseModel, EmailStr
from datetime import datetime, date
from typing import Optional

class OrgaoCreate(BaseModel):
    nome: str
    tipo_orgao: Optional[str] = None

class OrgaoOut(OrgaoCreate):
    id_orgao: int

class DepartamentoCreate(BaseModel):
    nome: str
    id_orgao: int

class DepartamentoOut(DepartamentoCreate):
    id_departamento: int

class AssiduidadeCreate(BaseModel):
    id_servidor: int
    data: date
    tipo_atividade: Optional[str] = None
    status_presenca: Optional[str] = None
    observacao: Optional[str] = None

class AssiduidadeOut(AssiduidadeCreate):
    id_assiduidade: int

class DuvidaCreate(BaseModel):
    id_servidor: int

class DuvidaOut(DuvidaCreate):
    id_duvida: int
    data_hora: datetime

class TreinamentoCreate(BaseModel):
    nome: str
    descricao: Optional[str] = None
    data_inicio: Optional[date] = None
    data_fim: Optional[date] = None
    observacao: Optional[str] = None
    id_servidor: Optional[int] = None
    id_departamento: Optional[int] = None

class TreinamentoOut(TreinamentoCreate):
    id_treinamento: int

class CertificacaoCreate(BaseModel):
    nome: str
    descricao: Optional[str] = None
    data_aplicacao: Optional[date] = None
    nota_obtida: Optional[float] = None
    gera_certificado: Optional[bool] = False
    id_servidor: Optional[int] = None
    id_departamento: Optional[int] = None

class CertificacaoOut(CertificacaoCreate):
    id_certificacao: int

class ClimaOrganizacionalCreate(BaseModel):
    id_departamento: int
    id_servidor: Optional[int] = None
    periodo: Optional[str] = None
    data_da_realizacao: Optional[date] = None
    indice_obtido: Optional[float] = None
    comentarios: Optional[str] = None

class ClimaOrganizacionalOut(ClimaOrganizacionalCreate):
    id_clima: int


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

class HistoricoUsuarioBase(BaseModel):
    acao: str
    detalhe: str | None = None

class HistoricoUsuarioCreate(HistoricoUsuarioBase):
    id_usuario: int

class HistoricoUsuarioOut(HistoricoUsuarioBase):
    id_historico: int
    data_hora: datetime

    class Config:
        orm_mode = True

class HistoricoPerguntaBase(BaseModel):
    pergunta: str
    resposta: str | None = None

class HistoricoPerguntaCreate(HistoricoPerguntaBase):
    id_usuario: int

class HistoricoPerguntaOut(HistoricoPerguntaBase):
    id_historico: int
    data_hora: datetime

    class Config:
        orm_mode = True