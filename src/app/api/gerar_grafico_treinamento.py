from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from sklearn.linear_model import LogisticRegression
import numpy as np
import base64
import matplotlib.pyplot as plt
from io import BytesIO
import pandas as pd
from db.database import get_db

# Import correto da função
from api.obter_treinamentos import obter_dados_treinamentos

router = APIRouter()

def gerar_grafico_base64(departamentos, valores, titulo):
    fig, ax = plt.subplots(figsize=(10,5))
    ax.bar(departamentos, valores, color='skyblue')
    ax.set_xlabel("Departamento")
    ax.set_ylabel("Valor")
    ax.set_title(titulo)
    ax.set_ylim(0,1)

    buf = BytesIO()
    plt.savefig(buf, format="png")
    buf.seek(0)
    plt.close(fig)
    grafico_base64 = base64.b64encode(buf.getvalue()).decode("utf-8")
    return grafico_base64

@router.get("/analise-treinamentos-grafico-json")
def analise_treinamentos_grafico_json(db: Session = Depends(get_db)):
    # Obter dados do banco
    df = obter_dados_treinamentos(db)
    
    # Predição fictícia
    X = df[['treinamentos_concluidos','certificacoes_concluidas','nota_certificacao']]
    y = np.random.randint(0,2,len(df))  # alvo fictício
    model = LogisticRegression()
    model.fit(X, y)
    df['probabilidade_sucesso'] = model.predict_proba(X)[:,1]
    df['predicao'] = np.where(df['probabilidade_sucesso']>0.5,'Alto','Baixo')
    
    # Agregação por departamento
    resumo_dep = df.groupby('departamento').agg(
        servidores_total=('servidor_id','count'),
        media_probabilidade_sucesso=('probabilidade_sucesso','mean'),
        alto_sucesso=('predicao', lambda x: (x=='Alto').sum())
    ).reset_index()
    
    # Gerar gráfico em base64
    grafico_base64 = gerar_grafico_base64(
        departamentos=resumo_dep['departamento'].tolist(),
        valores=resumo_dep['media_probabilidade_sucesso'].tolist(),
        titulo="Probabilidade média de sucesso em treinamentos por departamento"
    )
    
    return {
        "resumo_servidores": df.to_dict(orient='records'),
        "resumo_departamentos": resumo_dep.to_dict(orient='records'),
        "grafico_base64": grafico_base64
    }