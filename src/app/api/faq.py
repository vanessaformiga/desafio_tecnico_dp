from fastapi import APIRouter
from pathlib import Path
from typing import List
from api.schemas import FaqOut, FaqCreate

router = APIRouter(prefix="/faq", tags=["FAQ"])

FAQ_FILE = Path(__file__).parent / "data/faq.txt"

# Função para carregar FAQs do arquivo TXT
def carregar_faq() -> List[FaqOut]:
    faq_list = []
    if FAQ_FILE.exists():
        with FAQ_FILE.open("r", encoding="utf-8") as f:
            current_question = None
            current_answer = None
            idx = 1
            for line in f:
                line = line.strip()
                if not line:
                    continue  # ignora linhas em branco
                # detecta prefixos P. / P: / R. / R:
                if line.lower().startswith("p.") or line.lower().startswith("p:"):
                    current_question = line[3:].strip()  # remove P. ou P: + espaço
                elif line.lower().startswith("r.") or line.lower().startswith("r:"):
                    current_answer = line[3:].strip()  # remove R. ou R: + espaço
                    if current_question and current_answer:
                        faq_list.append(FaqOut(id=idx, pergunta=current_question, resposta=current_answer))
                        idx += 1
                        current_question = None
                        current_answer = None
    return faq_list

def adicionar_faq(faq: FaqCreate) -> FaqOut:
    with FAQ_FILE.open("a", encoding="utf-8") as f:
        f.write(f"P. {faq.pergunta}\nR. {faq.resposta}\n\n")  # mantém formato P./R.
    faq_list = carregar_faq()
    return faq_list[-1]  # retorna o último FAQ adicionado



@router.get("/", response_model=List[FaqOut])
async def get_faq():
    return carregar_faq()

@router.post("/", response_model=FaqOut)
async def post_faq(faq: FaqCreate):
    return adicionar_faq(faq)