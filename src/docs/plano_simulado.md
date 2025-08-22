# 1. Plano de Funcionamento Inicial (MVP)

Objetivo: permitir interação do usuário com a aplicação, incluindo perguntas textuais, upload de documentos e consulta a FAQ, com resposta via LLM.

**Fluxo Operacional:**

**Etapa	**Descrição**

- Início	Usuário acessa a aplicação via API ou interface web (Streamlit/Gradio).
- Autenticação (opcional)	Sistema verifica se usuário está logado. Se não, solicita login ou cadastro.
- Entrada do Usuário	Usuário envia: pergunta textual, upload de arquivo PDF, ou solicita FAQ.
- Verificação do Tipo de Entrada	Pergunta → RAG/FAQ
- Arquivo → Processamento de Documento
- Processamento de Documento	PDF é lido, convertido em texto e indexado para RAG (armazenamento no banco ou embeddings).
- Módulo RAG	Consulta o banco ou embeddings para recuperar trechos relevantes.
- Geração de Resposta (LLM)	Combina trechos recuperados com prompt do usuário e gera resposta via modelo de linguagem (LangChain/Ollama).
- Retorno ao Usuário	Exibe resposta na interface e opcionalmente salva histórico da interação (ID do usuário + pergunta).
- FAQ	Consulta arquivo FAQ.txt ou base de dados e retorna pergunta/resposta correspondente.
- Geração de relatórios de presenças
- Análise Preditica - Em treinamento, certificações obrigatórias
- Análise Preditica - engajamento em pesquisas de clima organizacional
- Geração de Gráficos - 
- Fim	Fluxo finaliza após resposta.

**Infraestrutura Inicial:**

Backend: FastAPI

Frontend: Streamlit ou Gradio

Banco: PostgreSQL/MySQL (ou Chroma para RAG)

Armazenamento de arquivos: local ou S3

LLM: Ollama via LangChain

Docker: A aplicação já está utilizando o docker

## 2. Plano de Evolução Simulada (12 meses)

Podemos dividir em trimestres para tornar a evolução gradual e realista:

**Mês 1-3: Consolidação do MVP**

Implementar logging de interações.

Fazer com que as dúvidas sejam consultadas na internet

Salvar histórico mínimo (ID do usuário + pergunta).

Criar uma base com as perguntas para fazer treinamento

Testes unitários e integração básica.

Fazer o endpoint de solicitação de férias

**Mês 4-6: Funcionalidades Avançadas**

Autenticação JWT completa, com perfis de usuário.

Histórico completo de interações no banco.

Processamento de arquivos em lote.

Indexação de documentos com embeddings mais robusta.

Integração de FAQ dinâmico (base de dados).

Interface mais amigável com Streamlit/Gradio ou front completo, mostrando histórico de perguntas.

**Mês 7-9: Melhoria de Inteligência e Automação**

Personalização de respostas baseado no histórico do usuário.

Detecção automática do tipo de arquivo e de perguntas.

Integração de novos modelos de LLM para melhor precisão.

Otimização de desempenho do módulo RAG.

**Mês 10-12: Escalabilidade e Recursos Extra**

Implementação de multiusuário com permissões.

Dashboard administrativo para monitorar interações e métricas.

Suporte a mais formatos de arquivo (Excel, DOCX, JSON).

Pipelines automáticas de ingestão de documentos.

Possível integração com sistemas externos via API (ERP, CRM).