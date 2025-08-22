**Fluxograma da Solução**


``````
Início → Usuário acessa a aplicação
  ↓
Autenticação
  ├─ Se logado → Entrada do Usuário
  └─ Se não logado → Solicita Login/Cadastro → depois Entrada do Usuário
  ↓
Entrada do Usuário
  ├─ Pergunta textual → Verificação Tipo de Entrada → Módulo RAG ou FAQ
  │  ├─ RAG → Consulta banco/embeddings → Recupera trechos → Geração de Resposta (LLM) → Retorno ao Usuário → Salva histórico
  │  └─ FAQ → Consulta FAQ.txt ou DB → Retorno ao Usuário → Salva pergunta no txt
  └─ Upload de arquivo (PDF/CSV) → Processamento de Documento → Lê arquivo → Converte em texto → Indexa/Armazena no banco → Módulo RAG → Continuação como acima
  ↓
Gerar Relatório
  → Gera Excel com informações de assínuidade
↓
Envio de Informações
  → Permite cadastro individual ou em lote nos endpoints
Análise Preditiva
  → Exibe resultado
  → Gera gráficos sobre presença em treinamentos, certificações e engajamento em pesquisas de clima
  ↓
Fim

``````