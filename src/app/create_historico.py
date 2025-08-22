from db.database import engine, Base
from db.models import HistoricoUsuario, HistoricoPergunta

# Cria somente as tabelas de histórico
Base.metadata.create_all(bind=engine, tables=[HistoricoUsuario.__table__, HistoricoPergunta.__table__])

print("Tabelas historico_usuario e historico_pergunta criadas com sucesso!")