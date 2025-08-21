from fastapi import FastAPI
from api import faq
from api import about
# from api import faqs
# from api import users
# from app.agente import rag

app = FastAPI(
    title="ServIA - Assistente de DP",
    description="API com Funcionalidades para o DP",
    version="1.0.0"
)

# Routers
app.include_router(about.router, tags=["About - Sobre a aplicação"])
app.include_router(faq.router)  


# Root
@app.get("/", tags=["Root"])
def read_root():
    return {
        "Mensagem": "Bem-vindo ao ServIA"
    }