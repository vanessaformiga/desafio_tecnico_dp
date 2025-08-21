from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter()

class AgentInfo(BaseModel):
    nome: str
    versao: str
    descricao: str
    funcionalidades: list[str]
    autor: str

@router.get("/about", response_model=AgentInfo, tags=["Assistente de IA"])
async def get_agent_info():
    """
    Retorna informações sobre o Assistente de IA ServIA - 
    """
    return AgentInfo(
        nome="ServIA - Assistente para Departamento Pessoal",
        versao="1.0",
        descricao="ServIA é um assistente inteligente para o Departamento Pessoal.",
        funcionalidades=[
            " - Consultar e dúvidas sobre afastamentos e licenças.;",
            " - Gerar relatórios de Assiduidade;  "
            " - Gerar análises preditivas sobre participação de servidores em treinamentos e certificações e engajamento em pesquisa de clima organizacional; "
            " - Obter relatórios e gráficos para tomada de decisão.; "


        ],
        autor="Vanessa Formiga"
    )