from pydantic import BaseModel

# --- FAQ ---

class FaqCreate(BaseModel):
    """
    Modelo para criação de um FAQ.
    """
    pergunta: str
    resposta: str

class FaqUpdate(BaseModel):
    """
    Modelo para atualizar um FAQ.
    """
    pergunta: str | None = None
    resposta: str | None = None

class FaqOut(BaseModel):
    """
    Modelo para retornar um FAQ com ID.
    """
    id: int
    pergunta: str
    resposta: str

    class Config:
        orm_mode = True