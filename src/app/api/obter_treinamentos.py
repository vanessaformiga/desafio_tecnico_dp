from sqlalchemy.orm import Session
from db.models import Servidor, Treinamento, Certificacao, ClimaOrganizacional, Departamento
import pandas as pd

def obter_dados_treinamentos(db: Session):
    #
    query = (
        db.query(
            Servidor.matricula.label("servidor_id"),
            Departamento.nome.label("departamento"),
            Treinamento.id_treinamento,
            Certificacao.id_certificacao,
            Certificacao.nota_obtida
        )
        .join(Departamento, Servidor.id_departamento == Departamento.id_departamento)
        .outerjoin(Treinamento, Treinamento.id_servidor == Servidor.matricula)
        .outerjoin(Certificacao, Certificacao.id_servidor == Servidor.matricula)
    )
    df = pd.read_sql(query.statement, db.bind)
    
   
    df_agg = df.groupby(['servidor_id', 'departamento']).agg(
        treinamentos_concluidos=('id_treinamento', 'count'),
        certificacoes_concluidas=('id_certificacao', 'count'),
        nota_certificacao=('nota_obtida', 'mean')
    ).reset_index()
    
    
    df_agg['treinamentos_totais'] = 5  # exemplo
    df_agg['certificacoes_totais'] = 3  # exemplo
    df_agg['nota_certificacao'] = df_agg['nota_certificacao'].fillna(0)
    
    return df_agg

def obter_dados_clima(db: Session):
    query = (
        db.query(
            Servidor.matricula.label("servidor_id"),
            Departamento.nome.label("departamento"),
            ClimaOrganizacional.id_clima,
            ClimaOrganizacional.indice_obtido
        )
        .join(Departamento, Servidor.id_departamento == Departamento.id_departamento)
        .outerjoin(ClimaOrganizacional, ClimaOrganizacional.id_servidor == Servidor.matricula)
    )
    df = pd.read_sql(query.statement, db.bind)
    
    # Calcular métricas
    df_agg = df.groupby(['servidor_id', 'departamento']).agg(
        pesquisas_participadas=('id_clima', 'count'),
        engajamento=('indice_obtido', 'mean')
    ).reset_index()
    
    df_agg['pesquisas_totais'] = 4  # exemplo
    df_agg['engajamento'] = df_agg['engajamento'].fillna(0)
    
    return df_agg