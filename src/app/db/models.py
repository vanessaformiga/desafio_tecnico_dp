from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, Boolean, DECIMAL, Date, Text
from sqlalchemy.sql import func
from app.db.database import Base

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