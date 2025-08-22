from fastapi import FastAPI
from api import faq, about, users, duvidas

# Imports para criar tabelas
from db.database import Base, engine
from db import models  # importa todos os modelos

# Cria as tabelas no banco
Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="ServIA - Assistente de DP",
    description="API com Funcionalidades para o DP",
    version="1.0.0"
)

# Routers
app.include_router(about.router)
app.include_router(faq.router)
app.include_router(users.router)
app.include_router(duvidas.router)

# Root
@app.get("/", tags=["Root"])
def read_root():
    return {"Mensagem": "Bem-vindo ao ServIA"}