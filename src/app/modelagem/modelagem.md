
**Entidades Principais e Atributos**

**Principais Tabelas:**

- Usuário
- Servidor
- Orgão
- Departamento
- Certificação
- Treinamento
- Departamento Pessoal
- Assiduidade
- Dúvidas
- Clima Organizacional

1. Usuário

Função: login e registro na API

Atributos:
id_usuario, nome, email, senha, tipo_usuario, data_criacao, ultimo_login

Relacionamentos:

Vinculado a um Servidor → (1 Servidor : 1 Usuário)

Pode ser responsável em Departamento_Pessoal → (1 Departamento_Pessoal : N Usuários)

2. Servidor

Função: informações do servidor

Atributos:
matricula, nome, id_orgao, id_departamento, cargo, data_admissao, tipo_servidor

Relacionamentos:

Pertence a um Órgão → (1 Órgão : N Servidores)

Pertence a um Departamento → (1 Departamento : N Servidores)

Associado a Assiduidade → (1 Servidor : N Assiduidade)

Associado a Dúvidas → (1 Servidor : N Dúvidas)

Associado a Clima Organizacional / Treinamento / Certificação → (1 Servidor : N Clima/Treinamento/Certificação)

3. Órgão

Função: estrutura organizacional superior

Atributos: id_orgao, nome, tipo_orgao

Relacionamentos:

Possui Departamentos → (1 Órgão : N Departamentos)

Possui Servidores → (1 Órgão : N Servidores)

4. Departamento

Função: estrutura organizacional intermediária

Atributos: id_departamento, nome, id_orgao

Relacionamentos:

Pertence a um Órgão → (1 Órgão : N Departamentos)

Possui Servidores → (1 Departamento : N Servidores)

Pode ter análises de Clima Organizacional / Treinamento / Certificação → (1 Departamento : N Clima/Treinamento/Certificação)

5. Departamento_Pessoal (DP)

Função: central de gestão de processos de pessoal

Atributos: id_dp, nome, responsavel, contato, observacao

Relacionamentos:

Vincula-se a Usuários responsáveis → (1 Departamento_Pessoal : N Usuários)

Pode analisar Assiduidade, Licença, Férias → (1 Departamento_Pessoal : N Assiduidade/Solicitações)

6. Assiduidade

Função: presença em atividades ou treinamentos

Atributos: id_assiduidade, id_servidor, data, tipo_atividade, status_presenca, observacao

Relacionamentos:

Associada a Servidor → (1 Servidor : N Assiduidade)

7. Dúvidas

Função: consultas sobre licenças, afastamentos ou férias (não persistir conteúdo da dúvida, apenas o usuário que perguntou)

Atributos: id_duvida, id_servidor, data_hora

Relacionamentos:

Feita por Servidor → (1 Servidor : N Dúvidas)

8. Treinamento

Função: informações sobre capacitação

Atributos: id_treinamento, nome, descricao, data_inicio, data_fim

Relacionamentos:

Associado a Servidor → (1 Servidor : N Treinamento)

Associado a Departamento → (1 Departamento : N Treinamento)

9. Certificação

Função: capacitação e avaliação

Atributos: id_certificacao, nome, descricao, data_aplicacao, nota_maxima

Relacionamentos:

Associada a Servidor → (1 Servidor : N Certificação)

Associada a Departamento → (1 Departamento : N Certificação)

10. Clima Organizacional

Função: pesquisas de clima

Atributos: id_clima, id_departamento, periodo, indicador_satisfacao, comentarios

Relacionamentos:

Associado a Servidor → (1 Servidor : N Clima)

Associado a Departamento → (1 Departamento : N Clima)

``````

**Diagrama Simples**

[Órgão] 1───N [Departamento]
   │            │
   │            │
   └───N [Servidor] 1───1 [Usuário]
                 │
                 │
   ┌─────────────┼─────────────┐
   │             │             │
[N Assiduidade] [N Dúvidas] [N Clima/Treinamento/Certificação]
                 │
             [Treinamento]  N
                 │
             [Certificação] N

[Departamento_Pessoal] 1───N [Usuário]

``````

**Explicação do diagrama**

Órgão → Departamento: um órgão possui vários departamentos.

Departamento → Servidor: um departamento possui vários servidores.

Servidor → Usuário: cada servidor pode ter um usuário para login (1:1).

Servidor → Assiduidade/Dúvidas/Clima/Treinamento/Certificação: relacionamentos 1:N.

Treinamento/Certificação → Departamento: também podem estar associados a departamentos para análises.

Departamento_Pessoal → Usuário: DP vincula usuários responsáveis, 1:N.

**Tabelas que podem ser geradas depois**

- Solicitação de Férias
- Aprovação
- Chat
- base de conhecimento

