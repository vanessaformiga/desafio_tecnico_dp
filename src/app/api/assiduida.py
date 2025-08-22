from fastapi import APIRouter, Depends, HTTPException, Query
from fastapi.responses import StreamingResponse
from sqlalchemy.orm import Session
from db.database import SessionLocal
from db.models import Assiduidade, User
from api.users import get_current_user
from datetime import date
from typing import Optional
from io import BytesIO
import pandas as pd
from api.schemas import AssiduidadeCreate, AssiduidadeOut

router = APIRouter(
    prefix="/assiduidade",
    tags=["Assiduidade"]
)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.post("/", response_model=AssiduidadeOut, status_code=201)
def create_assiduidade(
    assiduidade: AssiduidadeCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    new_registro = Assiduidade(**assiduidade.dict())
    db.add(new_registro)
    db.commit()
    db.refresh(new_registro)
    return new_registro


@router.get("/", response_model=list[AssiduidadeOut])
def list_assiduidade(
    servidor_id: Optional[int] = Query(None),
    data_inicio: Optional[date] = Query(None),
    data_fim: Optional[date] = Query(None),
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    query = db.query(Assiduidade)
    if servidor_id:
        query = query.filter(Assiduidade.id_servidor == servidor_id)
    if data_inicio:
        query = query.filter(Assiduidade.data >= data_inicio)
    if data_fim:
        query = query.filter(Assiduidade.data <= data_fim)
    registros = query.all()
    return registros


@router.get("/relatorio")
def relatorio_assiduidade(
    servidor_id: Optional[int] = Query(None),
    data_inicio: Optional[date] = Query(None),
    data_fim: Optional[date] = Query(None),
    export_excel: Optional[bool] = Query(False),
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    query = db.query(Assiduidade)
    
    if servidor_id:
        query = query.filter(Assiduidade.id_servidor == servidor_id)
    if data_inicio:
        query = query.filter(Assiduidade.data >= data_inicio)
    if data_fim:
        query = query.filter(Assiduidade.data <= data_fim)
    
    registros = query.all()
    
    if not registros:
        raise HTTPException(status_code=404, detail="Nenhum registro encontrado para os filtros aplicados.")


    dados = [
        {
            "ID Assiduidade": r.id_assiduidade,
            "ID Servidor": r.id_servidor,
            "Data": r.data,
            "Tipo Atividade": r.tipo_atividade,
            "Status Presença": r.status_presenca,
            "Observação": r.observacao
        } for r in registros
    ]
    
    if export_excel:
        df = pd.DataFrame(dados)
        output = BytesIO()
        with pd.ExcelWriter(output, engine="xlsxwriter") as writer:
            df.to_excel(writer, index=False, sheet_name="Assiduidade")
        output.seek(0)
        return StreamingResponse(
            output,
            media_type="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
            headers={"Content-Disposition": "attachment; filename=relatorio_assiduidade.xlsx"}
        )

    total_registros = len(registros)
    presencas = sum(1 for r in registros if r.status_presenca and r.status_presenca.lower() == "presente")
    faltas = sum(1 for r in registros if r.status_presenca and r.status_presenca.lower() == "ausente")

    return {
        "total_registros": total_registros,
        "total_presencas": presencas,
        "total_faltas": faltas,
        "percentual_presenca": round((presencas / total_registros) * 100, 2),
        "percentual_faltas": round((faltas / total_registros) * 100, 2),
        "detalhes": dados
    }