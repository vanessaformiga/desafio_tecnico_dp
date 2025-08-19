# Contexto do Desafio

**Contexto do Desafio para a vaga de Desenvolvedor de IA**

**Contexto da Organização**

A OSM possui uma solução que oferece suporte às atividades com foco na rotina de RH, desde a inicialização no órgão público até a sua saída. É uma solução completa para gestão de pessoas, cuja disponibilização é para órgãos federais e estaduais.

Eles armazenam diferentes dados dos servidores sendo dados pessoais dos servidores ativos e inativos, folha de ponto e de salários, treinamentos e certificações realizadas, chamados realizados no Mentorh e pesquisas de clima organizacional.

**Desafio proposto:**

Fazer um projeto de IA, cujo objetivo é o Departamento Pessoal;

Na solução devem ter dados que podem ser mocados ou gerados ou puxados de algum local;

Fazer alguma tarefa que seja automatizada para rotinas de dp;

Fazer uma análise preditiva em relação à participação dos servidores nas pesquisas de clima organizacional;

**Tarefas**:

- Identificar problemas do DP atrelados ao serviço público que podem ser resolvidas com IA;
- Realizar alguma tarefa automatizada como responder dúvidas sobre licenças e afastamentos;
- Gerar relatórios frequentes de assiduidade;
- Integrar ou consumir os dados de um banco relacional, podendo ser mysql ou postgresql

Desenvolver um modelo preditivo que identifique servidores com risco de afastamento  prolongado ou queda de engajamento, usando variáveis como:

- Frequência/atrasos.
- Participação em treinamentos obrigatórios.
- Resultados de pesquisas de clima organizacional.

1. Apresentar um fluxograma do funcionamento da solução e um plano de evolução simulada para os próximos 12 meses.

Artefatos que precisam ser entregues:

- Repositório com [REDAME.md](http://redame.md/), arquitetura, código fonte, bibliotecas, como executar entre outros
- No relatório:
    - Problema identificado;
    - Solução proposta;
    - Resultados esperados;

Pode ter como bônus uma análise preditiva sobre o risco em relação ao afastamento prolongado dos servidores ou queda de engajamento

Aplicar técnicas do PNQ na execução do desafio

Entrega pode ser um link do Github contendo o relatório e os arquivos

**Critérios de Avaliação**

Qualidade da entrega

Se enquadra com o serviço público

Aderência ao PNQ

Inovação e criatividade

**Tarefas:**

1. Escrever um relatório identificando três problemas do setor de DP destinado ao servidor públi que podem ser resolvidos com IA; No relatório precisa ter o problema, solução e resultados esperados;
2. Gerar respostas automatizadas sobre afastamentos e licenças
3. Geração de relatórios de assiduidade
4. Para a geração dos dados que podem ser mocados, devem ser feitos consultas em banco relacional, sendo mysql ou postgresql
5. Criar um modelo de uma análise preditiva que identifique servidores que correm o risco de afastamento prolongado ou queda de engajamento: Utilizando as variáveis de frequência, participação de treinamentos obrigatórios e resultados de pesquisa de clima organizacional
6. Criar um fluxograma da solução e uma simulação da evolução para os próximos 12 meses
7. Escrever o relatório

**Atividades:**

1. Pensar em problemas do DP destinado ao servidor público
2. Montar um banco de dados relacional com dados fictícios de servidores públicos federais e estaduais: Podendo ter as entidades servidor, órgão, treinamentos realizados, pesquisas de clima e de controle de ponto
3. Criar uma api que contém um chat como principais dúvidas sobre licença e afastamento, as respostas podem estar em um arquivo que pode ser usado para consulta e depois podem pensar em uma forma de trabalhar melhor a inserção das respostas
4. Utilizar o docker em conjunto com o mysql
5. Talvez da estilizada na interface da API
6. Criar um fluxograma da solução funcionando
7. Plano de simulação para os próximos 12 meses
8. Fazer o relatório
9. Enviar o email com repositório e o relatório
10. Crie uma análise preditiva que exiba com algum tipo de gráfico que pode ser atráves de outro endpoint da api que utiliza as variáveis de participação nos treinamentos obrigatórios e a realização das certificações. Essa análise pode exibir resultados sobre órgãos federais e estaduais e os setores por departamento

**Atividades do Kanban**

- [] Escrever o relatório
    
- [] Criar as tabelas e o banco no mysql
    
- []Inserir dados fictícios para consulta
    
- [] Enviar o email com o relatório e os artefatos
    
- [] Pensa em três situações do DP que podem ser resolvidas com ia
    
- [] Utilizar o docker para o uso do banco de dados
    
- [] Criar a api para a geração das respostas sobre afastamentos e licenças
    
- [] Criar as principais perguntas e respostas em arquivo faq
    
- [] Criar o relatório, deve ter três situações que podem ser resolvidas com IA e o detalhamento sobre a execução da solução do chat para responder dúvidas sobre afastamento e licenças, contendo problema, solução e resultados. E também a parte da análise preditiva da participação dos servidores no engajamento com o problema, solução, análise e próximos passos.
    
- [] Criar outro endpoints que pode ser post para gerar análise preditiva cuja o foco pode ser a participação nos treinamentos e certificações obrigatórias e os resultados dos servidores
    
- [] E outro endpoint também post para que possa exibir algum gráfico como saída da análise preditiva

**Observações:**

O Desafio Precisa ser aderente a realidade dos servidores públicos e que atenda regras do PNQ e também precisa ser inovador e criativo.