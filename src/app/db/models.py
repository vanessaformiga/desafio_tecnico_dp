from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, Boolean, DECIMAL, Date, Text, Numeric
from sqlalchemy.sql import func
from db.database import Base

class Orgao(Base):
    __tablename__ = "orgao"
    id_orgao = Column(Integer, primary_key=True, index=True)
    nome = Column(String(255), nullable=False)
    tipo_orgao = Column(String(50))

class Departamento(Base):
    __tablename__ = "departamento"
    id_departamento = Column(Integer, primary_key=True, index=True)
    nome = Column(String(255), nullable=False)
    id_orgao = Column(Integer, ForeignKey("orgao.id_orgao"), nullable=False)

class Servidor(Base):
    __tablename__ = "servidor"
    matricula = Column(Integer, primary_key=True, index=True)
    nome = Column(String(255), nullable=False)
    id_orgao = Column(Integer, ForeignKey("orgao.id_orgao"), nullable=False)
    id_departamento = Column(Integer, ForeignKey("departamento.id_departamento"), nullable=False)
    cargo = Column(String(100))
    data_admissao = Column(Date)
    tipo_servidor = Column(String(50))

class DepartamentoPessoal(Base):
    __tablename__ = "departamento_pessoal"
    id_dp = Column(Integer, primary_key=True, index=True)
    nome = Column(String(255), nullable=False)
    responsavel = Column(String(255))
    contato = Column(String(100))
    observacao = Column(Text)


class User(Base):
    __tablename__ = "usuario"
    id_usuario = Column(Integer, primary_key=True, index=True)
    id_servidor = Column(Integer, ForeignKey("servidor.matricula"), unique=True, nullable=True)
    id_dp = Column(Integer, ForeignKey("departamento_pessoal.id_dp"), nullable=True)
    nome = Column(String(255), nullable=False)
    email = Column(String(255), unique=True, nullable=False, index=True)
    senha = Column(String(255), nullable=False)
    tipo_usuario = Column(String(50), nullable=True)
    data_criacao = Column(DateTime, server_default=func.now())
    ultimo_login = Column(DateTime, nullable=True)


class Assiduidade(Base):
    __tablename__ = "assiduidade"

    id_assiduidade = Column(Integer, primary_key=True, index=True)
    id_servidor = Column(Integer, ForeignKey("servidor.matricula"), nullable=False)
    data = Column(Date, nullable=False)
    tipo_atividade = Column(String(100))
    status_presenca = Column(String(50))
    observacao = Column(Text)


class Duvida(Base):
    __tablename__ = "duvida"

    id_duvida = Column(Integer, primary_key=True, index=True)
    id_servidor = Column(Integer, ForeignKey("servidor.matricula"), nullable=False)
    data_hora = Column(DateTime, server_default=func.now())


class Treinamento(Base):
    __tablename__ = "treinamento"

    id_treinamento = Column(Integer, primary_key=True, index=True)
    nome = Column(String(255), nullable=False)
    descricao = Column(Text)
    data_inicio = Column(Date)
    data_fim = Column(Date)
    observacao = Column(Text)
    id_servidor = Column(Integer, ForeignKey("servidor.matricula"), nullable=True)
    id_departamento = Column(Integer, ForeignKey("departamento.id_departamento"), nullable=True)



class Certificacao(Base):
    __tablename__ = "certificacao"

    id_certificacao = Column(Integer, primary_key=True, index=True)
    nome = Column(String(255), nullable=False)
    descricao = Column(Text)
    data_aplicacao = Column(Date)
    nota_obtida = Column(Numeric(5, 2))
    gera_certificado = Column(Boolean, default=False)
    id_servidor = Column(Integer, ForeignKey("servidor.matricula"), nullable=True)
    id_departamento = Column(Integer, ForeignKey("departamento.id_departamento"), nullable=True)


class ClimaOrganizacional(Base):
    __tablename__ = "clima_organizacional"

    id_clima = Column(Integer, primary_key=True, index=True)
    id_departamento = Column(Integer, ForeignKey("departamento.id_departamento"), nullable=False)
    id_servidor = Column(Integer, ForeignKey("servidor.matricula"), nullable=True)
    periodo = Column(String(50))
    data_da_realizacao = Column(Date)
    indice_obtido = Column(Numeric(5, 2))
    comentarios = Column(Text)