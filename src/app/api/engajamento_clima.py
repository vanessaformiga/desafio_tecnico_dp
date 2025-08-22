from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from sklearn.linear_model import LogisticRegression
import numpy as np
from api.obter_treinamentos import obter_dados_clima
from db.database import SessionLocal
import matplotlib.pyplot as plt
from io import BytesIO
import base64
from fastapi.responses import HTMLResponse

router = APIRouter(
    prefix="/Analise Preditiva",
    tags=["Engajamento em Pesquisa de Clima Organizacional"]
)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

def gerar_grafico_base64(*, departamentos, valores, titulo):
    fig, ax = plt.subplots(figsize=(10,5))
    ax.bar(departamentos, valores, color='skyblue')
    ax.set_xlabel("Departamento")
    ax.set_ylabel("Participação Alta")
    ax.set_title(titulo)

    buf = BytesIO()
    plt.savefig(buf, format="png")
    buf.seek(0)
    plt.close(fig)
    return base64.b64encode(buf.getvalue()).decode("utf-8")

@router.get("/analise-clima-departamento", response_class=HTMLResponse)
def analise_clima_html(db: Session = Depends(get_db)):
    df = obter_dados_clima(db)
    
    # Checar se há registros suficientes
    if df.empty or len(df) < 2:
        df['probabilidade_participacao'] = 0.5
        df['predicao'] = 'Indefinido'
    else:
        X = df[['pesquisas_participadas','engajamento']]
        y = np.random.randint(0, 2, len(df))  # alvo fictício

        # Garantir que haja pelo menos duas classes
        if len(np.unique(y)) < 2:
            y[0] = 1 - y[0]

        model = LogisticRegression()
        model.fit(X, y)

        df['probabilidade_participacao'] = model.predict_proba(X)[:,1]
        df['predicao'] = np.where(df['probabilidade_participacao'] > 0.5, 'Alta', 'Baixa')

    resumo_departamento = df.groupby('departamento').agg(
        servidores_total=('servidor_id','count'),
        media_probabilidade_participacao=('probabilidade_participacao','mean'),
        alta_participacao=('predicao', lambda x: (x=='Alta').sum())
    ).reset_index()

    # Gerar gráfico
    grafico_base64 = gerar_grafico_base64(
        departamentos=resumo_departamento['departamento'].tolist(),
        valores=resumo_departamento['alta_participacao'].tolist(),
        titulo="Alta Participação por Departamento"
    )

    # Retornar HTML
    html = f"""
    <html>
        <head><title>Clima Organizacional</title></head>
        <body>
            <h1>Clima Organizacional por Departamento</h1>
            <img src="data:image/png;base64,{grafico_base64}" alt="Gráfico de Participação"/>
            <h2>Resumo dos Departamentos</h2>
            <table border="1" style="border-collapse: collapse; padding: 5px;">
                <tr>
                    <th>Departamento</th>
                    <th>Total de Servidores</th>
                    <th>Média de Probabilidade</th>
                    <th>Alta Participação</th>
                </tr>
    """
    for _, row in resumo_departamento.iterrows():
        html += f"""
                <tr>
                    <td>{row['departamento']}</td>
                    <td>{row['servidores_total']}</td>
                    <td>{row['media_probabilidade_participacao']:.2f}</td>
                    <td>{row['alta_participacao']}</td>
                </tr>
        """
    html += """
            </table>
        </body>
    </html>
    """

    return HTMLResponse(content=html)