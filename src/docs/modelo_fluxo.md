**Fluxo Geral da Solução**

``````

Início

Usuário acessa a aplicação (via API ou interface web/Streamlit).

Autenticação (opcional)

Verifica se o usuário está logado.

Se não, solicita login ou cadastro.

Entrada do Usuário

Pergunta, upload de arquivo (PDF/CSV) ou solicitação de FAQ.

Verificação do Tipo de Entrada

Pergunta textual → direciona para módulo RAG ou FAQ.

Upload de arquivo → direciona para processamento de documento.

Processamento de Documento

Lê o arquivo (PDF/CSV).

Converte em texto.

Indexa ou armazena no banco (para RAG).

Módulo RAG (Recuperação de Informações)

Consulta banco ou embeddings.

Recupera trechos relevantes.

Geração de Resposta (LLM)

Combina dados recuperados + prompt do usuário.

Chama modelo de linguagem (via LangChain/OlLama).

Retorno ao Usuário

Exibe resposta.

Salva histórico da interação (opcional: somente ID do usuário e pergunta).

FAQ

Consulta arquivo FAQ.txt ou base de dados.

Retorna pergunta/resposta correspondente.

Fim

``````

**Desenho do Fluxo**

[Início]
     |
[Autenticação?] --Não--> [Solicitar Login]
     |
     Sim
     |
[Entrada do Usuário] --> [Tipo de Entrada?]
                         |             |
                     Pergunta        Arquivo
                         |             |
                [Módulo RAG]   [Processamento de Documento]
                         |             |
                  [Geração de Resposta]
                         |
                [Exibe Resposta / Salva Histórico]
                         |
                       [Fim]