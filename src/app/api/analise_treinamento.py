from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from sklearn.linear_model import LogisticRegression
import numpy as np
from api.obter_treinamentos import obter_dados_treinamentos
from api.gerar_grafico import gerar_grafico_base64

from db.database import SessionLocal
router = APIRouter()

router = APIRouter(
    prefix="/Analise Preditiva",
    tags=["Análise Preditiva em Treinamentos e Certificações"]
)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/analise-treinamentos-departamento")
def analise_treinamentos(db: Session = Depends(get_db)):
    df = obter_dados_treinamentos(db)

    X = df[['treinamentos_concluidos','certificacoes_concluidas','nota_certificacao']]
    y = np.random.choice([0,1], size=len(df))  # garante pelo menos duas classes

    # Verifica se há pelo menos duas classes
    if len(np.unique(y)) < 2:
        df['probabilidade_sucesso'] = 0.5
        df['predicao'] = 'Indefinido'
    else:
        model = LogisticRegression()
        model.fit(X, y)
        df['probabilidade_sucesso'] = model.predict_proba(X)[:,1]
        df['predicao'] = np.where(df['probabilidade_sucesso']>0.5,'Alto','Baixo')

    resumo_departamento = df.groupby('departamento').agg(
        servidores_total=('servidor_id','count'),
        media_probabilidade_sucesso=('probabilidade_sucesso','mean'),
        alto_sucesso=('predicao', lambda x: (x=='Alto').sum())
    ).reset_index()

    return {
        "resumo_servidores": df.to_dict(orient='records'),
        "resumo_departamentos": resumo_departamento.to_dict(orient='records')
    }

@router.get("/analise-treinamentos-departamento-grafico")
def analise_treinamentos_grafico(db: Session = Depends(get_db)):
    df = obter_dados_treinamentos(db)
    
    # Certifica-se de que existem pelo menos 2 classes
    if len(df) < 2:
        return {"erro": "Não há dados suficientes para análise."}
    
    X = df[['treinamentos_concluidos','certificacoes_concluidas','nota_certificacao']]
    y = np.random.randint(0, 2, len(df))  # alvo fictício
    
    # Evita erro de apenas 1 classe
    if len(np.unique(y)) < 2:
        y[0] = 1  # garante pelo menos duas classes
    
    model = LogisticRegression()
    model.fit(X, y)
    
    df['probabilidade_sucesso'] = model.predict_proba(X)[:,1]
    df['predicao'] = np.where(df['probabilidade_sucesso'] > 0.5, 'Alto', 'Baixo')
    
    resumo_departamento = df.groupby('departamento').agg(
        servidores_total=('servidor_id','count'),
        media_probabilidade_sucesso=('probabilidade_sucesso','mean'),
        alto_sucesso=('predicao', lambda x: (x=='Alto').sum())
    ).reset_index()
    
    # Converte colunas do DataFrame para listas antes de passar para a função
    grafico_base64 = gerar_grafico_base64(
        departamentos=resumo_departamento['departamento'].tolist(),
        valores=resumo_departamento['media_probabilidade_sucesso'].tolist(),
        titulo="Probabilidade média de sucesso em treinamentos por departamento"
    )
    
    return {
        "resumo_servidores": df.to_dict(orient='records'),
        "resumo_departamentos": resumo_departamento.to_dict(orient='records'),
        "grafico_base64": grafico_base64
    }