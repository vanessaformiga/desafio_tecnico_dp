from fastapi import FastAPI
from api import faq, about, users, duvidas, assiduida, orgao_departamento, servidor, duvida, departamento_pessoal, treinamento, certificacao, clima_organizacional

from db.database import Base, engine
from db import models 


Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="ServIA - Assistente de DP",
    description="API com Funcionalidades para o DP",
    version="1.0.0"
)


app.include_router(about.router)
app.include_router(faq.router)
app.include_router(users.router)
app.include_router(duvidas.router)
app.include_router(assiduida.router)
app.include_router(orgao_departamento.router)
app.include_router(servidor.router)
app.include_router(duvida.router)
app.include_router(departamento_pessoal.router)
app.include_router(treinamento.router)
app.include_router(certificacao.router)
app.include_router(clima_organizacional.router)



@app.get("/", tags=["Root"])
def read_root():
    return {"Mensagem": "Bem-vindo ao ServIA"}