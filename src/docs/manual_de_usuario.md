# Manual de Uso - Assistente de IA para Departamento Pessoal

**1. Introdução**

Este manual descreve como utilizar o Assistente de IA desenvolvido para apoiar as rotinas do Departamento Pessoal (DP). O assistente permite:

- Consultar dúvidas sobre afastamentos e licenças.

- Gerar relatórios de assiduidade.

- Buscar informações em FAQs pré-cadastradas.

O objetivo é facilitar o acesso a informações do DP e automatizar tarefas simples.

**2. Requisitos**

- Acesso à rede corporativa (ou localhost se estiver em desenvolvimento).

- Navegador moderno (Chrome, Edge, Firefox).

- A API deve estar em execução (via Docker ou uvicorn local).

- Recomendável ter DBeaver para visualizar o banco de dados (MySQL/Postgres).

- Para utilizar é necessário baixar o ollama e o modelo que deseja

**3. Acessando a API**

Certifique-se que a API está rodando em:

``````
http://localhost:8000


Para ver os endpoints disponíveis, abra o Swagger UI:

http://localhost:8000/docs

``````

Na tela do Swagger, você verá todos os endpoints com descrição, parâmetros e exemplos de requisição.

**4. Principais Funcionalidades**

**4.1 Consultar FAQ**

``````

Endpoint: GET /faq/

Descrição: Retorna todas as perguntas e respostas cadastradas.

Como usar:

Acesse o Swagger /faq/.

Clique em Try it out.

Clique em Execute.

Exemplo de retorno:

[
  {
    "pergunta": "Como trocar a senha?",
    "resposta": "Envie seu pedido no sistema de RH."
  }
]

``````

**4.2 Enviar nova pergunta para o FAQ**

``````

Endpoint: POST /faq/

Descrição: Permite cadastrar uma nova pergunta e resposta.

Como usar:

Vá para /faq/ → POST.

Clique em Try it out.

Insira o JSON da pergunta:

{
  "pergunta": "Como registrar atestado?",
  "resposta": "Envie ao DP pelo sistema interno."
}


Clique em Execute.

``````

**4.3 Consultar usuários**

``````

Endpoint: GET /users/

Descrição: Lista os usuários cadastrados na aplicação.

Como usar: acessar pelo Swagger /users/ → Try it out → Execute.

``````

**4.4 Login de usuário**

Endpoint: POST /users/login

Descrição: Realiza autenticação do usuário.

Como usar:

Acesse /users/login.

Forneça email e senha.

Receberá um token de autenticação (necessário para endpoints que exigem login).

Observações sobre autenticação:

Para autenticar, insira email e senha.

O token expira em 60 minutos.

**5. Dicas de Uso**

Sempre consulte a documentação Swagger (/docs) antes de testar novos endpoints.

Para consultas rápidas no banco, utilize o DBeaver.

Use o modo --reload apenas em desenvolvimento.

Caso encontre mensagens de erro no Swagger, verifique se a API e os bancos estão ativos.

**6. Suporte**

Contato: vanessaformiga21@gmail.com

Para problemas técnicos, envie prints do Swagger e logs do Docker.